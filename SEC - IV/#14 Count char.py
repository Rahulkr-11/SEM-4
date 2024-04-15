def count_character_frequency(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            char_frequency = {}
            for char in content:
                if char.isalpha():  # Consider only alphabetic characters
                    char = char.lower()  # Convert to lowercase
                    char_frequency[char] = char_frequency.get(char, 0) + 1
            return char_frequency
    except FileNotFoundError:
        return None

# Call the function 
file_path = "sample.txt"  #the actual file path
result = count_character_frequency(file_path)
if result:
    print("Character frequency:")
    for char, freq in result.items():
        print(f"{char}: {freq}")
else:
    print(f"File '{file_path}' not found.")
