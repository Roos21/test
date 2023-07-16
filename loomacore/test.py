
import manager
import datetime
date = manager.DateManager()
date1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#print(date1.get_date())
old = datetime.datetime(2022,3,27,13,27,45,46000).strftime('%Y-%m-%d %H:%M:%S')
print(old)
secondes = date.date_in_annee(old)
print(secondes)