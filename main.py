def option_1():
    print("Du valde alternativ 1.")

def option_2():
    print("Du valde alternativ 2.")

def option_3():
    print("Du valde alternativ 3.")

def option_4():
    print("Du valde alternativ 4.")

def option_5():
    print("Du valde alternativ 5.")

def exit_menu():
    print("Avslutar programmet.")
    exit()

# Meny-funktionen
def show_menu():
    while True:
        print("\nHuvudmeny")
        print("1. Starta övervakningsläge")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Radera larm")
        print("5. Visa larm")
        print("6. Avsluta")

        choice = input("Välj ett alternativ (1-6): ")

        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            option_3()
        elif choice == "4":
            option_4()
        elif choice == "5":
            option_5()
        elif choice == "6":
            exit_menu()
        else:
            print("Ogiltigt val. Försök igen.")

# Starta menyn
show_menu()