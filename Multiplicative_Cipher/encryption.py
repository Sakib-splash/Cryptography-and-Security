

def encryption(plaintext, key):
    result = ""


    for i in range(len(plaintext)):
        char = plaintext[i]


        if char == ' ':
            result += char

        elif char.isupper():
            result += chr((((ord(char) -65) * key) % 26) + 65)

        else:
            result += chr(((((ord(char) - 97) * key) % 26) + 97) - 32)

    return result


input = open("input.txt", "r+")
output = open("output.txt", "w")
plaintxt = input.read();
key = 7;
result = encryption(plaintxt, key)
output.write(result)
input.truncate(0)

input.close()
output.close()