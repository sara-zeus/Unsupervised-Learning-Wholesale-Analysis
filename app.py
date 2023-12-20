import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


st.title("KMeans Clustering App")


file_path = "/Users/yasara/Unsupervised-Learning-Wholesale-Analysis/Unsupervised-Learning-Wholesale-Analysis/data/Wholesale_Data.csv"  # Replace with your file path
data = pd.read_csv(file_path)

st.sidebar.header("Set Parameters")
n_clusters = st.sidebar.number_input(
    "Number of Clusters", min_value=2, max_value=10, value=3
)

kmeans = KMeans(n_clusters=n_clusters, random_state=42)
data["cluster"] = kmeans.fit_predict(
    data[["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen"]]
)


st.write("## Clustered Data")
st.write(data)


fig, ax = plt.subplots()
scatter = ax.scatter(data["Fresh"], data["Milk"], c=data["cluster"], cmap="viridis")
legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
ax.add_artist(legend1)

st.write("## Clustering Visualization")
st.pyplot(fig)
