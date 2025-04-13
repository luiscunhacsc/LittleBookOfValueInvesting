import streamlit as st
import numpy as np
import pandas as pd

# Configure the Streamlit app
st.set_page_config(
    page_title="Valuation Masterclass",
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

# Sidebar navigation
st.sidebar.title("Valuation Topics")
section = st.sidebar.radio(
    "Select a Topic",
    [
        "0. Valuing a Company",
        "1. Intrinsic Value",
        "2. Relative Valuation",
        "3. Growth Companies",
        "4. Mature Companies",
        "5. Cyclical Companies",
        "6. Financial Companies"
    ]
)

# Main content based on selection
if section == "0. Valuing a Company":
    st.title("Valuing a Company – An Art, A Science, a Challenge!")
    st.markdown("---")

    # Introduction
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

    # Why Value?
    st.header("Why Value?")
    st.markdown("""
    Similarly, when investing in stocks or companies, the market price is just a starting point.  
    Valuation tells you the real worth and whether the investment makes sense.
    
    Valuation is the essential tool that prevents you from wandering blindly in the investment world.
    """)
    st.markdown("---")

    # Two Worlds, One Mission
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

    # The Science of Valuation
    st.header("The Science of Valuation")
    st.markdown("""
    Although valuation might seem like a subjective art, it follows a well-defined recipe:
    - **Mathematical Models:** Use formulas and projections.
    - **Real Financial Data:** Base your analysis on actual financial figures.
    - **Rational Assumptions:** Apply logical assumptions about growth and risk.
    
    But… there's also room for professional judgment. Even small differences in your estimates (for example, in growth or risk) can lead to large differences in the final valuation.
    """)
    st.subheader("Discounted Cash Flow (DCF) Calculator")
    cash_flow = st.number_input("Expected Annual Cash Flow ($)", value=100000.0, step=10000.0, format="%.2f")
    growth_rate = st.slider("Growth Rate (%)", min_value=0.0, max_value=20.0, value=5.0)
    discount_rate = st.slider("Discount Rate (%)", min_value=0.0, max_value=20.0, value=10.0)
    years = st.slider("Projection Period (years)", min_value=1, max_value=20, value=10)
    dcf_values = [cash_flow * ((1 + growth_rate/100)**year) / ((1 + discount_rate/100)**year) for year in range(1, years+1)]
    total_dcf = sum(dcf_values)
    st.write("**Estimated Company Value (DCF):** $", f"{total_dcf:,.2f}")
    st.markdown("---")

    # Price vs. Value
    st.header("Price vs. Value")
    st.markdown("""
    **The Classic Duel:**  
    - **Price:** What the market tells you—the sticker price.
    - **Value:** What you, after a deep analysis, believe the company is really worth.
    
    **Secret to Profitable Investing:** Buy when **Value > Price** (i.e., when the stock is undervalued).
    """)
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

    # Types of Valuation
    st.header("Types of Valuation")
    st.markdown("""
    There are three primary methods to value a company:
    1. **Intrinsic Valuation (DCF):**  
       Forecast the future cash flows the company will generate and discount them back to the present.
    2. **Relative Valuation (Multiples):**  
       Compare the company with similar firms.
    3. **Contingent Valuation (Real Options):**  
       For valuing future opportunities.
    """)
    st.markdown("---")

    # Valuation Challenges
    st.header("Valuation Challenges")
    st.markdown("""
    Even with solid methods and data, valuing a company is challenging because:
    - **Forecasting Imperfections**
    - **Market Emotions**
    - **Limited Data**
    
    Continuous practice and a solid knowledge base help refine the process over time.
    """)
    st.markdown("---")

    # Common Mistake
    st.header("Common Mistake")
    st.markdown("""
    **Pitfall:**  
    “The stock went up 20%—so it must be a good buy!”  
    
    **Reality:**  
    A price increase doesn’t necessarily mean that the fundamentals have changed.
    
    **Analogy:**  
    Buying a bicycle isn’t just about its looks; it must work properly, last long, and justify the cost.
    """)
    st.markdown("---")

    # Get Motivated!
    st.header("Get Motivated!")
    st.markdown("""
    **The Art of Valuation is Your Financial Superpower!**
    - **Build Confidence:** Learn to make better investment decisions.
    - **Prevent Bad Decisions:** Protect yourself from overpaying.
    - **Think Like an Analyst:** Empower your investment strategy.
    
    Every step you take in mastering valuation brings you closer to financial independence.
    """)
    st.markdown("---")

elif section == "1. Intrinsic Value":
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

    st.markdown("#### 2️⃣ Choose the Projection Horizon")
    st.markdown("""
    Typically, you choose a projection horizon of **5 to 10 years**.  
    After this period, we assume a stable growth and use a terminal value calculation.  
    *Think of it like a train that accelerates and then cruises at a steady speed.*
    """)
    st.markdown("---")

    st.markdown("#### 3️⃣ Estimate the Discount Rate")
    st.markdown("""
    The discount rate reflects the risk of the company.  
    - More stable companies (like large, established firms) → lower discount rate  
    - Riskier companies (startups, companies in unstable regions) → higher discount rate
    
    For companies, we usually use the WACC (Weighted Average Cost of Capital).
    """)
    discount_rate = st.slider("Discount Rate (%)", min_value=0.0, max_value=20.0, value=10.0)
    st.markdown("---")

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
    if discount_rate > g_rate:
        terminal_value = cash_flows[-1] * (1 + g_rate/100) / ((discount_rate/100) - (g_rate/100))
        terminal_value_pv = terminal_value / ((1 + discount_rate/100)**years)
        st.write("**Present Value of Terminal Value:** $", f"{terminal_value_pv:,.2f}")
        
        intrinsic_value = total_pv + terminal_value_pv
        st.markdown("### 📊 Calculated Intrinsic Value")
        st.write("**Intrinsic Value (based on DCF):** $", f"{intrinsic_value:,.2f}")
    else:
        st.error("Discount rate must be greater than growth rate for a valid terminal value.")
    st.markdown("---")

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

    st.markdown("### 💬 Special Considerations for Young or Uncertain Companies")
    st.markdown("""
    Young companies, those with losses or inconsistent histories, require:
    - More assumptions
    - Greater prudence
    - Sometimes even alternative methods (such as real options)
    """)
    st.markdown("---")

    st.markdown("### 📊 Why DCF is Still the Gold Standard")
    st.markdown("""
    The DCF method forces us to think about the fundamentals of a company:
    - **How does it generate cash?**
    - **How much does it reinvest?**
    - **What is the real risk?**
    
    It isn’t magic—it’s a practical tool for better understanding and evaluating businesses.
    """)
    st.markdown("---")

    st.markdown("### 🧠 Final Thought")
    st.markdown("> *\"The value of an asset is determined by the expected cash flows and the risk associated with them.\"*")

elif section == "2. Relative Valuation":
    st.title("🧭 Relative Valuation – The Game of Comparisons")
    st.markdown("""
    ### 🎯 What is Relative Valuation?
    It’s like looking at houses in the same neighborhood:
    - One house with 3 rooms costs **€300,000**
    - Another, also with 3 rooms, costs **€400,000**
    
    Naturally, you ask: *"What justifies the difference?"*  
    Relative valuation does exactly that – but with companies!
    """)
    st.markdown("---")

    st.markdown("""
    ### ⚖️ Relative Price vs. Absolute Value
    While intrinsic valuation asks, *"How much is this company worth by its own merits?"*  
    Relative valuation asks,  
    *"How much is this company worth compared to other similar companies?"*  
    It forces you to consider:
    - **“This stock seems cheap… but cheap compared to what?”**
    """)
    st.markdown("---")

    st.markdown("""
    ### 🔢 Multiples: The Units of Comparison
    Multiples are simple formulas that relate market price to a performance measure. Common examples include:
    
    | **Multiple**          | **Meaning**                                                                 |
    |-----------------------|------------------------------------------------------------------------------|
    | **P/E (Price/Earnings)**    | How much investors are paying for each € of profit                       |
    | **EV/EBITDA**         | How the entire firm (debt + equity) is valued relative to its operating results |
    | **P/BV (Price/Book Value)** | How much you pay for each € of net assets                                |
    | **P/Sales**           | How much you pay for each € of generated sales                               |
    
    These multiples serve as "quick measures" for comparing companies but should be used carefully.
    """)
    st.markdown("---")

    st.markdown("""
    ### 🕵️‍♂️ Steps for a Good Relative Valuation
    1️⃣ **Choose the Right Multiple:**  
       Depends on the sector and type of company.  
       *Example: Tech startups → P/Sales; Banks → P/BV; Mature companies → P/E*  
       **Golden Rule:** Use multiples aligned with the company's value creation.
    
    2️⃣ **Choose the Peer Group:**  
       Compare companies similar in:
       - Sector  
       - Size  
       - Risk  
       - Business model  
       *Example: Don't compare Apple with a tiny mobile app startup.*
    
    3️⃣ **Analyze the Differences:**  
       If a company has a much lower multiple than its peers, it might seem undervalued—but only if there’s no structural reason for that difference.  
       Always ask: **“Is this discount justified or is it an opportunity?”**
    """)
    st.markdown("---")

    st.markdown("""
    ### 💣 Traps to Avoid
    1. **Superficial Comparisons:**  
       Using multiples without understanding the fundamentals can be misleading.
    2. **Not Adjusting for Real Differences:**  
       Companies might appear similar but differ in risk, growth, or debt.
    3. **Taking Multiples as Absolute Truth:**  
       Multiples are symptoms – proper diagnosis requires deeper analysis!
    """)
    st.markdown("---")

    st.markdown("""
    ### 🤖 Statistical Adjustment Methods
    To avoid unfair comparisons, you might use:
    - Regressions (e.g. P/E adjusted for growth)
    - Sector median multiples
    - Standard deviation and z-scores
    
    These methods help assess how far a company's multiple deviates from the norm.
    """)
    st.markdown("---")

    st.markdown("""
    ### 🧠 A Concrete Example
    Imagine:
    - **Company A** has a P/E of **10**
    - **Company B** (in the same sector) has a P/E of **15**
    
    A hasty conclusion might be: “Company A is cheap!”  
    But consider:
    - Is Company A’s profit declining?
    - Does it carry huge debt?
    - Is it facing regulatory risks?
    
    A low multiple might actually be a red flag, not a buying opportunity.
    
    > *"A multiple doesn’t tell you the value. It tells you where to look."*
    """)
    st.markdown("---")

    st.header("Interactive Relative Valuation Example")
    st.markdown("""
    In this exercise, we’ll compare the target company’s P/E ratio with those of its peer group.  
    Enter the values below and see how the target company compares!
    """)
    target_pe = st.number_input("Enter the target company's P/E ratio:", min_value=0.0, value=10.0, step=0.1)
    n_peers = st.number_input("Number of peer companies:", min_value=1, max_value=20, value=3, step=1)
    peer_pe = []
    for i in range(1, int(n_peers)+1):
        value = st.number_input(f"Enter P/E ratio for Peer {i}:", min_value=0.0, value=12.0, step=0.1, key=f"peer_{i}")
        peer_pe.append(value)
    
    peer_pe = np.array(peer_pe)
    median_pe = np.median(peer_pe)
    std_pe = np.std(peer_pe)
    
    st.markdown("#### Peer Group Analysis")
    st.write("**Median P/E of Peer Group:**", median_pe)
    st.write("**Standard Deviation of P/E:**", std_pe)
    
    if target_pe < median_pe:
        st.success("The target company's P/E is below the peer median, which may indicate undervaluation. However, further analysis is necessary!")
    elif target_pe == median_pe:
        st.info("The target company's P/E is equal to the peer median.")
    else:
        st.error("The target company's P/E is above the peer median, which may indicate it is overvalued compared to its peers.")
    
    st.markdown("---")
    st.markdown("### Final Interactive Observation")
    st.markdown("""
    Relative valuation is a fast method to get an initial sense of whether a company might be mispriced.  
    **Remember:**
    - Adjust for differences in growth, risk, and debt.
    - Use statistical methods to refine your analysis.
    - Multiples are a starting point – they guide you, but do not provide definitive answers.
    """)

elif section == "3. Growth Companies":
    st.title("🚀 Valuing Growth Companies: Between Potential and Danger")
    st.markdown("""
    ### 🧨 The Challenge
    Many promising companies are not yet profitable—or even have chronic losses.  
    Yet the market believes in them, and investors bet strongly.  
    **How do you value something that is not yet generating cash?**
    """)
    st.markdown("---")

    st.markdown("""
    ### 🎢 Growth Companies: A Roller Coaster Ride
    - **Exciting journey:** They promise a thrilling ride.
    - **Future confidence:** They require belief in their future.
    - **Careful analysis:** It is essential to determine whether the ride leads to success—or an impending derailment.
    """)
    st.markdown("---")

    st.markdown("""
    ### 🏗️ Phases of Growth — The Life Curve of Companies
    1. **Startup Phase**  
       - Low revenues, recurring losses  
       - Extremely high risk  
       - But enormous growth potential
    2. **Expansion Phase**  
       - Accelerating revenues  
       - Profits are still small (or even nil)  
       - Growth begins to pave the way
    3. **Maturity Phase**  
       - Slowing growth  
       - Stabilized margins  
       - Consistent profitability emerges  
    
    **Key:** The secret lies in knowing in which phase the company is—and how it will transition to the next.
    """)
    st.markdown("---")

    st.markdown("""
    ### 📐 Adapting the DCF Model to Tough Realities
    **Fundamental Adjustments:**
    1. **Forecast Negative Cash Flows:**  
       Instead of ignoring losses, model them—including the need for additional capital (future financing).
    2. **Longer Projection Period:**  
       Often 10–15 years are needed until the company reaches a "stable" phase.
    3. **Variable Growth:**  
       Apply different growth rates over time—high at first, then gradually decreasing, and finally stabilizing.
    4. **Risk-Adjusted Discount Rates:**  
       Use higher rates initially (when risk is greater), then lower them as the company matures.
    """)
    st.markdown("---")

    st.markdown("""
    ### 💡 Tip: The Value is in the Future, Not the Present  
    The key is the potential future profits—and your ability to estimate them rationally.
    """)
    st.markdown("---")

    st.markdown("""
    ### 🧮 Simplified Example  
    Imagine a company that:
    - Has losses during the **first 3 years**.
    - Begins generating profits in the **4th year**.
    - Achieves stability by the **8th year**.
    
    Your DCF model must include:
    - **Negative cash flows** at the beginning.
    - The **need to raise capital** (dilution may occur).
    - **Non-linear growth.**
    - A **terminal value** after the stabilization phase.
    """)
    st.markdown("---")

    st.markdown("""
    ### 🧨 Hidden Risks
    1. **Underestimating Time to Profitability:**  
       Companies often take longer to become profitable than expected.
    2. **Overly Optimistic Assumptions:**  
       High margins? Eternal growth?
    3. **Shareholder Dilution:**  
       Extensive capital raises can shrink your ownership stake.
    4. **Fierce Competition:**  
       A promising sector might attract too many competitors.
    """)
    st.markdown("---")

    st.markdown("""
    ### 🔐 Strategies to Reduce Uncertainty
    - **Use Multiple Scenarios:**  
      *Optimistic, Realistic, and Conservative.*
    - **Perform Sensitivity Analysis:**  
      For instance:  
      - What if growth is 2% lower?  
      - What if profitability is delayed by 2 years?
    - **Consider Exit Strategies:**  
      IPO? Acquisition?
    """)
    st.markdown("---")

    st.markdown("""
    ### 🧠 Key Takeaway
    > *"In a growth company, value is not in what it is today—but in what it could become tomorrow."*
    """)
    st.markdown("---")

    st.markdown("""
    ### 🎓 Fundamental Lesson
    Valuing growth companies requires more than just formulas—it demands strategic vision, financial realism, and a dash of informed intuition.  
    It's like planting a tree:
    - You water it for years.
    - No fruits are visible in the early stages.
    - But one day, it might yield a generous harvest.
    """)
    st.markdown("---")

    st.header("Interactive DCF Model for a Growth Company")
    st.markdown("Adjust the parameters below to model a growth company’s cash flows across different phases:")
    
    st.subheader("1. Define Growth Phases")
    col1, col2 = st.columns(2)
    with col1:
        startup_years = st.number_input("Years in Startup Phase (losses)", min_value=0, max_value=10, value=3, step=1)
        expansion_years = st.number_input("Years in Expansion Phase", min_value=1, max_value=10, value=3, step=1)
    with col2:
        maturity_years = st.number_input("Years in Maturity Phase", min_value=1, max_value=20, value=2, step=1)
    total_years = startup_years + expansion_years + maturity_years
    st.markdown(f"**Total Projection Period:** {total_years} years")
    
    st.subheader("2. Cash Flows Input")
    st.markdown("Enter the average annual cash flows for each phase:")
    
    startup_cf = st.number_input("Average Annual Cash Flow in Startup Phase (negative)", value=-50000.0, step=1000.0)
    expansion_initial_cf = st.number_input("Cash Flow at the Start of Expansion Phase", value=20000.0, step=1000.0)
    expansion_growth_rate = st.slider("Annual Growth Rate during Expansion Phase (%)", min_value=0.0, max_value=50.0, value=20.0)
    maturity_growth_rate = st.slider("Annual Growth Rate during Maturity Phase (%)", min_value=0.0, max_value=20.0, value=5.0)
    
    st.subheader("3. Discount Rate and Scenario")
    st.markdown("Select a scenario for discount rate adjustment:")
    scenario = st.radio("Scenario", options=["Optimistic", "Realistic", "Conservative"], index=1)
    
    if scenario == "Optimistic":
        discount_rate = st.number_input("Discount Rate (%)", value=12.0, step=0.5)
    elif scenario == "Realistic":
        discount_rate = st.number_input("Discount Rate (%)", value=15.0, step=0.5)
    else:
        discount_rate = st.number_input("Discount Rate (%)", value=18.0, step=0.5)
    
    st.markdown("---")
    
    st.markdown("### Calculating Cash Flows and Present Values")
    cash_flow_series = []
    
    for t in range(1, startup_years + 1):
        cash_flow_series.append(startup_cf)
    
    cf = expansion_initial_cf
    for t in range(startup_years + 1, startup_years + expansion_years + 1):
        cash_flow_series.append(cf)
        cf = cf * (1 + expansion_growth_rate / 100)
    
    for t in range(startup_years + expansion_years + 1, total_years + 1):
        cash_flow_series.append(cf)
        cf = cf * (1 + maturity_growth_rate / 100)
    
    st.write("**Projected Cash Flows (by year):**")
    st.write(cash_flow_series)
    
    pv_values = [cf / ((1 + discount_rate / 100) ** t) for t, cf in enumerate(cash_flow_series, start=1)]
    total_pv = np.sum(pv_values)
    st.write("**Total Present Value of Cash Flows:** $", f"{total_pv:,.2f}")
    
    st.markdown("### Terminal Value Calculation")
    st.markdown(r"""
    Assuming the company reaches a stable state at the end of the projection period, we calculate the Terminal Value using:
    
    $$\text{Terminal Value} = \frac{FCF_{last} \times (1+g)}{(r - g)}$$
    
    Where:
    - $FCF_{last}$ is the cash flow in the final projected year
    - $g$ is the long-term stable (maturity) growth rate
    - $r$ is the discount rate
    """)
    if discount_rate > maturity_growth_rate:
        terminal_value = cash_flow_series[-1] * (1 + maturity_growth_rate / 100) / ((discount_rate / 100) - (maturity_growth_rate / 100))
        terminal_value_pv = terminal_value / ((1 + discount_rate / 100) ** total_years)
        st.write("**Present Value of Terminal Value:** $", f"{terminal_value_pv:,.2f}")
        
        intrinsic_value = total_pv + terminal_value_pv
        st.markdown("### 📊 Calculated Intrinsic Value for the Growth Company")
        st.write("**Intrinsic Value (DCF):** $", f"{intrinsic_value:,.2f}")
    else:
        st.error("Discount rate must be greater than maturity growth rate for a valid terminal value.")
    
    st.markdown("---")
    st.markdown("### Interactive Analysis")
    st.markdown("""
    **Observe the impact of changes:**  
    - Adjust the number of years in each phase.  
    - Modify cash flow inputs and growth rates.  
    - Experiment with different discount rate scenarios.
    
    Valuing growth companies is challenging due to initial losses, non-linear growth, and uncertainty in reaching profitability.  
    Use these tools to refine your analysis and better understand the risk-return trade-offs.
    """)

elif section == "4. Mature Companies":
    st.title("🧓 Evaluating Mature Companies: Less Fireworks, More Reliability")
    st.markdown("""
    ### 🧭 The Scenario
    Mature companies have already passed the turbulent growth phases:
    - **Modest growth** 📉  
    - **Saturated market** 🧱  
    - **Predictable cash flows** 💰  
    
    They may not look exciting, but they often form the backbone of a solid portfolio.
    """)
    st.markdown("---")

    st.markdown("""
    ### 🎯 The Valuation Objective
    The goal here is not to discover a "unicorn" but to determine whether the current market price accurately reflects the stable fundamentals of the company.
    """)
    st.markdown("---")

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

    st.markdown("### ⚠️ Hidden Dangers — Even in Mature Companies")
    st.markdown("""
    - **Complacency:** “Everything is fine now, so it will continue to be so” – not always true!
    - **Disguised Decline:** A slow drop in revenues can pass unnoticed.
    - **Excessive Debt:** Borrowing to sustain dividends can be risky.
    - **Forced Dividends:** Companies might pay dividends artificially high to please shareholders.
    """)
    st.markdown("---")

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
    
    dividend = st.number_input("Dividend per Share (D₀)", value=2.0, step=0.1, format="%.2f")
    discount_rate = st.number_input("Discount Rate (r) in %", value=8.0, step=0.5, format="%.2f")
    growth_rate = st.number_input("Growth Rate (g) in %", value=2.0, step=0.5, format="%.2f")
    
    D1 = dividend * (1 + growth_rate/100)
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

elif section == "5. Cyclical Companies":
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

    st.header("Interactive Exercise: Normalized P/E Calculation")
    st.markdown("""
    Fill in the details below to calculate the normalized P/E of a cyclical company.
    """)
    
    current_profit = st.number_input("Current Profit (in millions €)", min_value=0.0, value=10.0, step=0.5)
    normalized_profit = st.number_input("Average Profit over the Last 10 Years (in millions €)", min_value=0.0, value=6.0, step=0.5)
    current_pe = st.number_input("Current P/E", min_value=0.0, value=8.0, step=0.1)
    
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

elif section == "6. Financial Companies":
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

    st.header("Interactive Exercise: Fair P/BV Calculation")
    st.markdown("""
    Fill in the details below to calculate the fair Price-to-Book (P/BV) ratio using the magic formula.
    """)
    
    roe = st.number_input("Enter the ROE (as a percentage)", value=12.0, step=0.5, format="%.2f")
    cost_of_capital = st.number_input("Enter the Cost of Capital (r) in %", value=10.0, step=0.5, format="%.2f")
    expected_growth = st.number_input("Enter the Expected Growth Rate (g) in %", value=4.0, step=0.5, format="%.2f")
    
    roe_decimal = roe / 100
    cost_decimal = cost_of_capital / 100
    growth_decimal = expected_growth / 100
    
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

# Footer
st.markdown("---")
st.markdown("""
<div class="footer">
*Content by Luís Simões da Cunha – Licensed under <a href="https://creativecommons.org/licenses/by-nc/4.0/">CC‑BY‑NC</a>.*
</div>
""", unsafe_allow_html=True)