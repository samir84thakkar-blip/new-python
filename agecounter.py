def main():
	entered_value = input("Enter an integer: ").strip()

	try:
		number = int(entered_value)
	except ValueError:
		print("Value error: please enter an integer only.")
		return

	if number % 2 == 0:
		print(f"{number} is even.")
	else:
		print(f"{number} is odd.")


if __name__ == "__main__":
	main()
