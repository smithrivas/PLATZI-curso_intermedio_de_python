def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {'firstname': 'Brayan', 'lastname': 'Rivas'}

    # Lista de diccionarios
    super_list = [
        {'firstname': 'Brayan', 'lastname': 'Rivas'},
        {'firstname': 'Smith', 'lastname': 'Vargas'},
        {'firstname': 'Laura', 'lastname': 'Bustos'},
        {'firstname': 'Camila', 'lastname': 'Lopez'},
        {'firstname': 'Nelcy', 'lastname': 'Suarez'}
    ]

    # Diccionario de listas
    super_dict = {
        "Natural_nums": [1, 2, 3, 4, 5],
        "Integer_nums": [-1, -2, 0, 1, 2],
        "Floating_nums": [1.1, 4.5, 6.43]
    }

    # Ciclo for para recorrer el superdiccionario
    for key, value in super_dict.items():
        print(key, '-', value)
    
    # Ciclo for para recorrer la superlist
    # for i in super_list:
    #     for key, value in i.items():
    #         print(key, '-', value)
    for item in super_list:
        print(item['firstname'], item['lastname'])


if __name__ == '__main__':
    run()
