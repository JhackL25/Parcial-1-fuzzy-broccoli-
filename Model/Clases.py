# #Autor: Joel Garcia
# # Sitema de Biblioteca
from Database import FB as DB
               
class Libro:   
    def __init__(self):
        '''Este init inicializa lo que seran las variables con las cuales se almacenaran los datos'''
        self.DB = DB
        self.libros = self.DB.read_books()
        self._categorias_L = self.DB.read_cat()
    
    def añadir_Libro(self, nombre_libro, ISBN, categoria):
  
        if self._categorias_L.count(categoria) != 0:      #si encuentra la categoria devolvera un 1 sino un 0
            if ISBN == '':
                ISBN = 'Sin ISBN'    
                self.DB.create_book(nombre_libro, ISBN, categoria)
                print('si sirvo')
            else:      
                self.DB.create_book(nombre_libro, ISBN, categoria)
                print('si sirvo')                
        else:
             raise ('Categoria incorrecta')  
    
    def ver_libro(self, nombre):
         print(self.DB.read_book(nombre))
             
            
class Usuario:
    def __init__(self):
        self.DB = DB
    
    def crear_user(self,nombre, edad, sexo, rol, contraseña):
        try:
            self.DB.create_user(nombre, edad, sexo, rol, contraseña)
        except Exception as e:
             print('Error al crear usuario')

    def buscar_user(self, nombre):
        try:
            self.DB.read_user(nombre)
        except Exception as e:
             print('Error al buscar el user')

    def actualizar_user(self, nombre, key, val, clave):
         self.DB.update_user(nombre, key, val, clave)

    def borrar_user(self, nombre, clave):
         self.DB.delete_user(nombre,clave)

class Biblioteca:
     
    def __init__(self):
          self.Libro = Libro()
          self.Usuario = Usuario()
          self.DB = DB
    
    def registro_libros(self, nombre_libro, ISBN, categoria):
         self.Libro.añadir_Libro(nombre_libro, ISBN, categoria)
    
    def registro_usuario(self,nombre, edad, sexo, rol, contraseña):
         self.DB.create_user(nombre, edad, sexo, rol, contraseña)
    
    def rostrar_libros(self):
         return self.DB.read_books
    
    def mostrar_categorias(self):
         return self.DB.read_cat
     
       
    




# def __main__():
#     opcion = input('''
#     Bienvenido al sistemas de bilbiotecas unal
#        Elija que opcion desea:
#         1. Registrar libros
#         2. Registrar un nuevo usuario 
#     ''')
#     biblioteca_unal = Biblioteca()
#     if opcion == '1':
#         biblioteca_unal.añadir_L()
#     elif opcion == '2':
#         biblioteca_unal.añadir_usuario()
#     else: print('Elija una opcion valida'), __main__()

# if __name__ == "__main__":
#     __main__()

        
        
        
