import streamlit as st
import random
import pandas as pd
import datetime

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Eren Erdoğan | Enterprise Air Cargo Control Tower",
    page_icon="✈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Yan Menüden Modül Seçimi
st.sidebar.markdown("### 🎛️ CONTROL CENTER SUITE")
st.sidebar.markdown("---")
modul = st.sidebar.radio("Select Operational Module:", [
    "📦 Live AWB Tracking & Telemetry", 
    "💰 Demurrage & Storage Risk Suite", 
    "📊 Route Yield & Corridor Analytics",
    "🛄 ULD & Center of Gravity Optimizer",
    "🌱 CORSIA Green Logistics & ESG",
    "👤 About & Professional Profile"
])

# HER SAYFAYA ÖZEL FARKLI ARKA PLAN GÖRSELİ
bg_images = {
    "📦 Live AWB Tracking & Telemetry": "https://images.unsplash.com/photo-1570125909232-eb263c188f7e", 
    "💰 Demurrage & Storage Risk Suite": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d", 
    "📊 Route Yield & Corridor Analytics": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05", 
    "🛄 ULD & Center of Gravity Optimizer": "https://images.unsplash.com/photo-1519003722824-194d4455a60c", 
    "🌱 CORSIA Green Logistics & ESG": "https://images.unsplash.com/photo-1506015391300-4802dc74de2e", 
    "👤 About & Professional Profile": "https://images.unsplash.com/photo-1517976487492-5750f3195933" 
}

current_bg = bg_images.get(modul, bg_images["📦 Live AWB Tracking & Telemetry"])

# Profesyonel CSS & Renkli Glassmorphism Tasarım (Süslü Parantezler Çiftlendi)
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(4, 9, 20, 0.90), rgba(8, 15, 30, 0.94)), 
                          url("{current_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .main-header {{
        font-family: 'Helvetica Neue', sans-serif;
        color: #ffffff;
        font-weight: 900;
        letter-spacing: -0.5px;
        text-shadow: 0 2px 10px rgba(0, 210, 255, 0.3);
    }}
    .ticker-box {{
        background: linear-gradient(90deg, rgba(0, 210, 255, 0.15), rgba(58, 123, 213, 0.15));
        border-left: 5px solid #00d2ff;
        border-right: 5px solid #3a7bd5;
        padding: 12px 18px;
        border-radius: 8px;
        margin-bottom: 25px;
        font-size: 14px;
        color: #f1f5f9;
        box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }}
    .portfolio-box {{
        background: linear-gradient(135deg, rgba(15, 32, 67, 0.85), rgba(5, 15, 30, 0.95));
        border: 2px solid #00d2ff;
        padding: 45px;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.7);
        text-align: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Canlı Sistem Alarm Bandı (Ticker)
st.markdown(
    """
    <div class="ticker-box">
        <b>⚡ LIVE GATEWAY TICKER:</b> [IST HUB] Zone C capacity at 88% | [TK-1984] Flight en-route to FRA (FL350) | [CUSTOMS] Pre-declaration SLA: 99.6% | [SECURITY] ULD weight balance verified.
    </div>
    """,
    unsafe_allow_html=True
)

# Üst Başlık
st.markdown("<h1 class='main-header'>✈️ Global Air Freight Enterprise Control Tower</h1>", unsafe_allow_html=True)
st.markdown("**Next-Gen Logistics Operations, Real-Time Telemetry, Financial Risk Engine & ULD Suite**")
st.markdown("---")

st.sidebar.markdown("---")
st.sidebar.info("📌 **System Status:** Active (99.9% Uptime)\n\n🌐 **Gateway Hub:** IST Mega Core\n\n🔒 **Security:** Enterprise Grade A+")

# ----------------- MODÜL 1: LIVE AWB TRACKING -----------------
if modul == "📦 Live AWB Tracking & Telemetry":
    st.subheader("📦 Master Air Waybill (AWB) Real-Time Telemetry & Milestones")
    st.markdown("Monitor multi-leg shipment statuses, gateway checkpoints, and real-time SLA deviation risks.")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        awb_no = st.text_input("Master AWB Number:", "235-84920192")
    with col2:
        carrier = st.selectbox("Carrier Airline:", ["Turkish Cargo (THY)", "Lufthansa Cargo", "Qatar Cargo", "Emirates SkyCargo"])
    with col3:
        dest = st.selectbox("Destination Hub:", ["JFK (New York)", "FRA (Frankfurt)", "DXB (Dubai)", "ICN (Seoul)", "AMS (Amsterdam)"])

    if st.button("Execute Live Gateway Query", type="primary"):
        with st.spinner(f'Establishing secure API handshake with {carrier} network...'):
            st.success(f"Connection Verified | Carrier: **{carrier}** | Corridor: **IST ➔ {dest}** | AWB: **{awb_no}**")
            
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Current Milestone", "ARR (Arrived)", "+1.2h vs ETA")
            m2.metric("SLA Compliance", "99.6%", "Optimal Performance")
            m3.metric("Cold Chain (PHA)", "+4.1 °C", "Strict Range Maintained")
            m4.metric("Risk Index", "Low", "Secure Corridor")

            st.markdown("### 📍 Operational Milestone Progress Tracker")
            milestones = ["1. Booking (BK)", "2. RCS (Acceptance)", "3. BUILDP (Build-up)", "4. DEP (Departure)", "5. ARR (Arrival)", "6. RCF (Customs Transfer)", "7. DLV (Delivery)"]
            current_step = 5 
            progress_val = int((current_step / len(milestones)) * 100)
            st.progress(progress_val, text=f"Active Milestone Phase: {milestones[current_step-1]}")

            tab1, tab2, tab3 = st.tabs(["Flight Telemetry", "Audit Logs", "Customs & Compliance"])
            with tab1:
                st.write("**Aircraft Registration:** TC-LJC (Boeing 777F Freighter)")
                st.write("**Total Chargeable Weight:** 2,850 KG (Volumetric Ratio: 1:6)")
                st.write("**Special Service Codes:** EAT (Perishable Foodstuffs), GEN")
                st.write("**Warehouse Bay:** IST Cargo Terminal - Zone C, Rack 14")
            with tab2:
                log_df = pd.DataFrame({
                    "Timestamp": ["2026-10-06 14:30", "2026-10-06 09:15", "2026-10-05 22:00"],
                    "Checkpoint": [dest, "In-Flight Corridor", "IST Origin Hub"],
                    "Event Description": ["Aircraft landed, awaiting customs ramp transfer", "Cruising at FL350, fuel burn nominal", "Cargo build-up completed and loaded into PMC ULD"]
                })
                st.dataframe(log_df, use_container_width=True)
            with tab3:
                st.warning("⚠️ **Automated Notice:** Destination customs pre-declaration is active. Ensure commercial invoice and phytosanitary certificates are attached to prevent terminal dwell penalties.")

# ----------------- MODÜL 2: DEMURRAGE RISK SUITE -----------------
elif modul == "💰 Demurrage & Storage Risk Suite":
    st.subheader("💰 Demurrage & Storage Financial Risk Predictive Engine")
    st.markdown("Simulate holding penalties, warehouse dwell time impacts, and potential demurrage liabilities before they occur.")

    c1, c2, c3 = st.columns(3)
    with c1:
        kargo_tipi = st.selectbox("Cargo Classification:", ["General Cargo", "Perishable (Cold Chain)", "Dangerous Goods (DG)", "Valuable Cargo (VAL)"])
    with c2:
        agirlik_kg = st.number_input("Chargeable Weight (KG):", min_value=100, max_value=100000, value=4500)
    with c3:
        bekleme_gun = st.slider("Terminal Dwell Time (Days):", 1, 30, 6)

    if st.button("Run Financial Exposure Simulation", type="primary"):
        carpanlar = {"General Cargo": 0.18, "Perishable (Cold Chain)": 0.40, "Dangerous Goods (DG)": 0.65, "Valuable Cargo (VAL)": 0.95}
        gunluk_oran = carpanlar.get(kargo_tipi, 0.20)
        
        chargeable_days = max(0, bekleme_gun - 3) 
        total_cost = agirlik_kg * gunluk_oran * chargeable_days
        
        st.markdown("### 📊 Financial Exposure & Penalty Breakdown")
        r1, r2, r3, r4 = st.columns(4)
        r1.metric("Free Time Allowance", "3 Days", "Standard SLA")
        r2.metric("Billable Storage Days", f"{chargeable_days} Days")
        r3.metric("Daily Storage Rate", f"${gunluk_oran}/KG")
        r4.metric("Estimated Total Demurrage", f"${total_cost:,.2f}", delta_color="inverse")

        if total_cost > 0:
            st.error(f"🚨 **Critical Financial Alert:** Accumulated storage penalty has reached **${total_cost:,.2f}** due to extended dwell time on day {bekleme_gun}. Immediate broker escalation is mandatory.")
            
            with st.expander("📄 Generate Automated Demurrage Waiver Request Letter"):
                st.text(f"""
To: Terminal Operations Management
Subject: Waiver Request for Demurrage Charges - AWB 235-84920192

Dear Operations Team,
We kindly request an extension of the free time allowance for our consignment weighing {agirlik_kg} KG ({kargo_tipi}), 
currently held at terminal warehouse due to unexpected customs clearance delays. Total accumulated penalty stands at ${total_cost:,.2f}.
Your cooperation in waiving or reducing these charges is greatly appreciated.

Sincerely,
Eren Erdoğan
Operations Control Team
                """)
        else:
            st.success("✅ **Within Free Time Window:** Shipment is currently safe from demurrage and storage penalties.")

# ----------------- MODÜL 3: ROUTE ANALYTICS -----------------
elif modul == "📊 Route Yield & Corridor Analytics":
    st.subheader("📊 IST Hub Outbound Route Capacity & Yield Dashboard")
    st.markdown("Comprehensive performance metrics across strategic global air freight corridors.")

    data = {
        "Route Corridor": ["IST - JFK", "IST - FRA", "IST - DXB", "IST - ICN", "IST - AMS", "IST - NRT"],
        "Weekly Frequencies": [14, 21, 18, 7, 10, 5],
        "Load Factor (%)": [95.2, 89.1, 92.4, 97.6, 86.5, 93.8],
        "Total Uplifted Tonnage (Tons)": [1450, 1120, 1250, 960, 710, 590],
        "Average Yield ($/KG)": [3.45, 2.80, 2.95, 3.85, 2.70, 4.10]
    }
    df_hatlar = pd.DataFrame(data)
    
    st.dataframe(df_hatlar, use_container_width=True)
    st.markdown("### 📈 Corridor Load Factor Comparison")
    st.bar_chart(df_hatlar.set_index("Route Corridor")["Load Factor (%)"])

# ----------------- MODÜL 4: ULD OPTIMIZER -----------------
elif modul == "🛄 ULD & Center of Gravity Optimizer":
    st.subheader("🛄 Unit Load Device (ULD) Volume & Center of Gravity (CG) Suite")
    st.markdown("Advanced wide-body freighter contour space planning and weight distribution simulator.")

    col_a, col_b = st.columns(2)
    with col_a:
        uld_tipi = st.selectbox("ULD Container Type Profile:", ["LD3 (Lower Deck Contour - 4.5 m³)", "PMC (Main Deck Pallet - 6.8 m³)", "AKE (Standard Contour - 4.3 m³)"])
        kargo_hacmi = st.number_input("Total Consignment Volume (m³):", min_value=1.0, max_value=200.0, value=34.5)
    with col_b:
        max_payload = st.number_input("Max Allowable Payload per ULD (KG):", min_value=500, max_value=6800, value=1500)
        total_weight_input = st.number_input("Total Shipment Gross Weight (KG):", min_value=100, max_value=50000, value=4800)

    kapasite = 4.5 if "LD3" in uld_tipi else (6.8 if "PMC" in uld_tipi else 4.3)
    gereken_uld = int((kargo_hacmi // kapasite) + (1 if kargo_hacmi % kapasite > 0 else 0))

    if st.button("Compute Optimal ULD Matrix & CG", type="primary"):
        st.success(f"Selected ULD Specification: **{uld_tipi}**")
        c_1, c_2, c_3 = st.columns(3)
        c_1.metric("Required Container Count", f"{gereken_uld} Units")
        c_2.metric("Volumetric Space Efficiency", f"%{min(100, int((kargo_hacmi / (gereken_uld * kapasite)) * 100))}")
        c_3.metric("Center of Gravity (CG)", "Balanced (Limit: ±2.5%)", "Pass")
        st.info("💡 **Load Control Insight:** Main deck PMC pallet utilization yields higher structural stacking efficiency for heavy industrial machinery while keeping aircraft trim within safety envelopes.")

# ----------------- MODÜL 5: CORSIA ESG -----------------
elif modul == "🌱 CORSIA Green Logistics & ESG":
    st.subheader("🌱 Green Supply Chain & CORSIA Carbon Emission Estimator")
    st.markdown("Calculate estimated CO2 footprint for air cargo transportation in compliance with international aviation environmental standards.")

    col_x, col_y = st.columns(2)
    with col_x:
        dist_km = st.slider("Great Circle Flight Distance (KM):", 500, 18000, 5200)
    with col_y:
        cargo_tons = st.number_input("Consignment Weight (Metric Tons):", 1.0, 150.0, 22.5)
    
    co2_emission = dist_km * cargo_tons * 0.58 
    
    if st.button("Calculate Environmental Footprint", type="primary"):
        st.metric("Estimated CO2 Emissions", f"{co2_emission:,.2f} KG CO2")
        st.info("🌍 **CORSIA Advisory:** Carbon offset certificates via Sustainable Aviation Fuel (SAF) blending credits can be allocated to achieve net-zero transport compliance under international regulatory frameworks.")

# ----------------- MODÜL 6: ABOUT / PORTFOLIO -----------------
elif modul == "👤 About & Professional Profile":
    st.subheader("👤 Professional Profile & Academic Portfolio")
    st.markdown("Verified student portfolio and technical project credentials.")
    
    st.markdown(
        """
        <div class="portfolio-box">
            <h1 style="color: #00d2ff; margin-bottom: 10px; font-weight: 900; font-size: 38px;">Eren Erdoğan</h1>
            <p style="color: #ffffff; font-size: 20px; font-weight: 600; margin-bottom: 15px;">Civil Air Transportation Management Student</p>
            <p style="color: #00d2ff; font-size: 15px; font-weight: 500; letter-spacing: 1.5px; margin-bottom: 25px;">AIR CARGO OPERATIONS & CONTROL TOWER SYSTEMS PORTFOLIO</p>
            <hr style="border-color: rgba(0,210,255,0.4); margin: 25px 0;">
            <p style="color: #e2e8f0; font-size: 18px; margin-bottom: 15px;">📧 <b>Direct Professional Contact:</b> <a href="mailto:erenerdogan.808@gmail.com" style="color: #00d2ff; text-decoration: none;">erenerdogan.808@gmail.com</a></p>
            <p style="color: #cbd5e1; font-size: 16px; margin-top: 20px; line-height: 1.6; max-width: 800px; margin-left: auto; margin-right: auto;">
                Dedicated Civil Air Transportation Management student passionate about digital logistics architectures, real-time AWB tracking systems, demurrage risk mitigation workflows, and capacity optimization models. Bridging aviation management theory with modern software tools.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("### 🏆 Academic Focus & Technical Competencies")
    col_s1, col_s2, col_s3 = st.columns(3)
    col_s1.markdown("✔️ **Air Cargo Operations:** AWB tracking, RCS, DEP, ARR, RCF milestones & SLA management.")
    col_s2.markdown("✔️ **Data & Software Tools:** Python, Streamlit, Pandas, and interactive Control Tower design.")
    col_s3.markdown("✔️ **Risk & Cost Analysis:** Demurrage calculations, ULD load balancing, and CORSIA framework.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8;'>Civil Air Transportation Management Student | Enterprise Proof of Work Portfolio</p>", unsafe_allow_html=True)