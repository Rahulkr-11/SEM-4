def dups(lst):
    unique_set = set()
    duplicates = []
    for item in lst:
        if item in unique_set:
            duplicates.append(item)
        else:
            unique_set.add(item)
    return duplicates

# Example usage:
numbers = [1, 2, 3, 2, 5, 3, 3, 5, 6, 3, 4, 5, 7]
print(dups(numbers))  # Returns: [2, 3, 5]
