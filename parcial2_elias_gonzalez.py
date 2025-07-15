import random 

goles_reales_a = random.randint(0,9)
goles_reales_b = random.randint(0,9)


apuesta = int(input("Bienvenido, Ingrese su apuesta: $ "))

goles_equip_a = int(input("Ingrese su predicción de la cantidad de goles que anotará el equipo A (min 0, max 9): "))

goles_equip_b = int(input("Ingrese su predicción de la cantidad de goles que anotará el equipo B (min 0, max 9): "))

predict_exacto = apuesta * 20

predict_correcta_resultado = apuesta * 10



print(f"El resultado del partido fue: EQUIPO A {goles_reales_a} - {goles_reales_b } EQUIPO B")

if goles_equip_a == goles_reales_a and goles_equip_b == goles_reales_b:
    print (f"¡Felicidades! Adivinaste el resultado exacto, sus ganacias fueron de: {predict_exacto}")
else:
    if goles_equip_a > goles_equip_b and goles_reales_a > goles_reales_b:
        print (f"Predicción correcta del resultado, sus gananacias fueron de: {predict_correcta_resultado}")
    elif goles_equip_a < goles_equip_b and goles_reales_a < goles_reales_b:
        print (f"Predicción correcta del resultado, sus gananacias fueron de: {predict_correcta_resultado}")
    elif goles_equip_a == goles_equip_b and goles_reales_a == goles_reales_b:
        print (f"Predicción correcta del resultado, sus gananacias fueron de: {predict_correcta_resultado}")
    else:
        print ("Predicción incorrecta, no ganó nada.")





