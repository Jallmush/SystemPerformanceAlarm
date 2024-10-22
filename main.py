from monitor import MonitoringSystem
from alarm import AlarmManager

def main_menu():
    system = MonitoringSystem()
    alarm_manager = AlarmManager()

    while True:
        print("\n--- Huvudmeny ---")
        print("1. Starta övervakning")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Visa larm")
        print("5. Radera larm")
        print("6. Avsluta")

        choice = input("Välj ett alternativ: ")

        if choice == "1":
            system.start_monitoring(alarm_manager)
        elif choice == "2":
            system.list_active_monitoring()
        elif choice == "3":
            alarm_manager.create_alarm()
        elif choice == "4":
            alarm_manager.show_alarms()
        elif choice == "5":
            alarm_manager.delete_alarm()
        elif choice == "6":
            print("Avslutar programmet...")
            break
        else:
            print("Felaktigt val, försök igen.")

if __name__ == "__main__":
    main_menu()