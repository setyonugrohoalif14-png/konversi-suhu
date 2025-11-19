import streamlit as st

st.set_page_config(page_title="Konversi Suhu", page_icon="🌡️")

st.title("🌡️ Konversi Suhu dari Celsius")
st.write("Masukkan suhu dalam °C, lalu lihat hasil konversi ke Fahrenheit, Reamur, dan Kelvin secara real-time!")

# Input suhu dengan slider biar lebih keren
celsius = st.slider(
    "Masukkan suhu dalam Celsius (°C)",
    min_value=-50.0,
    max_value=100.0,
    value=25.0,
    step=0.5,
    help="Geser untuk mengubah nilai suhu"
)

# Fungsi konversi (sama persis seperti kode kamu)
def konversi_celsius(c):
    fahrenheit = (c * 9/5) + 32
    reamur = c * 4/5
    kelvin = c + 273.15
    return fahrenheit, reamur, kelvin

F, R, K = konversi_celsius(celsius)

# Tampilan hasil yang cantik
st.divider()
st.markdown(f"### Suhu awal: **{celsius:.2f} °C**")

col1, col2 = st.columns(2)
with col1:
    st.metric("Fahrenheit", f"{F:.2f} °F", delta=f"{F-32:.1f} dari titik beku air")
    st.metric("Reamur", f"{R:.2f} °Ré", delta=None)

with col2:
    st.metric("Kelvin", f"{K:.2f} K", delta=f"{K-273.15:.1f} dari nol mutlak")
    st.info("0 K = −273.15 °C (nol mutlak)")

# Bonus fakta menarik
st.caption(f"Contoh: Air mendidih pada 100°C = {konversi_celsius(100)[0]:.1f}°F = 373.15 K")

# Efek confetti saat suhu tinggi
if celsius >= 37:
    st.success("Suhu tubuh manusia normal ≈ 37°C")
    if celsius >= 50:
        st.balloons()
