
def greet(name):
    """Return a friendly greeting."""
    if not name:
        name = "World"
    return f"Hello, {name}!"


def main():
    print(greet("Migration Agent"))


if __name__ == "__main__":
    main()
