class FAQAgent:
    def generate(self, product_data):
        return [
            f"What is {product_data['name']}?",
            f"How much does {product_data['name']} cost?",
            f"What are the main features of {product_data['name']}?"
        ]