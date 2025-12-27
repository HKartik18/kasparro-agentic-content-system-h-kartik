class QuestionGeneratorAgent:
    def generate(self, product_data):
        return [
            f"What is the price of {product_data['name']}?",
            f"What features does {product_data['name']} offer?",
            f"Is {product_data['name']} worth buying?"
        ]