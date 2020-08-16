#write logs into a text file
import os
from datetime import date
import datetime
from os import path

#function to specify at which duration the log function were asked to write
def getDateTimeforFile():
    now = datetime.datetime.now()
    year = str('{:04d}'.format(now.year))
    month = str('{:02d}'.format(now.month))
    day = str('{:02d}'.format(now.day))
    hrs = str('{:02d}'.format(now.hour))
    minute = str('{:02d}'.format(now.minute))
    sec = str('{:02d}'.format(now.second))
    dateTime = year + "_" + month + "_" + day + " " + hrs + " h " + minute + " m " + sec + " s " + " : "
    return str(dateTime)

#Function to create a folder based on current date it had run and also append the logs when the function is called
def logfile(text):
    #To name the folder
    folder_name = str(date.today())

    #to get the current path where the directory is created
    current_path = str(os.getcwd())

    #Checking if the directory is present or not, if not present then create a directory
    if path.isdir(folder_name):
        pass
    else:
        os.mkdir(folder_name)

    #name the file
    text_file = current_path + "/" + folder_name + "/" + folder_name + ".txt"

    #file operation to append the text received
    log_file = open(text_file,"a+")
    log_file.write(getDateTimeforFile() + text + "\n")
    log_file.close()

logfile("This is a Sample Log")