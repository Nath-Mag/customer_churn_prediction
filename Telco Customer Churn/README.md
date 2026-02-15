📊 Customer Churn Prediction & Retention Strategy
🚀 Project Overview

Customer churn poses a significant revenue risk for subscription-based businesses.
This project builds an end-to-end machine learning pipeline to:

Identify customers at risk of churning

Understand key behavioural drivers

Provide data-driven retention recommendations

The final model achieved a ROC-AUC of 0.84, demonstrating strong ability to distinguish churners from non-churners.

📁 Dataset

Source: Telco Customer Churn (Kaggle)
Size: ~7,000 customers
Target Variable: Churn (Yes/No)

The dataset includes:

Customer tenure

Contract type

Monthly and total charges

Internet service type

Payment method

Demographic indicators

🛠 Tech Stack

Python (pandas, numpy)

scikit-learn

seaborn & matplotlib

Jupyter Notebook (VS Code)

Git & GitHub

🔍 Exploratory Data Analysis (EDA)
Key Findings:

📉 Overall churn rate ≈ 27%

📅 Short-tenure customers churn significantly more

📄 Month-to-month contracts show ~43% churn

📆 Two-year contracts reduce churn to ~3%

🌐 Fibre optic customers have highest churn (~42%)

💳 Electronic check users churn the most among payment methods

💰 Higher monthly charges increase churn probability

Strong correlation observed:

Tenure vs Churn: -0.35

Monthly Charges vs Churn: +0.19

⚙️ Feature Engineering

Converted service flags to binary indicators

Created tenure groups

Engineered billing features:

avg_monthly_spend

charges_per_tenure_bucket

One-hot encoded categorical variables

Removed redundant index column

Saved modelling-ready datasets

🤖 Modeling

Two models were evaluated:

Model	Accuracy	Precision	Recall	ROC-AUC
Logistic Regression	0.792	0.632	0.524	0.835
Random Forest	0.789	0.626	0.511	0.824
Model Selection

Logistic Regression was selected due to:

Slightly higher recall

Higher ROC-AUC

Strong interpretability

🎯 Why Accuracy Is Not Enough

The dataset is moderately imbalanced (~73% non-churn).

If all customers were predicted as non-churn:
Accuracy ≈ 73%

Therefore, Recall was prioritised:

Recall measures how many churners we correctly identify.
Missing churners directly impacts revenue.

At the default threshold, the model correctly identifies ~52% of churners.

🔑 Key Drivers of Churn

Top predictive features:

Tenure (shorter tenure = higher risk)

Contract type (month-to-month highest risk)

Monthly charges

Total charges (lifecycle effect)

Electronic check payment

Fibre optic service

Demographic variables showed relatively weak predictive power.

💼 Business Recommendations
1️⃣ Early Lifecycle Retention

Focus on customers within first 12 months.

2️⃣ Contract Conversion Strategy

Encourage month-to-month customers to move to long-term contracts.

3️⃣ Fibre Customer Monitoring

Implement satisfaction checks and targeted offers.

4️⃣ Promote Automatic Billing

Incentivise auto-pay adoption to reduce churn.

5️⃣ Proactive High-Value Outreach

Monitor high monthly charge customers early.