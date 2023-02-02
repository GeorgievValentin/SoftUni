from project.shopping_cart import ShoppingCart

# from oop.oop_exams.retake_exam_22_august_2022.project_test.shopping_cart import ShoppingCart

from unittest import TestCase, main


class ShoppingCartTests(TestCase):
    def setUp(self):
        self.cart = ShoppingCart("Shop", 100)
        self.cart_2 = ShoppingCart("ShopTwo", 100)

    def test_correct_initialization(self):
        self.assertEqual("Shop", self.cart.shop_name)
        self.assertEqual(100, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_initialization_incorrect_name_lower_letter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cart.shop_name = "shop"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_initialization_incorrect_name_numbers_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cart.shop_name = "Shop123"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_add_to_cart_too_expensive_product_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cart.add_to_cart("product", 101)
        self.assertEqual("Product product cost too much!", str(ex.exception))

    def test_add_to_cart_product_and_return_correctly(self):
        result = self.cart.add_to_cart("product", 50)
        self.assertEqual({"product": 50}, self.cart.products)
        self.assertEqual("product product was successfully added to the cart!", result)

    def test_remove_non_existing_product_from_cart_raises(self):
        self.cart.add_to_cart("prod", 50)
        with self.assertRaises(ValueError) as ex:
            self.cart.remove_from_cart("product")
        self.assertEqual("No product with name product in the cart!", str(ex.exception))

    def test_remove_product_from_cart_and_return_correctly(self):
        self.cart.products = {"product": 50, "product 2": 20}
        result = self.cart.remove_from_cart("product")
        self.assertEqual({"product 2": 20}, self.cart.products)
        self.assertEqual("Product product was successfully removed from the cart!", result)

    def test__add__two_shopping_carts(self):
        self.cart.add_to_cart("product 1", 50)
        self.cart_2.add_to_cart("product 2", 50)

        self.new_cart = self.cart + self.cart_2
        self.assertEqual("ShopShopTwo", self.new_cart.shop_name)
        self.assertEqual(200, self.new_cart.budget)
        self.assertEqual({"product 1": 50, "product 2": 50}, self.new_cart.products)

    def test_buy_products_without_enough_money_raises(self):
        excepted = "Not enough money to buy the products! Over budget with 20.00lv!"

        self.cart.products = {"product 1": 60, "product 2": 60}
        with self.assertRaises(ValueError) as ex:
            self.cart.buy_products()
        self.assertEqual(excepted, str(ex.exception))

    def test_buy_products_with_enough_money(self):
        expected = "Products were successfully bought! Total cost: 80.00lv."

        self.cart.add_to_cart("product 1", 40)
        self.cart.add_to_cart("product 2", 40)
        result = self.cart.buy_products()
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
