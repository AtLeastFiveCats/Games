import time

while True:
    newtime = input("Would you like to see 'Local' or 'UTC' time? ")
    #newtime stores user input
    if newtime.lower() == "utc":
        #If newtime equals to utc this if line will run
        print(time.strftime("The current time and date in UTC is: %c ", time.gmtime()))
        #strftime formats the struct_time from gmtime() into something more readable
        break
    elif newtime.lower() == "local":
        #If newtime equals to local this elif line will run
        print(time.strftime("The current time and date in local is: %c", time.localtime()))
        #strftime formats the struct_time from localtime() into something more readable
        break
    elif newtime.lower() != "local" or "utc":
        print("Input not recognized, please type 'Local' or 'UTC'")
        #If neither local or utc are inputed this prints
        