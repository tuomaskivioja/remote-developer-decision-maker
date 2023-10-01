def has_special_char(password):
    special_chars = "!@#$%^&*()_+-=[]{};:'\"\\|,.<>?~"  # List of special characters
    for char in password:
        if char in special_chars:
            return True
    return False

def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def is_valid_password(password):
    # 3. Check Length
    if len(password) < 7:
        return False, "Password is too short. It must be at least 7 characters long."
    
    # 4. Check for Special Characters
    if not has_special_char(password):
        return False, "Password must include at least 1 special character."
    
    # 5. Check for Numbers
    if not has_digit(password):
        return False, "Password must include at least 1 number."
    
    return True, "Password is strong!"

def main():
    # 1. Introduction
    print("Welcome to the Password Checker!")
    print("A strong password must meet the following criteria:")
    print("- At least 7 characters long")
    print("- Include at least 1 special character")
    print("- Include at least 1 number")
    
    attempts = 3  # Number of attempts for Bonus Challenge 7
    
    for _ in range(attempts):
        # 2. Taking Password Input
        password = input("\nEnter your password: ")
        
        # 6. Providing Feedback
        valid, message = is_valid_password(password)
        print(message)
        if valid:
            break
    else:
        print("\nSorry, you've exceeded the maximum number of attempts.")

if __name__ == "__main__":
    main()
