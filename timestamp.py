import datetime
import time
import tkinter as tk
from PIL import ImageTk,Image




# global declaration of time variables so that all functions can access them
todaysDate = datetime.date.today()
hour = time.strftime("%I")
minute = time.strftime("%M")
second = time.strftime("%S")
AM_or_PM = time.strftime("%p")
which_day = time.strftime("%A")


# simply returns today's date and time in the form of yyyy-mm-dd-hh-mm-ss
# function is executed whenever the button is pressed using the command parameter
def returnTime():
    print(datetime.datetime.today())
    #gonna write to text file to get record of the timestamp
    with open('Manual Time Log.txt', 'a+') as logger:

        if AM_or_PM=='AM':
            logger.write(f"{todaysDate} {which_day}: started work at {hour}:{minute} AM\n")
        else:
            logger.write(f"{todaysDate} {which_day}: left work at {hour}:{minute} PM\n\n")

# this function gets the current time from the time library
# if we wanted to push a label onto the window, we would have to make a label object and give it
# parameters like text and colors. however, because we want to preiodically change our labels configuration
# after the label object has been initialized, we do it this way
# We update the time by recursively calling the function every one second

