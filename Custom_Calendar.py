from time import sleep, strftime
from datetime import date,datetime
import numpy as np
import datetime as dt
import hashlib


name = raw_input("Whats your name ? ")
calendar  ={}
exp = {}
day_dict = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}



def welcome ():
  print "Welcome "+ name +" !"

  print "opening your calendar ..."
  sleep(1)

  print "Today is "+ strftime('%A %B %d, %Y')
  print "Current Time is "+ strftime('%H:%M:%S')
  sleep(1)

  print "What would you like to do?"

def start_calendar():
  welcome()

  start = True

  while(start):
    user_choice = raw_input('A to Add, U to Update,V to View, D to Delete, X to Exit, S to Schedule, C to Check Working Day or Not, E to Create Exceptions:')
    user_choice = user_choice.upper()

    if (user_choice == 'V'):
      if(len(calendar.keys()) < 1) :
        print "Your calendar is empty."
      else:
         print calendar,exp

    elif(user_choice == 'U'):
      date = raw_input ('What date ? ')
      update = raw_input ('Enter the update:')

      calendar[date] = update

    elif(user_choice == 'E'):
        date = raw_input('What date ?: ')
        date_check_f = datetime.strptime(date, '%m/%d/%y')
        exception(date_check_f)


    elif(user_choice == 'A'):

      event = raw_input ('Enter event: ')
      date = raw_input ('Enter  date (MM/DD/YYYY): ')


      if (len(date) > 10 or int (date[6:]) < int(strftime("%Y"))):

        print "Incorrect date or date format. Please re-enter the date"

        try_again = raw_input ("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()

        if(try_again == 'Y'):
          continue
        else:
          start = False
      else:
        calendar[date] = event


    elif(user_choice == 'D'):

      if(len(calendar.keys()) < 1):
        print "nothing to delete."
      else:

        event = raw_input("What event?")

        for date in calendar.keys():
          if (calendar[date] == event):
            del calendar[date]
            print "Event sucessfully deleted"
          else:
            print "no similar events"

    elif(user_choice == 'S'):
        event = raw_input ('Enter event: ')
        start_date = raw_input ('Enter start date (MM/DD/YYYY): ')
        end_date = raw_input('Enter end date (MM/DD/YYYY): ')
        # start_date, end_date = (map(int, start_date.split('/'))),(map(int, end_date.split('/')))
        start_date_f = datetime.strptime(start_date, '%m/%d/%y')
        end_date_f = datetime.strptime(end_date, '%m/%d/%y')
        day_range = daterange( end_date_f, start_date_f)
        print day_range



    elif(user_choice == 'C'):
        date = raw_input('What date ?: ')
        date_check_f = datetime.strptime(date, '%m/%d/%y')
        k1 = datetime.date(date_check_f).strftime("%Y-%m-%d")
        if hashlib.md5(k1).hexdigest() in exp.values():
            return exception(date_check_f)
        else:
            is_working(date_check_f)


    elif(user_choice == 'X'):
        start = False
    else:
      print "Invaid command. Calendar is exiting. . ."

def daterange(start_date, end_date):
    start = dt.date(start_date)
    end = dt.date(end_date)
    days = np.busday_count( start, end )


def is_working(d):
    print " Desire to check a date is Working or Non-Working ?"
    if datetime.date(d).weekday() in [0,1,2,3,4]:
        print "Bummer it's a working day!!"
    else:
        print "Its a Holiday, enjoy!"


def exception(d):
    if datetime.date(d).weekday() in [0,1,2,3,4]:
        print "Its a Holiday, enjoy!, Updated"
    else:
        print "Bummer it's a working day!!, Updated"
    if d:
        k = datetime.date(d).strftime("%Y-%m-%d")
        hash_obj = hashlib.md5(k)
        exp[k] = hash_obj.hexdigest()
        print exp


start_calendar()
