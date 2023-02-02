from oop.oop_exams.project.booths.open_booth import OpenBooth
from oop.oop_exams.project.booths.private_booth import PrivateBooth
from oop.oop_exams.project.delicacies.gingerbread import Gingerbread
from oop.oop_exams.project.delicacies.stolen import Stolen

class ChristmasPastryShopApp:
    types_of_delicacies = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
    }

    types_of_booths = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if name in [delicacy.name for delicacy in self.delicacies]:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.types_of_delicacies:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = self.types_of_delicacies[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in [booth.booth_number for booth in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.types_of_booths:
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = self.types_of_booths[type_booth](booth_number, capacity)
        self.booths.append(new_booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        else:
            raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            booth = [booth for booth in self.booths if booth.booth_number == booth_number][0]
        except IndexError:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = [delicacy for delicacy in self.delicacies if delicacy.name == delicacy_name][0]
        except IndexError:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = [booth for booth in self.booths if booth.booth_number == booth_number][0]
        bill = booth.price_for_reservation

        bill += sum(delicacy.price for delicacy in booth.delicacy_orders)
        self.income += bill

        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

