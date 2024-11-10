#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


# Set up seaborn for prettier plots
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


# Step 2: Load Dataset_1 and Dataset_2
dataset_1 = pd.read_excel(r"C:\Users\Deepkiran\Downloads\dataset_1.xlsx")
dataset_2 = pd.read_excel(r"C:\Users\Deepkiran\Downloads\dataset_2.xlsx")


# In[5]:


# Step 3: Inspect the data
print("Dataset_1 Info:")
dataset_1.info()
print("\nDataset_1 Preview:")
print(dataset_1.head())

print("\nDataset_2 Info:")
dataset_2.info()
print("\nDataset_2 Preview:")
print(dataset_2.head())


# In[6]:


# Step 4: Drop unnecessary columns in Dataset_2 if any (e.g., 'Unnamed: 0' if it exists)
if 'Unnamed: 0' in dataset_2.columns:
    dataset_2 = dataset_2.drop(columns=['Unnamed: 0'])


# In[7]:


# Step 5: Merge Dataset_1 and Dataset_2 on a common column ('instant' assumed here)
combined_data = pd.merge(dataset_1, dataset_2, on='instant')


# In[8]:


# Step 6: Check unique values for each column
unique_values = {col: combined_data[col].nunique() for col in combined_data.columns}
print("\nUnique Values per Column:")
print(unique_values)


# In[9]:


# Step 7: Check basic statistics for central tendency (mean, median)
central_tendency = combined_data.describe().loc[['mean', '50%']]
print("\nCentral Tendency (Mean, Median):")
print(central_tendency)


# In[10]:


# Step 8: Load Dataset_3
dataset_3 = pd.read_excel(r"C:\Users\Deepkiran\Downloads\dataset_3.xlsx")


# In[11]:


# Step 9: Inspect Dataset_3
print("\nDataset_3 Info:")
dataset_3.info()
print("\nDataset_3 Preview:")
print(dataset_3.head())


# In[12]:


# Step 10: Concatenate combined_data with Dataset_3 along rows if same structure
full_data = pd.concat([combined_data, dataset_3], ignore_index=True)


# In[13]:


# Step 11: Check for missing values and handle them
missing_values = full_data.isnull().sum()
print("\nMissing Values per Column:")
print(missing_values)


# In[16]:


# Select only numeric columns for calculating Q1, Q3, and IQR
numeric_data = full_data.select_dtypes(include=[np.number])

# Calculate the first (Q1) and third quartiles (Q3) for each numeric column
Q1 = numeric_data.quantile(0.25)
Q3 = numeric_data.quantile(0.75)
IQR = Q3 - Q1  # Interquartile Range

# Count outliers based on the IQR method
outliers = ((numeric_data < (Q1 - 1.5 * IQR)) | (numeric_data > (Q3 + 1.5 * IQR))).sum()
print("\nOutliers per Numeric Column:")
print(outliers)


# In[19]:


# Filter out the outliers from the dataset
outliers = ((numeric_data < (Q1 - 1.5 * IQR)) | (numeric_data > (Q3 + 1.5 * IQR))).sum()
print("\nOutliers per Column:")
print(outliers)


# In[21]:


# Step 13: Plotting and analyzing skewness and correlation
# Check skewness of the data
skewness = numeric_data.skew()
print("\nSkewness of Columns:")
print(skewness)


# In[23]:


# Plot correlation heatmap
plt.figure(figsize=(12,8))
sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# In[ ]:




