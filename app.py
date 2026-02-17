import streamlit as st
import pickle

st.title("Addiction Prediction App !")

st.set_page_config(page_title="Addiction_prediction", page_icon=":iphone:", layout="wide")

st.write("Welcome to addiction prediction app!")

def load_model():
    return pickle.load(open('linear_regression_model1.pkl', 'rb'))

model = load_model()

value1 = st.number_input("Hours spend on social media")
value2 = st.selectbox("Affects performance",[0,1])
st.write("you selected : ", value2)
value3 = st.number_input("Sleep_Hours_Per_NIght")
value4 = st.selectbox("Mental_Health_Score",[0,1,2,3,4,5,6,7,8,9,10])
st.write("you selected : ", value4)
value5 = st.selectbox("Conflict_Over_Social_Media",[0,1,2,3,4,5])
st.write("you selected : ", value5)

if st.button('Predict'):
    input_data = [[value1, value2, value3, value4, value5]]
    prediction = model.predict(input_data)
    st.write(f"Addiction Score: {prediction[0][0]:.2f}")


