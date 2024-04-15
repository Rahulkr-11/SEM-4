def count_characters_words_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            num_characters = len(content)
            num_words = len(content.split())
            num_lines = content.count('\n') + 1  # Count newline characters to get lines
            return num_characters, num_words, num_lines
    except FileNotFoundError:
        return None

# Call the function
file_path = "meteor.txt"  #the actual file path
result = count_characters_words_lines(file_path)
if result:
    num_characters, num_words, num_lines = result
    print(f"Number of characters: {num_characters}")
    print(f"Number of words: {num_words}")
    print(f"Number of lines: {num_lines}")
else:
    print(f"File '{file_path}' not found.")
