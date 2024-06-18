from time import sleep, strftime
from datetime import date,datetime,timedelta
import numpy as np
import datetime as dt
import hashlib
import os
import pickle
from dateutil.rrule import rrule, DAILY


name = input("Whats your name ? ")
calendar  ={}
exp = {}
date_parse = []
day_dict = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}

"""

"""

def welcome ():
    print("Welcome "+ name +" !")

    print ("opening your calendar ...")
    sleep(1)

    print ("Today is "+ strftime('%A %B %d, %Y'))
    print ("Current Time is "+ strftime('%H:%M:%S'))
    sleep(1)

    print("What would you like to do?")

def start_calendar():
  welcome()

  start = True

  while(start):
    user_choice = input('A to Add, U to Update,V to View, D to Delete, X to Exit, S to Schedule, C to Check Working Day or Not, E to Create Exceptions:')
    user_choice = user_choice.upper()

    if (user_choice == 'V'):

        if len(calendar.keys())>=1:
            print (calendar)

        elif (len(exp.keys()) >= 1) :
            try:
              if os.path.isfile("C:/Users/sayan/PycharmProjects/Design_Patterns_Full_Throttle/Design_Patterns/pickle")== True:
                  infile = open('picke.text', 'w')
                  newList = pickle.load(infile)
                  print  (newList)
            except IOError:
                print("File Not Found")
                print  ("Your exception container is empty.", calendar,exp)

    elif(user_choice == 'U'):
      date = input ('What date ? ')
      update = input ('Enter the update for event:')

      calendar[date] = update

    elif(user_choice == 'E'):           #please enter the date like 04/16/17
        date = input('What date ?: ')
        date_check_f = datetime.strptime(date, '%m/%d/%y')
        exception(date_check_f)


    elif(user_choice == 'A'):

      event = input ('Enter event: ')
      date = input ('Enter  date (MM/DD/YYYY): ') #please enter the date like 04/16/2017


      if (len(date) > 10 or int (date[6:]) < int(strftime("%Y"))):

        print("Incorrect date or date format. Please re-enter the date")

        try_again = input ("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()

        if(try_again == 'Y'):
          continue
        else:
          start = False
      else:
        calendar[date] = event


    elif(user_choice == 'D'):

      if(len(calendar.keys()) < 1):
        print ("nothing to delete.")
      else:

        event = input("What event?")

        for date in calendar.keys():
          if (calendar[date] == event):
            del calendar[date]
            print ("Event sucessfully deleted")
          else:
            print ("no similar events")

    elif(user_choice == 'S'):    #please enter the date like 04/16/17
        event = input ('Enter event: ')
        start_date = input ('Enter start date (MM/DD/YY): ')
        end_date = input('Enter end date (MM/DD/YY): ')
        start_date_f = datetime.strptime(start_date, '%m/%d/%y')
        date_parse.append(start_date_f)
        end_date_f = datetime.strptime(end_date, '%m/%d/%y')
        date_parse.append(end_date_f)
        if date_parse:
            print (date_parse)
        if len(exp.keys())>=1:
            date_parser(start_date_f, end_date_f)
        day_range = daterange( end_date_f, start_date_f)

    elif(user_choice == 'C'):    #please enter the date like 04/16/17
        date = input('What date ?: ')
        date_check_f = datetime.strptime(date, '%m/%d/%y')
        k1 = datetime.date(date_check_f).strftime("%Y-%m-%d")
        if hashlib.md5(k1).hexdigest() in exp.values():
            return exception(date_check_f)
        else:
            is_working(date_check_f)

    elif(user_choice == 'X'):
        start = False
    else:
      print ("Invaid command. Calendar is exiting. . .")

def daterange(start_date, end_date):
    start = datetime.date(start_date).strftime("%Y-%m-%d")
    end   = datetime.date(end_date).strftime("%Y-%m-%d")            #if len(exp.keys())>=1:
    # start = dt.date(start_date)                                        call data_parser()
    # end = dt.date(end_date)                                         call np
    days = abs(np.busday_count( (start), (end) ))
    print ("Business days :" + str(days))

def is_working(d):
    print ("Desire to check a date is Working or Non-Working ?")
    if datetime.date(d).weekday() in [0,1,2,3,4]:
        print ("Bummer it's a working day!!")
    else:
        print ("Its a Holiday, enjoy!")

def exception(d):
    if datetime.date(d).weekday() in [0,1,2,3,4]:
        print ("Its a Holiday, enjoy!, Updated")
    else:
        print ("Bummer it's a working day!!, Updated")
    if d:
        k = datetime.date(d).strftime("%Y-%m-%d")
        hash_obj = hashlib.md5(k)
        exp[k] = hash_obj.hexdigest()
        persist()
        print(exp)

def date_parser(a, b):
    try:
        if date_parse:
            a,b = date_parse[0],date_parse[1]
            for dt in rrule(DAILY, dtstart=a, until=b):
                if dt not  in date_parse:
                    date_parse.append(dt)
            for item in date_parse:
                for key in exp.keys():
                    if item.strftime('%Y/%m/%d') == key:
                        print ("Hello")
                        if exception(key) == "Bummer it's a working day!!, Updated":
                            return int(daterange(b, a)) + (1)
                        elif exception(key) == "Its a Holiday, enjoy!, Updated":
                            return int(daterange(b, a)) - (1)
    except NotImplemented:
        print ("please execute the S or schedule event first")

def persist():
    outFile = open('pickle.txt', 'w')
    pickle.dump(exp, outFile)
    outFile.close()
    sleep(1)

start_calendar()

