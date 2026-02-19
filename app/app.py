import pandas as pd
import streamlit as st
import plotly.express as px
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, roc_auc_score, confusion_matrix
import numpy as np


st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

# ---------- Load Data ----------
@st.cache_data
def load_data():
    project_root = Path(__file__).resolve().parents[1]

    data_path = project_root / "Telco Customer Churn" / "data" / "processed" / "telco_cleaned.csv"

    if not data_path.exists():
        st.error(f"❌ Data file not found at: {data_path}")
        st.stop()

    df = pd.read_csv(data_path)

    # Standardize target to 0/1 if needed
    if df["Churn"].dtype == "object":
        df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    return df

df = load_data()

@st.cache_resource
def train_and_score_model():
    project_root = Path(__file__).resolve().parents[1]

    X_path = project_root / "Telco Customer Churn" / "data" / "processed" / "X_features.csv"
    y_path = project_root / "Telco Customer Churn" / "data" / "processed" / "y_target.csv"

    if not X_path.exists() or not y_path.exists():
        return None

    X = pd.read_csv(X_path)
    y = pd.read_csv(y_path).squeeze()

    # Train/test split (stratified)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Scale for Logistic Regression
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_s, y_train)

    y_proba = model.predict_proba(X_test_s)[:, 1]
    auc = roc_auc_score(y_test, y_proba)

    return {
        "y_test": y_test.to_numpy(),
        "y_proba": y_proba,
        "roc_auc": auc
    }


# ---------- Sidebar Filters ----------
st.sidebar.title("Filters")

# Some Kaggle versions use different column names; this keeps it robust
contract_col = "Contract" if "Contract" in df.columns else None
internet_col = "InternetService" if "InternetService" in df.columns else None
payment_col = "PaymentMethod" if "PaymentMethod" in df.columns else None

min_tenure, max_tenure = int(df["tenure"].min()), int(df["tenure"].max())
tenure_range = st.sidebar.slider("Tenure range (months)", min_tenure, max_tenure, (min_tenure, max_tenure))

filtered = df[(df["tenure"] >= tenure_range[0]) & (df["tenure"] <= tenure_range[1])]

if contract_col:
    contract_options = ["All"] + sorted(filtered[contract_col].dropna().unique().tolist())
    contract_choice = st.sidebar.selectbox("Contract", contract_options)
    if contract_choice != "All":
        filtered = filtered[filtered[contract_col] == contract_choice]

if internet_col:
    internet_options = ["All"] + sorted(filtered[internet_col].dropna().unique().tolist())
    internet_choice = st.sidebar.selectbox("Internet Service", internet_options)
    if internet_choice != "All":
        filtered = filtered[filtered[internet_col] == internet_choice]

if payment_col:
    pay_options = ["All"] + sorted(filtered[payment_col].dropna().unique().tolist())
    pay_choice = st.sidebar.selectbox("Payment Method", pay_options)
    if pay_choice != "All":
        filtered = filtered[filtered[payment_col] == pay_choice]

# ---------- Tabs ----------
tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Drivers", "🤖 Model Performance"])

# ---------- Tab 1: Overview ----------
with tab1:
    st.title("Customer Churn Dashboard")
    total_customers = len(filtered)
    churn_rate = filtered["Churn"].mean() if total_customers else 0.0
    avg_monthly = filtered["MonthlyCharges"].mean() if "MonthlyCharges" in filtered.columns and total_customers else 0.0

    # simple estimate: expected monthly revenue at risk = churners * avg monthly charge
    estimated_rev_risk = (filtered["Churn"].sum() * avg_monthly) if total_customers else 0.0

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Customers (filtered)", f"{total_customers:,}")
    c2.metric("Churn Rate", f"{churn_rate*100:.1f}%")
    c3.metric("Avg Monthly Charges", f"{avg_monthly:.2f}")
    c4.metric("Est. Monthly Revenue at Risk", f"{estimated_rev_risk:,.2f}")


    st.subheader("Churn Distribution")
    churn_counts = filtered["Churn"].value_counts().rename(index={0: "No", 1: "Yes"}).reset_index()
    churn_counts.columns = ["Churn", "Count"]
    fig = px.bar(churn_counts, x="Churn", y="Count")
    st.plotly_chart(fig, use_container_width=True)

st.download_button(
    label="⬇️ Download filtered data (CSV)",
    data=filtered.to_csv(index=False),
    file_name="telco_filtered.csv",
    mime="text/csv"
)

# ---------- Tab 2: Drivers ----------
with tab2:
    st.subheader("Key Churn Drivers")

    left, right = st.columns(2)

    with left:
        if contract_col:
            st.markdown("**Churn Rate by Contract**")
            grp = filtered.groupby(contract_col)["Churn"].mean().reset_index()
            fig = px.bar(grp, x=contract_col, y="Churn")
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("**Tenure vs Churn**")
        fig = px.histogram(filtered, x="tenure", color=filtered["Churn"].map({0: "No", 1: "Yes"}), nbins=30)
        st.plotly_chart(fig, use_container_width=True)

    with right:
        if internet_col:
            st.markdown("**Churn Rate by Internet Service**")
            grp = filtered.groupby(internet_col)["Churn"].mean().reset_index()
            fig = px.bar(grp, x=internet_col, y="Churn")
            st.plotly_chart(fig, use_container_width=True)

        if "MonthlyCharges" in filtered.columns:
            st.markdown("**Monthly Charges by Churn**")
            filtered2 = filtered.copy()
            filtered2["ChurnLabel"] = filtered2["Churn"].map({0: "No", 1: "Yes"})
            fig = px.box(filtered2, x="ChurnLabel", y="MonthlyCharges")
            st.plotly_chart(fig, use_container_width=True)

st.subheader("Top At-Risk Segments (Churn Rate)")

segment_cols = []
for c in ["Contract", "InternetService", "PaymentMethod"]:
    if c in filtered.columns:
        segment_cols.append(c)

if segment_cols:
    seg = (
        filtered.groupby(segment_cols)["Churn"]
        .agg(churn_rate="mean", customers="size")
        .reset_index()
        .sort_values(["churn_rate", "customers"], ascending=[False, False])
    )
    st.dataframe(seg.head(10), use_container_width=True)
else:
    st.info("Segment columns not found in this dataset version.")


# ---------- Tab 3: Model Performance ----------
with tab3:
    st.subheader("Model Performance & Threshold Tuning")

    model_pack = train_and_score_model()
    if model_pack is None:
        st.error("❌ Could not find X_features.csv / y_target.csv. Make sure they are in data/processed.")
        st.stop()

    y_test = model_pack["y_test"]
    y_proba = model_pack["y_proba"]
    auc = model_pack["roc_auc"]

    st.write(f"**ROC-AUC (Logistic Regression):** {auc:.3f}")

    threshold = st.slider(
        "Decision Threshold (higher = fewer churn predictions)",
        min_value=0.05, max_value=0.95, value=0.50, step=0.01
    )

    y_pred = (y_proba >= threshold).astype(int)

    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    cm = confusion_matrix(y_test, y_pred)

    c1, c2, c3 = st.columns(3)
    c1.metric("Precision", f"{prec:.3f}")
    c2.metric("Recall", f"{rec:.3f}")
    c3.metric("Threshold", f"{threshold:.2f}")

    st.markdown("### Confusion Matrix (Actual vs Predicted)")
    cm_df = pd.DataFrame(
        cm,
        index=["Actual: No", "Actual: Yes"],
        columns=["Pred: No", "Pred: Yes"]
    )
    st.dataframe(cm_df, use_container_width=True)

    st.markdown("### Interpretation")
    st.write(
        "Lowering the threshold increases **recall** (catch more churners) but may reduce **precision** "
        "(more false alarms). For churn problems, higher recall is often preferred to reduce revenue loss "
        "from missed churners."
    )

