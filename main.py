
Main Controller for Multi-Agent Content Generation System
"""

from agents.data_parser_agent import DataParserAgent
from agents.product_page_agent import ProductPageAgent
from agents.comparison_agent import ComparisonAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.faq_agent import FAQAgent


def main():
    print("Starting Multi-Agent Content Generation System")

    data_agent = DataParserAgent()
    product_agent = ProductPageAgent()
    comparison_agent = ComparisonAgent()
    question_agent = QuestionGeneratorAgent()
    faq_agent = FAQAgent()

    product_data = data_agent.parse("sample_product_data")

    product_page = product_agent.generate(product_data)
    comparison = comparison_agent.compare(product_data)
    questions = question_agent.generate(product_data)
    faqs = faq_agent.generate(product_data)

    print("\n--- OUTPUT ---")
    print("Product Page:", product_page)
    print("Comparison:", comparison)
    print("Questions:", questions)
    print("FAQs:", faqs)


if __name__ == "__main__":
    main()