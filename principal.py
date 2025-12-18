from negocio import (
    registrar_usuario,
    iniciar_sesion,
    obtener_users_api,
    listado_usuarios_db,
    crear_user_api,
    modificar_user_api,
    eliminar_user_api,
    obtener_data_publicaciones,
    listado_publicaciones,
)
from interfaces_usuario import menu_inicial, menu_sistema
from auxiliares.jsonplaceholder_urls import url_users, url_posts
from servicios.serper import busqueda


def menu_sistema_loop():
    while True:
        menu_sistema()
        opcion = input("Opción: ")

        if opcion == "1":
            # GET usuarios desde la API y mostrarlos desde la BD
            obtener_users_api()
            listado_usuarios_db()
        elif opcion == "2":
            # POST usuario en la API
            crear_user_api()
        elif opcion == "3":
            # PUT usuario en la API
            modificar_user_api(url_users)
        elif opcion == "4":
            # DELETE usuario en la API
            eliminar_user_api(url_users)
        elif opcion == "5":
            # GET publicaciones desde la API y mostrarlas desde la BD
            obtener_data_publicaciones(url_posts)
            listado_publicaciones()
        elif opcion == "0":
            print("Sesión cerrada.")
            break
        else:
            print("Opción no válida.")


def app():
    while True:
        menu_inicial()
        opcion_inicial = input("Opción: ")

        if opcion_inicial == "1":
            registrar_usuario()
        elif opcion_inicial == "2":
            if iniciar_sesion():
                menu_sistema_loop()
        elif opcion_inicial == "3":
            # Zona para probar cosas extra (API de búsqueda, etc.)
            busqueda()
        elif opcion_inicial == "0":
            print("Fin del programa.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    app()