# class_static_methods_demo.py

class Calculator:
    """
    A class demonstrating the use of static methods and class methods in Python.
    It includes a class attribute, a static method for addition,
    and a class method for multiplication that accesses the class attribute.
    """

    # Class attribute: shared by all instances of the class and the class itself.
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        A static method that adds two numbers.
        Static methods do not receive a reference to the class (cls) or
        the instance (self) as their first argument. They behave like
        regular functions but are logically grouped with the class.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        A class method that multiplies two numbers.
        Class methods receive the class itself (conventionally named 'cls')
        as their first argument. This allows them to access and modify
        class attributes or call other class methods.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of a and b.
        """
        # Accessing the class attribute 'calculation_type' using 'cls'
        print(f"Calculation type: {cls.calculation_type}")
        return a * b