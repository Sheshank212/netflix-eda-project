#importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Setup results directory
results_dir = "results"
os.makedirs(results_dir, exist_ok=True)
    
    
#Loading the dataset
df = pd.read_csv("netflix_titles.csv")

#Preliminary data inspection
print(df.shape)
print(df.columns)
df.head()

#check for missing values
print(df.isnull().sum())

# Dropping 'director' column
df.drop(columns=['director'], inplace=True)

# Dropping remaining rows with null values
df.dropna(inplace=True)


#Exploratory data analysis
#Content type(Movie vs Tv shows)
sns.countplot(x='type', data=df)
plt.title('Distribution of Content Type on Netflix')
plt.savefig('results/type_distribution.png')  
plt.show()


#Top 10 genres
df['listed_in'].value_counts().head(10).plot(kind='barh')
plt.title('Top 10 Genres')
plt.savefig('results/top_genres.png')
plt.show()

#Release year distribution
df['release_year'].value_counts().sort_index().plot(kind='line', figsize=(10,5))
plt.title('Netflix Content Added Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.savefig('results/release_trend.png')
plt.show()


#Top producting countries
df['country'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Content Producing Countries')
plt.xticks(rotation=45)
plt.savefig('results/top_countries.png')
plt.show()

