from oop.oop_exams.retake_exam_22_august_2022.project import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for prod in self.products:
            if product_name == prod.name:
                return prod

    def remove(self, product_name: str):
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        return "\n".join([f"{product.name}: {product.quantity}" for product in self.products])
