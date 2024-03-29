

def Decryption(ciphertext, key):
    result = ""
    inverse = pow(7,-1,26)


    for i in range(len(ciphertext)):
            char = ciphertext[i]

            if char == ' ':
                result += char
            elif char.isupper():
                value = ord(char) - 65
                result += chr((((value * inverse) % 26) + 65) + 32)
            else:
                value = ord(char) - 97
                result += chr(((value * inverse) % 26) + 97)
    return result


input = open("output.txt", "r+")
output = open("input.txt", "w")

result = Decryption(input.read(), 7)
input.truncate(0)

output.write(result)

input.close()
output.close()