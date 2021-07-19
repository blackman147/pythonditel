def check_vowel(input):
    vowels = ['a', 'e', 'i', 'o', 'u']
    input = input.lower()
    for i in input:
        for x in vowels:
            if i == x:
                return "contains a vowel"

    return "does not contain a vowel"


input = "My name is blackie"
print(check_vowel(input))


# number = int(input("Enter a number: "))
#
# if number % 2 == 0:
#     print("is even")
# else:
#     print(" is odd")


