#!/usr/bin/env python3

def main():
    print(multiply(10, 2))
    print(multiply(-51, -4))
    print(multiply(3, 9))

def multiply(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    elif num2 < 0:
        num1 = num1 * -1
        num2 = num2 * -1
        return num1 + multiply(num1, num2 - 1)
    else:
        return num1 + multiply(num1, num2 - 1)


if __name__ == "__main__":
    main()