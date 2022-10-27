# Neel Sheth
# ITP-449 Fall 2021
# H05

import pandas as pd
import matplotlib.pyplot as plt


# Function for question 1
# params: none
# returns: nothing
# side effects: reads a csv and prints a 3x2 subplot
def q1():
    # Read the csv and create the initial dataframe. Convert date to datetime. Select only needed columns. Sort by date.
    df = pd.read_csv("avocado.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df = df[['Date', 'AveragePrice', 'Total Volume']]
    df.sort_values(by=['Date'], inplace=True)

    # Create the new TotalRevenue column. Make a new df where the data is grouped by and aggregated by date.
    # Fix the AveragePrice column with division (because it was aggregated/summed it is not an average anymore).
    df['TotalRevenue'] = df['AveragePrice'] * df['Total Volume']
    df_grouped = df.groupby(['Date']).sum()
    df_grouped['AveragePrice'] = df_grouped['TotalRevenue'] / df_grouped['Total Volume']

    # Create the smoothed average price and total volume
    smooth_avg_price = df_grouped['AveragePrice'].rolling(20).mean()
    smooth_total_vol = df_grouped['Total Volume'].rolling(20).mean()

    # Create the subplots, fill the first subplot with data and style it
    fig, ax = plt.subplots(3, 2)
    ax[0, 0].scatter(df['Date'], df['AveragePrice'], s=1)
    ax[0, 0].set_ylabel('Average Price (USD)', fontsize=6, labelpad=1.5)
    ax[0, 0].set_title('Average Price of Avocados', fontsize=8, pad=3)
    ax[0, 0].tick_params('x', labelsize=5, labelrotation=23.5, pad=0.01)
    ax[0, 0].tick_params('y', labelsize=5)

    # Fill the second subplot with data and style it
    ax[0, 1].scatter(df['Date'], df['Total Volume'], s=1)
    ax[0, 1].set_ylabel('Total Volume (millions)', fontsize=6, labelpad=1.5)
    ax[0, 1].set_title('Total Volume of Avocados', fontsize=8, pad=3)
    ax[0, 1].tick_params('x', labelsize=5, labelrotation=23.5, pad=0.01)
    ax[0, 1].tick_params('y', labelsize=5)
    ax[0, 1].yaxis.offsetText.set_fontsize(5)

    # Fill the third subplot with data and style it
    ax[1, 0].plot(df_grouped['AveragePrice'], marker='.', markersize=1, linewidth=0.75)
    ax[1, 0].set_ylabel('Average Price (USD)', fontsize=6, labelpad=1.5)
    ax[1, 0].tick_params('x', labelsize=5, labelrotation=23.5, pad=0.01)
    ax[1, 0].tick_params('y', labelsize=5)

    # Fill the fourth subplot with data and style it
    ax[1, 1].plot(df_grouped['Total Volume'], marker='.', markersize=1, linewidth=0.75)
    ax[1, 1].set_ylabel('Total Volume (millions)', fontsize=6, labelpad=1.5)
    ax[1, 1].tick_params('x', labelsize=5, labelrotation=23.5, pad=0.01)
    ax[1, 1].tick_params('y', labelsize=5)
    ax[1, 1].yaxis.offsetText.set_fontsize(5)

    # Fill the fifth subplot with data and style it
    ax[2, 0].plot(smooth_avg_price, marker='.', markersize=1, linewidth=0.75)
    ax[2, 0].set_ylabel('Average Price (USD)', fontsize=6, labelpad=1.5)
    ax[2, 0].set_xlabel('Time', fontsize=7)
    ax[2, 0].tick_params('x', labelsize=5, labelrotation=23.5, pad=0.01)
    ax[2, 0].tick_params('y', labelsize=5)

    # Fill the sixth and final subplot with data and style it
    ax[2, 1].plot(smooth_total_vol, marker='.', markersize=1, linewidth=0.75)
    ax[2, 1].set_ylabel('Total Volume (millions)', fontsize=6, labelpad=1.5)
    ax[2, 1].set_xlabel('Time', fontsize=7)
    ax[2, 1].tick_params('x', labelsize=5, labelrotation=23.5, pad=0.01)
    ax[2, 1].tick_params('y', labelsize=5)
    ax[2, 1].yaxis.offsetText.set_fontsize(5)

    # Add a title to the whole figure and show the plots
    fig.suptitle('Avocado Prices and Volume Time Series', fontsize=8)
    plt.show()


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
