import random 


def adivinar(tries): 
    numero = random.randint(0,100) 
    print('Adivine el numero') 
    
    while tries>0: 
        print('Tiene', tries, 'intentos') 
        tries -= 1
        num_adivinado = int(input('Ingrese su numero: '))  
        
        if (num_adivinado == numero):
            print('Adivino correctamente el numero', numero) 
            break 

        if (num_adivinado > numero): 
            print('El numero es menor al ingresado') 
        else: 
            print('El numero es mayor al ingresado') 

def main(): 
    adivinar(4) 




if __name__ == '__main__': 
    main() 
