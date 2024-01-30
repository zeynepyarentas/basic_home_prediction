import streamlit as st
import pickle

# ML modelini yükle
with open("basic_home_price_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)


st.title("HELLO")
st.subheader("This is basic home prediction web app")
st.markdown("---")


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


with st.form("Form"):
    area_value = st.text_input("Area")

    if is_float(area_value):
        prediction = model.predict([[float(area_value)]])
        st.success(f"Prediction: {round(prediction[0])}")
    else:
        st.error("Please enter integer number")

    submit_button = st.form_submit_button("Submit")
