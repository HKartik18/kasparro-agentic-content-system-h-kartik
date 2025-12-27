class ComparisonAgent:
    def compare(self, product_data):
        return {
            "product": product_data["name"],
            "comparison": "This product is better than competitors in price and features."
        }