from pathlib import Path
from csv import reader

from datetime import datetime
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler
import schedule
import time

new_list = []
#my_file = Path("name.csv")
def ckeckList(lst):
  
    ele = lst[0]
    chk = True
      
    # Comparing each element with first item 
    for item in lst:
        if ele != item:
            chk = False
            break
    if (chk == True): 
        return True
    
#if my_file.is_file():

    with open('name.csv', 'r') as f:
    # pass the file object to reader() to get the reader object
        csv_reader = reader(f)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
                id = row[3]
                if str(83017015)==id:
                    name = row[1]
                    last_name = row[2]
                    age = row[0]
        print(name)
        print(age)
        print (last_name)    
        print (id)


a = 88
b = '88'
print (str(a)==b)

time_toronto = pytz.timezone('America/Toronto')
print(time_toronto)
#print(pytz.all_timezones)
sched = BlockingScheduler()
def reminder():
    'func calls "callmsg", which will send the link to a user'
    #daily basis routine func

    sched.add_job(callmsg, 'cron', day_of_week='mon-sun', hour=20, minute=14, timezone=time_toronto)

def callmsg():
    print('time to work')
#sched.start()

#schedule.every(5).seconds.do(callmsg)

#while True:
    #schedule.run_pending()
    #time.sleep(1)
c = 2
d = '?showall=&start='
a = 'https://darebee.com/programs/back-and-core.html'
b = a+d+str(c)
print (b)