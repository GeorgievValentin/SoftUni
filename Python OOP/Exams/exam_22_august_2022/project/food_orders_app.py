from oop.oop_exams.retake_exam_22_august_2022.project.client import Client
from oop.oop_exams.retake_exam_22_august_2022.project.meals.meal import Meal


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def __check_is_client_registered(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return True

    def __get_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return client

    def register_client(self, client_phone_number: str):
        if self.__check_is_client_registered(client_phone_number):
            raise Exception("The client has already been registered!")
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *args: Meal):
        for meal in args:
            if meal.__class__.__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        menu_details = []
        for meal in self.menu:
            menu_details.append(meal.details())
        return "\n".join(menu_details)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **kwargs):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        if not self.__check_is_client_registered(client_phone_number):
            self.register_client(client_phone_number)

        client = self.__get_client(client_phone_number)
        meals_to_order = []
        current_bill = 0

        for wanted_meal, wanted_quantity in kwargs.items():
            for meal in self.menu:
                if wanted_meal == meal.name:
                    if wanted_quantity <= meal.quantity:
                        meals_to_order.append(meal)
                        current_bill += meal.price * wanted_quantity
                        break
                    else:
                        raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal.name}!")
            else:
                raise Exception(f"{wanted_meal} is not on the menu!")

        for wanted_meal, wanted_quantity in kwargs.items():
            client.ordered_meals[wanted_meal] = wanted_quantity
            for meal in self.menu:
                if meal.name == wanted_meal:
                    meal.quantity -= wanted_quantity

        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill

        return f"Client {client.phone_number} successfully ordered " \
               f"{', '.join(meal.name for meal in client.shopping_cart)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__get_client(client_phone_number)

        if not client.shopping_cart:
            raise Exception(f"There are no ordered meals!")

        for meal_name, quantity in client.ordered_meals.items():
            for meal in self.menu:
                if meal_name == meal.name:
                    meal.quantity += quantity

        client.ordered_meals = {}
        client.shopping_cart.clear()
        client.bill = 0

        return f"Client {client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__get_client(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill
        FoodOrdersApp.receipt_id += 1
        client.shopping_cart = []
        client.bill = 0
        client.ordered_meals = {}

        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} " \
               f"was successfully paid for {client.phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
