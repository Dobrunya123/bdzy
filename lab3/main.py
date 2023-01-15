from controller import Controller

def main():
    dict_table = {
        1 : ['plant_id', 'name', 'address'],
        2 : ['department_id', 'name', 'plant_id'],
        3 : ['product_id', 'name', 'department_id', 'price'],
        4 : ['order_id', 'plant_id', 'data', 'customers_id'],
        5 : ['order_id', 'product_id'],
        6 : ['customers_id', 'name']
    }
    dbname = 'Plant'
    user = 'postgres'
    password = '1234'
    host = 'localhost'
    port = 5432
    control = Controller(dict_table, dbname, user, password, host, port)
    control.menu()

if __name__ == '__main__':
    main()
