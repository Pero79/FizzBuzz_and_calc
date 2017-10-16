# -*- coding: utf-8 -*-
print ("Dobrodošli v FizzBuzz igri")
nov_poskus = "da"
while nov_poskus == "da":
    konec = raw_input("Prosim vnesi celo število med 1 in 100: ")
    def jeCelo(x):
        if(x%1 == 0):
            return True
        else:
            return False
    if jeCelo(float(konec)):
        konec = int(konec)
        if konec >= 1 and konec <= 100:
            try:
                for num in range(1, konec+1):
                    if num % 3 == 0 and num % 5 ==0:
                        print ("FizzBuzz")
                    elif num % 3 == 0:
                        print ("Fizz")
                    elif num % 5 == 0:
                        print ("Buzz")
                    else:
                        print (num)
            except:
                print ("")
        else:
            print ("")

    else:
        print ("Nisi vnesel celega števila med 1 in 100!!! ")

    nov_poskus = raw_input("Želite novo pretvorbo? (da / ne)\n")
    nov_poskus = nov_poskus.lower()
else:
    print ("Ugašam program")
