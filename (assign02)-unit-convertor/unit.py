import streamlit as st
from PIL import Image
import base64

# Function to convert image to base64
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Encode the icon
icon_base64 = get_image_base64("unit_icon.png")

# Use the icon in Streamlit title
st.markdown(f"""
    <h1 class="stTitle">
        <img src="data:image/png;base64,{icon_base64}" /> Unit Converter
    </h1>
    <style>
        .stTitle {{
            color: white;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-top: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .stTitle img {{
            width: 40px;
            height: 40px;
            margin-right: 10px;
        }}
        .stContainer {{
            background-color: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(30px);
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.15);
            max-width: 600px;
            margin: auto;
            margin-top: 24px;
            margin-bottom: 12px;
            color: white;
        }}
        .stHeader {{
            color: navy;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 5px;
            text-transform: uppercase;
        }}
        .stSelectbox label, .stNumberInput label {{
            font-weight: bold;
            font-size: 16px;
            color: navy;
            margin-top: 3px;
            margin-bottom: 3px;
        }}
        .stButton button {{
            background: linear-gradient(135deg, #00004d 0%, #00008B 60%);
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 12px;
            width: 100%;
            transition: 0.3s;
        }}
        .stButton button:hover {{
            background-color: #e68900;
            transform: scale(1.05);
        }}
        .stSuccess {{
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #76ff03;
            margin-top: 20px;
        }}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="stContainer">', unsafe_allow_html=True)

# Define conversion factors globally
conversion_factors = {
    "Length": {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1000000,
        "Pound": 2.20462,
        "Ounce": 35.274
    },
    "Temperature": {
        "Celsius": lambda x: x,
        "Fahrenheit": lambda x: (x * 9/5) + 32,
        "Kelvin": lambda x: x + 273.15
    }
}

def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        value_in_base = conversion_factors[category][from_unit](value)
        return conversion_factors[category][to_unit](value_in_base) if callable(conversion_factors[category][to_unit]) else value_in_base
    else:
        value_in_base = value / conversion_factors[category][from_unit]
        return value_in_base * conversion_factors[category][to_unit]

st.markdown('</div>', unsafe_allow_html=True)  # Close the container

# ✅ **Added spacing below white container**
st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

# ✅ **Now adding field names after spacing**
st.markdown('<p class="stHeader">Select Category:</p>', unsafe_allow_html=True)
category = st.selectbox("", ["Length", "Weight", "Temperature"], key="category_select")

st.markdown('<p class="stHeader">From Unit:</p>', unsafe_allow_html=True)
from_unit = st.selectbox("", list(conversion_factors[category].keys()), key="from_unit_select")

st.markdown('<p class="stHeader">To Unit:</p>', unsafe_allow_html=True)
to_unit = st.selectbox("", list(conversion_factors[category].keys()), key="to_unit_select")

st.markdown('<p class="stHeader">Enter Value:</p>', unsafe_allow_html=True)

# ✅ **Check if session state exists before using it**
if "input_value" not in st.session_state:
    st.session_state["input_value"] = 0.0

value = st.number_input("", min_value=0.0, step=0.1, key="input_value")

if st.button("Convert", key="convert_button"):
    result = convert_units(value, from_unit, to_unit, category)
    st.markdown(f'<p class="stSuccess">{value} {from_unit} = {result:.4f} {to_unit}</p>', unsafe_allow_html=True)

# ✅ **Reset Function Instead of Directly Modifying Session State**
def reset_input():
    st.session_state["input_value"] = 0.0

# ✅ **Add Reset Button to Call the Function**
st.button("Reset", on_click=reset_input)

# ✅ **Add Heart Icon with "Khizra Irfan" at the Bottom in Black**
st.markdown("""
    <div style="text-align: center; margin-top: 30px; font-size: 18px; color: black; font-weight: bold;">
        ~Made with ❤️ by <span style="color: black;">Khizra Irfan~</span>
    </div>
""", unsafe_allow_html=True)

