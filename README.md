# Wholesale Customer Data Analysis

## Introduction

This project involves analyzing wholesale customer data using various techniques like KMeans clustering, PCA, and more. The dataset comprises customer annual spending across different product categories.

## Data Preprocessing

- **Scaling:** Considered scaling data for distance-based models.
- **Elbow Rule:** Utilized the Elbow Rule for optimal cluster selection in KMeans.
- **PCA:** Analyzed Principal Component Analysis for dimensionality reduction.

## Outlier Analysis Summary

### Findings:
- Few outliers detected in each product category, with the maximum percentage in any category around 5%.
- I'm contemplating whether or not to remove outliers because they offer valuable insights into understanding customer spending habits. 
- Outliers contain valuable information for clustering algorithms, especially for Agglomerative Clustering. 

### Impact on Analysis Methods:
- PCA requires variance representation, and outliers contribute to this variance. Hence, not removing them.
- KMeans clustering may be influenced by outliers but with a limited number, resilience to outliers is expected (not many outliers).
### Outlier Statistics:

| Category          | # Outliers | % Outliers |
|-------------------|------------|------------|
| Fresh             | 8          | 1.82       |
| Milk              | 20         | 4.55       |
| Grocery           | 12         | 2.73       |
| Frozen            | 23         | 5.23       |
| Detergents_Paper  | 22         | 5          |
| Delicassen        | 19         | 4.32       |


### Conclusion:
- Outliers are essential for PCA analysis and less impactful on Agglomerative Clustering.
- Not removing outliers, aiming for resilience in KMeans clustering due to their relatively low presence in the dataset.






## Some Code Snippets



#### Elbow Method for Optimal Clusters






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
 


