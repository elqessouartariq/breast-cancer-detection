import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
import streamlit as st


from web_functions import train_model

def app(df, X, y):
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.title("Visualise Some Demographics")

    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")

        fig = plt.figure(figsize = (8, 6))
        ax = sns.heatmap(df.iloc[:, 1:].corr(), annot = True)
        bottom, top = ax.get_ylim()
        ax.set_ylim(bottom + 0.5, top - 0.5)
        st.pyplot(fig)

    if st.checkbox("fractal dimension vs perimeter"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.scatterplot(x="fractal_dimension_mean",y="perimeter_mean",data=df)
        st.pyplot()

    if st.checkbox("concavity vs smoothness"):
        sns.color_palette("winter", as_cmap=True)
        ax=sns.scatterplot(x="concavity_mean",y="smoothness_mean",data=df)
        st.pyplot()

    if st.checkbox("Show Sample Results"):
        safe = (df['diagnosis'] == 0).sum()
        prone = (df['diagnosis'] == 1).sum()
        data = [safe,prone]
        labels = ['Safe', 'Prone']
        colors = sns.color_palette('pastel')[0:7]
        plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
        st.pyplot()


    if st.checkbox("Plot Decision Tree"):
        X_copy = X.copy()
        y_copy = y.copy()
        model, score = train_model(X_copy, y_copy)
        dot_data = tree.export_graphviz(
            decision_tree=model, out_file=None, filled=True, rounded=True,
            feature_names=X.columns, class_names=['0', '1']
        )
        st.graphviz_chart(dot_data)