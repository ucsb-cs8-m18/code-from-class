def convert_from_decimal_to_binary(n):
    # return a string of binary digits that represent n
    answer = ""

    # keep extracting digits while n isn't 0
    while n != 0:
        digit = n % 2
        answer = str(digit) + answer
        n = n // 2 # make n smaller so that I can get the rest of the digits

    return answer

def convert_from_decimal_to_base(n, base):
    assert(2 <= base <= 16)

    # return a string of binary digits that represent n
    answer = ""

    digits = "0123456789ABCDEF"

    # keep extracting digits while n isn't 0
    while n != 0:
        digit = n % base
        answer = digits[digit] + answer
        n = n // base # make n smaller so that I can get the rest of the digits

    return answer

if __name__ == '__main__':
    num = int(input("Enter a number: "))
    base = int(input("Enter a base: "))
    print(convert_from_decimal_to_base(num, base))