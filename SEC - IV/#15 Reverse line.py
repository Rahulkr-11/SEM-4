def print_lines_in_reverse(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in reversed(lines):
                print(line.strip())  # Remove trailing newline
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

# Call the function
file_path = "meteor.txt"  #the actual file path
print_lines_in_reverse(file_path)
