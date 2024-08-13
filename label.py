# streamlit_app.py
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Sample data
data = {
    'URL': ["www.marketplus.com.ar/cart/includes/local/1.php", 
            "www.qu100.com/phpmyadmin/778766777/index.html", 
            "uploads.boxify.me/83141/novo.ini", 
            "moedasgeraaaa.blogspot.com/", 
            "paypal.com.us.cgi.bin.webscr.cmd.login.member....", 
            "bit.ly/M77GIA?ferias=93840923804983", 
            "home.comcast.net/~rlewis260/ISAPIdllCustomerSu...",
            "montecitoweddings.com/wp-content//themes/Karma...", 
            "webcamopenchat.blogspot.com/", 
            "www.eov.cl/noticias/imagenes/paypal.com.au/htt..."],
    'Protocol': [0.0, 0.0, 0.0, 'NaN', 2.0, 0.0, 0.0, 1.0, 'NaN', 'NaN'],
    'Label': [1, 1, 1, 0, 1, 0, 0, 0, 0, 1]
}

df = pd.DataFrame(data)

# Preprocess data
le = LabelEncoder()
df['Label'] = le.fit_transform(df['Label'])

# Replace 'NaN' with actual NaN values
df['Protocol'] = pd.to_numeric(df['Protocol'], errors='coerce')

# Impute missing values
imputer = SimpleImputer(strategy='mean')
df['Protocol'] = imputer.fit_transform(df[['Protocol']])

# Train a simple model (Random Forest)
X = df[['Protocol']]
y = df['Label']
clf = RandomForestClassifier()
clf.fit(X, y)

# Streamlit App
st.title("URL Label Predictor")

# Input form for user to enter URL and Protocol
url_input = st.text_input("Enter URL:")
protocol_input = st.number_input("Enter Protocol:", min_value=0.0, max_value=10.0)

# Prediction button
if st.button("Predict"):
    # Make prediction
    input_data = pd.DataFrame({'Protocol': [protocol_input]})
    prediction = clf.predict(input_data)[0]

    # Display result
    st.write(f"The predicted label for URL: {url_input} with Protocol: {protocol_input} is {prediction}")
