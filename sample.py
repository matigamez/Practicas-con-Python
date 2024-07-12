def imprimir_resultados():
    print('Resultados hasta ahora')  
    read_file = open("data.txt", "r")
    print(read_file.read())
    read_file.close()
    
def ingresar_comentarios():
    while True:
        print('Por favor, introduzca la evaluación entre 1 y 5')  
        point = input()
        while True:
            if point.isdecimal():
                point = int(point)
            else:
                print('Por favor, introduzca los puntos de evaluación como un número') 
            if point <= 0 or point > 5:  # Condición: menor o igual a 0 o mayor que 5
                print('Por favor, introduzca un número entre 1 y 5')  
                point = input()
            else:
                break
        
        print('Por favor, introduzca su comentario')  
        comment = input()
        post = f'Puntos: {point} Comentarios: {comment}'  
        file_pc = open("data.txt", 'a')
        file_pc.write(f'{post} \n')
        file_pc.close()
        break

def imprimir_menu():
    print('Por favor, seleccione la operación que desea realizar')  
    print('1:Introducir puntos de evaluación y comentarios')   
    print('2:Consultar los resultados hasta ahora')  
    print('3:Salir')    
    
def main():
    while True:
        imprimir_menu()
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_comentarios()             
            elif num == 2:
                imprimir_resultados()
            elif num == 3:
                print('Salir') 
                break  # Estructura para finalizar el bucle
            else:
                print('Por favor, introduzca un número entre 1 y 3')   
        else:
            print('Por favor, introduzca un número entre 1 y 3')  
main()