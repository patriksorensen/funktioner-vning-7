
telregister = {}
for n in range(0,5):
    inp = input("Mata in namn och telefonnummer")
    parts = inp.split(' ')
    namn = parts[0]
    tel = parts[1]
    telregister[namn] = tel;

while(true):
    namn = input("Mata in namn du vill söka på")
    if namn in telregister:
        print(f"{namn} har tel {telregister[namn]}")
    else:
        print("Finns ej i registret")
