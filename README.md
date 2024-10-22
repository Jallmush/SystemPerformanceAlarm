# SystemPerformanceAlarm
Övervakningsapplikation skriven i Python. Samlar in CPU, RAM och disk info samt konfigurerar alarm.

Planering för övervakningsapplikationens uppdelning

main.py          # Hanterar huvudmenyn och programflödet.
monitor.py       # Hanterar övervakningen av CPU, minne och disk.
alarm.py         # Hanterar skapande, visning och borttagning av larm.
utils.py         # Hjälpfunktioner som inputvalidering, formatering.
logs             # Mapp för att spara loggfiler.
alarms.json      # Fil för att spara och ladda larmkonfigurationer.

extra idé: Gör en visuell bar till övervakningsläget.

