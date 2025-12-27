class ComparisonAgent:
    def compare(self, product_data):
        return f"""
Comparison Summary:
- Product Name: {product_data['name']}
- Price: {product_data['price']}
- Number of Features: {len(product_data['features'])}
"""