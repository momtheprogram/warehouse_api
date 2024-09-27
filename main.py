from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session


app = FastAPI()


@app.post('/products/',)
def create_product():
    ...


@app.get('/products/',)
def read_products():
    ...


@app.get('/products/{product_id}',)
def read_product():
    ...


@app.put('/products/{product_id}',)
def update_product():
    ...


@app.delete('/products/{product_id}',)
def delete_product():
    ...


@app.post('/orders/',)
def create_order():
    ...


@app.get('/orders/',)
def read_orders():
    ...


@app.get('/orders/{order_id}',)
def read_order():
    ...


@app.patch('/orders/{order_id}/status',)
def update_order_status():
    ...
