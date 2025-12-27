class ProductPageAgent:
    def generate(self, product_data):
        return f"""
Product Name: {product_data['name']}
Price: {product_data['price']}
Features:
- {product_data['features'][0]}
- {product_data['features'][1]}
- {product_data['features'][2]}
"""