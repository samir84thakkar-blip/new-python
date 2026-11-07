class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity

    def fare(self):
        # Default fare is seating capacity * 100
        return self.seating_capacity * 100

class Bus(Vehicle):
    def fare(self):
        # Get the base fare from the parent Vehicle class
        base_fare = super().fare()
        # Add a 10% maintenance charge
        total_fare = base_fare + (base_fare * 0.10)
        return int(total_fare)

# Example Usage:
school_bus = Bus("School Bus", 50)
print(f"The total fare for the bus ride is: INR {school_bus.fare()}")
