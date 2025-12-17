# Real Data, Real Insights

[![Format](https://img.shields.io/badge/Format-CSV-orange)]()
[![Type](https://img.shields.io/badge/Type-Invoice%20Data-blue)]()
[![Source](https://img.shields.io/badge/Source-EU%20Open%20Data-lightgrey)](https://data.europa.eu/data/datasets/https-catalog-ale-se-store-1-resource-91?locale=en)
[![Country](https://img.shields.io/badge/Country-Sweden-lightgrey)]()

---

## Why it matters

The objective of this project is to build a realistic and reusable analytics use case that reflects common challenges in procurement and finance data. To achieve this, I selected real public-sector invoice data instead of synthetic or sales-oriented datasets.

## What the data represents

The dataset represents accounts payable transactions published by a Swedish municipality and made available through the European Open Data Portal. The dataset includes invoice transactions over 2024.

Each record represents an individual supplier invoice and includes:
- supplier information
- invoice amounts
- invoice dates
- organisational units
- expense account classifications

## How the data is used

The invoice data is aggregated to meaningful supplier level features.
- Total spend
- Number of invoices
- Average invoice amount
- Spend variability
- Activity over time 

## Notes

- Data publised under Creative Commons Attribution 4.0 (CC BY 4.0) license
- Language: Swedish (columns translated)  
- Data: Not included; download and place in `data/raw/`


