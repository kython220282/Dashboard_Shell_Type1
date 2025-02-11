import streamlit as st
from datetime import datetime

st.set_page_config(layout="wide")
# Load the CSS file
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title("Streamlit Dashboard")

# Define the reusable component function
def add_filters(key_prefix):
    st.subheader('Report Filters',divider="grey")
    
    # Date range picker
    date_range = st.date_input("Select date range", [datetime(2022, 1, 1), datetime(2022, 12, 31)], key=f"{key_prefix}_date_range")
    st.write('')
    # Two filters
    filter1 = st.selectbox("Select filter 1", ["Option 1", "Option 2", "Option 3"], key=f"{key_prefix}_filter1")
    st.write('')
    filter2 = st.selectbox("Select filter 2", ["Option A", "Option B", "Option C"], key=f"{key_prefix}_filter2")
    st.write('')
    return date_range, filter1, filter2

# Create tabs
tab1, tab2, tab3 = st.tabs(['Overall Performance', 'Performance Measure # 1', 'Performance Measure # 2'])

with tab1:
    col1, col2 = st.columns([1, 3])

    with col1:
        # Call the component function with a unique key prefix
        date_range, filter1, filter2 = add_filters("tab1_col1")

    with col2:
        st.subheader('Overall Performance',divider="grey")    
        a, b, c, d, e = st.columns(5)
        a.metric("Temperature", "30°F", "-9°F", border=True)
        b.metric("Wind", "4 mph", "2 mph", border=True)     
        c.metric("Humidity", "77%", "5%", border=True)
        d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)
        e.metric("Visibility", "10 mi", "0 mi", border=True)

        st.write('')
        f,g = st.columns(2)

        with f:
            st.markdown("<h4 class='chart-title'>Trend Chart</h4>", unsafe_allow_html=True)
            st.line_chart([1, 2, 3, 4])
            
        with g:
            st.markdown("<h4 class='chart-title'>Bar Chart</h4>", unsafe_allow_html=True)
            st.bar_chart([10, 12, 23, 14])

with tab2:
    col1, col2 = st.columns([1, 3])

    with col1:
        # Call the component function with a unique key prefix
        date_range, filter1, filter2 = add_filters("tab2_col1")

    with col2:
        st.subheader('Performance Measure #1',divider="grey")
        
        a,b = st.columns(2)
        with a:
            st.markdown("<h4 class='chart-title'>Trend Chart</h4>", unsafe_allow_html=True)
            st.line_chart([1, 2, 3, 4])
        with b:
            st.markdown("<h4 class='chart-title'>Bar Chart</h4>", unsafe_allow_html=True)
            st.bar_chart([10, 12, 23, 14])
        
        c,d = st.columns(2)
        with c:
            st.markdown("<h4 class='chart-title'>Trend Chart</h4>", unsafe_allow_html=True)
            st.line_chart([1, 2, 3, 4])
        with d:
            st.markdown("<h4 class='chart-title'>Bar Chart</h4>", unsafe_allow_html=True)
            st.bar_chart([10, 12, 23, 14])
        

with tab3:
    col1, col2 = st.columns([1, 3])

    with col1:
        # Call the component function with a unique key prefix
        date_range, filter1, filter2 = add_filters("tab3_col1")

    with col2:
        st.subheader('Performance Measure #2',divider="grey")
        a,b = st.columns(2)
        with a:
            st.markdown("<h4 class='chart-title'>Trend Chart</h4>", unsafe_allow_html=True)
            st.line_chart([1, 2, 3, 4])
        with b:
            st.markdown("<h4 class='chart-title'>Bar Chart</h4>", unsafe_allow_html=True)
            st.bar_chart([10, 12, 23, 14])
        
        c,d = st.columns(2)
        with c:
            st.markdown("<h4 class='chart-title'>Trend Chart</h4>", unsafe_allow_html=True)
            st.line_chart([1, 2, 3, 4])
        with d:
            st.markdown("<h4 class='chart-title'>Bar Chart</h4>", unsafe_allow_html=True)
            st.bar_chart([10, 12, 23, 14])
