from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "welcome to fastapi"

products = [
    Product(id=1, name="Laptop", price=999.99, description="A high-performance laptop", quantity=10),
    Product(id=2, name="Smartphone", price=499.99, description="A powerful smartphone", quantity=20),
    Product(id=3, name="Headphones", price=199.99, description="Noise-cancelling headphones", quantity=15),
    Product(id=4, name="Tablet", price=299.99, description="A portable tablet", quantity=25),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"message": "Product not found"}

@app.post("/product")
def create_product(product: Product):
    products.append(product)
    return {"message": "Product created successfully"}

@app.put("/product/{id}")
def update_product(id: int, product: Product):
    for i, p in enumerate(products):
        if p.id == id:
            products[i] = product
            return {"message": "Product updated successfully"}
    return {"message": "Product not found"}

@app.delete("/product/{id}")
def delete_product(id: int):
    for i, product in enumerate(products):
        if product.id == id:
            del products[i]
            return {"message": "Product deleted successfully"}
    return {"message": "Product not found"}