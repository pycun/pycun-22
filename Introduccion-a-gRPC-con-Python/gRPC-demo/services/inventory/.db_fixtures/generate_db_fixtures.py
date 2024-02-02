import json
import uuid
import random
import string

# region utils
def generate_random_string(length=20):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
# endregion


# region 
def generate_product(index):
    return {
        "model": "inventory.product",
        "pk": str(uuid.uuid4()),
        "fields": {
            "name": F"Product #{index}",
            "price": str(round(random.uniform(10000, 80000), 2)),
            "description": random.choice([None, generate_random_string()]),
        }
    }


def generate_inventory(index, product_pk):
    return {
        "model": "inventory.inventory",
        "pk": index,
        "fields": {
            "quantity": round(random.randint(5, 9999)) ,
            "product": product_pk,
        }
    }
# endregion



product_items = []
inventory_items = []

for i in range(1, 1000):
    product = generate_product(i)
    inventory = generate_inventory(i, product['pk'])

    product_items.append(product)
    inventory_items.append(inventory)



# write
with open('products.json', "w") as file:
    json.dump(product_items, file, indent=2)

with open('inventory.json', "w") as file:
    json.dump(inventory_items, file, indent=2)

print("Fixture files created successfully.")
