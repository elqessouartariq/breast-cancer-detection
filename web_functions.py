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
    model = DecisionTreeClassifier(
        ccp_alpha=0.0, class_weight=None, criterion='entropy',
        max_depth=4, max_features=None, max_leaf_nodes=None,
        min_impurity_decrease=0.0, min_samples_leaf=1,
        min_samples_split=2, min_weight_fraction_leaf=0.0,
        random_state=42, splitter='best'
    )

    model.fit(X, y)
    score = model.score(X, y)
    return model, score

def predict(X, y, features):
    model, score = train_model(X, y)
    features_df = pd.DataFrame([features], columns=X.columns)
    prediction = model.predict(features_df)
    # prediction = model.predict(np.array(features).reshape(1, -1))
    return prediction, score