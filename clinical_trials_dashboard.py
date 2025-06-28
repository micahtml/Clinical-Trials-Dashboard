
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("clinical_trials_mock_data.csv")
df['start_date'] = pd.to_datetime(df['start_date'])
df['completion_date'] = pd.to_datetime(df['completion_date'])
df['start_year'] = df['start_date'].dt.year

# Sidebar filters
st.sidebar.header("Filter Options")
conditions = df['condition'].unique()
statuses = df['status'].unique()

selected_condition = st.sidebar.selectbox("Select Condition", ["All"] + list(conditions))
selected_status = st.sidebar.selectbox("Select Status", ["All"] + list(statuses))

# Apply filters
filtered_df = df.copy()
if selected_condition != "All":
    filtered_df = filtered_df[filtered_df['condition'] == selected_condition]
if selected_status != "All":
    filtered_df = filtered_df[filtered_df['status'] == selected_status]

# Dashboard title
st.title("🧪 Clinical Trial Data Dashboard")

# Charts
st.subheader("Trial Count by Phase")
fig_phase = px.histogram(filtered_df, x='phase', color='status', barmode='group', title="Trial Count by Phase")
st.plotly_chart(fig_phase)

st.subheader("Trial Count by Start Year")
fig_year = px.histogram(filtered_df, x='start_year', color='condition', barmode='group', title="Trial Count by Start Year")
st.plotly_chart(fig_year)

# Data table
st.subheader("Filtered Data")
st.dataframe(filtered_df)
