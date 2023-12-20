# Wholesale Customer Data Analysis

## Introduction

This project involves analyzing wholesale customer data using various techniques like KMeans clustering, PCA, and more. The dataset comprises customer annual spending across different product categories.

## Data Preprocessing

- **Scaling:** Considered scaling data for distance-based models.
- **Elbow Rule:** Utilized the Elbow Rule for optimal cluster selection in KMeans.
- **PCA:** Analyzed Principal Component Analysis for dimensionality reduction.

## Code Snippets

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

## Principal Component Analysis (PCA)

# Function to plot explained variance ratio for PCA
def plot_explained_variance_ratio(pca_model):
    # Code for plotting explained variance ratio
    plt.scatter(...)
    plt.show()

---





