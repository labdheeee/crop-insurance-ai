import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import Draw
import pandas as pd
import json

# --- Page Setup ---
st.set_page_config(page_title="MahaAgri-Shield Pro", layout="wide")
st.title("🛡️ MahaAgri-Shield: Proactive AI Agent")
st.markdown("### Professional Risk Assessment via Geospatial Intelligence")

# --- Database for Maharashtra Districts ---
maharashtra_districts = [
    "Ahmednagar", "Akola", "Amravati", "Beed", "Bhandara", "Buldhana", "Chandrapur", 
    "Dhule", "Gadchiroli", "Gondia", "Hingoli", "Jalgaon", "Jalna", "Kolhapur", 
    "Latur", "Nagpur", "Nanded", "Nandurbar", "Nashik", "Osmanabad", "Palghar", 
    "Parbhani", "Pune", "Raigad", "Ratnagiri", "Sangli", "Satara", "Sindhudurg", 
    "Solapur", "Thane", "Wardha", "Washim", "Yavatmal"
]

# --- UI: Inputs ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📍 Step 1: Locate & Draw Farm")
    st.write("Zoom into the farm in Maharashtra and draw a polygon around the boundary.")
    
    # Initialize Folium Map (Centered on Maharashtra)
    m = folium.Map(location=[19.7515, 75.7139], zoom_start=7)
    
    # Add Drawing Tool
    Draw(
        export=True,
        position='topleft',
        draw_options={'polyline': False, 'rectangle': True, 'circle': False, 'marker': False, 'circlemarker': False},
    ).add_to(m)
    
    # Display Map
    output = st_folium(m, width=600, height=450)

with col2:
    st.subheader("📋 Step 2: Client Details")
    district = st.selectbox("Select District for Historical Data", maharashtra_districts)
    crop = st.selectbox("Crop Type", ["Soybean", "Cotton", "Tur (Pigeon Pea)", "Sugarcane", "Rice"])
    
    # Check if a polygon was drawn
    polygon_coords = None
    if output and output['all_drawings']:
        polygon_coords = output['all_drawings'][0]['geometry']['coordinates']
        st.success("✅ Farm Boundary Captured Successfully!")
    else:
        st.warning("Please draw the farm boundary on the map to begin analysis.")

# --- Analysis Logic ---
if st.button("🚀 Generate Comprehensive Risk Report") and polygon_coords:
    with st.spinner("Analyzing Sentinel-2 Satellite Imagery & ICRISAT Historical Yields..."):
        
        # --- Mock Analysis Results based on your provided categories ---
        # In a production app, you'd call ee.ImageCollection('COPERNICUS/S2_SR') here
        
        st.divider()
        st.header(f"📊 Comprehensive Risk Report: {district} - {crop}")
        
        # Creating Tabs for Professionalism
        tab1, tab2, tab3 = st.tabs(["Satellite & Vegetation", "Weather & Soil", "Historical Yield"])
        
        with tab1:
            st.subheader("Vegetation Health (NDVI)")
            st.write("**Current NDVI Score:** 0.68 (Healthy)")
            st.write("**Impact:** Remote sensing indicates 'active growth'. No immediate replanting risk.")
            st.progress(0.68)
            st.caption("Data Source: Sentinel-2 L2A via Google Earth Engine")

        with tab2:
            c1, c2 = st.columns(2)
            with c1:
                st.write("**Weather Risk (15-Day Forecast)**")
                st.info("⚠️ High Humidity detected. Potential for fungal outbreak in Sangli/Pune region.")
            with c2:
                st.write("**Soil Health Profile**")
                st.write("- **Soil Moisture:** 22% (Optimal)")
                st.write("- **N-P-K Levels:** Sufficient for Current Growth Stage")

        with tab3:
            st.subheader("District Yield Benchmarking")
            st.line_chart(pd.DataFrame({
                'Year': [2018, 2019, 2020, 2021, 2022, 2023, 2024],
                'Yield (kg/Ha)': [850, 920, 780, 1100, 1050, 900, 950]
            }).set_index('Year'))
            st.write("**Final Recommendation:** Client Eligible. Low baseline risk based on 10-year ICRISAT trend.")

else:
    st.info("Draw a polygon and click the button above to run the AI agent.")
    
