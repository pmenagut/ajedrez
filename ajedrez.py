def imprimir_tablero(tablero):
    for fila in tablero:
        for casilla in fila:
            print(casilla, end='\t')
        print()

def guardar_tablero_en_archivo(nombre_archivo, tablero):
    with open(nombre_archivo, 'a') as archivo:
        for fila in tablero:
            fila_str = '\t'.join(map(str, fila))
            archivo.write(fila_str + '\n')

def main():
    nombre_archivo = input("Ingrese el nombre del archivo para guardar la partida de ajedrez: ")
    
    tablero_inicial = np.array([
        ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
        ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
        ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
    ])

    guardar_tablero_en_archivo(nombre_archivo, tablero_inicial)
    imprimir_tablero(tablero_inicial)

    turno = 1
    while True:
        mover = input("¿Quiere hacer un movimiento? (s/n): ").lower()
        if mover != 's':
            break

        print(f"Turno {turno}")
        fila_origen = int(input("Ingrese la fila de la pieza que quiere mover: "))
        col_origen = int(input("Ingrese la columna de la pieza que quiere mover: "))
        fila_destino = int(input("Ingrese la fila a la que quiere mover la pieza: "))
        col_destino = int(input("Ingrese la columna a la que quiere mover la pieza: "))

        tablero_inicial[fila_destino][col_destino] = tablero_inicial[fila_origen][col_origen]
        tablero_inicial[fila_origen][col_origen] = ' '

        guardar_tablero_en_archivo(nombre_archivo, tablero_inicial)
        imprimir_tablero(tablero_inicial)

        turno += 1

if __name__ == "__main__":
    main()
