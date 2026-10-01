import math


def calculate_trig_value(function, angle, unit):
	functions = {
		"sin": math.sin,
		"cos": math.cos,
		"tan": math.tan,
	}
	if function not in functions:
		raise ValueError("Choose sin, cos, or tan.")
	if unit not in ("degrees", "radians"):
		raise ValueError("Choose degrees or radians.")
	if not math.isfinite(angle):
		raise ValueError("Enter a finite number for the angle.")

	angle_in_radians = math.radians(angle) if unit == "degrees" else angle
	if function == "tan" and math.isclose(
		math.cos(angle_in_radians), 0.0, abs_tol=1e-12
	):
		raise ValueError("Tangent is undefined for this angle.")

	return functions[function](angle_in_radians)


def main():
	print("Trigonometry Calculator")
	while True:
		print("\nChoose a function:")
		print("1. Sine (sin)")
		print("2. Cosine (cos)")
		print("3. Tangent (tan)")
		print("4. Exit")
		choice = input("Enter 1, 2, 3, or 4: ").strip()

		if choice == "4":
			print("Goodbye!")
			break

		function = {"1": "sin", "2": "cos", "3": "tan"}.get(choice)
		if function is None:
			print("Please choose 1, 2, 3, or 4.")
			continue

		try:
			angle = float(input("Enter the angle: "))
		except ValueError:
			print("Please enter the angle as a number.")
			continue

		unit_choice = input("Use degrees or radians? (d/r): ").strip().lower()
		if unit_choice not in ("d", "r"):
			print("Please enter d for degrees or r for radians.")
			continue
		unit = "degrees" if unit_choice == "d" else "radians"

		try:
			result = calculate_trig_value(function, angle, unit)
		except ValueError as error:
			print(error)
			continue

		print(f"{function}({angle:g} {unit}) = {result:.10g}")


if __name__ == "__main__":
	main()
