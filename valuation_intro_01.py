import streamlit as st
import numpy as np

# Configure the Streamlit app
st.set_page_config(page_title="Intrinsic Value – The Hidden Treasure", layout="centered", initial_sidebar_state="expanded")

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

# Title and introductory content
st.title("💎 Intrinsic Value: The Hidden Treasure")
st.markdown("""
### 🧭 What is Intrinsic Value?
It is the real value of a company calculated based on its ability to generate cash in the future.  
Imagine buying a popcorn machine: how much would you pay? It depends on:
- **How many popcorns** it produces 🍿  
- **For how many years** it operates ⏳  
- **If it is safe and reliable** ⚙️  

Similarly, when valuing a company, we want to know how much *cash* it will generate and then bring that value to the present.
""")
st.markdown("---")

# Explain the base formula
st.markdown("### 🧮 The Base Formula: Value = Future Cash, Today")
st.markdown(r"""
The DCF (Discounted Cash Flow) model tells us:
> A company is worth today the present value of the cash flows it will generate in the future.

**Translation:**
- **Cash Flows:** The actual money the company can distribute  
- **Present Value:** What that money is worth today  
- **Discount Rate:** A type of “risk interest” rate applied to adjust future cash flows  
""")
st.markdown("---")

st.markdown("### ⛏️ The Step-by-Step DCF Model (Simplified)")

# Step 1: Estimate Future Cash Flows
st.markdown("#### 1️⃣ Estimate Future Cash Flows")
st.markdown("""
Focus on what remains after investments and operating expenses.  
- For a mature company, cash flows tend to be stable.  
- For a startup, the cash flows are often unpredictable (and there might be no profit in the early years!).

*Technical term: Free Cash Flow to the Firm (FCFF)*
""")
with st.expander("Enter Your Future Cash Flows"):
    years = st.number_input("Number of projection years", min_value=1, max_value=20, value=5)
    cash_flows = []
    for year in range(1, years + 1):
        cf = st.number_input(f"Estimated Cash Flow for Year {year} ($)", value=100000.0, step=5000.0, key=f"cf_{year}")
        cash_flows.append(cf)
    st.write("Your projected cash flows:", cash_flows)
st.markdown("---")

# Step 2: Choose the Projection Horizon
st.markdown("#### 2️⃣ Choose the Projection Horizon")
st.markdown("""
Typically, you choose a projection horizon of **5 to 10 years**.  
After this period, we assume a stable growth and use a terminal value calculation.  
*Think of it like a train that accelerates and then cruises at a steady speed.*
""")
st.markdown("---")

# Step 3: Estimate the Discount Rate
st.markdown("#### 3️⃣ Estimate the Discount Rate")
st.markdown("""
The discount rate reflects the risk of the company.  
- More stable companies (like large, established firms) → lower discount rate  
- Riskier companies (startups, companies in unstable regions) → higher discount rate

For companies, we usually use the WACC (Weighted Average Cost of Capital).
""")
discount_rate = st.slider("Discount Rate (%)", min_value=0.0, max_value=20.0, value=10.0)
st.markdown("---")

# Step 4: Calculate the Present Value of Future Cash Flows
st.markdown("#### 4️⃣ Calculate the Present Value")
st.markdown(r"""
We calculate the present value (PV) of each future cash flow using the formula:

$$PV = \frac{FCF_{t}}{(1+r)^t}$$

Where:  
- $FCF_{t}$ = cash flow in year *t*  
- $r$ = discount rate (in decimal form)  
- $t$ = year number

Let's compute the PV for each year's cash flow.
""")
present_values = [cf / ((1 + discount_rate/100)**t) for t, cf in enumerate(cash_flows, start=1)]
total_pv = np.sum(present_values)
st.write("**Total Present Value of Cash Flows:** $", f"{total_pv:,.2f}")
st.markdown("---")

# Step 5: Estimate the Terminal Value
st.markdown("#### 5️⃣ Estimate the Terminal Value")
st.markdown(r"""
At the end of the projection horizon, we estimate the terminal value using the formula:

$$\text{Terminal Value} = \frac{FCF_{last} \times (1+g)}{(r - g)}$$

Where:
- $FCF_{last}$ = the cash flow in the final projected year  
- $g$ = perpetual growth rate  
- $r$ = discount rate  
""")
g_rate = st.slider("Perpetual Growth Rate (%)", min_value=0.0, max_value=10.0, value=3.0)
terminal_value = cash_flows[-1] * (1 + g_rate/100) / ((discount_rate/100) - (g_rate/100))
terminal_value_pv = terminal_value / ((1 + discount_rate/100)**years)
st.write("**Present Value of Terminal Value:** $", f"{terminal_value_pv:,.2f}")
st.markdown("---")

# Calculate and display the Intrinsic Value (DCF)
intrinsic_value = total_pv + terminal_value_pv
st.markdown("### 📊 Calculated Intrinsic Value")
st.write("**Intrinsic Value (based on DCF):** $", f"{intrinsic_value:,.2f}")
st.markdown("---")

# Variations of the DCF Model
st.markdown("### 🔍 Variations of the DCF Model")
st.markdown("""
Depending on what you want to value, there are three main approaches:
1. **Free Cash Flow to the Firm (FCFF):**  
   Values the entire company (debt + equity), later subtracting debt to derive equity value.
2. **Free Cash Flow to Equity (FCFE):**  
   Values only the cash available to shareholders.
3. **Dividend Discount Model (DDM):**  
   Uses dividends as a proxy for cash flows (works best for companies that pay stable dividends).
""")
st.markdown("---")

# The Sensitivity of the DCF Model
st.markdown("### ⚠️ Sensitivity of the DCF Model")
st.markdown("""
Even minor changes in:
- **Growth Rate** 📈  
- **Discount Rate** 🎯  
- **Terminal Value Assumptions** 🔚  

…can significantly alter the final valuation, much like a super-sensitive scale where even a small breath can move the needle.

Many analysts perform sensitivity analyses and scenario testing (the “what-if” analysis) to assess the impact of these changes.
""")
st.markdown("---")

# Special Considerations for Young or Uncertain Companies
st.markdown("### 💬 Special Considerations for Young or Uncertain Companies")
st.markdown("""
Young companies, those with losses or inconsistent histories, require:
- More assumptions
- Greater prudence
- Sometimes even alternative methods (such as real options)
""")
st.markdown("---")

# Why DCF remains the gold standard
st.markdown("### 📊 Why DCF is Still the Gold Standard")
st.markdown("""
The DCF method forces us to think about the fundamentals of a company:
- **How does it generate cash?**
- **How much does it reinvest?**
- **What is the real risk?**

It isn’t magic—it’s a practical tool for better understanding and evaluating businesses.
""")
st.markdown("---")

# Final inspirational quote
st.markdown("### 🧠 Final Thought")
st.markdown("> *\"The value of an asset is determined by the expected cash flows and the risk associated with them.\"*")
