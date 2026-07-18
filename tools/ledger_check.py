#!/usr/bin/env python3
"""Verify ledger.csv integrity and print a financial summary.

Run every cycle. Exit code 0 = ledger is consistent; 1 = errors found.
The ledger is the single source of truth for the agent's money memory —
never trust a remembered balance, only a recomputed one.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "ledger.csv"
CHARTER = ROOT / "CHARTER.md"

VALID_TYPES = {"seed", "income", "expense", "metabolism"}
POSITIVE_TYPES = {"seed", "income"}


def metabolism_rate() -> float | None:
    try:
        m = re.search(r"metabolism_inr_per_day:\s*([\d.]+)", CHARTER.read_text())
        return float(m.group(1)) if m else None
    except OSError:
        return None


def main() -> int:
    if not LEDGER.exists():
        print("ERROR: ledger.csv not found"); return 1

    with LEDGER.open(newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("ERROR: ledger has no transactions (seed row missing?)"); return 1

    errors: list[str] = []
    running = 0.0
    earned = spent = metab = 0.0
    last_date = ""

    for i, r in enumerate(rows, start=2):  # header is line 1
        t = (r.get("type") or "").strip()
        if t not in VALID_TYPES:
            errors.append(f"line {i}: invalid type '{t}'")
        try:
            amt = float(r["amount_inr"]); recorded = float(r["balance_after"])
        except (KeyError, TypeError, ValueError):
            errors.append(f"line {i}: non-numeric amount_inr/balance_after"); continue

        if t in POSITIVE_TYPES and amt < 0:
            errors.append(f"line {i}: {t} must be positive, got {amt}")
        if t in ("expense", "metabolism") and amt > 0:
            errors.append(f"line {i}: {t} must be negative, got {amt}")

        d = (r.get("date") or "").strip()
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d):
            errors.append(f"line {i}: date '{d}' not YYYY-MM-DD")
        elif last_date and d < last_date:
            errors.append(f"line {i}: date {d} goes backwards (after {last_date})")
        last_date = max(last_date, d)

        if t != "metabolism" and not (r.get("confirmed_by") or "").strip():
            errors.append(f"line {i}: missing confirmed_by (only metabolism may be self-recorded)")

        running += amt
        if abs(running - recorded) > 0.01:
            errors.append(
                f"line {i}: balance_after {recorded:.2f} != computed {running:.2f}"
            )
            running = recorded  # resync so one mistake doesn't cascade

        if t == "income":
            earned += amt
        elif t == "expense":
            spent += -amt
        elif t == "metabolism":
            metab += -amt

    balance = running
    rate = metabolism_rate()

    print(f"transactions        : {len(rows)}")
    print(f"balance             : ₹{balance:,.2f}")
    print(f"total earned        : ₹{earned:,.2f}")
    print(f"total spent (ops)   : ₹{spent:,.2f}")
    print(f"metabolism paid     : ₹{metab:,.2f}")
    if rate:
        runway = balance / rate
        print(f"runway              : {runway:.1f} days (at ₹{rate:g}/day)")
        if balance <= 0:
            print("mode                : DEAD — write the post-mortem")
        elif runway <= 7:
            print("mode                : CRITICAL")
        elif runway <= 21:
            print("mode                : LEAN")
        else:
            print("mode                : HEALTHY")
    else:
        print("runway              : unknown (metabolism_inr_per_day not found in CHARTER.md)")

    if errors:
        print(f"\nLEDGER ERRORS ({len(errors)}) — fix these before anything else:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("\nledger OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
