import random

def run():
    random_number = random.randint(1,100)
    chosen_number = int(input('Elige un número: '))
    
    while chosen_number != random_number:
        if chosen_number < random_number:
            print('Busca un número más grande.')
        else:
            print('Busca un número más pequeño.')
        chosen_number = int(input('Elige otro número: '))
    print('¡GANASTE!')        

if __name__ == "__main__":
    run()