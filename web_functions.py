import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st

@st.cache_resource()
def load_data():
    df = pd.read_csv('breast-cancer.csv')

    X = df[['radius_mean','texture_mean','perimeter_mean','area_mean','smoothness_mean','compactness_mean','concavity_mean','symmetry_mean','fractal_dimension_mean']]
    y = df['diagnosis']

    return df, X, y

@st.cache_resource()
def train_model(X, y):
    model = DecisionTreeClassifier()

    model.fit(X, y)
    score = model.score(X, y)
    return model, score

def predict(X, y, features):
    model, score = train_model(X, y)
    features_df = pd.DataFrame([features], columns=X.columns)
    prediction = model.predict(features_df)
    # prediction = model.predict(np.array(features).reshape(1, -1))
    return prediction, score