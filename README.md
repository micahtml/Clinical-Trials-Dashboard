# 🧪 Clinical Trial Data Dashboard

This project is an interactive dashboard designed to visualize clinical trial data using **Streamlit**, **Plotly**, and **Pandas**. It simulates real-world clinical trial records and provides filtering and visual analytics useful to researchers, analysts, and healthcare stakeholders.

---

## 📊 Features

- Filter trials by:
  - Medical condition (e.g., Cancer, COVID-19)
  - Trial status (e.g., Recruiting, Completed)
- Visualize:
  - Number of trials by phase (I, II, III, IV)
  - Year-over-year trend of trial starts
- View raw clinical trial records in a dynamic table

---

## 🧂 Sample Data Fields

- `nct_id` – Unique trial ID
- `title` – Trial name
- `condition` – Medical condition
- `status` – Trial status
- `phase` – Trial phase
- `start_date`, `completion_date`

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Plotly Express

---

## 🚀 How to Run Locally

1. Clone this repo or download the files.
2. Install dependencies:
    ```bash
    pip install streamlit pandas plotly
    ```
3. Run the app:
    ```bash
    streamlit run clinical_trials_dashboard.py
    ```

---

## 🌐 Deployment (Optional)

To deploy online:
1. Push your code and CSV file to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and create a new app.
3. Point to the `clinical_trials_dashboard.py` file and deploy!

---

## 📌 Use Case

This project showcases:
- Data filtering and visualization skills
- Knowledge of clinical trial metadata
- Capability to create lightweight, deployable dashboards

Perfect for portfolio demonstration in **Data Analyst** or **Healthcare Analytics** roles.