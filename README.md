# Wholesale Customer Data Analysis 📊

Utilize unsupervised learning techniques to construct multiple learning models using a wholesale dataset, discerning customer groupings based on expenditure across various product categories (e.g., Grocery, Milk, Detergent_Products, Fresh food, Frozen food, Deli). This aims to enhance skills in:

- Exploratory data analysis and pre-processing 🔍
- KMeans and hierarchical clustering 📈
- Principal Component Analysis (PCA) 🧬

  ![Data Analysis in Action](https://media.giphy.com/media/2ldspiMPFVdXJ34gDc/giphy.gif)


## Project Phases 🚀

1. **Exploratory Data Analysis:** Utilize Pandas and Python methods for data analysis.
2. **Data Preprocessing:** Engineer features and address missing values and outliers.
3. **Model Training:** Employ KMeans, Hierarchical Clustering, and PCA.
4. **Model Evaluation:** Compare model performance with scaled and non-scaled data.
5. **Created a Streamlit app.** 

## Project Scope 🌐

This project applies unsupervised learning to real-world wholesale data, visualizing insights derived from the analysis. Tasks include:

- **Exploratory Data Analysis:** Clean data, analyze relationships, and perform feature engineering.
- **Unsupervised Learning:** Apply k-means and hierarchical clustering, and PCA to identify patterns and group similar data points.
- **Insight Communication:** Communicate findings using visualizations and metrics for informed decision-making.

## Key Findings 🔑

- KMeans and Hierarchical Clustering revealed three distinct customer segments based on expenditure across product categories.
- PCA analysis demonstrated that 86% variance can be explained by two principal components (PC1 and PC2), and 93% with three components (PC1, PC2, PC3). Opting for two components balances variance coverage and simplifies analyses.
- Scaled data didn't provide clearer insights in clustering. Unscaled data resulted in more interpretable Elbow Plots and cleaner model outcomes.

## Reflection and Next Steps 🤔

This project highlighted areas for further exploration:

- Exploring scaling techniques to improve convergence without distorting model outcomes.
- Assessing the tradeoff between dimensionality reduction and capturing variance.
- Investigating alternative visualization methods for clustering without relying on specific code.

## Pending Questions ❓

1. Does retaining three dimensions significantly impact downstream applications compared to the gained 7% variance?
2. How can this tradeoff between dimensionality and variance retention be quantified?

## Learning Goals 🎓

Further understanding sought in exploring scaling methods, evaluating dimensionality, and discovering alternative visualization approaches for clustering.

...

## Streamlit Application for Interactive Analysis 🌐

As part of this project, I developed an interactive web application using Streamlit, enabling users to dynamically explore KMeans clustering of wholesale data. The app provides a user-friendly interface to set the number of clusters and visually analyze the resulting cluster distribution. Note: The application is currently developed but not yet deployed.

### App Features
- **Dynamic Clustering**: Users can select the number of clusters for KMeans analysis, allowing for flexible and interactive data exploration.
- **Interactive Visualization**: The app includes a scatter plot visualization for an intuitive understanding of clustering based on user-selected parameters.
- **Data Exploration**: The app facilitates an engaging way to interact with and explore the clustered data.

### Streamlit App Code Snippet

```python
import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

st.title("KMeans Clustering App")

# Adjust the file path as needed for deployment
file_path = "path_to_data/Wholesale_Data.csv"
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
```

### Some Code Snippets 📜


#### Elbow Method for Optimal Clusters

```python
# Function for plotting distortion in Elbow Rule

def plot_distortion(X, max_clusters=10):
    # Code for finding distortion values for different clusters
    # Plotting distortion against number of clusters
    plt.plot(range(1, max_clusters + 1), distortions, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Distortion')
    plt.title('Elbow Method for Optimal Clusters')
    plt.show()
```
## The Dendrogram:
![Dendrogram](image/Dendogram.png)


