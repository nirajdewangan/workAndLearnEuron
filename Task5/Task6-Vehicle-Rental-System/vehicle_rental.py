"""A mini vehicle rental application using Python inheritance."""


class Vehicle:
    """Represent a general vehicle available for rent."""

    def __init__(self, vehicle_number, brand, model, rental_price_per_day):
        if rental_price_per_day <= 0:
            raise ValueError("Rental price per day must be greater than zero.")

        self.vehicle_number = vehicle_number
        self.brand = brand
        self.model = model
        self.rental_price_per_day = float(rental_price_per_day)

    def display_details(self):
        """Display the common details of a vehicle."""
        print(f"Vehicle Number : {self.vehicle_number}")
        print(f"Brand          : {self.brand}")
        print(f"Model          : {self.model}")
        print(f"Rent Per Day   : Rs. {self.rental_price_per_day:.2f}")

    def calculate_rent(self, days):
        """Calculate and return rent for a valid number of days."""
        if not self.is_valid_rental_duration(days):
            raise ValueError("Rental duration must be a positive integer.")

        return self.rental_price_per_day * days

    @staticmethod
    def is_valid_rental_duration(days):
        """Return True when rental days is a positive integer."""
        return isinstance(days, int) and not isinstance(days, bool) and days > 0


class Car(Vehicle):
    """Represent a rental car with a seat count."""

    def __init__(
        self,
        vehicle_number,
        brand,
        model,
        rental_price_per_day,
        number_of_seats,
    ):
        super().__init__(vehicle_number, brand, model, rental_price_per_day)

        if number_of_seats <= 0:
            raise ValueError("Number of seats must be greater than zero.")

        self.number_of_seats = number_of_seats

    def display_details(self):
        """Display inherited details and the number of seats."""
        super().display_details()
        print(f"Number of Seats: {self.number_of_seats}")


class Bike(Vehicle):
    """Represent a rental bike with an engine capacity."""

    def __init__(
        self,
        vehicle_number,
        brand,
        model,
        rental_price_per_day,
        engine_capacity,
    ):
        super().__init__(vehicle_number, brand, model, rental_price_per_day)

        if engine_capacity <= 0:
            raise ValueError("Engine capacity must be greater than zero.")

        self.engine_capacity = engine_capacity

    def display_details(self):
        """Display inherited details and the engine capacity."""
        super().display_details()
        print(f"Engine Capacity: {self.engine_capacity} cc")


def main():
    """Create two cars and two bikes and demonstrate rental calculation."""
    car1 = Car("KA01AB1234", "Hyundai", "Creta", 2500, 5)
    car2 = Car("KA02CD5678", "Maruti Suzuki", "Ertiga", 3000, 7)

    bike1 = Bike("KA03EF9012", "Royal Enfield", "Classic 350", 1200, 349)
    bike2 = Bike("KA04GH3456", "Yamaha", "R15", 900, 155)

    rentals = [
        (car1, 3),
        (car2, 5),
        (bike1, 2),
        (bike2, 7),
    ]

    print("VEHICLE RENTAL SYSTEM")
    print(f"Total vehicles available: {len(rentals)}")

    for vehicle, days in rentals:
        print(f"\n--- {vehicle.__class__.__name__} Details ---")
        vehicle.display_details()
        total_rent = vehicle.calculate_rent(days)
        print(f"Rental Duration: {days} days")
        print(f"Total Rent     : Rs. {total_rent:.2f}")

    print("\n--- Rental Duration Validation ---")
    print(f"Is 5 days valid? {Vehicle.is_valid_rental_duration(5)}")
    print(f"Is 0 days valid? {Vehicle.is_valid_rental_duration(0)}")


if __name__ == "__main__":
    main()
