import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('All_Diets.csv').copy()

# Clean Data
df.fillna(df.select_dtypes(include='number').mean(), inplace=True)

# Compute Metrics

# - Average Macros Per Diet
avg_macros = df.groupby('Diet_type')[['Protein(g)','Carbs(g)','Fat(g)']].mean()

# - Top 5 protein recipes per diet
top_protein = df.sort_values('Protein(g)', ascending=False).groupby('Diet_type').head(5)

# - Ratios
df['Protein_to_Carbs_ratio'] = df['Protein(g)'] / df['Carbs(g)']
df['Carbs_to_Fat_ratio'] = df['Carbs(g)'] / df['Fat(g)']

# Bar Chart
avg_macros.plot(kind='bar', figsize=(12,6))
plt.title("Average Macronutrient Content per Diet Type")
plt.ylabel("Grams")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_avg_macros.png")
plt.close()

# Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(avg_macros, annot=True, cmap="YlGnBu", fmt=".1f")
plt.title("Heatmap of Macronutrients by Diet Type")
plt.tight_layout()
plt.savefig("heatmap_macros.png")
plt.close()

# Scatter Plot
plt.figure(figsize=(12,6))
sns.scatterplot(
    data=top_protein,
    x='Cuisine_type',
    y='Protein(g)',
    hue='Diet_type'
)
plt.title("Top 5 Protein-Rich Recipes per Diet Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("scatter_top5_protein.png")
plt.close()

print('Analysis complete. All plots saved.')