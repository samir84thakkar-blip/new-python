class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


modelX = Vehicle(176, 13)
print("Model X has a max speed of", modelX.max_speed, "and mileage of", modelX.mileage)

