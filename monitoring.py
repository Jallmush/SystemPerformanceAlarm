import time
from utils import display_warning

class MonitoringSystem:
    def __init__(self):
        self.monitoring_active = False
        self.cpu_usage = 35
        self.memory_usage = 65  # In percent
        self.memory_total = 8  # GB
        self.disk_usage = 80  # In percent
        self.disk_total = 500  # GB

    def start_monitoring(self, alarm_manager):
        self.monitoring_active = True
        print("\nÖvervakning startad...")
        while self.monitoring_active:
            print("\nÖvervakning är aktiv, tryck på valfri tangent för att återgå till menyn.")
            time.sleep(5)
            # Larmhantering
            alarm_manager.check_alarms(self.cpu_usage, self.memory_usage, self.disk_usage)
            user_input = input("Tryck på valfri tangent för att avsluta övervakning: ")
            self.monitoring_active = False

    def list_active_monitoring(self):
        print("\nStatus för övervakning:")
        print(f"Övervakning: {'Aktiv' if self.monitoring_active else 'Inaktiv'}")
        print(f"CPU Användning: {self.cpu_usage}%")
        print(f"Minnesanvändning: {self.memory_usage}% ({self.memory_usage * self.memory_total / 100:.2f} GB out of {self.memory_total} GB used)")
        print(f"Diskanvändning: {self.disk_usage}% ({self.disk_usage * self.disk_total / 100:.2f} GB out of {self.disk_total} GB used)")
        input("\nTryck valfri tangent för att gå tillbaka till huvudmeny.")
