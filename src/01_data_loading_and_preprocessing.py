#%% md
# ## Project environment
#%%
# Importing libraries
import pandas as pd
from pathlib import Path

# Project root (current working) directory
project_root = Path.cwd()

# Define project directory
data_dir = project_root / "data" / "raw"
processed_dir = project_root / "data" / "processed"
#%% md
# ## Load source data
# [![Format](https://img.shields.io/badge/Format-CSV-orange)]()
# [![Type](https://img.shields.io/badge/Type-Invoice%20Data-blue)]()
# [![Source](https://img.shields.io/badge/Source-EU%20Open%20Data-lightgrey)](https://data.europa.eu/data/datasets/https-catalog-ale-se-store-1-resource-91?locale=en)
#%%
source_file = "public_spending.csv" # Source data filename
invoice_df = pd.read_csv(data_dir / source_file, sep=',') # Read CSV-file (comma separated)
#%% md
# ## Preview and explore the data
#%%
invoice_df.head() # View first records
invoice_df.info(verbose=True) # Summary information
invoice_df.columns # Column names
#%% md
# ## Rename columns
#%%
# Renaming column header names
invoice_df = invoice_df.rename(columns={
    "avtal": "contract_id",
    "belopp": "invoice_amount",
    "datum": "invoice_date",
    "fakturanummer": "invoice_number",
    "forvaltning": "department_name",
    "grund": "invoice_descr8iption",
    "kommun_id": "municipality_id",
    "konto_nr": "gl_account_number",
    "konto_text": "gl_account_description",
    "kopare": "buyer_name",
    "kopare_id": "buyer_id",
    "leverantor": "supplier_name",
    "leverantor_id": "supplier_id",
    "s_kod_nr": "category_code",
    "verifikationsnummer": "voucher_number"})
#%% md
# ## Select relevant columns
#%%
### Selecting relevant columns
invoice_df = invoice_df[[
    "invoice_amount",
    "invoice_date",
    "invoice_number",
    "department_name",
    "gl_account_number",
    "gl_account_description",
    "supplier_name",
    "supplier_id"]]
#%% md
# ## Handle missing values
#%%
# =============================================================================
# NOTE:
# Rows with missing supplier_id are removed, because supplier_id is required
# to aggregate the data on supplier-level and link invoices to a supplier.
# =============================================================================
invoice_df.isna().sum() # Check each column for missing values
invoice_df = invoice_df[invoice_df["supplier_id"].notna()] # Remove rows with missing supplier_id
#%% md
# ## Convert data types
#%%
# Clean and convert invoice_amount to float
invoice_df["invoice_amount"] = (invoice_df["invoice_amount"]
                                .astype(str) # Convert to string
                                .str.replace(" ", "",regex=False) # Remove white spaces
                                .str.replace(",", ".",regex=False) # Replace , by . character
                                .astype(float) # Convert to float
                                .round(2)) # Round to 2 decimals
# Convert invoice_date to datetime
invoice_df["invoice_date"] = pd.to_datetime(invoice_df["invoice_date"], format='%Y-%m-%d')
# Convert supplier_id to integer
invoice_df["supplier_id"] = invoice_df["supplier_id"].astype(int)
# Convert supplier_name to string
invoice_df["supplier_name"] = invoice_df["supplier_name"].astype(str).str.upper()
#%% md
# ## Save processed data
#%%
output_file = "invoice_df_processed.parquet" # Save as Parquet file
invoice_df.to_parquet(processed_dir / output_file, index=False)