import json

data = [
    {
        "id": "001",
        "complexity": "Short / Simple",
        "retrieval": "None",
        "instruction": "What does APY stand for?",
        "input": "",
        "output": "APY stands for Annual Percentage Yield. It reflects the total amount of interest you earn on a deposit over one year, taking into account the effect of compounding interest.",
    },
    {
        "id": "002",
        "complexity": "Short / Simple",
        "retrieval": "Policy",
        "instruction": "What is the maximum daily ATM withdrawal limit?",
        "input": "",
        "output": "Our standard daily ATM withdrawal limit is $1,000 per business day. This limit resets daily at midnight EST. If you need a temporary increase, you can request one in the mobile app.",
    },
    {
        "id": "003",
        "complexity": "Short / Simple",
        "retrieval": "Account",
        "instruction": "Did my direct deposit from Acme Corp clear today?",
        "input": "Account Status: Active | Pending ACH: Acme Corp $2,450.00 settled 06:15 AM EST | Available Balance: $3,120.45",
        "output": "Yes, your direct deposit of $2,450.00 from Acme Corp settled today at 6:15 AM EST. Your new available balance is $3,120.45.",
    },
    {
        "id": "004",
        "complexity": "Short / Simple",
        "retrieval": "Both",
        "instruction": "Why was I charged a $12 maintenance fee on my checking account?",
        "input": "Policy: Minimum balance required $1,500 to waive $12 fee | Account: Daily balance fell to $850 on Aug 15",
        "output": "You were assessed a $12 monthly maintenance fee on August 15 because your daily balance fell to $850, which is below the account's $1,500 minimum balance waiver threshold.",
    },
    {
        "id": "005",
        "complexity": "Short / Hard",
        "retrieval": "None",
        "instruction": "If a check is post-dated, is the bank legally prohibited from paying it early under UCC rules?",
        "input": "",
        "output": "Under Uniform Commercial Code (UCC) § 4-401, a bank may pay a post-dated check before its date unless you have provided timely formal notice of post-dating that describes the check with reasonable certainty.",
    },
    {
        "id": "006",
        "complexity": "Short / Hard",
        "retrieval": "Policy",
        "instruction": "What specific criteria determine whether a Regulation CC funds availability hold is extended to 7 business days?",
        "input": "",
        "output": "An exception hold extending availability up to 7 business days applies under Reg CC if: the deposit exceeds $5,525 in a single day, the account is repeatedly overdrawn, the check was previously returned unpaid, or there is reasonable cause to doubt collectibility.",
    },
    {
        "id": "007",
        "complexity": "Short / Hard",
        "retrieval": "Account",
        "instruction": "Why does my available balance show $450 when my posted ledger balance is $1,200?",
        "input": "Ledger Balance: $1,200.00 | Pending Authorizations: Hotel Pre-auth $650.00, Debit Card $100.00 | Available Balance: $450.00",
        "output": "Your ledger balance reflects settled transactions, while your available balance accounts for pending authorizations. You currently have a pending $650 hotel pre-authorization hold and a $100 pending debit charge, leaving $450 available to spend.",
    },
    {
        "id": "008",
        "complexity": "Short / Hard",
        "retrieval": "Both",
        "instruction": "I initiated a $15,000 international wire transfer yesterday; why is it on hold and what documentation is required?",
        "input": "Policy: Transactions >$10k require BSA/OFAC manual verification | Account: Pending Wire $15,000 outbound",
        "output": "Your wire transfer is currently held by our compliance department under OFAC/BSA verification protocols because it exceeds our $10,000 automated processing limit. Please provide an invoice or bill of sale along with proof of recipient relationship via the secure document portal.",
    },
    {
        "id": "009",
        "complexity": "Long / Simple",
        "retrieval": "None",
        "instruction": "I'm teaching my teenager about financial literacy and I want to explain the difference between a debit card and a credit card in clear, simple terms so they understand how interest and bank balances work.",
        "input": "",
        "output": "A debit card spends money directly from your existing checking account—when you swipe, the funds leave your account immediately. A credit card borrows money from the bank up to a set credit limit; you receive a monthly bill and will be charged interest on any balance you do not pay off in full.",
    },
    {
        "id": "010",
        "complexity": "Long / Simple",
        "retrieval": "Policy",
        "instruction": "I am planning to travel to Japan and South Korea next month for three weeks. Do I need to notify the bank about my travel dates, and will I be charged international transaction fees when using my debit card abroad?",
        "input": "",
        "output": "You do not need to set a travel notice, as our automated fraud systems monitor foreign transactions seamlessly. However, using your standard debit card abroad incurs a 3% foreign transaction fee per purchase and a $5 out-of-network international ATM fee plus local operator charges.",
    },
    {
        "id": "011",
        "complexity": "Long / Simple",
        "retrieval": "Account",
        "instruction": "I was looking at my statement from last week and noticed three separate charges at Starbucks on Tuesday, but I only bought coffee once that morning. Can you look into these specific charges and see if they posted?",
        "input": "Account History (Tuesday Aug 11): 1x Posted $6.25, 2x Pending Holds $6.25 (duplicate authorization)",
        "output": "Looking at your account history for Tuesday, August 11, there is one posted charge of $6.25 and two pending authorization holds of $6.25 each. The two pending charges were duplicate settlement attempts and will automatically drop off within 48 business hours without debiting your funds.",
    },
    {
        "id": "012",
        "complexity": "Long / Simple",
        "retrieval": "Both",
        "instruction": "I deposited a $4,000 cashier's check on Friday afternoon through mobile deposit, but only $225 is showing as available right now. When will the rest become available according to your funds availability schedule?",
        "input": "Policy: Mobile cut-off 5:00 PM Friday; Next-day $225 immediate, remainder on next business day (Tuesday) | Account: Deposit Friday 5:45 PM $4,000",
        "output": "Under our standard Funds Availability Policy, mobile deposits made after 5:00 PM on Friday are processed on the next business day (Monday). The initial $225 is available immediately, with the remaining $3,775 scheduled to clear and become fully available by Tuesday morning at 9:00 AM EST.",
    },
    {
        "id": "013",
        "complexity": "Long / Hard",
        "retrieval": "None",
        "instruction": "If an unauthorized ACH debit occurs via an illicit corporate Nacha corporate trade exchange (CTX) versus a consumer prearranged payment (PPD), what is the difference in liability and the legal return timeframe for each?",
        "input": "",
        "output": "Under Nacha rules, consumer accounts (PPD/WEB) carry a 60-calendar-day return window from the settlement date with full unauthorized debit protection under Regulation E. In contrast, corporate/commercial accounts (CTX/CCD) are not covered by Regulation E and must return unauthorized entries by the standard 2-business-day return cutoff (Rule Return Code R05/R29).",
    },
    {
        "id": "014",
        "complexity": "Long / Hard",
        "retrieval": "Policy",
        "instruction": "If I open a 5-year Certificate of Deposit with a promotional 4.5% APY and need to withdraw $10,000 early for an emergency, what is the exact calculation method used for the early withdrawal penalty and will it eat into my principal if insufficient interest has accrued?",
        "input": "",
        "output": "Early withdrawals on a 5-year CD incur a penalty equal to 180 days of simple interest on the amount withdrawn, calculated at the contractual rate ($10,000 * 4.5% * (180/365) = $221.92). If your earned interest is less than $221.92 at the time of withdrawal, the remaining penalty balance will be deducted directly from your principal deposit.",
    },
    {
        "id": "015",
        "complexity": "Long / Hard",
        "retrieval": "Account",
        "instruction": "I have a linked overdraft setup between my checking, savings, and credit line. Yesterday I had three transactions hit simultaneously totaling $1,200 with only $500 in checking: how did the system draw the funds, what is my credit line balance now, and was an overdraft fee triggered?",
        "input": "Account Setup: Linked Checking ($500), Savings ($400), Overdraft Line ($0 balance, 14.99% APR) | Total Transaction: $1,200",
        "output": "Your $500 checking balance was exhausted first. The system then transferred your available $400 from savings, and drew the remaining $300 balance from your linked credit line. Your credit line now has a balance of $300 at 14.99% APR; because you used automatic linked-account transfers, no overdraft penalty fees were incurred.",
    },
    {
        "id": "016",
        "complexity": "Long / Hard",
        "retrieval": "Both",
        "instruction": "A recurring subscription of $89.99 posted to my account yesterday after I had placed a formal stop payment order on that merchant two weeks ago. Why did it post, will my stop payment fee be refunded, and how do we resolve the disputed charge?",
        "input": "Policy: Stop payment mismatch requires agent fee reversal & company ID refresh | Account: Stop payment set on Merchant A; Transaction posted under Merchant A Subsid. $89.99",
        "output": "The stop payment failed because the merchant billed under a different corporate originator ID than the previous transaction. I have applied a provisional credit of $89.99, refunded the $30 stop payment fee due to the system mismatch, and updated the block list with the merchant's new originator ID to prevent future debits.",
    },
]

output_filename = "banking_sft.jsonl"
with open(output_filename, "w", encoding="utf-8") as f:
    for row in data:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")

print(f"Successfully generated {len(data)} rows in {output_filename}")