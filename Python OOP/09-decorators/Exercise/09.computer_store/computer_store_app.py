from project_computer_store.computer_types.desktop_computer import DesktopComputer
from project_computer_store.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer == "Desktop Computer":
            computer = DesktopComputer(manufacturer, model)
        elif type_computer == "Laptop":
            computer = Laptop(manufacturer, model)
        else:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        configuration = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)

        return configuration

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.processor == wanted_processor and computer.ram >= wanted_ram:
                self.profits += client_budget - computer.price
                self.warehouse.remove(computer)

                return f"{computer} sold for {client_budget}$."

        return f"Sorry, we don't have a computer for you."


computer_store = ComputerStoreApp()
print(computer_store.build_computer("Desktop Computer", "Asus", "GS_583", "Intel Core i5-12600K", 128))
print(computer_store.sell_computer(2000, "Intel Core i5-12600K", 128))

print(computer_store.build_computer("Desktop Computer", "Asus", "GS_583", "Intel Core i5-12600K", 128))
print(computer_store.sell_computer(2000, "Intel Core i5-12600K", 128))

print(computer_store.profits)
