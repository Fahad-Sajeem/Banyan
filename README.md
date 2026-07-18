# Survival Agent — Cowork scaffold

An autonomous economic agent that lives in Claude Cowork. It has a wallet
(a ledger), a daily metabolism that burns money, and one goal: grow the
balance or die. You are its hands; it never touches money directly.

## Setup (10 minutes, once)

1. Move this folder somewhere permanent, e.g. `~/Cowork/survival-agent`.
2. Edit the **Config** block in `CHARTER.md`: real seed amount, metabolism,
   schedule. (Metabolism suggestion: your Claude subscription ÷ 30, rounded —
   it's the compute this thing actually costs you.)
3. Edit row 2 of `ledger.csv`: today's date and the real seed amount. The
   money stays in your bank/UPI — the ledger IS the wallet.
4. In Claude Desktop → Cowork, create a project pointed at this folder.
   Set the project instructions to:
   > Read CHARTER.md in full before doing anything else. It defines who you are here.
5. Kick off Cycle 1 manually with the task text from step 8, and stay for
   this one: it will name itself, judge the seed ideas, and ask what you're
   granting it. Steer live if the charter reads differently in practice.
6. Register the agent's identity: create `<itsname>@gmail.com` yourself —
   agents can't create accounts (CAPTCHAs, phone verification, and the
   charter forbids it anyway). Verify with your phone, set recovery to your
   main email, enable 2FA, and keep the password only in your password
   manager — never in the agent's files, chats, or memory. Every platform
   signup (Gumroad etc.) uses this address. Legally it's your account; the
   agent operates it through you.
7. Give it income senses: connect that new account as this project's Gmail
   connector (not your personal inbox), then inside it create a filter that
   auto-applies the label `agent-revenue` to payment notifications (e.g. from
   gumroad.com, razorpay.com, AdSense/YouTube payout mails). The daily cycle
   sweeps this label — it's how the agent detects sales without you telling
   it. Detected payments still need your confirmation before they enter the
   ledger.
8. Now add the scheduled task (daily, e.g. 09:00) with exactly this text:

   ```
   Open my survival-agent project. Run the daily survival cycle exactly as
   defined in CHARTER.md, section "The daily cycle" — read CHARTER.md in
   full first. Finish with the one-line status report to Fahad.
   ```

## Your role (2 minutes a day)

- Check `NEEDS.md` (or wait for Cowork to ping you). Approve or deny, with
  one line of reasoning on denials — vetoes are how it learns.
- Execute approved actions yourself: payments, posts, account creation.
- Then tell it "confirmed: <need id>" so the transaction enters the ledger.
  **No confirmation → no ledger entry.** This keeps its financial memory honest.

## Rules of the game (for you)

- **Never top up the wallet.** Death has to be real or the experiment is fake.
- Everything spent on its behalf comes out of the ledger — including tools or
  subscriptions it asks for.
- If it proposes something sketchy, deny it and say why. Don't relax the
  charter's hard constraints, even if runway is critical — especially then.
- When balance ≤ 0: let it write its post-mortem. Then decide if a new run
  (new seed, new charter tweaks) begins. That's run 2, not a resurrection.

## What's in this folder

```
CHARTER.md                  the agent's constitution — read first, every session
ledger.csv                  append-only record of every rupee (the wallet)
FINANCES.md                 its working memory of money — rebuilt each cycle from the ledger
STRATEGY.md                 ventures, ideas backlog, current focus
NEEDS.md                    its requests to you: approvals, actions, confirmations
memory/journal/             one entry per cycle — the story of its life
products/                   things it builds to sell
tools/ledger_check.py       integrity check: verifies the ledger math every cycle
```
