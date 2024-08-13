import streamlit as st
import pickle
import re
from sklearn import preprocessing

st.title('url phishing System')
st.subheader("Natural Language Processing")

model1 = pickle.load(open('model1.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
model2 = pickle.load(open('model2-transform.pkl', 'rb'))

def recommend(drugname):
    recommended_drugs = model1[model1['URL'] == URL].sort_values(
        by='url', ascending=False)
    rec_url_list = recommended_url[['URL']]
    rec_url_list = rec_url_list.reset_index(drop=True)
    return rec_url_list

# Text cleaning, lowercase, removing special characters
def clean_summary(text):
    # Removing everything other than alphabets and numbers with spaces
    text = re.sub('\W+', ' ', text)
    text = text.lower()  # Converts all the text to lowercase
    return text

text_in = st.text_area('Enter protocal')
rec = [clean_summary(text_in)]

if st.button('Predict'):
    t = model2.transform(rec)
    pr = model.predict(t)
    
    # Assuming model1 is your DataFrame containing url phishing
    # Ensure model1 is defined somewhere in your code
    recommended_url = recommend(pr[0])
    
    st.write('url phishing based on the prediction are:', recommended_url)
