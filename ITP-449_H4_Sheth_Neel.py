# Neel Sheth
# ITP-449 Fall 2021
# H04

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Function for question 1
# params: none
# returns: nothing
# side effects: prints a question and an answer, also reads a csv file for data
def q1():
    print("What jurisdiction in the US currently has the highest number of confirmed cases?:")

    # Create the df by reading the csv
    df = pd.read_csv("10-07-2021.csv")

    # Create a variable to hold the answer, single most confirmed cases, and print answer
    answer = df.sort_values(by='Confirmed', ascending=False).head(1)
    print("\n" + answer["Province_State"][5] + " with " + str(answer["Confirmed"][5]))


# Function for question 2
# params: none
# returns: nothing
# side effects: prints a question and an answer, also reads a csv file for data
def q2():
    print("What is the difference in the testing rate between the jurisdiction that tests the most and the "
          "jurisdiction that tests the least?")

    # Create the df by reading the csv and remove the null values with .notnull()
    df = pd.read_csv("10-07-2021.csv")
    not_null = pd.notnull(df["Testing_Rate"])

    # Create two variables that hold the single most and single least value for testing rate by sorting the df by rate
    most = df[not_null].sort_values(by=["Testing_Rate"], ascending=False).head(1)
    least = df[not_null].sort_values(by=["Testing_Rate"]).head(1)

    # Create a variable that holds the difference between the rates and print answer
    diff = np.subtract(float(most["Testing_Rate"][45]), float(least["Testing_Rate"][2]))
    print("\n" + most["Province_State"][45] + " tests the most; " + least["Province_State"][2] + " tests the least.\n" +
          "The difference in testing rates is: " + str(diff))


# Function for question 3
# params: none
# returns: nothing
# side effects: reads 2 csv files and plots 2 graphs
def q3():
    # Create the confirmed cases df, set index to country, and filter to get the top 5
    df_confirmed = pd.read_csv("time_series_covid19_confirmed_global.csv")
    df_confirmed.set_index('Country/Region', inplace=True)
    top_five_confirmed = df_confirmed.sort_values(by="7/1/21", ascending=False).head(5)

    # Transpose the df to get the dates(columns) on x, use .diff to get the daily diff, and splice for correct range
    new_confirmed_df = top_five_confirmed.transpose()
    new_confirmed_df = new_confirmed_df["1/22/20":"10/7/21"].diff()
    final_confirmed = new_confirmed_df.loc["7/1/20":"7/1/21"]

    # Create the recovered cases df, set index to country, and filter to get the top 5
    df_recovered = pd.read_csv("time_series_covid19_recovered_global.csv")
    df_recovered.set_index('Country/Region', inplace=True)
    top_five_recovered = df_recovered.sort_values(by="7/1/21", ascending=False).head(5)

    # Transpose the df to get the dates(columns) on x, use .diff to get the daily diff, and splice for correct range
    new_recovered_df = top_five_recovered.transpose()
    new_recovered_df = new_recovered_df["1/22/20":"10/7/21"].diff()
    final_recovered = new_recovered_df.loc["7/1/20":"7/1/21"]

    # Create the subplots, fill the first subplot with data and style it
    fig, ax = plt.subplots(1, 2)
    ax[0].plot(final_confirmed["US"], label='US')
    ax[0].plot(final_confirmed["India"], label='India')
    ax[0].plot(final_confirmed["Brazil"], label='Brazil')
    ax[0].plot(final_confirmed["France"], label='France')
    ax[0].plot(final_confirmed["Russia"], label='Russia')
    ax[0].set_title('Confirmed cases per day')
    ax[0].set_xlabel('Date')
    ax[0].set_ylabel('Confirmed per day')
    ax[0].legend(loc='best')

    # Fill the second subplot with data, style it, and show both of the subplots
    ax[1].plot(final_recovered["India"], label='India')
    ax[1].plot(final_recovered["Brazil"], label='Brazil')
    ax[1].plot(final_recovered["Turkey"], label='Turkey')
    ax[1].plot(final_recovered["Russia"], label='Russia')
    ax[1].plot(final_recovered["Argentina"], label='Argentina')
    ax[1].legend(loc='best')
    ax[1].set_title('Recovered cases per day')
    ax[1].set_xlabel('Date')
    ax[1].set_ylabel('Recovered per day')
    ax[1].legend(loc='best')
    fig.suptitle('COVID-19 Data: Top Five Countries for Confirmed and Recovered Cases, July 2020 to July 2021')
    plt.show()


# main
def main():
    # While loop to ask for what question to answer until grader wants to quit
    valid = True
    while valid:
        number = input("Enter the number of the HW question (just the integer). Enter q to quit.\n").lower().strip()
        if number == "1":
            q1()
        elif number == "2":
            q2()
        elif number == "3":
            q3()
        elif number == "q":
            return
        else:
            print("Please input a valid correct HW question number (just the integer)")


if __name__ == '__main__':
    main()
