import json

class Alarm:
    def __init__(self, alarm_type, threshold): #__init__-metoden är en konstruktör som skapar ett nytt Alarm-objekt med två attribut
        self.alarm_type = alarm_type           #alarm_type (typ av larm)  
        self.threshold = threshold             #threshold (gränsvärde för när larmet ska aktiveras)

    def __str__(self):                                      #Definierar hur ett Alarm-objekt ska representeras som en sträng, 
        return f"{self.alarm_type} larm {self.threshold}%"  #Vilket gör att objekten kan skrivas ut på ett lättförståeligt sätt.

alarms = []  #Tom lista för att spara alla larm

def configure_alarm():                          #definerar funktionen för att skapa en undermeny där man konfigurerar alarm 
    while True:
        print("\nKonfigurera larm:")
        print("1. CPU användning")
        print("2. Minnesanvändning")
        print("3. Diskanvändning")
        print("0. Tillbaka till huvudmeny")

        choice = input("Välj ett alternativ: ")

        if choice == '0':
            break
        elif choice in ['1', '2', '3']:
            alarm_type = ""
            if choice == '1':
                alarm_type = "CPU"
            elif choice == '2':
                alarm_type = "Minne"
            elif choice == '3':
                alarm_type = "Disk"

            try:
                threshold = int(input("Ställ in nivå för alarm mellan 1-100: "))
                if 1 <= threshold <= 100:
                    new_alarm = Alarm(alarm_type, threshold)
                    alarms.append(new_alarm)
                    print(f"Larm för {alarm_type} användning satt till {threshold}%")
                else:
                    print("Fel: Nivån måste vara mellan 1-100.")
            except ValueError:
                print("Fel: Ange ett giltigt tal.")
        else:
            print("Ogiltigt val, försök igen.")

def list_alarms():
    if alarms:
        print("Konfigurerade larm:")
        for alarm in alarms:
            print(alarm)
    else:
        print("Inga konfigurerade larm.")

def delete_alarm():
    if not alarms:
        print("\nInga larm att radera.")
        return

    print("\nVälj ett larm att radera:")
    for i, alarm in enumerate(alarms, start=1):
        print(f"{i}. {alarm}")

    try:
        choice = int(input("Ange nummer på larm att radera: "))
        if 1 <= choice <= len(alarms):
            removed_alarm = alarms.pop(choice - 1)
            print(f"Larm {removed_alarm} har raderats.")
        else:
            print("Ogiltigt val.")
    except ValueError:
        print("Fel: Ange ett giltigt nummer.")

def save_alarms_to_file():
    with open('alarms.json', 'w') as file:
        json.dump([alarm.__dict__ for alarm in alarms], file)

def load_alarms_from_file():
    try:
        with open('alarms.json', 'r') as file:
            if file.read().strip():
                file.seek(0)
                alarm_dicts = json.load(file)
                for alarm_dict in alarm_dicts:
                    alarms.append(Alarm(alarm_dict['alarm_type'], alarm_dict['threshold']))
    except FileNotFoundError:
        print("Ingen tidigare konfiguration funnen.")