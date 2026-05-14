from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "welcome to fastapi"

products = [
    Product(id=1, name="Laptop", price=999.99, description="A high-performance laptop", quantity=10),
    Product(id=2, name="Smartphone", price=499.99, description="A powerful smartphone", quantity=20),
    Product(id=3, name="Headphones", price=199.99, description="Noise-cancelling headphones", quantity=15)
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