import base64
import os
import random
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="CargoPulse | Air Cargo Control Suite",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if "logged_in" not in st.session_state:
  st.session_state.logged_in = False

query_params = st.query_params
if "action" in query_params and query_params["action"] == "start":
  st.session_state.logged_in = True

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COVER_IMAGE_PATH = os.path.join(BASE_DIR, "cargopulse_cover.png")

img_b64 = ""
if os.path.exists(COVER_IMAGE_PATH):
  with open(COVER_IMAGE_PATH, "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode()

# ---------------------------------------------------------
# SPLASH SCREEN / FULLSCREEN KAPAK VE GET STARTED BUTONU
# ---------------------------------------------------------
if not st.session_state.logged_in:
  bg_css = (
      f'background-image: url("data:image/png;base64,{img_b64}");'
      if img_b64
      else "background-color: #0b1329;"
  )
  st.markdown(
      f"""
    <style>
    header {{ visibility: hidden !important; height: 0 !important; }}
    #MainMenu {{ visibility: hidden !important; }}
    footer {{ visibility: hidden !important; }}
    
    .stApp {{
        background-color: #0b1329 !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
    }}
    .block-container {{
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }}
    .fullscreen-bg {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        {bg_css}
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        z-index: 999;
    }}
    .custom-get-started-btn {{
        position: fixed;
        top: 82%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 230px;
        height: 55px;
        background: rgba(14, 116, 144, 0.9);
        border: 2px solid #38bdf8;
        border-radius: 30px;
        z-index: 1001;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-decoration: none;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.6);
        transition: all 0.3s ease;
    }}
    .custom-get-started-btn:hover {{
        background: rgba(56, 189, 248, 1);
        border-color: #ffffff;
        box-shadow: 0 0 35px rgba(56, 189, 248, 1);
        color: #ffffff !important;
    }}
    </style>

    <div class="fullscreen-bg"></div>
    <a href="/?action=start" target="_self" class="custom-get-started-btn">
        GET STARTED ➔
    </a>
    """,
      unsafe_allow_html=True,
  )

else:
  # ---------------------------------------------------------
  # ANA UYGULAMA EKRANI (UÇAK ANIMASYONU VE PARLAK BEYAZ BANT)
  # ---------------------------------------------------------
  st.markdown(
      """
        <style>
        .stApp {
            background-color: #f8fafc !important;
            color: #0f172a !important;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        h1, h2, h3, h4, h5, h6, p, span, label, div {
            color: #0f172a !important;
        }
        .main .block-container {
            padding-bottom: 90px !important;
            padding-top: 2rem !important;
        }
        .thy-header {
            background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
            padding: 24px 35px;
            border-radius: 16px;
            box-shadow: 0 10px 25px -5px rgba(30, 58, 138, 0.3);
            margin-bottom: 25px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: relative;
            overflow: hidden;
        }
        .thy-header * { color: #ffffff !important; }
        .thy-logo-title {
            font-size: 2.2rem;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 14px;
        }
        .thy-motto {
            font-size: 1.15rem;
            color: #bae6fd !important;
            font-style: italic;
        }

        /* EKG Pulse Animasyonu */
        .pulse-svg path {
            stroke-dasharray: 600;
            stroke-dashoffset: 600;
            animation: dash 2.5s linear infinite;
        }
        @keyframes dash {
            from { stroke-dashoffset: 600; }
            to { stroke-dashoffset: 0; }
        }

        /* Hareketli Uçak Animasyonu (Başlığın Sağ Tarafında) */
        .flying-plane {
            font-size: 1.8rem;
            display: inline-block;
            animation: fly-plane 6s ease-in-out infinite;
            margin-left: 15px;
        }
        @keyframes fly-plane {
            0% { transform: translateX(0px) translateY(0px) rotate(0deg); opacity: 0.7; }
            50% { transform: translateX(25px) translateY(-5px) rotate(5deg); opacity: 1; }
            100% { transform: translateX(0px) translateY(0px) rotate(0deg); opacity: 0.7; }
        }

        /* Modern Yatay Menü */
        div[data-testid="stRadio"] {
            background: #ffffff;
            padding: 12px 18px;
            border-radius: 12px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03);
            margin-bottom: 25px;
        }
        div[data-testid="stRadio"] div[role="radiogroup"] {
            display: flex;
            flex-direction: row;
            gap: 12px;
            flex-wrap: wrap;
        }
        div[data-testid="stRadio"] label {
            background: #f1f5f9 !important;
            padding: 8px 14px !important;
            border-radius: 8px !important;
            border: 1px solid #cbd5e1 !important;
        }
        div[data-testid="stRadio"] label p {
            color: #0f172a !important;
            font-weight: 700 !important;
            font-size: 0.92rem !important;
        }

        /* DGR ve Selectbox Açılır Menü */
        div[data-baseweb="select"] div, div[data-baseweb="popover"] div, ul[role="listbox"] li, div[role="option"] {
            color: #ffffff !important;
            background-color: #1e293b !important;
        }
        div[data-baseweb="select"] span {
            color: #ffffff !important;
        }

        .hub-table {
            width: 100%;
            border-collapse: collapse;
            background: #ffffff;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid #e2e8f0;
        }
        .hub-table th {
            background: #1e3a8a !important;
            color: #ffffff !important;
            font-weight: 700;
            padding: 14px;
            text-align: left;
        }
        .hub-table td {
            padding: 12px 14px;
            color: #334155 !important;
            border-bottom: 1px solid #f1f5f9;
        }
        .status-badge {
            background: #dcfce7;
            color: #166534 !important;
            padding: 4px 10px;
            border-radius: 20px;
            font-weight: 700;
        }
        .equal-img-container img {
            height: 250px !important;
            object-fit: cover !important;
            border-radius: 12px !important;
        }
        .purpose-img {
            width: 100% !important;
            height: 320px !important;
            object-fit: cover !important;
            border-radius: 12px !important;
        }

        /* Alt Sabit Canlı Bant - TÜM YAZILAR KESİN %100 BEYAZ */
        .ticker-container-fixed {
            position: fixed !important;
            bottom: 0 !important;
            left: 0 !important;
            width: 100% !important;
            height: 44px !important;
            background-color: #0b1329 !important;
            box-shadow: 0 -4px 20px rgba(0,0,0,0.5) !important;
            z-index: 999999 !important;
            border-top: 3px solid #38bdf8 !important;
            display: flex !important;
            align-items: center !important;
            overflow: hidden !important;
        }
        .ticker-live-badge {
            background: #1e3a8a !important;
            color: #ffffff !important;
            font-weight: 900 !important;
            font-size: 0.85rem !important;
            height: 100% !important;
            display: flex !important;
            align-items: center !important;
            padding: 0 18px !important;
            z-index: 1000000 !important;
            letter-spacing: 1px !important;
            white-space: nowrap !important;
        }
        .ticker-scroll-wrap {
            width: 100% !important;
            overflow: hidden !important;
            white-space: nowrap !important;
        }
        .ticker-scroll-text {
            display: inline-block !important;
            padding-left: 100% !important;
            animation: ticker-anim 35s linear infinite !important;
        }
        .ticker-item {
            display: inline-block !important;
            padding: 0 2rem !important;
            font-size: 0.95rem !important;
            color: #ffffff !important;
            font-weight: 600 !important;
            font-family: monospace !important;
        }
        .ticker-item, .ticker-item span, .ticker-item b {
            color: #ffffff !important;
        }
        @keyframes ticker-anim {
            0% { transform: translate3d(0, 0, 0); }
            100% { transform: translate3d(-100%, 0, 0); }
        }
        </style>
        """,
      unsafe_allow_html=True,
  )

  st.markdown(
      """
        <div class="thy-header">
            <div>
                <div class="thy-logo-title">
                    <svg class="pulse-svg" width="50" height="35" viewBox="0 0 100 40">
                        <path d="M0,20 L25,20 L30,5 L38,35 L45,10 L52,28 L58,20 L100,20" 
                              fill="none" stroke="#38bdf8" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    <span>CARGO<span style="color: #38bdf8;">PULSE</span></span>
                    <span class="flying-plane">✈️</span>
                </div>
                <div class="thy-motto">"Measuring the Pulse of Your Cargo"</div>
            </div>
            <div style="text-align: right; background: rgba(255,255,255,0.15); padding: 8px 18px; border-radius: 20px;">
                <span style="font-weight:700; font-size: 0.95rem; color: #ffffff !important;">Global Fleet Control Suite</span>
            </div>
        </div>
        """,
      unsafe_allow_html=True,
  )

  module = st.radio(
      "Navigation",
      [
          "Home and Live Fleet Pulse",
          "AWB Flight Ticket and Route Generator",
          "IATA Chargeable Weight Engine",
          "DGR and Hazmat Compliance",
          "ULD and Aircraft Clearance",
          "Purpose of CargoPulse",
          "About Developer",
      ],
      horizontal=True,
      label_visibility="collapsed",
  )

  st.markdown("<br>", unsafe_allow_html=True)

  IMG_HOME_1 = "https://images.pexels.com/photos/912050/pexels-photo-912050.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  IMG_HOME_2 = "https://images.pexels.com/photos/46148/aircraft-jet-landing-cloud-46148.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  IMG_HOME_3 = "https://images.pexels.com/photos/358319/pexels-photo-358319.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  IMG_TICKET = "https://images.pexels.com/photos/2026324/pexels-photo-2026324.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  IMG_IATA = "https://images.pexels.com/photos/4483610/pexels-photo-4483610.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  IMG_DGR = "https://images.pexels.com/photos/2026322/pexels-photo-2026322.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  IMG_ULD = "https://images.pexels.com/photos/1004584/pexels-photo-1004584.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  IMG_PURPOSE_1 = "https://images.pexels.com/photos/726233/pexels-photo-726233.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  IMG_PURPOSE_2 = "https://images.pexels.com/photos/6169052/pexels-photo-6169052.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
  IMG_DEV = "https://images.pexels.com/photos/590022/pexels-photo-590022.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"

  if module == "Home and Live Fleet Pulse":
    st.subheader("Global Network Control and Cargo Telemetry")
    col_img1, col_img2, col_img3 = st.columns(3)
    with col_img1:
      st.markdown(
          f'<div class="equal-img-container"><img src="{IMG_HOME_1}"'
          ' style="width:100%;"></div>',
          unsafe_allow_html=True,
      )
    with col_img2:
      st.markdown(
          f'<div class="equal-img-container"><img src="{IMG_HOME_2}"'
          ' style="width:100%;"></div>',
          unsafe_allow_html=True,
      )
    with col_img3:
      st.markdown(
          f'<div class="equal-img-container"><img src="{IMG_HOME_3}"'
          ' style="width:100%;"></div>',
          unsafe_allow_html=True,
      )

    st.markdown("### Live Telemetry Metrics")
    m1, m2, m3, m4 = st.columns(4)
    with m1:
      st.metric(
          label="Active Cargo Flights", value="48 Aircraft", delta="+4 Active"
      )
    with m2:
      st.metric(
          label="Daily Freight Tonnage", value="1,850 Tons", delta="+12.2%"
      )
    with m3:
      st.metric(
          label="On-Time Delivery SLA", value="99.6%", delta="+0.4%"
      )
    with m4:
      st.metric(
          label="Fleet Cargo Pulse", value="78 BPM", delta="Normal Rhythm"
      )

    st.markdown("---")
    st.markdown("### Gateway Hub Operations Status")
    st.markdown(
        """
        <table class="hub-table">
            <thead>
                <tr>
                    <th>Hub Code</th>
                    <th>Gateway Airport</th>
                    <th>Inbound Tonnage</th>
                    <th>Outbound Tonnage</th>
                    <th>Operational Status</th>
                </tr>
            </thead>
            <tbody>
                <tr><td><b>IST</b></td><td>Istanbul Airport (IST) Cargo City</td><td>420 Tons</td><td>490 Tons</td><td><span class="status-badge">Optimal</span></td></tr>
                <tr><td><b>JFK</b></td><td>John F. Kennedy Intl (JFK)</td><td>380 Tons</td><td>410 Tons</td><td><span class="status-badge">Smooth</span></td></tr>
                <tr><td><b>FRA</b></td><td>Frankfurt Airport (FRA) CargoHub</td><td>510 Tons</td><td>480 Tons</td><td><span class="status-badge" style="background:#fef3c7; color:#92400e !important;">High Density</span></td></tr>
                <tr><td><b>HND</b></td><td>Tokyo Haneda Airport (HND)</td><td>290 Tons</td><td>320 Tons</td><td><span class="status-badge">Optimal</span></td></tr>
                <tr><td><b>DXB</b></td><td>Dubai World Central (DWC)</td><td>460 Tons</td><td>510 Tons</td><td><span class="status-badge">Smooth</span></td></tr>
            </tbody>
        </table>
        """,
        unsafe_allow_html=True,
    )

  elif module == "AWB Flight Ticket and Route Generator":
    st.subheader("Air Waybill (AWB) Cargo Ticket Generator")
    col_form, col_ticket = st.columns([1, 1.2])

    with col_form:
      st.markdown("#### Flight and Cargo Booking Details")
      origin = st.selectbox(
          "Origin Gateway",
          [
              "IST - Istanbul, Turkiye",
              "FRA - Frankfurt, Germany",
              "DXB - Dubai, UAE",
          ],
      )
      destination = st.selectbox(
          "Destination Gateway",
          [
              "JFK - New York, USA",
              "HND - Tokyo, Japan",
              "CDG - Paris, France",
              "LHR - London, UK",
          ],
      )
      cargo_type = st.selectbox(
          "Cargo Nature",
          [
              "General Freight (GEN)",
              "Perishable Goods (PER)",
              "Pharmaceuticals (PIL)",
              "High Tech Electronics",
          ],
      )
      pcs = st.number_input("Number of Pieces", min_value=1, value=5)
      weight = st.number_input("Gross Weight (kg)", min_value=1.0, value=350.0)
      st.button("Generate Cargo Ticket", type="primary")

    with col_ticket:
      awb_num = f"235-IST-{random.randint(10000000, 99999999)}"
      flt_num = f"TK-{random.randint(6500, 6599)}"
      st.markdown(
          f"""
            <div style="background: white; padding: 20px; border-radius: 12px; border: 2px dashed #cbd5e1;">
                <h3 style="color:#1e3a8a; display:flex; align-items:center; gap:8px;">
                   🎫 CARGOPULSE AIR WAYBILL
                </h3>
                <hr>
                <p style="color:#0f172a !important;"><b>AWB:</b> {awb_num} | <b>Flight:</b> {flt_num}</p>
                <p style="color:#0f172a !important;"><b>From:</b> {origin} <b>To:</b> {destination}</p>
                <p style="color:#0f172a !important;"><b>Pieces:</b> {pcs} CTN | <b>Weight:</b> {weight} KG</p>
                <img src="{IMG_TICKET}" style="width:100%; height:180px; object-fit:cover; border-radius:8px;" />
            </div>
            """,
          unsafe_allow_html=True,
      )

  elif module == "IATA Chargeable Weight Engine":
    st.subheader("IATA Chargeable Weight Engine")
    col1, col2 = st.columns(2)
    with col1:
      length = st.number_input("Length (cm)", min_value=1.0, value=120.0)
      width = st.number_input("Width (cm)", min_value=1.0, value=80.0)
      height = st.number_input("Height (cm)", min_value=1.0, value=100.0)
      gross_weight = st.number_input(
          "Gross Actual Weight (kg)", min_value=0.1, value=150.0
      )
    with col2:
      rate_per_kg = st.number_input(
          "Base Air Freight Rate ($)", min_value=0.1, value=3.80
      )
      st.image(IMG_IATA, use_container_width=True)

    volumetric_weight = (length * width * height) / 6000.0
    chargeable_weight = max(gross_weight, volumetric_weight)
    total_cost = chargeable_weight * rate_per_kg

    st.markdown("---")
    r1, r2, r3 = st.columns(3)
    with r1:
      st.metric("Volumetric Weight", f"{volumetric_weight:.2f} kg")
    with r2:
      st.metric("Chargeable Weight", f"{chargeable_weight:.2f} kg")
    with r3:
      st.metric("Total Freight Cost", f"${total_cost:,.2f}")

  elif module == "DGR and Hazmat Compliance":
    st.subheader("Dangerous Goods (DGR) Verification")
    col1, col2 = st.columns(2)
    with col1:
      un_num = st.selectbox(
          "UN Number",
          ["UN3480 (Lithium Batteries)", "UN1845 (Dry Ice)", "UN1230 (Methanol)"],
      )
      qty = st.number_input("Package Net Quantity (kg)", min_value=0.1, value=10.0)
      st.success(f"COMPLIANT: {un_num} approved for dispatch under limit.")
    with col2:
      st.image(IMG_DGR, use_container_width=True)

  elif module == "ULD and Aircraft Clearance":
    st.subheader("ULD and Aircraft Cargo Door Clearance")
    col1, col2 = st.columns(2)
    with col1:
      c_wid = st.number_input("Width (cm)", min_value=1, value=180)
      c_hgt = st.number_input("Height (cm)", min_value=1, value=150)

      MAX_DOOR_WIDTH = 372
      MAX_DOOR_HEIGHT = 305

      if c_wid <= MAX_DOOR_WIDTH and c_hgt <= MAX_DOOR_HEIGHT:
        st.success(
            f"PASSED: Item ({c_wid}x{c_hgt} cm) clears Boeing 777F door aperture"
            f" threshold ({MAX_DOOR_WIDTH}x{MAX_DOOR_HEIGHT} cm)."
        )
      else:
        st.error(
            f"FAILED: Item dimensions ({c_wid}x{c_hgt} cm) EXCEED main door"
            f" limit ({MAX_DOOR_WIDTH}x{MAX_DOOR_HEIGHT} cm)!"
        )

    with col2:
      st.image(IMG_ULD, use_container_width=True)

  elif module == "Purpose of CargoPulse":
    st.subheader("Purpose of CargoPulse")
    col1, col2 = st.columns(2)
    with col1:
      st.markdown(
          f'<img src="{IMG_PURPOSE_1}" class="purpose-img">',
          unsafe_allow_html=True,
      )
      st.markdown(
          """
          <br>
          <ul style="padding-left: 20px; margin-top: 5px;">
              <li style="font-weight: 700; color: #0f172a;">Revenue Protection</li>
              <li style="font-weight: 700; color: #0f172a; margin-top: 6px;">Safety Assurance</li>
              <li style="font-weight: 700; color: #0f172a; margin-top: 6px;">Compatibility</li>
          </ul>
          """,
          unsafe_allow_html=True,
      )
    with col2:
      st.markdown(
          f'<img src="{IMG_PURPOSE_2}" class="purpose-img">',
          unsafe_allow_html=True,
      )
      st.markdown(
          "<br>CargoPulse is a modern air cargo tracking platform designed to"
          " provide real-time shipment visibility and streamlined cargo"
          " operations. It brings flight and cargo destination data together in"
          " a clean, intuitive interface, making logistics tracking faster and"
          " more efficient.",
          unsafe_allow_html=True,
      )

  elif module == "About Developer":
    st.subheader("About Developer")
    col1, col2 = st.columns(2)
    with col1:
      st.markdown(
          """
            ### Eren Erdoğan
            * **Department:** Civil Aviation Transportation Management (İstanbul Bilgi Üniversitesi)
            * **Project:** CargoPulse Control Tower
            * **Email:** [eren.erdogan05@bilgiedu.net](mailto:eren.erdogan05@bilgiedu.net)
            """
      )
    with col2:
      st.image(IMG_DEV, use_container_width=True)

  # Live Ticker Bant (Zorunlu Saf Beyaz Yazılar)
  st.markdown(
      """
        <div class="ticker-container-fixed">
            <div class="ticker-live-badge">
                LIVE DESTINATION TELEMETRY
            </div>
            <div class="ticker-scroll-wrap">
                <div class="ticker-scroll-text">
                    <div class="ticker-item">IST -> FRA | TK6501 | B777F | CARGO: 38.4T | STATUS: IN TRANSIT</div>
                    <div class="ticker-item">DXB -> LHR | EK9204 | B777F | CARGO: 42.1T | STATUS: ON SCHEDULE</div>
                    <div class="ticker-item">HKG -> ORD | CX082 | B747-8F | CARGO: 98.5T | STATUS: CRUISING FL340</div>
                    <div class="ticker-item">IST -> JFK | TK6505 | B777F | CARGO: 45.0T | STATUS: DEPARTED</div>
                    <div class="ticker-item">FRA -> SIN | LH8402 | B777F | CARGO: 31.2T | STATUS: BOARDING</div>
                </div>
            </div>
        </div>
        """,
      unsafe_allow_html=True,
  )