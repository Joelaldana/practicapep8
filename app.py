def parar():
    P=input("presione <ENTER> para continuar")

def capturar():
    try:
        T=float(input("por favor dijite la temperatura: "))
        return T
    except Exception as ex:
        print(ex)

def CelsiusFahrenheit(C):
    return (C * 9/5)+32

def CelsiusKelvin(C):
    return C + 273.15

def KelvinFahrenheit(K):
    return (K - 273.15) * 9/5 + 32

def KelvinCelsius(K):
    return K - 273.15

def FahrenheitKelvin(F):
    return (F - 32) * 5/9 + 273.15

def FahrenheitCelsius(F):
    return (F - 32) * 5/9

def main():
    try:
        continuar=True
        T=0
        while continuar==True:
            opcion=input("Seleccione una opcion:")
            print("1. Capturar Temperatura")
            print("2. Celsius a fahrenheit")
            print("3. celsius a Kelvin")
            print("4. Kelvin a fahrenheit")
            print("5. Kelvin a celsius")
            print("6. fahrenheit a Kelvin")
            print("7. fahrenheit a celsius")
            print("0. Salir")
            if opcion=='1':
                T=capturar()
            elif opcion=='2':
                print(f"{T}°C = {CelsiusFahrenheit(T)} °F")
                parar()
            elif opcion=='3':
                print(f"{T}°C = {CelsiusKelvin(T)} °K")
                parar()
            elif opcion=='4':
                print(f"{T}°K = {KelvinFahrenheit(T)} °F")
                parar()
            elif opcion=='5':
                print(f"{T}°K = {KelvinCelsius(T)} °C")
                parar()
            elif opcion=='6':
                print(f"{T}°F = {FahrenheitKelvin(T)} °K")
                parar()
            elif opcion=='7':
                print(f"{T}°F = {FahrenheitCelsius(T)} °C")
            elif opcion=='0':
                print("Bye")
                continuar=False
            else:
                print("Seleccione una opcion Valida")
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()