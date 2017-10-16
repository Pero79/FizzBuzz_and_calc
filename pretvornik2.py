# -*- coding: utf-8 -*-
print ("Jaz sem program ki spreminja kilometre v milje ali obratno \n")
nov_poskus = "da"
milja = 1.609344
kilometer = 0.621371192
while nov_poskus == "da":
    sprem = raw_input("Kaj si želiš izračunati, vpiši (km / mil) \n")
    sprem = sprem.lower()
    if sprem == "km":
        vnos = int(raw_input("Prosim vnesite milje: "))
        print ("To je " + str(vnos * milja) + " kilometrov.\n")
    elif sprem == "mil":
        vnos = int(raw_input("Prosim vnesite kilometre: "))
        print ("To je " + str(vnos / milja) + " milje.\n")
    else:
        print ("Nisi izbral prave spremenljivke")

    nov_poskus = raw_input("Želite novo pretvorbo? (da / ne)\n")
    nov_poskus = nov_poskus.lower()
else:
    print ("Ugašam program")

