import psutil
import threading
import time
from alarm import alarms

monitoring_active = False

def start_monitoring():
    global monitoring_active
    monitoring_active = True
    print("\nÖvervakning startad.")

def list_active_monitoring():
    if not monitoring_active:
        print("\nIngen övervakning är aktiv.")
        
    else:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        print("\nAktiv övervakning:")
        print(f"CPU Användning: {cpu}%")
        print(f"Minnesanvändning: {memory.percent}% ({memory.used / (1024**3):.1f} GB out of {memory.total / (1024**3):.1f} GB used)")
        print(f"Diskanvändning: {disk.percent}% ({disk.used / (1024**3):.1f} GB out of {disk.total / (1024**3):.1f} GB used)")
    input("\nTryck valfri tangent för att gå tillbaka till huvudmeny")

def start_monitoring_mode():
    def monitoring_loop():
        while monitoring_active:
            cpu = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent

            print(f"\nÖvervakning är aktiv... CPU: {cpu}%, Minne: {memory}%, Disk: {disk}%")

            # Kontrollera om något larm har triggats
            for alarm in alarms:
                if alarm.alarm_type == "CPU" and cpu > alarm.threshold:
                    print(f"***VARNING, LARM AKTIVERAT, CPU ANVÄNDNING ÖVERSTIGER {alarm.threshold}%***")
                elif alarm.alarm_type == "Minne" and memory > alarm.threshold:
                    print(f"***VARNING, LARM AKTIVERAT, MINNESANVÄNDNING ÖVERSTIGER {alarm.threshold}%***")
                elif alarm.alarm_type == "Disk" and disk > alarm.threshold:
                    print(f"***VARNING, LARM AKTIVERAT, DISKANVÄNDNING ÖVERSTIGER {alarm.threshold}%***")

            time.sleep(2)

    global monitoring_active
    monitoring_active = True
    print("\nÖvervakningsläge startat. Tryck på valfri tangent för att återgå till huvudmenyn.")

    monitoring_thread = threading.Thread(target=monitoring_loop)
    monitoring_thread.daemon = True
    monitoring_thread.start()

    input()  # Vänta på att användaren trycker på en tangent
    monitoring_active = False
    print("\nÅtergår till huvudmenyn...")