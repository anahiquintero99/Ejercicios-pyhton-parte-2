
def run(number):
    for i in range(2, number):
        if number % i != 0:
            print('Es primo')
            break
        else:
            print('No es primo')
            break

if __name__ == "__main__":
    print('NUMEROS PRIMOS')
    number = int(input('Ingresa número: '))
    run(number)