from project_computer_store.computer_types.computer import Computer


class Laptop(Computer):
    AVAILABLE_PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200
    }

    MAX_RAM = 64

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):

        if processor not in Laptop.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if ram not in self.ram_memory(Laptop.MAX_RAM):
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price += (self.ram_memory(Laptop.MAX_RAM).index(self.ram) + 1) * 100
        self.price += Laptop.AVAILABLE_PROCESSORS[self.processor]

        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."
