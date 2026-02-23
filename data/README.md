# Real Data, Real Insights

[![Format](https://img.shields.io/badge/Format-CSV-orange)]()
[![Type](https://img.shields.io/badge/Type-Invoice%20Data-blue)]()
[![Source](https://img.shields.io/badge/Source-EU%20Open%20Data-lightgrey)](https://data.europa.eu/data/datasets/https-catalog-ale-se-store-1-resource-91?locale=en)
[![Country](https://img.shields.io/badge/Country-Sweden-lightgrey)]()

---

## Overview

This project uses real-world accounts payable data published by a Swedish municipality via the European Open Data Portal.

Each record represents an individual supplier invoice and includes:

* Supplier identifier and name
* Invoice amount
* Invoice date
* Department / organisational unit
* General ledger account classification

The dataset provides a realistic representation of procurement spend and supplier activity.

---

## Purpose within this project

The raw invoice data is transformed into supplier-level features used for supplier segmentation and clustering.

Derived features include:

* Total spend per supplier
* Total number of invoices
* Average invoice amount
* Spend variability
* Supplier activity period
* Spend concentration patterns

These features form the basis for unsupervised machine learning (K-Means clustering).

---

## Data availability

The original dataset is **not included in this repository**.

You can download the data from:

European Open Data Portal:

https://data.europa.eu/data/datasets/https-catalog-ale-se-store-1-resource-91?locale=en

After downloading, place the file in:

```
data/raw/
```

---

## Expected file format

The notebooks expect a CSV file containing invoice-level transactions.

Example structure:

| supplier_id | invoice_amount | invoice_date | department | gl_account |
| ----------- | -------------- | ------------ | ---------- | ---------- |
| 100045      | 1250.00        | 2023-03-15   | IT         | Software   |

Column names do not need to match exactly, as long as equivalent fields are present.

---

## Using your own dataset

You can use any accounts payable dataset with similar structure.

Minimum required fields:

* supplier identifier
* invoice amount
* invoice date

Optional but recommended:

* department
* account classification

Place your file in:

```
data/raw/
```

and run the notebooks in sequence.

---

## License

Original data:

Creative Commons Attribution 4.0 (CC BY 4.0)

This repository contains no original data.

---

## Why the data is not included

The data is excluded to:

* keep the repository lightweight
* respect data governance best practices
* allow users to apply the pipeline to their own procurement data

This project is designed to work with any comparable accounts payable dataset.
