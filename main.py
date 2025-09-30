from Controllers.biblioteca_controller import BibliotecaController

b1 = BibliotecaController()
#print(b1.create_biblioteca("Central", "123 Main St"))


for row in b1.get_all_bibliotecas():
    print(row.__dict__)

#print(b1.get_biblioteca_by_id(1).__dict__)

#print(b1.update_biblioteca(7, "Biblioteca Central", "456 Elm St"))

#b1.delete_biblioteca(7)