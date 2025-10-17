from Model.Clases import Biblioteca

def main():
    biblio = Biblioteca()

    while True:
        opcion = input("""
======== MENÚ PRINCIPAL ========
1. Gestión de biblioteca
2. Gestión de usuarios
3. Salir
Seleccione una opción: """)

        match opcion:
            case "1":
                while True:
                    opcion2 = input("""
---- MENÚ BIBLIOTECA ----
1. Registrar nuevo libro
2. Mostrar todos los libros
3. Mostrar categorías
4. Volver
Seleccione una opción: """)

                    match opcion2:
                        case "1":
                            while True:
                                nombre_libro = input('Ingrese el nombre del libro: ')
                                ISBN = input('Ingrese el ISBN (deje vacío si no tiene): ')
                                categoria = input('Ingrese la categoría (Sci-ficcion, Terror, Romance, Novela historica): ')

                                try:
                                    biblio.registro_libros(nombre_libro, ISBN, categoria)
                                    print("✅ Libro registrado correctamente.")
                                except Exception as e:
                                    print(f"❌ Error al registrar el libro: {e}")

                                again = input("¿Registrar otro libro? (s/n): ")
                                if again.lower() != "s":
                                    break

                        case "2":
                            try:
                                libros = biblio.DB.read_books()
                                print("\n=== LIBROS REGISTRADOS ===")
                                for k, v in libros.items():
                                    print(f"{k}: {v}")
                            except Exception as e:
                                print(f"❌ Error al leer libros: {e}")

                        case "3":
                            try:
                                categorias = biblio.DB.read_cat()
                                print("\n=== CATEGORÍAS DISPONIBLES ===")
                                for cat in categorias:
                                    print(f"- {cat}")
                            except Exception as e:
                                print(f"❌ Error al mostrar categorías: {e}")

                        case "4":
                            break

                        case _:
                            print("Opción inválida, intente de nuevo.")

            case "2":
                while True:
                    opcion3 = input("""
---- MENÚ USUARIOS ----
1. Registrar nuevo usuario
2. Buscar usuario
3. Actualizar usuario
4. Eliminar usuario
5. Volver
Seleccione una opción: """)

                    match opcion3:
                        case "1":
                            nombre = input("Nombre: ")
                            edad = input("Edad: ")
                            sexo = input("Sexo: ")
                            rol = input("Rol (admin, lector, etc): ")
                            contraseña = input("Contraseña: ")

                            try:
                                biblio.registro_usuario(nombre, edad, sexo, rol, contraseña)
                                print("✅ Usuario registrado correctamente.")
                            except Exception as e:
                                print(f"❌ Error al crear usuario: {e}")

                        case "2":
                            nombre = input("Nombre a buscar: ")
                            try:
                                print(biblio.DB.read_user(nombre))
                            except Exception as e:
                                print(f"❌ Error al buscar usuario: {e}")

                        case "3":
                            nombre = input("Nombre de usuario a actualizar: ")
                            key = input("Campo a modificar: ")
                            val = input("Nuevo valor: ")
                            clave = input("Clave del usuario: ")

                            try:
                                biblio.DB.update_user(nombre, key, val, clave)
                                print("✅ Usuario actualizado.")
                            except Exception as e:
                                print(f"❌ Error al actualizar: {e}")

                        case "4":
                            nombre = input("Nombre del usuario a eliminar: ")
                            clave = input("Clave: ")
                            try:
                                biblio.DB.delete_user(nombre, clave)
                                print("✅ Usuario eliminado.")
                            except Exception as e:
                                print(f"❌ Error al eliminar: {e}")

                        case "5":
                            break

                        case _:
                            print("Opción inválida, intente de nuevo.")

            case "3":
                print("👋 Saliendo del sistema...")
                break

            case _:
                print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
