import re

while True:

    print("Voer je kenteken in:")
    invoer = input("> ")

    patroon = '[A-Z]{2}-+\d{3}-+[A-Z]{3}'

    matches = re.findall(patroon, invoer)

    
    if (len(matches) > 0):
        break

print("Bedankt kenteken in juiste formaat:", matches[0])