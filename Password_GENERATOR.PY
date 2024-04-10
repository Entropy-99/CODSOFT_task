import random
import string
def main():
    print("Welcome to password Generator")
    length = int(input("Enter the lengthn of password :"))
    lower_D = string.ascii_lowercase
    upper_D = string.ascii_uppercase
    digit_D = string.digits
    symbols_D = string.punctuation
    combine = lower_D + upper_D + digit_D + symbols_D
    x = random.sample(combine,length)
    password="".join(x)
    print(password)
    main()

main()
