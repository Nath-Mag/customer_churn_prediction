# Customer Churn Analytics & Retention Strategy

**Python · Machine Learning · Customer Analytics · Streamlit**

An end-to-end customer analytics project that combines exploratory analysis, predictive modelling, and an interactive dashboard to identify customers at risk of churn and support targeted retention decisions.

## Live Dashboard

[Open the Interactive Streamlit Dashboard](https://customerchurnprediction-7efk42xq3brtjwrgamaxbs.streamlit.app)

The dashboard provides interactive filters, churn KPIs, driver analysis, customer-risk breakdowns, and a configurable classification threshold.

## Executive Summary

Customer churn reduces recurring revenue, limits customer lifetime value, and increases the pressure to acquire replacement customers.

This project analyses approximately 7,000 telecommunications customers to understand the behaviours and service characteristics associated with churn. It combines data cleaning, exploratory analysis, feature engineering, model comparison, and business interpretation within a reproducible machine-learning workflow.

The selected Logistic Regression model achieved a ROC-AUC of approximately **0.84** and identified around **52% of churners** at the default classification threshold. Logistic Regression was selected over Random Forest because it provided slightly stronger recall and ROC-AUC while remaining straightforward to interpret.

The findings indicate that churn risk is especially concentrated among newer customers, month-to-month subscribers, fibre-optic users, electronic-check users, and customers facing higher monthly charges. These insights can support prioritised retention campaigns rather than broad, untargeted incentives.

## Business Problem

A subscription business needs to understand not only how many customers leave, but also:

- Which customers are most likely to churn?
- At what point in the customer lifecycle is churn highest?
- Which contracts, services, and payment methods are associated with elevated risk?
- Which customers should receive proactive retention attention?
- How should model performance be evaluated when failing to identify churners has a business cost?

This project addresses those questions through descriptive customer analysis and interpretable predictive modelling.

## Project Objectives

- Assess and prepare customer data for analysis.
- Measure churn across important customer and service groups.
- Identify the strongest behavioural and commercial churn indicators.
- Engineer features that improve customer-risk analysis.
- Compare classification models using business-relevant metrics.
- Select an interpretable model for retention decision support.
- Translate analytical results into practical recommendations.
- Build an interactive dashboard for exploring churn risk.

## Dataset

The project uses the Telco Customer Churn dataset, containing approximately 7,000 customer records.

The data covers:

| Area | Example variables |
|---|---|
| Customer lifecycle | Tenure and churn status |
| Contracts | Month-to-month, one-year, and two-year contracts |
| Billing | Monthly charges and total charges |
| Services | Internet, phone, streaming, security, and support services |
| Payment | Payment method and paperless billing |
| Demographics | Partner, dependants, gender, and senior-citizen indicators |

The target variable is:

```text
Churn: Yes or No
```

## Analytical Workflow

```text
Customer Data
      ↓
Data Quality Assessment
      ↓
Cleaning and Transformation
      ↓
Exploratory Customer Analysis
      ↓
Feature Engineering and Encoding
      ↓
Model Training and Comparison
      ↓
Threshold and Metric Evaluation
      ↓
Churn-Driver Interpretation
      ↓
Retention Recommendations
      ↓
Interactive Streamlit Dashboard
```

## Data Preparation

The preparation stage included:

- Inspecting data types, completeness, and distributions.
- Converting billing variables into appropriate numeric formats.
- Removing redundant index information.
- Transforming service flags into model-ready indicators.
- Encoding categorical variables.
- Creating tenure-based customer groups.
- Producing modelling-ready datasets.
- Separating predictors from the churn target.

## Exploratory Analysis

### Overall churn

Approximately **27%** of customers in the dataset had churned.

Because roughly 73% had not churned, a model predicting every customer as non-churn could still achieve about 73% accuracy. This means accuracy alone would provide a misleading view of model usefulness.

### Tenure

Short-tenure customers demonstrated substantially greater churn risk.

This indicates that the early customer lifecycle is a critical period for onboarding, engagement, and service-quality intervention.

### Contract type

Churn varied sharply by contract arrangement:

- Month-to-month customers: approximately **43% churn**
- Two-year contract customers: approximately **3% churn**

The result suggests that contractual commitment and customer retention are strongly associated.

### Internet service

Fibre-optic customers experienced the highest churn rate, at approximately **42%**.

This warrants further investigation into service expectations, reliability, support experience, and perceived value.

### Payment method

Electronic-check customers showed the highest churn among payment groups.

This may reflect differences in customer behaviour or friction in the billing experience. The relationship should not automatically be treated as causal.

### Monthly charges

Customers with higher monthly charges were more likely to churn.

This suggests that price sensitivity and perceived value may be important retention considerations, particularly for newer customers.

## Feature Engineering

The modelling workflow included:

- Binary transformation of service indicators.
- One-hot encoding of categorical features.
- Creation of tenure groups.
- Creation of billing-related features, including:

```text
avg_monthly_spend
charges_per_tenure_bucket
```

- Removal of redundant fields.
- Export of model-ready datasets for reproducibility.

## Model Development

Two classification models were evaluated:

| Model | Accuracy | Precision | Recall | ROC-AUC |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.792 | 0.632 | 0.524 | 0.835 |
| Random Forest | 0.789 | 0.626 | 0.511 | 0.824 |

## Selected Model

**Logistic Regression** was selected because it provided:

- Slightly higher recall.
- Higher ROC-AUC.
- Comparable overall accuracy.
- Strong interpretability.
- Clearer communication of customer-risk drivers.

The objective was not merely to maximise accuracy. It was to develop a useful and explainable model for identifying customers who may require retention attention.

## Why Recall Matters

Recall measures the proportion of actual churners correctly identified.

At the default classification threshold, the selected model identified approximately **52% of customers who churned**.

In a retention setting, false negatives represent customers who are likely to churn but are not flagged for intervention. That makes recall a particularly important metric.

However, improving recall generally increases false positives. The appropriate operating threshold should therefore depend on:

- The cost of a retention intervention.
- The expected value of retaining a customer.
- Available campaign capacity.
- The acceptable number of unnecessary contacts.

The dashboard includes a threshold control to demonstrate this trade-off.

## Key Churn Drivers

The analysis identified the following important indicators:

1. Short customer tenure.
2. Month-to-month contracts.
3. Higher monthly charges.
4. Total charges and customer lifecycle.
5. Electronic-check payments.
6. Fibre-optic service.

Demographic characteristics showed comparatively weaker predictive value than service, contract, billing, and lifecycle variables.

## Business Interpretation

### Early lifecycle risk

The concentration of churn among short-tenure customers indicates that retention should begin during onboarding rather than only after dissatisfaction becomes visible.

### Contract flexibility and churn

Month-to-month customers have greater freedom to leave and show markedly higher churn. Longer contracts are associated with lower churn, although the analysis does not establish that contract conversion alone causes retention.

### Service-value concerns

High churn among fibre-optic and high-charge customers may indicate a gap between customer expectations and the value or experience delivered.

### Behaviour over demographics

Service use, billing, contract type, and tenure appear more informative than demographic characteristics. This supports behaviour-led rather than demographic-led retention decisions.

## Business Recommendations

### 1. Strengthen early-life retention

Create structured onboarding and engagement activity during the first 12 months.

Potential actions include:

- Early customer check-ins.
- Service-setup support.
- Usage education.
- Satisfaction monitoring.
- Rapid escalation of service issues.

### 2. Target month-to-month customers selectively

Identify high-value month-to-month customers with elevated churn probability and test incentives for longer commitments.

Offers should be targeted rather than given to the entire customer base.

### 3. Investigate fibre-optic experience

Examine service quality, support interactions, outages, speed expectations, and pricing among fibre-optic customers.

The churn pattern should be investigated operationally before assuming a single cause.

### 4. Review billing and payment friction

Assess why electronic-check customers churn more frequently and whether alternative payment methods improve convenience or retention.

### 5. Prioritise high-charge, short-tenure customers

Customers with both high monthly charges and limited tenure may warrant earlier contact because they combine price exposure with limited established loyalty.

### 6. Use probability-based retention queues

Rank customers using predicted churn probabilities and prioritise intervention based on:

- Churn risk.
- Customer value.
- Campaign capacity.
- Contact cost.
- Expected retention benefit.

This would be more useful than treating every customer above a fixed threshold identically.

## Streamlit Dashboard

The application supports:

- Interactive filters for tenure, contract, internet service, and payment method.
- Churn KPI cards.
- Customer and service breakdowns.
- Churn-driver visualisations.
- A configurable prediction threshold.
- Exploration of the relationship between customer characteristics and churn.

Run it locally with:

```bash
streamlit run app/app.py
```

## Repository Structure

```text
customer_churn_prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_modelling.ipynb
│   └── 05_business_insights.ipynb
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── requirements_full.txt
```

## Notebook Guide

| Notebook | Purpose |
|---|---|
| `01_data_cleaning.ipynb` | Reviews data quality and prepares the customer dataset |
| `02_eda.ipynb` | Examines churn across customer, contract, billing, and service groups |
| `03_feature_engineering.ipynb` | Creates model-ready variables and encoded datasets |
| `04_modelling.ipynb` | Trains, compares, and evaluates classification models |
| `05_business_insights.ipynb` | Interprets the findings and develops retention recommendations |

## Tools and Technologies

- **Python:** analysis and modelling.
- **pandas and NumPy:** data preparation and transformation.
- **scikit-learn:** preprocessing, model development, and evaluation.
- **Matplotlib and Seaborn:** analytical visualisation.
- **Streamlit:** interactive dashboard development.
- **Jupyter Notebook:** reproducible workflow.
- **Git and GitHub:** version control and documentation.

## Skills Demonstrated

- Customer analytics.
- Predictive modelling.
- Classification.
- Exploratory data analysis.
- Feature engineering.
- Model comparison.
- Metric selection.
- Threshold analysis.
- Business interpretation.
- Retention strategy.
- Interactive dashboard development.
- Analytical storytelling.

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Nath-Mag/customer_churn_prediction.git
cd customer_churn_prediction
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

**Windows**

```bash
.venv\Scripts\activate
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the notebooks in sequence

```text
01_data_cleaning.ipynb
02_eda.ipynb
03_feature_engineering.ipynb
04_modelling.ipynb
05_business_insights.ipynb
```

### 5. Launch the dashboard

```bash
streamlit run app/app.py
```

## Limitations

- The dataset represents customers from one telecommunications context.
- The data does not include detailed service interactions, complaints, outages, or campaign history.
- Relationships identified through exploratory analysis should not automatically be interpreted as causal.
- Model performance should be validated on new or live customer data.
- The default prediction threshold may not be optimal for every retention budget.
- Recommendations should be tested through controlled experiments before broad implementation.
- Predicted churn should support human decision-making rather than automatically determine customer treatment.

## Future Improvements

- Calibrate predicted probabilities.
- Optimise the threshold using intervention costs and expected customer value.
- Add customer lifetime value estimates.
- Compare additional models using cross-validation.
- Introduce SHAP-based local and global explanations.
- Track model performance across customer segments.
- Add automated data-quality checks.
- Deploy an API for real-time predictions.
- Monitor drift in customer behaviour and model performance.
- Test retention strategies through controlled experiments.

## Author

**Nathaniel Magit**

Data Scientist and Analyst specialising in Python, SQL, statistics, machine learning, customer analytics, and business intelligence.

[View my GitHub profile](https://github.com/Nath-Mag)
