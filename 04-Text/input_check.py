import re

while True:

    print("Voer je mobiele nummer in:")
    invoer = input("> ")

    patroon = '^06-?\d{8}$'

    matches = re.findall(patroon, invoer)

    
    if (len(matches) > 0):
        break

print("Bedankt nummer in juiste formaat:", matches[0])