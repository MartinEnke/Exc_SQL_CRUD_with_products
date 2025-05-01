from setup_database import session, Base, engine
from models import Products


Base.metadata.create_all(engine)


def add_product(name, price, quantity):
    new_product = Products(name=name, price=price, quantity=quantity)

    session.add(new_product)
    session.commit()
    print("New Product added")

#add_product("Iphone13", 600,5)
# add_product("Iphone14", 800,10)
# add_product("Iphone15", 1000,20)


def delete_product(id, quantity):
    delete_id = session.query(Products).filter_by(id=id).first()

    session.delete(delete_id)
    session.commit()
    print(f"Product with id {id} deleted")

#delete_product(4)

def update_product(name, price, quantity):
    product_to_update = session.query(Products).filter_by(name=name).first()

    product_to_update.price = price
    product_to_update.quantity = quantity
    session.commit()
    print(f"{name} updated")

#update_product("Iphone14", 700, 9)


def show_all_products():
    products = session.query(Products).all()

    for product in products:
        print(f"id: {product.id}, name: {product.name}, price: {product.price}, quantity: {product.quantity}")


show_all_products()