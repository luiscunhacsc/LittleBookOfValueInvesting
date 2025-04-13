import streamlit as st
import numpy as np
import pandas as pd

# Configure page settings (centered layout works well on mobile)
st.set_page_config(page_title="Valuing a Company – An Art, A Science, a Challenge!", layout="centered", initial_sidebar_state="expanded")

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

# Sidebar navigation: each section is an intuitive step in understanding valuation.
st.sidebar.title("Navigation")
sections = [
    "Introduction",
    "Why Value?",
    "Two Worlds, One Mission",
    "The Science of Valuation",
    "Price vs. Value",
    "Types of Valuation",
    "Valuation Challenges",
    "Common Mistake",
    "Get Motivated!"
]
selection = st.sidebar.radio("Go to", sections)

# =============================================================================
# Section: Introduction
# =============================================================================
if selection == "Introduction":
    st.title("Valuing a Company – An Art, a Science, and a Challenge!")
    st.markdown("""
    **Welcome!**  
    Imagine you're about to buy a house—you don’t just admire its looks. You ask:
    
    - **How much is it really worth?**
    - **Is it overpriced?**
    - **Is it a good deal?**
    
    The same applies to stocks and companies. Valuation acts like a GPS that guides you through the complex world of investments.
    """)
    st.image("https://via.placeholder.com/700x300.png?text=Valuation+Journey", use_column_width=True)
    st.markdown("---")

# =============================================================================
# Section: Why Value?
# =============================================================================
elif selection == "Why Value?":
    st.header("Why Value?")
    st.markdown("""
    **Imagine you're buying a house:**  
    You don't settle for its facade. You want to know:
    
    - **How much is it really worth?**
    - **Is it overpriced?**
    - **Is it a good deal?**
    
    Similarly, when investing in stocks or companies, the market price is just a starting point. Valuation tells you the real worth and whether the investment makes sense.
    
    Valuation is the essential tool that prevents you from wandering blindly in the investment world.
    """)
    st.markdown("---")

# =============================================================================
# Section: Two Worlds, One Mission
# =============================================================================
elif selection == "Two Worlds, One Mission":
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
elif selection == "The Science of Valuation":
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
    cash_flow = st.number_input("Expected Annual Cash Flow ($)", value=100000.0, step=10000.0, format="%.2f")
    growth_rate = st.slider("Growth Rate (%)", min_value=0.0, max_value=20.0, value=5.0)
    discount_rate = st.slider("Discount Rate (%)", min_value=0.0, max_value=20.0, value=10.0)
    years = st.slider("Projection Period (years)", min_value=1, max_value=20, value=10)
    
    # Calculate DCF using a simple model
    dcf_values = [cash_flow * ((1 + growth_rate/100)**year) / ((1 + discount_rate/100)**year) for year in range(1, years+1)]
    total_dcf = sum(dcf_values)
    st.write("**Estimated Company Value (DCF):** $", f"{total_dcf:,.2f}")
    st.markdown("---")

# =============================================================================
# Section: Price vs. Value
# =============================================================================
elif selection == "Price vs. Value":
    st.header("Price vs. Value")
    st.markdown("""
    **The Classic Duel:**  
    
    - **Price:** What the market tells you—the sticker price.
    - **Value:** What you, after a deep analysis, believe the company is really worth.
    
    **Secret to Profitable Investing:** Buy when **Value > Price** (i.e., when the stock is undervalued).
    
    Use the graph below to compare a sample stock’s market price and its estimated intrinsic value.
    """)
    
    # Example data for demonstration purposes
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
elif selection == "Types of Valuation":
    st.header("Types of Valuation – Three Distinct Paths")
    st.markdown("""
    There are three primary methods to value a company:
    """)
    
    st.markdown("### 1. Intrinsic Valuation (Discounted Cash Flow - DCF)")
    st.markdown("""
    - **Concept:**  
      Forecast the future cash flows the company will generate and discount them back to the present (using a discount rate).  
      It’s akin to asking, “What is today's value of the money I will receive tomorrow?”
      
    - **Estimates Required:**  
      - Future profits  
      - Growth rates  
      - Risk (represented by the discount rate)
    """)
    
    st.info("Use the DCF calculator in the 'The Science of Valuation' section above to explore intrinsic valuation.")
    
    st.markdown("### 2. Relative Valuation (Multiples)")
    st.markdown("""
    - **Concept:**  
      Compare the company with similar ones. For instance, if one company is valued at 10 times its earnings, how does that compare to its peers?
      
    - **Analogy:**  
      It’s like comparing houses in the same neighborhood. If one is priced significantly higher, you might wonder if it’s really worth it.
      
    - **Tradeoff:**  
      This method is simpler and faster, though it is less precise.
    """)
    st.subheader("Relative Valuation Calculator")
    earnings = st.number_input("Enter the Company's Earnings ($)", value=500000.0, step=50000.0, format="%.2f")
    multiple = st.number_input("Enter the P/E Multiple", value=10.0, step=1.0)
    relative_value = earnings * multiple
    st.write("**Estimated Company Value (Relative):** $", f"{relative_value:,.2f}")
    
    st.markdown("### 3. Contingent Valuation (Real Options)")
    st.markdown("""
    - **Concept:**  
      Incorporates financial option theory to value future opportunities (for example, the option to expand, to halt operations, or to sell parts of the business).
      
    - **Usage:**  
      Especially useful for companies facing significant uncertainty where management decisions can dramatically influence future cash flows.
    """)
    st.subheader("Real Options Simulation")
    baseline_value = st.number_input("Baseline Company Value ($)", value=relative_value, step=10000.0, format="%.2f")
    expansion_gain = st.number_input("Potential Value Increase if Expanded ($)", value=50000.0, step=5000.0, format="%.2f")
    success_prob = st.slider("Probability of Successful Expansion (%)", min_value=0, max_value=100, value=70)
    # Calculate expected extra value from the option
    option_value = baseline_value + expansion_gain * (success_prob/100)
    st.write("**Estimated Company Value with Expansion Option:** $", f"{option_value:,.2f}")
    
    st.markdown("---")

# =============================================================================
# Section: Valuation Challenges
# =============================================================================
elif selection == "Valuation Challenges":
    st.header("What Makes Valuation Difficult?")
    st.markdown("""
    Even with solid methods and data, valuing a company is challenging because:
    
    - **Forecasting Imperfections:**  
      No one can predict the future perfectly.
      
    - **Market Emotions:**  
      Prices can be driven by sentiment rather than fundamentals.
      
    - **Limited Data:**  
      Sometimes, you don't have access to all the information needed.
      
    Continuous practice, common sense, and a solid knowledge base help refine the process over time.
    """)
    
    # Simple interactive quiz to reinforce understanding
    st.subheader("Quick Quiz: What do you think is the most challenging factor in valuation?")
    challenge = st.radio("Select the biggest challenge:", options=[
        "Forecasting Imperfections",
        "Market Emotions",
        "Limited Data",
        "All of the Above"
    ])
    if challenge:
        if challenge == "All of the Above":
            st.success("Correct! All these factors contribute to the difficulty in valuation.")
        else:
            st.error("That’s one factor, but in practice, all these challenges play a role.")
    
    st.markdown("---")

# =============================================================================
# Section: Common Mistake
# =============================================================================
elif selection == "Common Mistake":
    st.header("The Biggest Mistake: Confusing Value with Price")
    st.markdown("""
    **Pitfall:**  
    “The stock went up 20%—so it must be a good buy!”  
    **Reality:**  
    A price increase doesn’t necessarily mean that the fundamentals have changed.
    
    **Analogy:**  
    Buying a bicycle isn’t just about its looks. It must work properly, last long, and justify the cost.
    """)
    st.subheader("Test Your Understanding")
    mistake_quiz = st.radio("What should you focus on when investing?", 
                              options=["Market Price", "Intrinsic Value", "Both Equally", "None"])
    if mistake_quiz:
        if mistake_quiz == "Intrinsic Value":
            st.success("Correct! Focus on the intrinsic value rather than just the market price.")
        else:
            st.error("Not quite. Remember, investing smartly means focusing on what the company is really worth.")
    
    st.markdown("---")

# =============================================================================
# Section: Get Motivated!
# =============================================================================
elif selection == "Get Motivated!":
    st.header("Get Motivated!")
    st.markdown("""
    **The Art of Valuation is Your Financial Superpower!**
    
    - **Build Confidence:**  
      With proper valuation skills, you can make better investment decisions.
      
    - **Prevent Bad Decisions:**  
      A solid analysis protects you from overpaying or falling for market hype.
      
    - **Think Like an Analyst:**  
      Learning to value a company empowers you to think critically about every investment.
      
    Even if you're not a professional fund manager or analyst, knowing how to value an asset is like learning to cook—you gain independence and a better understanding, reducing reliance on others.
    """)
    st.markdown("Remember: Every step you take in mastering valuation brings you closer to financial independence and smarter investing!")
    st.markdown("---")

# =============================================================================
# Footer with Licensing and Credit
# =============================================================================
st.markdown("""
---
*Content by Luís Simões da Cunha – Licensed under [CC‑BY‑NC](https://creativecommons.org/licenses/by-nc/4.0/).*
""", unsafe_allow_html=True)
