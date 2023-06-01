import string
import random

def generate_password(length=12, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    print("\nGenerated Password: " + generate_password() + "\n")