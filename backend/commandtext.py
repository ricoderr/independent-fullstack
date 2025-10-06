import sys

def greet(name="World"):
    print(f"Hello, {name}!")

def add(x, y):
    result = int(x) + int(y)
    print(f"{x} + {y} = {result}")

# Command dispatcher
commands = {
    "greet": greet,
    "add": add
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cli.py <command> [args]")
        sys.exit(1)

    command_name = sys.argv[1]
    args = sys.argv[2:]

    if command_name in commands:
        commands[command_name](*args)
    else:
        print(f"Unknown command: {command_name}")