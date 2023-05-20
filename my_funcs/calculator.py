def simple_calculator(num_1: float | int, num_2: float | int, operation: str) -> float | int:
    if operation == "/":
        return num_1 / num_2
    elif operation == "*":
        return num_1 * num_2
    elif operation == "+":
        return num_1 + num_2
    elif operation == "-":
        return num_1 - num_2
