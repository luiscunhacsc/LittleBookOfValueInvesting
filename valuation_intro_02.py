import streamlit as st
import numpy as np
import pandas as pd

# Configure the Streamlit app
st.set_page_config(page_title="Relative Valuation – The Game of Comparisons", layout="centered", initial_sidebar_state="expanded")

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
st.title("🧭 Relative Valuation – The Game of Comparisons")
st.markdown("""
### 🎯 What is Relative Valuation?
It’s like looking at houses in the same neighborhood:
- One house with 3 rooms costs **€300,000**
- Another, also with 3 rooms, costs **€400,000**

Naturally, you ask: *"What justifies the difference?"*  
Relative valuation does exactly that – but with companies!

---

### ⚖️ Relative Price vs. Absolute Value
While intrinsic valuation asks, *"How much is this company worth by its own merits?"*  
Relative valuation asks,  
*"How much is this company worth compared to other similar companies?"*  
It forces you to consider:
- **“This stock seems cheap… but cheap compared to what?”**

---

### 🔢 Multiples: The Units of Comparison
Multiples are simple formulas that relate market price to a performance measure. Common examples include:

| **Multiple**          | **Meaning**                                                                 |
|-----------------------|------------------------------------------------------------------------------|
| **P/E (Price/Earnings)**    | How much investors are paying for each € of profit                       |
| **EV/EBITDA**         | How the entire firm (debt + equity) is valued relative to its operating results |
| **P/BV (Price/Book Value)** | How much you pay for each € of net assets                                |
| **P/Sales**           | How much you pay for each € of generated sales                               |

These multiples serve as "quick measures" for comparing companies but should be used carefully.

---

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

---

### 💣 Traps to Avoid
1. **Superficial Comparisons:**  
   Using multiples without understanding the fundamentals can be misleading.
2. **Not Adjusting for Real Differences:**  
   Companies might appear similar but differ in risk, growth, or debt.
3. **Taking Multiples as Absolute Truth:**  
   Multiples are symptoms – proper diagnosis requires deeper analysis!

---

### 🤖 Statistical Adjustment Methods
To avoid unfair comparisons, you might use:
- Regressions (e.g. P/E adjusted for growth)
- Sector median multiples
- Standard deviation and z-scores

These methods help assess how far a company's multiple deviates from the norm.

---

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

# Interactive Relative Valuation Example
st.header("Interactive Relative Valuation Example")
st.markdown("""
In this exercise, we’ll compare the target company’s P/E ratio with those of its peer group.  
Enter the values below and see how the target company compares!
""")
# Input for target company
target_pe = st.number_input("Enter the target company's P/E ratio:", min_value=0.0, value=10.0, step=0.1)

# Interactive peer group input
n_peers = st.number_input("Number of peer companies:", min_value=1, max_value=20, value=3, step=1)
peer_pe = []
for i in range(1, int(n_peers)+1):
    value = st.number_input(f"Enter P/E ratio for Peer {i}:", min_value=0.0, value=12.0, step=0.1, key=f"peer_{i}")
    peer_pe.append(value)

peer_pe = np.array(peer_pe)

# Calculate statistics: median and standard deviation
median_pe = np.median(peer_pe)
std_pe = np.std(peer_pe)

st.markdown("#### Peer Group Analysis")
st.write("**Median P/E of Peer Group:**", median_pe)
st.write("**Standard Deviation of P/E:**", std_pe)

# Determine relative positioning
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
