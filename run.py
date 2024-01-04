import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI For Everyone!",
    page_icon="👋",
)

# Add background image using HTML
st.markdown(
    """
    <style>
        body {
            background-image: url('https://cdn1.expresscomputer.in/wp-content/uploads/2023/09/29160852/EC_Gen_AI_02_Technology_750.jpg');
            background-size: cover;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.success("Input Field!") 
st.title("AI For Everyone!")

uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(uploaded_file)
        
    # Display the dataset shape after upload
    st.sidebar.markdown("## Dataset Shape")
    st.sidebar.text(f"Number of Rows: {df.shape[0]}")
    st.sidebar.text(f"Number of Columns: {df.shape[1]}")
    
    # Collect all column names
    all_columns = df.columns.tolist()
    
    # Create a column selector for y_var
    selected_y_var = st.sidebar.selectbox(" Select Y variable:", ['Select a column'] + all_columns)
    if selected_y_var != 'Select a column':
        y_var = df[selected_y_var]    
    
    # Remove y_var from available columns
    available_columns = [col for col in all_columns if col != selected_y_var]
    print(available_columns)
    
    # Create a column selector for multiple columns
    selected_columns = st.sidebar.multiselect("Select Junk columns:", available_columns)
    
    # Always display the dataset
    dataset_preview = st.markdown("## Dataset Preview")
    dataset_preview.write(df)
    
    if st.sidebar.button("Preview!"):
        # Drop selected columns
        df_highlighted = df.drop(selected_columns, axis=1)
        dataset_preview.empty()  # Clear previous output
        dataset_preview = st.markdown("## Updated Dataset Preview")
        dataset_preview.write(df_highlighted)
        
        # Display the updated dataset shape after removing junk columns
        st.sidebar.markdown("## Updated Dataset Shape")
        st.sidebar.markdown(f'<span style="color:green;">Number of Rows:</span> {df_highlighted.shape[0]}', unsafe_allow_html=True)
        st.sidebar.markdown(f'<span style="color:green;">Number of Columns:</span> {df_highlighted.shape[1]}', unsafe_allow_html=True)
        
        # Ask if dataset has categorical values
        categorical = st.sidebar.radio("Does your dataset have categorical values?", ("Yes", "No"))
        if categorical == "Yes":
            # Display buttons for categorical operations
            st.sidebar.markdown(
                '<div style="display: flex; justify-content: space-between;">'
                '<button type="submit" style="background-color: black; color: white; border: none; padding: 10px 20px; cursor: pointer;">GET DUMMIES</button>'
                '<button type="submit" style="background-color: black; color: white; border: none; padding: 10px 20px; cursor: pointer;">FIT TRANSFORM</button>'
                '</div>', unsafe_allow_html=True
            )
        else:
            st.sidebar.write("No categorical values in dataset.")
