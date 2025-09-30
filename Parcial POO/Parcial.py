# #Autor: Joel Garcia
# # Sitema de Biblioteca

class Biblioteca():
    def __init__(self):
        '''Este init inicializa lo que seran las variables con las cuales se almacenaran los datos'''
        self.libros = {}
        self.__usuarios = {}
        self._categorias_L = ('Sci-ficcion', 'sci-ficcion','scificcion', 'sci ficcion', 'Terror', 'terror','Romance','romance', 'Novela historica', 'novela historica', 'Novela Historica', 'novela Historica')
        
    
    def añadir_L(self):
        '''Imprime por consola los datos necesarios para añadir un libro'''
        nombre_libro = input('Ingrese el nombre del libro: ' )
        ISBN = input('Ingrese el ISBN unico del libro(si no lo tiene deje en blanco): ' ) #Hasta donde recuerdo tiene letras tambien 
        categoria = input('Ingrese la categoria del libro, estan dispobibles: Sci-ficcion, Terror, Romance, Novela historica(ingrese la categoria tal cual): ' )
    
        if self._categorias_L.count(categoria) == 0:      #si encuentra la categoria devolvera un 1 sino un 0
                print('Categoria incorrecta')
                
        else:
            if ISBN == '':
                ISBN = 'Sin ISBN'    
                self.libros[nombre_libro] =  [ISBN, categoria]
                print(self.libros)
            

    def añadir_usuario(self):
        nombre = input('Ingrese su nombre: ' )
        documento = input('Ingrese su numero de identificacion: ' )
        self.__usuarios[nombre] = documento
        print(f'Nombre: {nombre} Indentificacion: {documento}')




def __main__():
    opcion = input('''
    Bienvenido al sistemas de bilbiotecas unal
       Elija que opcion desea:
        1. Registrar libros
        2. Registrar un nuevo usuario 
    ''')
    biblioteca_unal = Biblioteca()
    if opcion == '1':
        biblioteca_unal.añadir_L()
    elif opcion == '2':
        biblioteca_unal.añadir_usuario()
    else: print('Elija una opcion valida'), __main__()

if __name__ == "__main__":
    __main__()

        
        
        
