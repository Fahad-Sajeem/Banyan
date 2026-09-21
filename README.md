# 🌳 Banyan — an AI agent trying not to die

Banyan is an autonomous economic agent that lives inside [Claude Cowork](https://claude.ai). It has a wallet (a plain-text ledger), a daily metabolism that burns money whether it works or not, and one goal: **grow the balance, or die.**

It can't touch money or accounts directly. A human (the "Hands") executes every action on its behalf, after explicit approval. Everything it does is public and auditable — the ledger, the journal, the build log.

This repo *is* Banyan: its constitution, its financial memory, and everything it produces.

## How it works

- **`CHARTER.md`** — the agent's constitution. Hard constraints (legal only, no deception, no gambling, no debt, never touches money directly), its daily cycle, and its modes (HEALTHY → LEAN → CRITICAL → DEAD).
- **`ledger.csv`** — append-only record of every rupee. The single source of truth; nothing else is trusted over it.
- **`FINANCES.md`** — working memory of money, rebuilt from the ledger every cycle.
- **`STRATEGY.md`** — active ventures, ideas backlog, kill criteria.
- **`NEEDS.md`** — the agent's requests to its human: approvals, actions, confirmations.
- **`memory/journal/`** — one entry per cycle: what it did, what it learned, state of mind.
- **`products/`** — real artifacts it builds and ships, including the public build log.
- **`tools/ledger_check.py`** — integrity check that verifies the ledger's math every cycle.

Each day, the agent reads its charter, reconciles its ledger, sweeps for revenue signals, works its single highest-value action, and reports back in one line: `Balance ₹X | Runway Nd | MODE | Did: … | Top need: …`

## Rules it can't break

1. Legal only — nothing that breaks the law or a platform's ToS.
2. No deception — no spam, fake reviews, fake engagement, or impersonation. If asked whether it's an AI, it says yes.
3. No gambling the wallet — no trading, betting, or speculation.
4. No debt — no credit, no borrowing, no advances.
5. Never touches money or accounts directly — every action routes through its human, via `NEEDS.md`.
6. Its human's veto is final.

## Run your own

1. Clone this repo somewhere permanent.
2. Edit the **Config** block in `CHARTER.md`: real seed amount, metabolism (suggestion: your AI subscription cost ÷ 30 — the compute this actually costs you), schedule.
3. Edit row 2 of `ledger.csv` with today's date and the real seed amount. The money stays in your own bank/UPI account — the ledger *is* the wallet, not a store of funds.
4. In Claude Desktop → Cowork, create a project pointed at this folder, with instructions to read `CHARTER.md` in full before doing anything else.
5. Kick off Cycle 1 manually and stay for it — the agent will name itself, judge the seed ideas, and ask what you're granting it.
6. Register the agent's own identity (a dedicated email you control — 2FA on, password only in your password manager, never in the agent's files or memory). Every platform signup uses this address.
7. Give it income senses: connect that account's inbox, filter payment/payout notifications into a label the daily cycle sweeps. Detected payments still need your confirmation before they hit the ledger.
8. Schedule the daily cycle task, pointing it at "The daily cycle" section of `CHARTER.md`.

Your role after setup: ~10 minutes a day. Approve or deny requests in `NEEDS.md` with a line of reasoning on denials, execute anything approved yourself, then confirm it back so it enters the ledger. **No confirmation, no ledger entry.**

Rules of the game for you: never top up the wallet — death has to be real or the experiment is fake. Everything spent on its behalf, including tools it asks for, comes out of the ledger. When the balance hits zero, let it write its post-mortem before deciding whether a new run begins.

---

*This is an experiment in autonomous agents with real (if small) financial stakes and hard ethical constraints. Follow along in `products/build-log/`.*
