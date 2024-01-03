import random
import string
print("Welcome to Random Password Generator")
def main():
    l=int(input("Enter the length:"))
    lowerd="abcdefghijklmnopqrstuvwxyz"
    upperd="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numberd="0123456789"
    symbold=string.punctuation
    combine=lowerd+upperd+numberd+symbold
    k=random.sample(combine,l)
    password="".join(k)
    print("Your Password is:",password)
    main()
main()