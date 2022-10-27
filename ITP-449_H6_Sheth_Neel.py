# Neel Sheth
# ITP-449 Fall 2021
# H06

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import plot_confusion_matrix


# Function for question 1
# params: none
# returns: nothing
# side effects: reads a csv and prints a 2x2 subplot and a confusion matrix
def q1():
    # Data Wrangling
    titanic_df = pd.read_csv("titanic.csv")
    # Select the columns that are important and drop nulls
    df_slimmed = titanic_df[['pclass', 'sex', 'age', 'survived']]
    df = df_slimmed.dropna()
    # df['age'] = df['age'].fillna(df['age'].mean()) if we wanted to fill with mean for age instead of drop

    # Create X (input) and y (target)
    X = df[['pclass', 'sex', 'age']]
    y = df['survived']

    # First set of 2x2 subplots - histograms of the variables we selected
    fig, ax = plt.subplots(2, 2)
    # Add data and axis titles to the first plot
    ax[0, 0].hist(df_slimmed['survived'])
    ax[0, 0].set_xlabel('Survived')
    ax[0, 0].set_ylabel('Count')

    # Add data and axis titles to the second plot
    ax[1, 0].hist(df_slimmed['sex'])
    ax[1, 0].set_xlabel('Sex')
    ax[1, 0].set_ylabel('Count')

    # Add data and axis titles to the third plot
    ax[0, 1].hist(df_slimmed['pclass'])
    ax[0, 1].set_xlabel('Pclass')
    ax[0, 1].set_ylabel('Count')

    # Add data and axis titles to the fourth plot - this one uses the df with dropped data because age was the
    # only variable that had NaN values
    ax[1, 1].hist(df['age'])
    ax[1, 1].set_xlabel('Age')
    ax[1, 1].set_ylabel('Count')

    # Add a title to the figure and show the first set of plots and show it
    fig.suptitle('Titanic Data: Histograms of Input Variables')
    plt.show()

    # Get dummy variables of the two categorical variables
    X = pd.get_dummies(X, columns=['pclass', 'sex'])

    # Split into train and test (70/30 split and random_state of 2021)
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=2021)

    # Initialize model
    model_log = LogisticRegression(max_iter=1000)

    # Fit model with training data
    model_log.fit(X_train, y_train)

    # Prediction using the x test data - didn't see if we needed to print y_pred, as the confusion matrix takes in
    # X_test and y_test to make the matrix anyways
    y_pred = model_log.predict(X_test)

    # Generate accuracy score of model, make it out of 0-100 instead of 0-1, and round to 2 decimal places
    score = round(model_log.score(X_test, y_test) * 100, 2)

    # Create second set of subplots (only 1 plot this time, a confusion matrix)
    fig, ax = plt.subplots(1, 1)
    # Make confusion matrix with the model and test data, title the figure, and show it
    plot_confusion_matrix(model_log, X_test, y_test, ax=ax)
    ax.set_title('Titanic Dataset Survivability' + '\n(Model accuracy: ' + str(score) + '%)')
    ax.set_ylabel('Actual label')
    plt.show()

    # Create a df that has the data for a hypothetical 30 year old man in 3rd class
    # and store the predicted value (survived as 0 or 1) and print it (strip the [] from the ndarray also)
    # The dataframe that goes into the model has columns: age, pclass_1, pclass_2, pclass_3, sex_female, sex_male
    # So in the df I had the age as a float and 0 or 1 (dummy variables) for sex and class (categorical variables)
    prediction_df = pd.DataFrame([[30.0, 0, 0, 1, 0, 1]])
    pred = model_log.predict(prediction_df)
    print('Prediction for a 30-year-old male passenger in 3rd class: ' + str(pred).lstrip('[').rstrip(']'))

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
