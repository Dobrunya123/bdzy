from controller import Controller

def main():
    dict_table = {
        'Plant': ['plant_id', 'name', 'address'],
        'Plant_department': ['department_id', 'name', 'plant_id'],
        'Product': ['product_id', 'name', 'department_id', 'price'],
        'Order': ['order_id', 'plant_id', 'data', 'customers_id'],
        'Order_Product': ['order_id', 'product_id'],
        'Customers': ['customers_id', 'name']
    }
    dbname = 'Plant'
    user = 'postgres'
    password = '1234'
    host = 'localhost'
    port = '5432'
    control = Controller(dict_table, dbname, user, password, host, port)
    control.menu()

if __name__ == '__main__':
    main()
