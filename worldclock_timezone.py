import datetime
import pytz

def start():
  atz = (pytz.all_timezones)
  timezone = input("Enter Timezone : ")
  while(True):
    for tz in pytz.all_timezones:
      if timezone.lower() == tz.lower() or timezone.upper() == tz.upper() :
        abc = pytz.timezone(timezone)
        xyz = datetime.datetime.now(abc)
        
        
        print(xyz)
        print('\033c')
       #continue
        
      #else:
       # print('enter a valid statement')

start()        
