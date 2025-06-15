import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Data Mining Guide for Data Scientists",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main app title and description
st.title("Data Mining Guide for Data Scientists")
st.markdown("""
Welcome to the **Data Mining Guide**! This app helps data scientists mine data for businesses, projects, and research firms. Navigate to:
- **Guide**: Learn about data mining concepts, applications, and tools.
- **Application**: Upload datasets, explore data, and visualize insights.
""")

# Footer
st.markdown("""
---
**Built with Streamlit** | Powered by xAI's Grok 3 | For API details, visit [xAI's API](https://x.ai/api).
""")
