import streamlit as st
import numpy as np
import pandas as pd

# Configure page settings (centered layout works well on mobile)
st.set_page_config(
    page_title="Valuing a Company – An Art, A Science, a Challenge!",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for mobile responsiveness and readability
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

# =============================================================================
# Table of Contents (Optional)
# =============================================================================
st.title("Valuing a Company – An Art, A Science, a Challenge!")
st.markdown("### Table of Contents")
st.markdown("""
1. **Introduction**  
2. **Why Value?**  
3. **Two Worlds, One Mission**  
4. **The Science of Valuation**  
5. **Price vs. Value**  
6. **Types of Valuation**  
7. **Valuation Challenges**  
8. **Common Mistake**  
9. **Get Motivated!**
""")
st.markdown("---")

# =============================================================================
# Section: Introduction
# =============================================================================
st.header("Introduction")
st.markdown("""
**Welcome!**  
Imagine you're about to buy a house—you don’t just admire its looks. You ask:

- **How much is it really worth?**
- **Is it overpriced?**
- **Is it a good deal?**

The same applies to stocks and companies. Valuation acts like a GPS that guides you through the complex world of investments.
""")
st.markdown("---")

# =============================================================================
# Section: Why Value?
# =============================================================================
st.header("Why Value?")
st.markdown("""
**Imagine you're buying a house:**  
You don't settle for its facade. You want to know:

- **How much is it really worth?**
- **Is it overpriced?**
- **Is it a good deal?**

Similarly, when investing in stocks or companies, the market price is just a starting point.  
Valuation tells you the real worth and whether the investment makes sense.

Valuation is the essential tool that prevents you from wandering blindly in the investment world.
""")
st.markdown("---")

# =============================================================================
# Section: Two Worlds, One Mission
# =============================================================================
st.header("Two Worlds, One Mission")
st.markdown("""
There are two main types of investors:

1. **The Technical Analyst (Chartist):**  
   Focuses on charts, trends, and market movements.
2. **The Fundamental Analyst:**  
   Digs deep to understand the real value of a company, like a financial detective.

**Key Insight:**  
Valuation lies at the heart of fundamental analysis, helping you differentiate between what you pay (price) and what you actually receive (value).
""")
st.markdown("---")

# =============================================================================
# Section: The Science of Valuation
# =============================================================================
st.header("The Science of Valuation")
st.markdown("""
Although valuation might seem like a subjective art, it follows a well-defined recipe:

- **Mathematical Models:** Use formulas and projections.
- **Real Financial Data:** Base your analysis on actual financial figures.
- **Rational Assumptions:** Apply logical assumptions about growth and risk.

But… there's also room for professional judgment. Even small differences in your estimates (for example, in growth or risk) can lead to large differences in the final valuation.

**Interactive Exercise:** Adjust the parameters below to see how small changes impact a simplified Discounted Cash Flow (DCF) model.
""")
st.subheader("Discounted Cash Flow (DCF) Calculator")
cash_flow = st.number_input("Expected Annual Cash Flow ($)", value=100000.0, step=10000.0, format="%.2f", key="dcf_cashflow")
growth_rate = st.slider("Growth Rate (%)", min_value=0.0, max_value=20.0, value=5.0, key="dcf_growth")
discount_rate = st.slider("Discount Rate (%)", min_value=0.0, max_value=20.0, value=10.0, key="dcf_discount")
years = st.slider("Projection Period (years)", min_value=1, max_value=20, value=10, key="dcf_years")
dcf_values = [cash_flow * ((1 + growth_rate/100)**year) / ((1 + discount_rate/100)**year) for year in range(1, years+1)]
total_dcf = sum(dcf_values)
st.write("**Estimated Company Value (DCF):** $", f"{total_dcf:,.2f}")
st.markdown("---")

# =============================================================================
# Section: Price vs. Value
# =============================================================================
st.header("Price vs. Value")
st.markdown("""
**The Classic Duel:**  

- **Price:** What the market tells you—the sticker price.
- **Value:** What you, after a deep analysis, believe the company is really worth.

**Secret to Profitable Investing:** Buy when **Value > Price** (i.e., when the stock is undervalued).

Use the graph below to compare a sample stock’s market price and its estimated intrinsic value.
""")
# For demonstration purposes, we reuse the DCF result to generate sample data.
sample_years = list(range(1, 11))
intrinsic = [total_dcf * (1 + i*0.02) for i in range(10)]
market = [total_dcf * (1 + i*0.015) for i in range(10)]
chart_data = pd.DataFrame({
    "Year": sample_years,
    "Intrinsic Value": intrinsic,
    "Market Price": market,
})
st.line_chart(chart_data.set_index("Year"))
st.markdown("---")

# =============================================================================
# Section: Types of Valuation
# =============================================================================
st.header("Types of Valuation – Three Distinct Paths")
st.markdown("""
There are three primary methods to value a company:

1. **Intrinsic Valuation (DCF):**  
   Forecast the future cash flows the company will generate and discount them back to the present.
2. **Relative Valuation (Multiples):**  
   Compare the company with similar firms.
3. **Contingent Valuation (Real Options):**  
   For valuing future opportunities.
""")
st.info("Use the DCF calculator in the 'The Science of Valuation' section to explore intrinsic valuation.")
st.markdown("---")

# =============================================================================
# Section: Valuation Challenges
# =============================================================================
st.header("What Makes Valuation Difficult?")
st.markdown("""
Even with solid methods and data, valuing a company is challenging because:

- **Forecasting Imperfections**
- **Market Emotions**
- **Limited Data**

Continuous practice and a solid knowledge base help refine the process over time.
""")
st.markdown("---")

# =============================================================================
# Section: Common Mistake
# =============================================================================
st.header("The Biggest Mistake: Confusing Value with Price")
st.markdown("""
**Pitfall:**  
“The stock went up 20%—so it must be a good buy!”  

**Reality:**  
A price increase doesn’t necessarily mean that the fundamentals have changed.

**Analogy:**  
Buying a bicycle isn’t just about its looks; it must work properly, last long, and justify the cost.
""")
st.markdown("---")

# =============================================================================
# Section: Get Motivated!
# =============================================================================
st.header("Get Motivated!")
st.markdown("""
**The Art of Valuation is Your Financial Superpower!**

- **Build Confidence:** Learn to make better investment decisions.
- **Prevent Bad Decisions:** Protect yourself from overpaying.
- **Think Like an Analyst:** Empower your investment strategy.

Every step you take in mastering valuation brings you closer to financial independence.
""")
st.markdown("---")

# =============================================================================
# Footer with Licensing and Credit
# =============================================================================
st.markdown("""
---
*Content by Luís Simões da Cunha – Licensed under [CC‑BY‑NC](https://creativecommons.org/licenses/by-nc/4.0/).*
""", unsafe_allow_html=True)
