ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
BASE = len(ALPHABET)


def encode(number):
    if number == 0:
        return ALPHABET[0]

    encoded = ""

    while number > 0:
        remainder = number % BASE
        encoded += ALPHABET[remainder]
        number //= BASE

    return encoded[::-1]
def decode(short_code):
    number = 0

    for character in short_code:
        value = ALPHABET.index(character)
        number = number * BASE + value

    return number

if __name__ == "__main__":
    print("Encode:")
    print(encode(125))

    print("\nDecode:")
    print(decode("CB"))
