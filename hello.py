"""
First Python program demostrating software
"""

def greet(name: str) -> str:
    """
    Return a greeting messge.

    Args:
        name: The Person's name

    Returns:
        A formatted greeting string
    """

    return f"Hello, {name}! Welcome to software engineering."

if __name__ == "__main__":
    result = greet("Developer")
    print(result)