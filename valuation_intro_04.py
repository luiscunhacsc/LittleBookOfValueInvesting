import streamlit as st
import pandas as pd

# Configure the Streamlit app
st.set_page_config(page_title="Evaluating Mature Companies", layout="centered", initial_sidebar_state="expanded")

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
# Title and Scenario Description
# ----------------------------------------------------------------------------
st.title("🧓 Evaluating Mature Companies: Less Fireworks, More Reliability")
st.markdown("""
### 🧭 The Scenario
Mature companies have already passed the turbulent growth phases:
- **Modest growth** 📉  
- **Saturated market** 🧱  
- **Predictable cash flows** 💰  

They may not look exciting, but they often form the backbone of a solid portfolio.

---

### 🎯 The Valuation Objective
The goal here is not to discover a "unicorn" but to determine whether the current market price accurately reflects the stable fundamentals of the company.

---
""")

# ----------------------------------------------------------------------------
# Typical Characteristics of Mature Companies
# ----------------------------------------------------------------------------
st.markdown("### 📊 Typical Characteristics of Mature Companies")
characteristics = {
    "Characteristic": [
        "Low Growth", 
        "Stable Cash Flow", 
        "Reduced Investment", 
        "Frequent Dividends", 
        "Controlled Debt"
    ],
    "Example": [
        "0–3% per year", 
        "High predictability", 
        "Few new projects", 
        "High dividend distribution rate", 
        "Good financial health"
    ]
}
df_chars = pd.DataFrame(characteristics)
st.table(df_chars)

st.markdown("---")

# ----------------------------------------------------------------------------
# Valuation Tools for Mature Companies
# ----------------------------------------------------------------------------
st.markdown("### 🧮 Most Suitable Valuation Tools")

st.markdown("""
1️⃣ **Discounted Cash Flow (DCF) – Stable Version**  
   - Cash flow forecasts are relatively constant  
   - Less uncertainty → greater confidence in the results  
   - Often, a projection of 5 years plus a terminal value is enough

2️⃣ **Dividend Discount Model (DDM)**  
   - Ideal for companies with regular, predictable dividends  
   - Focuses on the present value of a constant stream of future dividends  
   
   **Typical Formula:**  
   $$\\text{Value} = \\frac{D_1}{r - g}$$  
   Where:  
   - $D_1$ = Dividend expected next year  
   - $r$ = Discount rate  
   - $g$ = Dividend growth rate

3️⃣ **Relative Multiples** (e.g., P/E, EV/EBITDA)  
   - Commonly used for "cash cow" companies  
   - Helps confirm if the market is paying a reasonable price
""")
st.markdown("---")

# ----------------------------------------------------------------------------
# Hidden Dangers in Mature Companies
# ----------------------------------------------------------------------------
st.markdown("### ⚠️ Hidden Dangers — Even in Mature Companies")
st.markdown("""
- **Complacency:** “Everything is fine now, so it will continue to be so” – not always true!
- **Disguised Decline:** A slow drop in revenues can pass unnoticed.
- **Excessive Debt:** Borrowing to sustain dividends can be risky.
- **Forced Dividends:** Companies might pay dividends artificially high to please shareholders.
""")
st.markdown("---")

# ----------------------------------------------------------------------------
# Tips for a Solid Valuation
# ----------------------------------------------------------------------------
st.markdown("### 💡 Tips for a Solid Valuation")
st.markdown("""
✅ Check for consistent earnings in recent years.  
✅ Review the payout ratio (dividends/net income).  
✅ Compare with peers in the same sector.  
✅ Watch long-term trends for structural declines.  
✅ Consider disruption risks (new technologies, global competition).
""")
st.markdown("---")

st.markdown("### 🧠 Key Phrase to Remember")
st.markdown("> *\"Mature companies offer stability, but stability is not synonymous with immortality.\"*")
st.markdown("---")

st.markdown("### 🎓 Pedagogical Analogy")
st.markdown("""
Evaluating a mature company is like caring for a fully grown plant:  
- It doesn't require daily intensive attention.  
- But if you stop watering or ignore pests, it may wither.
""")
st.markdown("---")

# ----------------------------------------------------------------------------
# Mini-Exercise: The DDM Calculation
# ----------------------------------------------------------------------------
st.markdown("### 🛠️ Mini-Exercise for the Classroom")

st.markdown("""
**Given:**  
- A company pays stable dividends of **2€ per share**  
- Discount rate: **8%**  
- Expected growth rate: **2%**

**Question:**  
What would be the value of the share based on the DDM?

**Formula:**  
$$\\text{Value} = \\frac{D_1 \\times (1+g)}{r - g}$$

For this example:  
$$\\text{Value} = \\frac{2 \\times 1.02}{0.08 - 0.02} = \\frac{2.04}{0.06} \\approx 34\\,€$$
""")
st.markdown("---")

st.markdown("### Interactive DDM Calculation")
st.markdown("Adjust the parameters below to compute the share value using DDM:")

# Interactive inputs for DDM
dividend = st.number_input("Dividend per Share (D₀)", value=2.0, step=0.1, format="%.2f")
discount_rate = st.number_input("Discount Rate (r) in %", value=8.0, step=0.5, format="%.2f")
growth_rate = st.number_input("Growth Rate (g) in %", value=2.0, step=0.5, format="%.2f")

# Calculate the expected dividend next year, D₁ = D₀ * (1+g)
D1 = dividend * (1 + growth_rate/100)

# Compute the share value using the DDM formula
# Ensure denominator (r - g) is not zero; convert percentages to decimals.
if discount_rate > growth_rate:
    value = D1 / ((discount_rate - growth_rate) / 100)
    st.write(f"**Calculated Share Value (DDM):** {value:,.2f} €")
else:
    st.error("Discount rate must be greater than growth rate for a valid calculation.")

st.markdown("---")
st.markdown("### Final Takeaway")
st.markdown("""
Mature companies may not have fireworks, but their predictable cash flows and stable fundamentals make them a reliable backbone for an investment portfolio. Always keep in mind that even in maturity, vigilance is key!
""")
