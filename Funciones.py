
print ("Bienvenido al sistema de registro proveedores y electrodomesticos, a continuacion ingrese sus datos:")

proveedor = []
producto = []
def menu ():
    menu = True
    while menu:
        print("1. Registro de Proveedores")
    
        proveedor.append(input("Código proveedor:"))
        proveedor.append(input("Nombre:"))
        proveedor.append(input("País:"))
        proveedor.append(input("Dirección:"))
        proveedor.append(input("Telefono:"))
        proveedor.append(input("Correo electronico de contacto:"))

        print("2. Registro de producto:")

        producto.append(input("Codigo producto electronico:"))
        producto.append(input("Categoría (Computador, Cámara fotográfica o Drone):"))
        producto.append(input("Marca:"))
        producto.append(input("Modelo:"))
        producto.append(input("Continente de procedencia:"))
        producto.append(input("Costo monetario:"))
        producto.append(input("Cantidad:"))
        producto.append(input("Proveedor:"))
    menu = False
menu()


                      
    
    

