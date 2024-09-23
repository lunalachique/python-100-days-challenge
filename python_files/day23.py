print("Your Login System")
print()

def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == "diana" and password == "100daysPython":
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Please try again.")
            continue
login()
