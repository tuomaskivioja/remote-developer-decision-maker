
def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        raise ValueError("Invalid email address")

email = input("give me your email ")


try:
    validate_email(email)
    print("Logged in succesfully")
except ValueError as e:
    # If a ValueError is raised (which happens if the email is invalid), this block is executed
    print("Invalid email, try again")

salad = 2
steak_and_rice = 3
eggs = 4
banana = 10

print("breakfast cost:")
print("eggs")


print("lunch cost:")
print(salad)

print("dinner cost:")
print(steak_and_rice + eggs)
# login(email)