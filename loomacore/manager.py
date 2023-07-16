'''
    Fichier complementaire pour personnaliser certaines options 
'''
import time
import datetime

# format de la date en anglais
def today():
    return datetime.date.today().strftime('%Y-%m-%d')

# format de la date en français
def aujoudhui():
    return datetime.date.today().strftime('%d-%m-%Y')

# Mise en pause du programme
def pause(secondes=1):
    time.sleep(secondes)
# gestionnaire de calcul des temps 
class DateManager():
    def __init__(self):
        self.date_format = '%Y-%m-%d'
        self.date_time_format = '%Y-%m-%d %H:%M:%S'
        self.date = datetime.datetime.now().strftime(self.date_format)
    
    def set_date(self, date):
        self.date = date
    
    def get_date(self):
        return self.date
    
    def set_date_format(self, format):
        self.date_format = format
        
    
    def get_date_format(self):
        return self.date_format

    def set_date_aujourdhui(self):
        self.date = aujoudhui()
    
    def set_date_today(self):
        self.date = today()
    
    def get_date_aujourdhui(self):
        return self.date
    
    def get_date_today(self):
        return self.date
    
    def get_date_et_heure(self):
        return datetime.datetime.now().strftime(self.date_time_format)
    
    def date_in_secondes(self,date):
        now = self.get_date_et_heure()
        return (datetime.datetime.strptime(now, self.date_time_format) - datetime.datetime.strptime(date, self.date_time_format)).total_seconds()
    
    def date_in_jours(self,date):
        now = self.get_date_et_heure()
        return (datetime.datetime.strptime(now, self.date_time_format) - datetime.datetime.strptime(date, self.date_time_format)).days
    
    
    def date_in_mois(self,date):
        now = self.get_date_et_heure()
        return (datetime.datetime.strptime(now, self.date_time_format) - datetime.datetime.strptime(date, self.date_time_format)).days/30
    
    def date_in_annee(self,date):
        now = self.get_date_et_heure()
        return (datetime.datetime.strptime(now, self.date_time_format) - datetime.datetime.strptime(date, self.date_time_format)).days/365
    
    def date_in_semaines(self,date):
        now = self.get_date_et_heure()
        return (datetime.datetime.strptime(now, self.date_time_format) - datetime.datetime.strptime(date, self.date_time_format)).days/7
    
    def date_in_heure(self,date):
        now = self.get_date_et_heure()
        return (datetime.datetime.strptime(now, self.date_time_format) - datetime.datetime.strptime(date, self.date_time_format)).seconds/3600
    
    def date_in_minute(self,date):
        now = self.get_date_et_heure()
        return (datetime.datetime.strptime(now, self.date_time_format) - datetime.datetime.strptime(date, self.date_time_format)).seconds/60