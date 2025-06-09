# 💱 Exchange Rate Analysis (NGN to USD/GBP)

This project explores the exchange rate trends of the Nigerian Naira (NGN) against the US Dollar (USD) and British Pound (GBP), using data visualization, statistical testing, and an interactive Streamlit dashboard.

---

## 📁 Project Contents

- **Enhanced_ExchangeRate_Data.xlsx** – Cleaned and enriched exchange rate dataset.
- **Exploratory_Data_Analysis.ipynb** – A Jupyter Notebook containing:
  - Descriptive statistics
  - Visualizations
  - Hypothesis testing (ANOVA, correlation)
- **exchange_rate_app.py** – A Streamlit web app for:
  - Interactive data filtering
  - Summary statistics
  - Visual and statistical insights

---

## ⚙️ How to Run the Streamlit App

1. Clone the repository:


git clone https://github.com/your-username/exchange-rate-analysis.git
cd exchange-rate-analysis

2. Create a virtual environment (optional but recommended):


python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux

3. Install required packages:


pip install -r requirements.txt

4. Run the app:


streamlit run exchange_rate_app.py

📊 Key Insights
There is no significant difference in USD exchange rates across weekdays.

GBP exchange rates are fairly stable across months with no strong evidence of monthly variation.

There is a very strong and statistically significant positive correlation between USD and GBP exchange rates, suggesting they trend together.

🛠 Tech Stack
Python (Pandas, NumPy, SciPy, Matplotlib, Seaborn)

Streamlit – for dashboard development

Jupyter Notebook – for exploratory analysis

Excel – final output file format

📌 Motivation
This project was developed to practice:

Real-world data cleaning and analysis

Statistical hypothesis testing

Interactive web app development using Streamlit

📬 Contact
Feel free to connect or reach out via:

GitHub: @Udeibom

LinkedIn: Caleb Udeibom
