import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import io

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_excel("Enhanced_ExchangeRate_Data.xlsx")

df = load_data()

st.title("📊 Currency Exchange Rate Analysis App")
st.markdown("""
This project was built as part of my journey in IBM's Exploratory Data for Machine Learning course. 
It demonstrates my ability to perform real-world data cleaning, EDA, hypothesis testing, and storytelling with data.
""")

st.header("🔍 1. Overview of the Dataset")
st.dataframe(df.head())
st.write(f"**Shape of dataset:** {df.shape[0]} rows and {df.shape[1]} columns")

st.subheader("Column Descriptions")
st.markdown("""
- **Date**: Daily timestamp
- **USD_NGN / GBP_NGN / EUR_NGN**: Daily official rates
- **Weekday**: Name of the day
- **Month**: Numeric month
""")

st.header("📈 2. Exploratory Data Analysis")
st.subheader("Exchange Rate Trends Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
df.plot(x='Date', y=['USD_NGN', 'GBP_NGN', 'EUR_NGN'], ax=ax)
plt.ylabel("Rate (₦)")
plt.title("Exchange Rates Over Time")
st.pyplot(fig)

st.subheader("Weekday Patterns for USD")
fig2, ax2 = plt.subplots()
sns.boxplot(x='Weekday', y='USD_NGN', data=df, ax=ax2)
plt.title("USD Rate by Day of Week")
st.pyplot(fig2)

st.subheader("Monthly Patterns for GBP")
fig3, ax3 = plt.subplots()
sns.boxplot(x='Month', y='GBP_NGN', data=df, ax=ax3)
plt.title("GBP Rate by Month")
st.pyplot(fig3)

st.header("🧪 3. Hypotheses & Significance Testing")

st.markdown("**H1: The mean USD exchange rate differs across weekdays**")
weekday_groups = [group["USD_NGN"].dropna().values for name, group in df.groupby("Weekday")]
f1, p1 = stats.f_oneway(*weekday_groups)
st.write(f"**Result**: F = {f1:.4f}, p = {p1:.4f}")
st.success("Interpretation: There IS a statistically significant difference in USD rates across weekdays." if p1 < 0.05 else "Interpretation: No significant weekday effect on USD rates.")

st.markdown("**H2: The GBP rate varies significantly by month**")
month_groups = [group["GBP_NGN"].dropna().values for name, group in df.groupby("Month")]
f2, p2 = stats.f_oneway(*month_groups)
st.write(f"**Result**: F = {f2:.4f}, p = {p2:.4f}")
st.success("Interpretation: There IS a monthly effect on GBP rates." if p2 < 0.05 else "Interpretation: GBP rates are stable across months.")

st.markdown("**H3: USD and GBP exchange rates are positively correlated**")
corr, p_corr = stats.pearsonr(df["USD_NGN"], df["GBP_NGN"])
st.write(f"**Pearson r = {corr:.4f}, p = {p_corr:.4f}**")
st.success("Interpretation: There is a strong, statistically significant positive correlation between USD and GBP rates." if p_corr < 0.05 else "Interpretation: No significant correlation.")

st.header("✅ 4. Key Takeaways")

st.markdown("""
- There is **no significant difference** in USD exchange rates across weekdays.
- GBP exchange rates are **fairly stable** across months with no strong evidence of monthly variation.
- There is a **very strong and statistically significant positive correlation** between USD and GBP exchange rates, suggesting they trend together.
""")



output = io.BytesIO()
with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False)
output.seek(0)

st.download_button(
    label="Download Excel",
    data=output,
    file_name="Enhanced_ExchangeRate_Data.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)



st.header("📬 6. Connect With Me")
st.markdown("[🔗 Visit my LinkedIn](https://www.linkedin.com/in/caleb-udeibom-3495a023b/)")
