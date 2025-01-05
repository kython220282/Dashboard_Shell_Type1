# Streamlit Dashboard Shell Type 1

This is a Streamlit-based interactive dashboard for visualizing and analyzing performance data across multiple dimensions. The dashboard provides customizable filters, metrics, and visualizations to help users gain insights into overall performance and specific performance measures.

## Features

- **Responsive Design**: A wide layout optimized for better usability.
- **Reusable Components**: A modular `add_filters` function for adding consistent filters across tabs.
- **Customizable Filters**: 
  - Date range picker for selecting specific periods.
  - Two dropdown filters with customizable options.
- **Tabs for Insights**:
  - **Overall Performance**: Displays key metrics and visualizations for a holistic view.
  - **Performance Measure #1**: Focused visualizations and metrics for a specific dimension.
  - **Performance Measure #2**: Detailed insights into another performance dimension.
- **Interactive Visualizations**:
  - Line charts and bar charts for trend and comparative analysis.
- **Metrics Display**: Highlights key indicators like temperature, wind, humidity, pressure, and visibility in a visually engaging format.

## File Structure

- **`main.py`**: Core Streamlit script for the dashboard.
- **`styles.css`**: Custom CSS for styling the dashboard (ensure this file is in the same directory as `main.py`).

## Setup and Usage

### Prerequisites
- Python 3.7 or higher
- Streamlit library installed (`pip install streamlit`)

### Installation
1. Clone this repository or copy the script into your project directory.
2. Ensure `styles.css` is in the same directory as `main.py`.

### Running the Application
1. Navigate to the directory containing `main.py`.
2. Run the Streamlit server:
   ```bash
   streamlit run main.py
