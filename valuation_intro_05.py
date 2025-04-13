import streamlit as st
import pandas as pd
import numpy as np

# Configure the Streamlit app
st.set_page_config(page_title="Evaluating Cyclical Companies", layout="centered", initial_sidebar_state="expanded")

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
# Title and Introduction
# ----------------------------------------------------------------------------
st.title("🎢 Evaluating Cyclical Companies: The Rhythm of Ups and Downs")

st.markdown("""
### What Are Cyclical Companies?
These are companies whose performance depends strongly on the economic cycle.

**Classic Examples:**
- Automobiles 🚗  
- Steel & Aluminum 🏗️  
- Tourism 🏖️  
- Construction 🧱  
- Aviation ✈️  

When the economy is booming → profits soar 📈  
When it slows down → profits evaporate 📉 (or losses may even occur!)
""")
st.markdown("---")

st.markdown("""
### Market Seasons
Cyclical companies go through cycles:
- **Expansion:** Demand and profits rise.
- **Cycle Peak:** Maximum margins, high optimism.
- **Recession:** Sharp decline in demand and profits.
- **Recovery:** Slow rise back up.

Evaluating them is like trying to estimate the average height of a wave… while you’re surfing it 🌊.
""")
st.markdown("---")

st.markdown("""
### The Most Common Mistake in Cyclical Evaluation
Using current profits as if they were sustainable in the future.  
If you value a cyclical company at the peak of its cycle, you might fall into the trap of:
- Believing that those high profits will last.
- Relying on misleading multiples (P/E, EV/EBITDA).
""")
st.markdown("---")

st.markdown("""
### How to Evaluate with More Rigor
1️⃣ **Use Normalized Earnings:**  
   Estimate the average profit over a full cycle (e.g., the past 10 years) to eliminate extremes (peaks and valleys).  
   *Key Term:* **Earnings Power** – the average ability to generate profit in normal conditions.

2️⃣ **Avoid Short-Term Earnings Models:**  
   While a DCF model can still work, it is more reliable when based on normalized cash flows using longer projection periods and conservative margins.

3️⃣ **Relative Valuation with Cyclical Peers:**  
   Compare only with companies at the same point in the cycle.  
   *For example:* Do not compare Ford (at the bottom of the cycle) with Tesla (in an expansion phase), even if both sell cars.
""")
st.markdown("---")

st.markdown("""
### Golden Tip: Look at the Cycle, Not the Moment
"A P/E of 6 may seem cheap—until you realize that if profits are at their peak, the 'E' will fall and the P/E will skyrocket."
""")
st.markdown("---")

st.markdown("""
### Pedagogical Example
Consider a cyclical company with the following data:
- **Current Profit:** €10M  
- **Average (Normalized) Profit over the Last 10 Years:** €6M  
- **Current P/E:** 8  

At first glance, a P/E of 8 might seem attractive (Market Price = 10M × 8 = €80M).  
However, if the sustainable profit is only €6M, then the **Normalized P/E** is:
  
$$ P/E_{normalized} = \\frac{\\text{Market Price}}{\\text{Average Profit}} = \\frac{80M}{6M} \\approx 13.3 $$

In other words, it may not be as cheap as it initially appears!
""")
st.markdown("---")

st.markdown("""
### Other Useful Tools
- **Revenue-Based Multiples:**  
  When profits oscillate too much, revenue can provide a more stable basis.
- **Sector and Macroeconomic Analysis:**  
  Understanding where we are in the cycle is vital.
""")
st.markdown("---")

st.markdown("""
### Key Phrase to Remember
*"Don’t value a cyclical company at the top of the mountain; wait for the plateau view."*
""")
st.markdown("---")

st.markdown("""
### Evaluating Risk
Cyclical companies require:
- A higher margin of safety.
- Stress testing.
- More conservative assumptions for cash flows and growth rates.
""")
st.markdown("---")

st.markdown("""
### Classroom Analogy
Evaluating cyclical companies is like preparing a farmer for all seasons:
- In summer, everything seems wonderful 🌞.
- But winter will come ❄️.
A good evaluation plan must anticipate both.
""")
st.markdown("---")

# ----------------------------------------------------------------------------
# Interactive Mini-Exercise: Normalized P/E Calculation
# ----------------------------------------------------------------------------
st.header("Interactive Exercise: Normalized P/E Calculation")

st.markdown("""
Fill in the details below to calculate the normalized P/E of a cyclical company.
""")

# Input interactive parameters
current_profit = st.number_input("Current Profit (in millions €)", min_value=0.0, value=10.0, step=0.5)
normalized_profit = st.number_input("Average Profit over the Last 10 Years (in millions €)", min_value=0.0, value=6.0, step=0.5)
current_pe = st.number_input("Current P/E", min_value=0.0, value=8.0, step=0.1)

# Calculate the market price and normalized P/E
market_price = current_profit * current_pe

if normalized_profit > 0:
    normalized_pe = market_price / normalized_profit
    st.write(f"**Market Price:** € {market_price:.2f} million")
    st.write(f"**Normalized P/E:** {normalized_pe:.2f}")
else:
    st.error("The average profit over the last 10 years must be greater than zero to calculate the normalized P/E.")

st.markdown("---")

st.markdown("""
### Final Thoughts
Remember: when evaluating cyclical companies, it is essential not to get caught up with peak-cycle numbers.  
Use normalized earnings to obtain a realistic view of the company’s sustainable potential.
""")
