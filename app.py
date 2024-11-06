def add_numbers(a, b):
    """Additionne deux nombres et retourne le résultat."""
    return a + b


# Introducing an unused function, which SonarCloud should flag
def unused_function():
    x = "This function does nothing"
    print(x)


# Introducing a variable with a single letter (SonarCloud prefers descriptive names)
if __name__ == "__main__":
    result = add_numbers(5, 7)
    print(f"Le résultat de l'addition est : {result}")
