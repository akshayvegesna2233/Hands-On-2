def bubble_up(sequence):
    length = len(sequence)
    for outer in range(length - 1):
        smallest = outer
        # Locate the smallest element in the unsorted portion
        for inner in range(outer + 1, length):
            if sequence[inner] < sequence[smallest]:
                smallest = inner
        # If a smaller element is found, swap it with the current position
        if smallest != outer:
            sequence[outer], sequence[smallest] = sequence[smallest], sequence[outer]

# Demonstration
numbers = [83, 15, 74, 36, 9]
bubble_up(numbers)
print("Arranged sequence:", numbers)