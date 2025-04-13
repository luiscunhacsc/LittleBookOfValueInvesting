import streamlit as st
import pandas as pd
import numpy as np

# Configure the Streamlit app
st.set_page_config(page_title="Evaluating Financial Companies: A Special Case", layout="centered", initial_sidebar_state="expanded")

# Custom CSS for improved readability on mobile devices
st.markdown("""
    <style>
    .main {
        max-width: 800px;
        margin: auto;
        padding: 20px;
    }
    .footer {
        font-size: 0.8em;
        text-align: center;
        color: #777;
    }
    </style>
    """, unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# Title and Challenge Description
# ----------------------------------------------------------------------------
st.title("🏦 Evaluating Financial Companies: A Special Case")

st.markdown("""
### The Challenge
Financial companies do not produce physical goods or own factories. They work with money as their raw material:
- They **buy money** (paying interest to depositors)
- They **sell money** (lending funds and charging interest)

**Result:** Traditional valuation models, such as the classic DCF, are not directly applicable.
""")
st.markdown("---")

st.markdown("""
### What Makes Financial Companies Different?
Below is a comparison between normal companies and financial companies:

| **Aspect**              | **Normal Companies**            | **Financial Companies**                    |
|-------------------------|---------------------------------|--------------------------------------------|
| **Debt**                | Something to control            | Integral to the business                   |
| **Tangible Assets**     | Factories, machines, inventory  | Loans, investments                         |
| **Free Cash Flow**      | Clearly defined                 | Difficult to define                        |
| **Regulation**          | Light to moderate               | Highly regulated                           |
| **Revenue Sources**     | Products sold                   | Interest, commissions, premiums            |

So, how do you evaluate these "financial beasts"?  
Return to basics: **Value = Assets – Liabilities** (adapted to the sector). The main tools become:
""")
st.markdown("---")

st.markdown("""
### 1. Relative Multiples
- **The King: Price-to-Book (P/BV)**  
  Compares the stock price with its book value per share (net assets). This is widely used in banks.  
  **Example:**  
  If a stock is trading at 1.2 times its book value, the market is paying a premium.

  **Interpretation:**  
  - **P/BV > 1:** The market expects returns above the cost of capital.  
  - **P/BV < 1:** The market is skeptical about the company's profitability or the quality of its assets.
  
- **Other Multiples:**  
  - ROE (Return on Equity) is fundamental to understand the profitability of equity.  
  - P/E, but only if profits are stable.  
  Many analyses cross-reference ROE and P/BV using a "magic formula":

  $$ P/BV = \\frac{ROE - g}{r - g} $$

  Where:  
  - *ROE* = Return on Equity  
  - *g* = Expected growth  
  - *r* = Cost of Capital

  This formula helps estimate the “fair” P/BV and compare it with the market.
""")
st.markdown("---")

st.markdown("""
### 2. Dividend Discount Model (DDM) for Banks
Banks typically pay stable and predictable dividends, making the DDM a suitable model.  
The formula is:

$$ \\text{Value} = \\frac{D_1}{r - g} $$

Where:  
- $D_1$ = Dividend expected next year  
- $r$ = Discount rate  
- $g$ = Growth rate

*Note:* This method requires a good estimate of the growth rate and is sensitive to regulatory risk and capital strength.
""")
st.markdown("---")

st.markdown("""
### 3. Asset Quality and Regulatory Risk
When valuing financial companies, you cannot ignore:
- **Credit Portfolio Quality:** The level of non-performing loans.
- **Capital Ratios:** Such as Tier 1 capital.
- **Exposure to Systemic Risk**

*Example:* Some banks collapsed because they had many “good” assets on paper, but with hidden risk.
""")
st.markdown("---")

st.markdown("""
### Key Phrase to Remember
*"In a financial company, value is found both in the confidence it inspires and the numbers it presents."*
""")
st.markdown("---")

# ----------------------------------------------------------------------------
# Interactive Mini-Exercise: Fair P/BV Calculation
# ----------------------------------------------------------------------------
st.header("Interactive Exercise: Fair P/BV Calculation")

st.markdown("""
Fill in the details below to calculate the fair Price-to-Book (P/BV) ratio using the magic formula.
""")

# Inputs for the mini-exercise
roe = st.number_input("Enter the ROE (as a percentage)", value=12.0, step=0.5, format="%.2f")
cost_of_capital = st.number_input("Enter the Cost of Capital (r) in %", value=10.0, step=0.5, format="%.2f")
expected_growth = st.number_input("Enter the Expected Growth Rate (g) in %", value=4.0, step=0.5, format="%.2f")

# Convert percentages to decimals
roe_decimal = roe / 100
cost_decimal = cost_of_capital / 100
growth_decimal = expected_growth / 100

# Calculate the fair P/BV using the magic formula
if cost_decimal > growth_decimal:
    fair_pbv = (roe_decimal - growth_decimal) / (cost_decimal - growth_decimal)
    st.write(f"**Fair P/BV:** {fair_pbv:.2f}")
    
    st.markdown("""
    **Mini-Exercise Recap:**  
    If a bank has:  
    - ROE = 12%  
    - Cost of Capital = 10%  
    - Expected Growth = 4%  

    Then the fair P/BV is calculated as:  

    $$ P/BV = \\frac{0.12 - 0.04}{0.10 - 0.04} = \\frac{0.08}{0.06} \\approx 1.33 $$

    If the bank is trading at a P/BV of 1.1, it might be undervalued.
    """)
else:
    st.error("Cost of Capital must be greater than Expected Growth for a valid calculation.")

st.markdown("---")

st.markdown("""
### Analyst Checklist – Visual Summary
- **Consistent and high ROE?**  
- **P/BV below the theoretical value?**  
- **Sustainable and growing dividends?**  
- **Strong regulation and capitalization?**  
- **High-quality credit portfolio?**
""")
st.markdown("---")

st.markdown("""
### Classroom Analogy
Evaluating a bank is like assessing a dam:  
It may appear stable on the outside, but what really matters is the quality of the water (assets) and the strength of the floodgates (capital and regulation).
""")
