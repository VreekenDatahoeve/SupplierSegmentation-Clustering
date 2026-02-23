#%% md
# ## Project environment
#%%
# Importing libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Project folder directory
os.chdir("C:/GitHub/SupplierSegmentation-Clustering") # Main project folder
processed_dir = Path('data/processed') # Location processed data file
#%% md
# ## Load processed (aggregated) data
#%%
aggregated_data = "aggregated_supplier_df.parquet" # Aggregated data filename
agg_df = pd.read_parquet(processed_dir / aggregated_data) # Read Parquet file
#%% md
# ## Feature selection and scaling
#%%
# Selecting model features
features = ["total_spend_log", "total_invoices_log", "avg_invoice_amount"]
X_agg = agg_df[features].copy()

# Apply scaling to standardize feature values
scaler = StandardScaler()
agg_scaled = scaler.fit_transform(X_agg)
#%% md
# ## Model parameters
#%%
# Apply Elbow method for selecting number of clusters
inertia = []
K = range(2, 11)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=26)
    kmeans.fit(agg_scaled)
    inertia.append(kmeans.inertia_)

# Visualize Elbow output
plt.plot(K, inertia, marker='o')
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow plot (inertia)")
plt.show()
#%% md
# ## Run k-means clustering
#%%
# Run k-means with k clusters
k = 3
kmeans = KMeans(
    n_clusters=k,
    random_state=26
)
agg_df['cluster'] = kmeans.fit_predict(agg_scaled)

# Add cluster labels to the df
cluster_labels = {
    2: "Strategic suppliers",
    0: "High-value suppliers",
    1: "Tail suppliers"
}
agg_df['cluster_label'] = agg_df['cluster'].map(cluster_labels)
#%% md
# ## Validation
#%%
# Silhouette score
score = silhouette_score(agg_scaled, agg_df["cluster"])
print("Silhouette score:", round(score, 3))

# Summary table
cluster_summary = (
    agg_df
    .groupby("cluster_label")
    .agg(
        suppliers=("supplier_id", "count"),
        total_spend=("total_spend", "sum"),
        total_spend_median=("total_spend", "median"),
        total_invoices=("total_invoices", "sum")
    )
    .round(0)
    .sort_values("total_spend", ascending=False)
)
cluster_summary
#%% md
# ## Export results
#%%
# Export to CSV
output_file = "supplier_segmentation.csv"
agg_df.to_csv(processed_dir / output_file)
#%%
agg_df.info()
#%%
# Visualize supplier clusters

plt.figure(figsize=(8,6))

sns.scatterplot(
    data=agg_df,
    x="total_invoices_log",
    y="total_spend_log",
    hue="cluster_label",
    palette="Set1",
    alpha=0.7
)
plt.tight_layout()
plt.title("Supplier segmentation based on total spend and invoice frequency")
plt.show()