temperature = 40
if temperature > 30:
    print("Temperature is "  +  str(temperature)  + " and this is high")



temperature = 60
if temperature > 30:
    print("Temepratre is high")

elif temperature < 30:        #Another condition
    print("Temperature is cold")  

else:                               #No condition above was met
    print("temperature is normal")



Name = "abe"

if len(Name) < 3:
    print("Name should be more than 3 Characters")

elif len(Name) > 15:
    print("Name should be less than 15 character")

else:
    print("Name is okay")