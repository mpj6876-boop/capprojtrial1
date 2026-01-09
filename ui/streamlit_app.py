import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="wide")
st.title("Offline Financial Risk Simulator")

# -------------------------------
# Inputs
# -------------------------------
st.sidebar.header("Financial Profile")
income = st.sidebar.number_input("Monthly Income", value=50000)
expenses = st.sidebar.number_input("Monthly Expenses", value=30000)
goal_months = st.sidebar.slider("Simulation Months", 6, 120, 24)

st.sidebar.subheader("Job Loss Scenario")
enable_job_loss = st.sidebar.checkbox("Enable Job Loss")
job_loss_start = st.sidebar.number_input("Job loss start month", 1, goal_months, 3)
job_loss_duration = st.sidebar.number_input("Job loss duration (months)", 1, goal_months, 6)

st.sidebar.subheader("Inflation Scenario")
enable_inflation = st.sidebar.checkbox("Enable Inflation")
inflation_rate = st.sidebar.slider("Inflation Rate (%)", 0, 50, 15) / 100

# -------------------------------
# Run Simulation
# -------------------------------
if st.sidebar.button("Run Simulation"):
    payload = {
        "income": income,
        "expenses": expenses,
        "goal_months": goal_months,
        "enable_job_loss": enable_job_loss,
        "job_loss_start": job_loss_start,
        "job_loss_duration": job_loss_duration,
        "enable_inflation": enable_inflation,
        "inflation_rate": inflation_rate
    }

    response = requests.post("http://localhost:8000/run", json=payload)

    if response.status_code != 200:
        st.error("Backend Error")
        st.text(response.text)
    else:
        st.session_state["data"] = response.json()

# -------------------------------
# Charts
# -------------------------------
if "data" in st.session_state:
    data = st.session_state["data"]
    base_df = pd.DataFrame(data["baseline"])
    scn_df = pd.DataFrame(data["scenario"])

    st.subheader("Cash Balance Comparison (Never Negative)")
    cash_df = pd.DataFrame({
        "Baseline": base_df.set_index("month")["cash_balance"],
        "Scenario": scn_df.set_index("month")["cash_balance"]
    })

    st.line_chart(cash_df)
    st.caption("Cash balance is clamped to zero and never negative.")


    st.subheader("Net Worth Comparison")
    st.line_chart(pd.DataFrame({
        "Baseline": base_df.set_index("month")["net_worth"],
        "Scenario": scn_df.set_index("month")["net_worth"]
    }))
    st.subheader("Debt Over Time")
    st.line_chart(scn_df.set_index("month")["debt"])
    st.subheader("Scenario Outcome Summary")
    st.json(data["outcome_summary"])

    st.subheader("AI-Generated Financial Guidance")
    for a in data["advice"]:
        st.markdown(f"• {a}")


    if data["failure"]:
        st.error(f"Failure Detected: {data['failure']['type']} in month {data['failure']['month']}")
        st.write("Suggested Recovery Options:", data["recovery_options"])
