class Informacion:
    def mi_lista(selft):
        lista_Nperros=["Copito","Akira","Peny"]
        for x in lista_Nperros:
            print(x)

    def mi_tupla(selft):
        tupla_Razas=("Pastor aleman","Gran danes","Chihuahua")
        for c in tupla_Razas:
            print(c)

    def mi_conjunto(selft):
        Conjunto_Ropa={"Vestido","Moños","Corbata"}
        for b in Conjunto_Ropa:
            print(b)
    
    def mi_diccionario(selft):
        diccionario_Colores={
            "Pastor aleman":"Cafe",
            "Gran danes":"Negro",
            "Chuhuahua":"Blanco"
        }
        for x, y in diccionario_Colores.items():
            print(x,y)

# Creando el objeto

datos=Informacion()
print("--Listado de Nombres de perros--")
datos.mi_lista()
print("--Listado de Razas de perros--")
datos.mi_tupla()
print("--Listado de Ropa de perros--")
datos.mi_conjunto()
print("--Listado de Colores de perros--")
datos.mi_diccionario()