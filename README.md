# scRNA-seq Analysis: Erythroblast to Megakaryocyte Reprogramming

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Scanpy](https://img.shields.io/badge/Tools-Scanpy%20%7C%20Harmonypy-green) ![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Project Overview
This project reproduces the key single-cell RNA sequencing (scRNA-seq) analysis findings from the study: **"Direct chemical reprogramming of human cord blood erythroblasts to induced megakaryocytes that produce platelets"** (Qin et al., *Cell Stem Cell*, 2022).

The study investigates the dynamic gene expression changes during the reprogramming of untreated erythroblasts (EBs) into induced megakaryocytes (iMKs) using a four-small-molecule cocktail.

### 🎯 Objectives
This analysis covers the standard scRNA-seq workflow and advanced topics:
1.  **Preprocessing & QC**: Filtering low-quality cells and normalizing gene expression.
2.  **Batch Correction**: Integrating data from different timepoints (D0, D3, D5, D7) using **Harmony**.
3.  **Clustering & Annotation**: Identifying cell types based on marker genes (e.g., *FLI1*, *MEIS1*).
4.  **GO Enrichment**: Functional enrichment analysis for cluster-specific markers.
5.  **Trajectory Inference**: Reconstructing the developmental lineage from EBs to iMKs (Advanced Topic).

## 📂 Data Availability
The raw data for this project is sourced from the GEO repository:
* **Accession**: [GSE207654](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE207654)
* **Samples**:
    * EB (Day 0)
    * iMKd3 (Day 3)
    * iMKd5 (Day 5)
    * iMKd7 (Day 7)

*> Note: Raw data files are not included in this repository due to size constraints. Please download them from the link above.*

## 🛠️ Environment & Requirements
The analysis is performed using **Python** and the **Scanpy** ecosystem. 

To reproduce the environment:
```bash
conda create -n scRNA_env python=3.11
conda activate scRNA_env
pip install -r requirements.txt
```

Key Libraries:

scanpy

harmonypy (for Batch Correction)

scrublet (for Doublet Removal)

gseapy (for GO Enrichment)

matplotlib & seaborn


## 📊 Key Results Reproduction
1. Batch Correction & Clustering
We successfully integrated datasets from four distinct timepoints. The UMAP visualization demonstrates the transition from early erythroblasts to late-stage induced megakaryocytes.

2. Marker Gene Visualization
Key transcription factors essential for MK differentiation (FLI1, MEIS1) were visualized using UMAP and Violin plots, confirming their upregulation in iMK clusters.

3. Trajectory Analysis
Using diffusion pseudotime (DPT), we inferred the developmental trajectory, revealing a continuous progression from Day 0 progenitors to Day 7 mature-like iMKs.

## 📄 Reference
Original Paper: Qin, J., Zhang, J., Jiang, J., ... & Pei, X. (2022). Direct chemical reprogramming of human cord blood erythroblasts to induced megakaryocytes that produce platelets. Cell Stem Cell, 29(8), 1229-1245. Link

Assignment: Fall 2025 - Assignment 1.

## 👤 Author
Name: [Chen Xuanzhi]

ID: [2300012257]

Contact: [2300012257@stu.pku.edu.cn]
