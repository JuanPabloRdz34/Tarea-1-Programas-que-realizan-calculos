def main():
    #escribe tu código abajo de esta línea
    #5.7 mm/s (milímetros por segundo)
    minutos = float(input('Dame los minutos: '))
    s = minutos * 60 
    mm_s = s * 5.7
    cm = mm_s / 10
    print("Centímentros recorridos:",cm)


if __name__ == '__main__':
    main()
