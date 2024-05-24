import streamlit as st
import pandas as pd
from firebase_init import firestore_db

# Get data from a Firestore collection
users = firestore_db.collection('user').stream()
# Convert data to a list of dictionaries
users_data = [doc.to_dict() for doc in users]
# Create DataFrame
df = pd.DataFrame(users_data)

df