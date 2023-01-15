import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Plant(Base):
    __tablename__ = 'Plant'
    plant_id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

    def __init__(self, name, address):
        self.name = name
        self.address = address
        super(Plant, self).__init__()

class PlantDepartment(Base):
    __tablename__ = 'Plant_department'
    department_id = Column(Integer, primary_key=True)
    name = Column(String)
    plant_id = Column(Integer, ForeignKey('Plant.plant_id'))

    plant = relationship('Plant', foreign_keys=[plant_id])

    def __init__(self, name, plant_id):
        self.name = name
        self.plant_id = plant_id
        super(PlantDepartment, self).__init__()


class Product(Base):
    __tablename__ = 'Product'
    product_id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('Plant_department.department_id'))
    price = Column(Integer)

    department = relationship('PlantDepartment', foreign_keys=[department_id])

    def __init__(self, name, department_id, price):
        self.name = name
        self.department_id = department_id
        self.price = price
        super(Product, self).__init__()


class Order(Base):
    __tablename__ = 'Order'
    order_id = Column(Integer, primary_key=True)
    plant_id = Column(Integer, ForeignKey('Plant.plant_id'))
    data = Column(sqlalchemy.Time)
    customers_id = Column(Integer, ForeignKey('Customers.customers_id'))

    plant = relationship("Plant", foreign_keys=[plant_id])
    customers = relationship("Customers", foreign_keys=[customers_id])

    def __init__(self, plant_id, date, customers_id):
        self.plant_id = plant_id
        self.date = date
        self.customers_id = customers_id
        super(Order, self).__init__()


class OrderProduct(Base):
    __tablename__ = 'Order_Product'
    order_id = Column(Integer, ForeignKey('Order.order_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('Product.product_id'), primary_key=True)

    order = relationship("Order", foreign_keys=[order_id])
    product = relationship("Product", foreign_keys=[product_id])

    def __init__(self, order_id, product_id):
        self.order_id = order_id
        self.product_id = product_id
        super(OrderProduct, self).__init__()


class Customers(Base):
    __tablename__ = 'Customers'
    customers_id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
        super(Customers, self).__init__()
