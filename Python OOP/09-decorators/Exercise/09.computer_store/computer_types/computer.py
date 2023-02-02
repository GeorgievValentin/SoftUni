class Computer:

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value == "" or value.isspace():
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value == "" or value.isspace():
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    def configure_computer(self, processor: str, ram: int):
        pass

    @staticmethod
    def ram_memory(num: int):
        available_ram = [2]
        while max(available_ram) < num:
            available_ram.append(max(available_ram) * 2)
        return available_ram

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
