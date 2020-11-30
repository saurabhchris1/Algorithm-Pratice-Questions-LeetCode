# Write a function that takes in a non-empty string and returns its run-length↵ encoding.

def runLengthEncoding(string):
    currentLength = 1
    chars = []

    for i in range(1, len(string)):

        currentChar = string[i]
        previousChar = string[i - 1]

        if currentLength == 9 or currentChar != previousChar:
            chars.append(str(currentLength))
            chars.append(previousChar)
            currentLength = 0

        currentLength += 1
    chars.append(str(currentLength))
    chars.append(string[len(string) - 1])

    return "".join(chars)
