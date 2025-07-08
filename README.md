# 🧠 Data Preprocessing & Instance Reduction Tools

This project consists of three Python programs for data preprocessing and instance reduction using CSV files: **NormalizeValues**, **ENN**, and **IB2**. These programs are useful in machine learning workflows, particularly for cleaning and reducing training datasets before classification.

---

## 📁 Programs Overview

### 1. 🔄 NormalizeValues

**Purpose:**  
Normalize all numeric attributes in a CSV file to the `[0, 1]` range, excluding the **class attribute** (typically the last column).

**How it works:**
- Reads a CSV file.
- Identifies numeric columns (excluding the class label).
- For each numeric column:
  \[
  \text{normalized} = \frac{\text{value} - \text{min}}{\text{max} - \text{min}}
  \]
- Keeps the class label unchanged.
- Writes the normalized data to a new file.

**Output:**  
`normalized_data.csv`

---

### 2. 🧹 ENN (Edited Nearest Neighbor)

**Purpose:**  
Apply the Edited Nearest Neighbor algorithm on a **normalized CSV file** to remove noisy or misclassified instances.

**How it works:**
- For each instance:
  - Finds its `k` nearest neighbors (typically `k=3`) using Euclidean distance.
  - If the majority of its neighbors have a different class → the instance is **removed**.
- The goal is to clean the dataset by removing inconsistencies.

**Output:**  
`edited_data.csv`

---

### 3. 📉 IB2 (Instance-Based Learning - Version 2)

**Purpose:**  
Reduce the dataset size by selecting a representative subset of instances from a **normalized CSV file**.

**How it works:**
- Start with the first instance as the initial subset.
- For each next instance:
  - Classify it using nearest neighbor from the current subset.
  - If it’s misclassified → add it to the subset.
  - If it’s correctly classified → discard it.
- This creates a smaller dataset that still represents the original data well.

**Output:**  
`reduced_data.csv`

---

## ⚙️ Technologies Used

- Python
- CSV file handling
- Euclidean distance
- Basic machine learning preprocessing
