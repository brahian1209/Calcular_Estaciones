edad_como_cadena = input("Dime tu edad: ")
edad = int(edad_como_cadena)

# Ahora sí comparamos

if edad >= 0 and edad < 14:
    print("Niño")
elif edad >= 14 and edad <= 28:
    print("Adolescente")
elif edad >= 28 and edad <= 60:
    print("Adulto")
elif edad > 60:
    print("Adulto Mayor")
else:
    print("Edad inválida")