'''
Neel Sheth
ITP115, Summer 2020
ndsheth@usc.edu
Homework 6
'''

# Create the months dictionary
monthsDictionary = {"January":"31",
                    "February":"29",
                    "March":"31",
                    "April":"30",
                    "May":"31",
                    "June":"30",
                    "July":"31",
                    "August":"31",
                    "September":"30",
                    "October":"31",
                    "November":"30",
                    "December":"31"}
# print(monthsDictionary)

# Create an empty dictionary for the calender
calenderDictionary = {}

# Create a loop for a list of empty strings for each month
for key in monthsDictionary:
    monthsList = []
    for item in range(0, int(monthsDictionary[key])):
        monthsList.append("")
    calenderDictionary[key] = monthsList
# print(calenderDictionary)

# While loop until the user just hits enter key
while True:
    userDate = input("Enter a date for a holiday (for example \"July 1\"): ")
    if not userDate:
        break

    # Splits the input into two sections, month and day
    userDateList = userDate.split()
    # Will use this conditional for one of the error statements
    monthFound = False

    # Loop over all the months
    for key in monthsDictionary:
        if len(userDateList) != 2:         # Only goes further if there is ONLY a length of two (ideally one month and one day)
            print("I don't see good input in there. ")
            break
        if key == userDateList[0].capitalize():     # If the user input = month
            userDay = (userDateList[1])
            monthFound = True             # Update this boolean so the error later on doesn't print
            if int(monthsDictionary[key]) >= int(userDay):    # This conditional leads into the holiday input
                userDay = int(userDay)
                userHoliday = input("What happens on " + userDateList[0].capitalize() + " " + str(userDay) + "? ")
                calenderDictionary[key][userDay - 1] = userHoliday  # Userday - 1 because index starts at 0 and month starts at 1
                break
            else:     # Prints if the user inputs an invalid number that is too high
                print(userDateList[0].capitalize() + " only has " + monthsDictionary[key] + " days. ")
                break
    if monthFound == False:    # Covers for one of the errors
        print("The month " + userDateList[0].capitalize() + " doesn't exist. ")

# Loop over the dictionary to print only things that are not empty
for month in calenderDictionary:
    counter = int(0)
    for string in calenderDictionary[month]:
        counter += 1
        if string != "":
            print(month + " " + str(counter) + " : " + string)






