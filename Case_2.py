class Vehicle:
    """Базовый класс Транспортное средство"""
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def start_engine(self):
        return "Двигатель запущен"

    def get_info(self):
        return f"Модель: {self.model}, Год выпуска: {self.year}"

class Car(Vehicle):
    """Производный класс Легковой автомобиль"""
    def __init__(self, model, year, fuel_type):
        super().__init__(model, year)
        self.fuel_type = fuel_type

    def start_engine(self):  
        return f"Двигатель автомобиля {self.model} запущен (Топливо: {self.fuel_type})"

    def open_trunk(self):  
        return "Багажник открыт"

class Truck(Vehicle):
    """Производный класс Грузовик"""
    def __init__(self, model, year, load_capacity):
        super().__init__(model, year)
        self.load_capacity = load_capacity

    def start_engine(self): 
        return f"Двигатель грузовика {self.model} запущен с ревом!"

    def load_cargo(self, weight):
        if weight <= self.load_capacity:
            return f"Груз {weight} кг загружен"
        return f"Превышена грузоподъемность! Максимум {self.load_capacity} кг"

class ElectricVehicle(Vehicle):
    """Производный класс Электромобиль"""
    def __init__(self, model, year, battery_capacity):
        super().__init__(model, year)
        self.battery_capacity = battery_capacity

    def start_engine(self):
        return f"Электромобиль {self.model} активирован (Батарея: {self.battery_capacity} kWh)"

    def charge_battery(self): 
        return "Батарея заряжается"

def demonstrate_vehicles():
    vehicle = Vehicle("Общая модель", 2025)
    car = Car("Toyota Camry", 2023, "бензин")
    truck = Truck("Volvo FH16", 2025, 20000)
    ev = ElectricVehicle("Tesla Model S", 2021, 100)

    # Работа методов
    print("=== Демонстрация работы транспортных средств ===")
    for v in [vehicle, car, truck, ev]:
        print(f"\n{v.get_info()}")
        print(v.start_engine())
        
        # Вызов уникальных методов для каждого типа
        if isinstance(v, Car):
            print(v.open_trunk())
        elif isinstance(v, Truck):
            print(v.load_cargo(15000))
        elif isinstance(v, ElectricVehicle):
            print(v.charge_battery())

    # Проверка наследования
    print("\n=== Проверка наследования ===")
    print(f"Car является Vehicle: {isinstance(car, Vehicle)}")
    print(f"Truck является Vehicle: {isinstance(truck, Vehicle)}")
    print(f"ElectricVehicle является Vehicle: {isinstance(ev, Vehicle)}")
    print(f"Vehicle является Car: {isinstance(vehicle, Car)}")

if __name__ == "__main__":
    demonstrate_vehicles()