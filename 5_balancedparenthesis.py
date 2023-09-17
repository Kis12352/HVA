def are_brackets_balanced(testVariable, startIndex=0, currentIndex=0):
    stack = []  # Initialize an empty stack
    brackets = {')': '(', '}': '{', ']': '['}

    try:
        for i in range(startIndex, len(testVariable)):
            if testVariable[i] in '([{':
                stack.append(testVariable[i])
            elif testVariable[i] in ')]}':
                if not stack or stack[-1] != brackets[testVariable[i]]:
                    return False  # Unmatched closing bracket
                stack.pop()

            currentIndex += 1

            if not stack:
                return currentIndex  # Balanced brackets found

    except Exception as e:
        print(f"Error: {e}")
        return False  # Handle incorrect input gracefully

    return False  # Unmatched open bracket

# Example usage:
while True:
    testVariable = input("Enter a string with brackets: ").strip()
    if not testVariable:
        print("Input cannot be empty.")
        continue

    startIndex = 0
    currentIndex = 0

    result = are_brackets_balanced(testVariable, startIndex, currentIndex)
    if result:
        print(f"Brackets are balanced. They close at index {result - 1}.")
    else:
        print("Brackets are not balanced.")

    play_again = input("Check another string? (yes/no): ")
    if play_again.lower() != "yes":
        print("Goodbye!")
        break


