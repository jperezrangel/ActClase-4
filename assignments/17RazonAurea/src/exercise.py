import math
def main():
    #escribe tu código abajo de esta línea
    
    varphi = (1 + math.sqrt(5)) / 2
    
    numero = float(input("Número: "))
    decimales = int(input("Decimales a mostrar: "))
    
    print("Razón áurea:", round(varphi * numero, decimales))
    
    pass
    
if __name__ == '__main__':
    main()

