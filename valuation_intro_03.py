import streamlit as st
import numpy as np

# Configure the Streamlit app
st.set_page_config(page_title="Valuing Growth Companies", layout="centered", initial_sidebar_state="expanded")

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

# Title and descriptive text
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

# Interactive DCF model for a growth company
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

# Startup phase: average negative cash flow
startup_cf = st.number_input("Average Annual Cash Flow in Startup Phase (negative)", value=-50000.0, step=1000.0)

# Expansion phase: initial positive cash flow and growth rate during expansion
expansion_initial_cf = st.number_input("Cash Flow at the Start of Expansion Phase", value=20000.0, step=1000.0)
expansion_growth_rate = st.slider("Annual Growth Rate during Expansion Phase (%)", min_value=0.0, max_value=50.0, value=20.0)

# Maturity phase: growth rate during the stable maturity phase
maturity_growth_rate = st.slider("Annual Growth Rate during Maturity Phase (%)", min_value=0.0, max_value=20.0, value=5.0)

st.subheader("3. Discount Rate and Scenario")
st.markdown("Select a scenario for discount rate adjustment:")
scenario = st.radio("Scenario", options=["Optimistic", "Realistic", "Conservative"], index=1)

# Adjust the discount rate based on the chosen scenario
if scenario == "Optimistic":
    discount_rate = st.number_input("Discount Rate (%)", value=12.0, step=0.5)
elif scenario == "Realistic":
    discount_rate = st.number_input("Discount Rate (%)", value=15.0, step=0.5)
else:
    discount_rate = st.number_input("Discount Rate (%)", value=18.0, step=0.5)

st.markdown("---")

st.markdown("### Calculating Cash Flows and Present Values")
cash_flow_series = []

# Calculate cash flows in the Startup Phase (constant losses)
for t in range(1, startup_years + 1):
    cash_flow_series.append(startup_cf)

# Calculate cash flows in the Expansion Phase: start with the initial value and grow annually
cf = expansion_initial_cf
for t in range(startup_years + 1, startup_years + expansion_years + 1):
    cash_flow_series.append(cf)
    cf = cf * (1 + expansion_growth_rate / 100)

# Calculate cash flows in the Maturity Phase: continue growth at the maturity rate
for t in range(startup_years + expansion_years + 1, total_years + 1):
    cash_flow_series.append(cf)
    cf = cf * (1 + maturity_growth_rate / 100)

st.write("**Projected Cash Flows (by year):**")
st.write(cash_flow_series)

# Calculate the present value of the cash flows for each year
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
terminal_value = cash_flow_series[-1] * (1 + maturity_growth_rate / 100) / ((discount_rate / 100) - (maturity_growth_rate / 100))
terminal_value_pv = terminal_value / ((1 + discount_rate / 100) ** total_years)
st.write("**Present Value of Terminal Value:** $", f"{terminal_value_pv:,.2f}")

# Sum up to get the intrinsic value from the DCF model
intrinsic_value = total_pv + terminal_value_pv
st.markdown("### 📊 Calculated Intrinsic Value for the Growth Company")
st.write("**Intrinsic Value (DCF):** $", f"{intrinsic_value:,.2f}")

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
