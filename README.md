# Wholesale Customer Data Analysis

## Introduction

This project involves analyzing wholesale customer data using various techniques like KMeans clustering, PCA, and more. The dataset comprises customer annual spending across different product categories.

## Data Preprocessing

- **Scaling:** Considered scaling data for distance-based models.
- **Elbow Rule:** Utilized the Elbow Rule for optimal cluster selection in KMeans.
- **PCA:** Analyzed Principal Component Analysis for dimensionality reduction.

## Code Snippets

#### Elbow Method for Optimal Clusters




Certainly! In Markdown format for a README file on GitHub, you'd use triple backticks to create a code block with Python syntax highlighting. Here's the Python function converted into a code snippet in Markdown:

```python

Function for plotting distortion in Elbow Rule

def plot_distortion(X, max_clusters=10):
# Code for finding distortion values for different clusters
# Plotting distortion against number of clusters
plt.plot(range(1, max_clusters + 1), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.title('Elbow Method for Optimal Clusters')
plt.show()
```

## Principal Component Analysis (PCA)
```python
# Function to plot explained variance ratio for PCA
def plot_explained_variance_ratio(pca_model):
    # Code for plotting explained variance ratio
    plt.scatter(...)
    plt.show()

```


## Conclusion

Cluster Analysis: Identified 3 main customer groups using KMeans and Hierarchical clustering.
PCA Findings: PCA revealed 86% variance in just two principal components.
Scaling Observations: Non-scaled data provided clearer insights in cluster analyses.

---

## Key Insights

### Clustering Patterns:
KMeans analysis and Hierarchical Clustering both identified three distinct customer segments based on their spending across six product categories.

### Dimensionality Reduction:
PCA revealed that 86% variance was explained by PC1 and PC2, rising to 93% with PC3. Opting for two principal components balances variance coverage and simplifies analyses.

### Scaling Impact:
Scaling, although applied for model convergence, hindered interpretation of the Elbow Graph due to extremely small inertia values. Optimal clusters (n_clusters=3) were better discerned in unscaled data.

### Challenges and Considerations:
StandardScaler usage obscured insights. Exploring alternative scaling methods could maintain convergence rates while enhancing graph interpretability and overall model utility.
 


