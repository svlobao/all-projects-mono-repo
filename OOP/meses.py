
# Aqui tomas el input del user como en tu otro ejercicio
mes = int(input("Por favor, digite el numero del mes: \n"))


# Aqui haces el "Error handling", osea, tratar de lanzar una excepcion para caso el usuario inpute numeros diferentes. Podrias tambien poner una excepcion para caracteres especiales y alfabeticos. Seria interesante googlear para que aprendas.
if mes <= 0 or mes > 12:
    raise Exception("El numero inputado tiene que ser un entero de 1 a 12. ")


# Aqui, he creado un dicionario para que no tenga que hacer 12 IFs, como mas abajo comentado
meses_del_año = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
}

print(f"El mes elegido fue {meses_del_año[mes]}")


"""

if mes == 1:
    print("El mes elegido fue Enero")

if mes == 2:
    print("El mes elegido fue Febrero")

if mes == 3:
    print("El mes elegido fue Marzo")

if mes == 4:
    print("El mes elegido fue Abril")

if mes == 5:
    print("El mes elegido fue Mayo")

if mes == 6:
    print("El mes elegido fue Junio")

if mes == 7:
    print("El mes elegido fue Julio")

if mes == 8:
    print("El mes elegido fue Agosto")

if mes == 9:
    print("El mes elegido fue Septiembre")

if mes == 10:
    print("El mes elegido fue Octubre")

if mes == 11:
    print("El mes elegido fue Noviembre")

if mes == 12:
    print("El mes elegido fue Diciembre")


"""
