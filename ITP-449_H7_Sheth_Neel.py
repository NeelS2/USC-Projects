# Neel Sheth
# ITP-449 Fall 2021
# H07

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Normalizer
from sklearn.cluster import KMeans


# Function for question 1
# params: none
# returns: nothing
# side effects: reads a csv and prints a plot and a crosstab, as well as some text
def q1():
    # Data Wrangling - Import df and drop wine column, store quality separately and then drop quality
    df = pd.read_csv("wineQualityReds.csv")
    wine_df = df.drop(columns=['Wine'])
    quality = wine_df['quality']  # y (target)
    wine_df = wine_df.drop(columns=['quality'])  # X (features)

    # Normalize data
    norm = Normalizer()
    wine_norm = pd.DataFrame(norm.transform(wine_df), columns=wine_df.columns)

    # Create loop to get all the inertias for each number of ks (clusters) from 1-10
    ks = range(1, 11)
    inertias = []
    for k in ks:
        model = KMeans(n_clusters=k)
        model.fit(wine_norm)
        inertias.append(model.inertia_)

    # Create a line plot of inertia vs ks (clusters)
    plt.plot(ks, inertias, "-o")
    plt.xlabel('Number of clusters (k)')
    plt.xticks(ks)
    plt.ylabel('Inertia')
    plt.title('Inertia vs Number of Clusters')
    plt.show()

    # Print answer to question - What K (number of clusters) would you pick for KMeans?
    print("I would pick 6 clusters for the KMeans.")

    # Create the final model with the finalized number of clusters (6), and get the cluster label for each row and add
    # it to the df as another column
    final_model = KMeans(n_clusters=6, random_state=2021)
    final_model.fit(wine_norm)
    labels = final_model.predict(wine_norm)
    wine_norm['Cluster Label'] = pd.Series(labels)

    # Add quality back into the df so we can make a crosstab to compare cluster label and quality
    wine_norm['quality'] = quality

    # Print crosstab of cluster number/label and quality
    print(pd.crosstab(wine_norm['quality'], wine_norm['Cluster Label']))

    # Answer final question - Do the clusters represent the quality of wine? Why or why not.
    print("The cluster labels do not represent the quality of the wine. As we can see in the crosstab, each of the"
          "clusters has an about even distribution of the actual quality in relation \nto the other clusters (for "
          "example, each cluster has proportionally few 3, 4, and 8 quality wines, a proportionally medium amount of 7 "
          "quality wine, and a proportionally large \namount of 5 and 6 quality wine except cluster 5, which has "
          "proportionally more 5 quality wine than the other clusters. However, this is only one out of 6 clusters, "
          "and alone is not \nsufficient enough to come to the conclusion that the clusters are representative of the "
          "wine quality, as the other clusters have similar proportions regarding the distribution of \nwine quality, "
          "meaning one can not use the clusters as a grouping of quality (i.e. can't say that cluster 2 has wine that "
          "is 6 quality because other clusters have a similar \nproportion of wines that are 6 quality.")


# main
def main():
    # While loop to ask for what question to answer until grader wants to quit
    valid = True
    while valid:
        number = input("Enter the number of the HW question (just the integer). Enter q to quit.\n").lower().strip()
        if number == "1":
            q1()
        elif number == "q":
            return
        else:
            print("Please input a valid correct HW question number (just the integer)")


if __name__ == '__main__':
    main()
