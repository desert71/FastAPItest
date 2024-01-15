from fastapi import FastAPI

product_app = FastAPI()

sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]

@product_app.get('/product/{product_id}')
async def get_product(product_id: int):
    for i in sample_products:
        if i["product_id"] == product_id:
            return i
    return {"message": "Такого объекта нет :("}

@product_app.get('/products/search')
async def get_spec_product(keyword:str, category:str=None, limit:int=10):
    category_list = []
    result = []
    keyword = keyword.lower()
    if category:
        category = category.lower()
        for i in sample_products:
            if i["category"].lower() == category:
                category_list.append(i)
        for i in category_list:
            if keyword in i["name"].lower():
                result.append(i)
    else:
        for i in sample_products:
            if keyword in i["name"].lower():
                result.append(i)
    if result:
        return result[:limit]
    else:
        return {"message": "Таких совпадений нет :(("}
