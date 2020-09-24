# Hier importeer je de os module
import os
import time

# De huidige directory opvragen en opslaan in de variabele: werkmap
werkmap = os.getcwd()

# De letters cwd staan voor: current working directory (de huidige map!)







mapnaam = ""

lengte_mapnaam = 0

while lengte_mapnaam == 0:


  mapnaam = input("Geef de map een naam: ")
  lengte_mapnaam = len(mapnaam)
  
  if lengte_mapnaam > 0:
      os.mkdir(mapnaam)
      time.sleep(1)

  else:
      print("De naam moet minimaal 1 character bevatten.")
      time.sleep(1)



print("" + mapnaam + " is de naam van uw nieuwe map.")


      
