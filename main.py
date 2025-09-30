from Controllers.biblioteca_controller import BibliotecaController
from Controllers.seccion_controller import SeccionController

from prettytable import PrettyTable
table = PrettyTable()

b1 = BibliotecaController()
#print(b1.create_biblioteca("Central", "123 Main St"))


#for row in b1.get_all_bibliotecas():
#    print(row.__dict__)

#print(b1.get_biblioteca_by_id(1).__dict__)

#print(b1.update_biblioteca(7, "Biblioteca Central", "456 Elm St"))

#b1.delete_biblioteca(7)

s1 = SeccionController()

#for row in s1.get_all_secciones():
#    print(row.__dict__)


table.field_names = ["Nombre Seccion", "Piso"]

for row in s1.get_secciones_by_biblioteca(1):
    table.add_row([row['nombre_seccion'], row['piso']])    
    table.title = f"Secciones de la Biblioteca {row['nombre_biblioteca']}"



print(table)