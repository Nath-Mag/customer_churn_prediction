# 📊 Customer Churn Prediction & Retention Strategy

---

## 🚀 Project Overview

Customer churn poses a significant revenue risk for subscription-based businesses.  
This project builds an **end-to-end machine learning pipeline** to:

- Identify customers at risk of churning  
- Understand key behavioural drivers  
- Provide data-driven retention recommendations  

The final model achieved a **ROC-AUC of 0.84**, demonstrating strong ability to distinguish churners from non-churners.

---

## 📁 Dataset

- **Source:** Telco Customer Churn (Kaggle)  
- **Size:** ~7,000 customers  
- **Target Variable:** `Churn` (Yes/No)

The dataset includes:

- Customer tenure  
- Contract type  
- Monthly and total charges  
- Internet service type  
- Payment method  
- Demographic indicators  

---

## 🛠 Tech Stack

- Python (pandas, numpy)
- scikit-learn
- seaborn & matplotlib
- Jupyter Notebook (VS Code)
- Git & GitHub

---

## 🔍 Exploratory Data Analysis (EDA)

### Key Findings

- 📉 Overall churn rate ≈ **27%**
- 📅 Short-tenure customers churn significantly more
- 📄 Month-to-month contracts show ~**43%** churn
- 📆 Two-year contracts reduce churn to ~**3%**
- 🌐 Fibre optic customers have highest churn (~**42%**)
- 💳 Electronic check users churn the most among payment methods
- 💰 Higher monthly charges increase churn probability

### Strong Correlations

- Tenure vs Churn: **-0.35**
- Monthly Charges vs Churn: **+0.19**

---

## ⚙️ Feature Engineering

- Converted service flags to binary indicators  
- Created tenure groups  
- Engineered billing features:
  - `avg_monthly_spend`
  - `charges_per_tenure_bucket`
- One-hot encoded categorical variables  
- Removed redundant index column  
- Saved modelling-ready datasets  

---

## 🤖 Modeling & Evaluation

Two models were evaluated:

| Model | Accuracy | Precision | Recall | ROC-AUC |
|-------|----------|-----------|--------|---------|
| Logistic Regression | **0.792** | 0.632 | **0.524** | **0.835** |
| Random Forest | 0.789 | 0.626 | 0.511 | 0.824 |

### Selected Model: Logistic Regression

Chosen due to:

- Slightly higher recall  
- Higher ROC-AUC  
- Strong interpretability  

---

## 🎯 Why Accuracy Is Not Enough

The dataset is moderately imbalanced (~73% non-churn).

If all customers were predicted as non-churn:

**Accuracy ≈ 73%**

Therefore, **Recall** was prioritised.

> Recall measures how many churners are correctly identified.  
> Missing churners directly impacts revenue.

At the default threshold, the model correctly identifies ~**52%** of churners.

---

## 🔑 Key Drivers of Churn

Top predictive features:

1. Tenure (shorter tenure = higher risk)
2. Contract type (month-to-month highest risk)
3. Monthly charges
4. Total charges (lifecycle effect)
5. Electronic check payment
6. Fibre optic service

Demographic variables showed relatively weak predictive power.

---

## 💼 Business Recommendations

### 1️⃣ Early Lifecycle Retention  
Focus on customers within first 12 months.

### 2️⃣ Contract Conversion Strategy  
Encourage month-to-month customers to move to long-term contracts.

### 3️⃣ Fibre Customer Monitoring  
Implement satisfaction checks and targeted offers.

### 4️⃣ Promote Automatic Billing  
Incentivise auto-pay adoption to reduce churn.

### 5️⃣ Proactive High-Value Outreach  
Monitor high monthly charge customers early.

---

## 📂 Project Structure

```
customer_churn_prediction/
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb        # Data cleaning & preprocessing
│   ├── 02_eda.ipynb                  # Exploratory data analysis
│   ├── 03_feature_engineering.ipynb  # Feature creation & encoding
│   ├── 04_modelling.ipynb            # Model training & evaluation
│   └── 05_business_insights.ipynb    # Final insights & recommendations
│
├── data/
│   └── processed/                    # Cleaned datasets (raw data excluded)
│
├── requirements.txt                  # Project dependencies
├── .gitignore                        # Ignored files & folders
└── README.md                         # Project documentation
```

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Nath-Mag/customer_churn_prediction.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run notebooks in order:
   - `01_data_cleaning.ipynb`
   - `02_eda.ipynb`
   - `03_feature_engineering.ipynb`
   - `04_modelling.ipynb`
   - `05_business_insights.ipynb`

---

## ▶️ Run the Streamlit Dashboard

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

### Dashboard Features
- Interactive filters (tenure, contract, internet service, payment method)
- KPI cards and churn breakdown
- Key driver visuals
- Threshold slider


## 👤 Author

**Nathaniel Magit**  
Data Science | Machine Learning | Analytics
