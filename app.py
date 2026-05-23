import streamlit as st
import pandas as pd
import plotly.express as px
import base64

# Function to Load Local Image
def get_base64_image(image_path):

    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    return encoded

# App Title
st.set_page_config(
    page_title="AI Data Analyst",
    layout="wide"
)

# Load Banner Image
image_base64 = get_base64_image("assets/banner.jpg")

# Custom CSS
st.markdown(
    f"""
    <style>

    .main {{
        background-color: #0E1117;
        color: white;
    }}

    .hero {{
        background-image: url("data:image/jpg;base64,{image_base64}");
        background-size: cover;
        background-position: center;
        padding: 120px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
    }}

    .hero h1 {{
        font-size: 50px;
        color: white;
    }}

    .hero p {{
        font-size: 22px;
        color: white;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# Hero Section
st.markdown(
    """
    <div class="hero">
        <h1>AI Data Analyst</h1>
        <p>Upload CSV Files • Generate Insights • Visualize Data</p>
    </div>
    """,
    unsafe_allow_html=True
)


# Sidebar
st.sidebar.header("Upload Your File")

# File Upload
uploaded_file = st.sidebar.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

# If file uploaded
if uploaded_file is not None:

    # Read CSV safely
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8')

    except UnicodeDecodeError:
        df = pd.read_csv(uploaded_file, encoding='latin1')

    except Exception as e:
        st.error(f"Error reading file: {e}")

    # Success Message
    st.success("CSV uploaded successfully!")

    # =========================
    # Dataset Preview
    # =========================

    st.subheader("Dataset Preview")

    st.dataframe(df, use_container_width=True)

    # =========================
    # Dataset Shape
    # =========================

    st.subheader("Dataset Shape")

    rows, columns = df.shape

    st.write(f"Rows: {rows}")
    st.write(f"Columns: {columns}")

    # =========================
    # Column Information
    # =========================

    st.subheader("Column Information")

    column_info = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes.astype(str)
    })

    st.dataframe(column_info, use_container_width=True)

    # =========================
    # Missing Values
    # =========================

    st.subheader("Missing Values")

    missing_values = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum().values
})

    st.dataframe(missing_values, use_container_width=True)

    # =========================
    # Duplicate Rows
    # =========================

    st.subheader("Duplicate Rows")

    duplicates = df.duplicated().sum()

    st.write(f"Duplicate Rows: {duplicates}")

    # =========================
    # Summary Statistics
    # =========================

    st.subheader("Summary Statistics")

    try:
        st.dataframe(
            df.describe(include='all'),
            use_container_width=True
        )

    except Exception as e:
        st.warning(f"Could not generate summary statistics: {e}")

    # =========================
    # KPI CARDS
    # =========================

    st.subheader("Dashboard KPIs")

    # KPI Calculations
    total_rows = df.shape[0]
    total_columns = df.shape[1]
    missing_values_count = df.isnull().sum().sum()
    duplicate_rows = df.duplicated().sum()

    numeric_columns = df.select_dtypes(include=['number']).columns
    total_numeric_columns = len(numeric_columns)

    # Create Columns for KPI Cards
    col1, col2, col3, col4, col5 = st.columns(5)

    # KPI Cards
    col1.metric("Rows", total_rows)

    col2.metric("Columns", total_columns)

    col3.metric("Missing Values", missing_values_count)

    col4.metric("Duplicate Rows", duplicate_rows)

    col5.metric("Numeric Columns", total_numeric_columns)

    # =========================
    # AUTOMATIC CHART GENERATOR
    # =========================

    st.subheader("Automatic Visualizations")

    # Detect Numeric Columns
    numeric_cols = df.select_dtypes(include=['number']).columns

    # Detect Categorical Columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    # =========================
    # Histogram For Numeric Data
    # =========================

    if len(numeric_cols) > 0:

        selected_numeric = st.selectbox(
            "Select Numeric Column",
            numeric_cols
        )

        fig_hist = px.histogram(
            df,
            x=selected_numeric,
            nbins=30,
            title=f"Distribution of {selected_numeric}"
        )

        st.plotly_chart(fig_hist, use_container_width=True)

    # =========================
    # Bar Chart
    # =========================

    if len(categorical_cols) > 0 and len(numeric_cols) > 0:

        selected_category = st.selectbox(
            "Select Categorical Column",
            categorical_cols
        )

        selected_value = st.selectbox(
            "Select Value Column",
            numeric_cols
        )

        grouped_df = (
        df.groupby(selected_category, dropna=False)[selected_value]
        .sum()
        .reset_index()
        )

        fig_bar = px.bar(
            grouped_df,
            x=selected_category,
            y=selected_value,
            title=f"{selected_value} by {selected_category}"
        )

        st.plotly_chart(fig_bar, use_container_width=True)

    # =========================
    # Pie Chart
    # =========================

    if len(categorical_cols) > 0:

        pie_category = st.selectbox(
            "Select Column For Pie Chart",
            categorical_cols
        )

        pie_data = (
            df[pie_category]
            .value_counts()
            .head(10)
            .reset_index()
        )

        pie_data.columns = [pie_category, "Count"]

        fig_pie = px.pie(
            pie_data,
            names=pie_category,
            values="Count",
            title=f"Distribution of {pie_category}"
        )

        st.plotly_chart(fig_pie, use_container_width=True)