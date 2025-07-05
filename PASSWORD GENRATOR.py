import random
import string

def generate_password(length, complexity):
    """
    Generate a random password based on length and complexity.

    Parameters:
        length (int): Desired password length.
        complexity (int): 
            1 - Letters only
            2 - Letters + digits
            3 - Letters + digits + symbols

    Returns:
        str: The generated password or None if invalid input.
    """
    
    char_sets = [
        string.ascii_letters,                                
        string.ascii_letters + string.digits,                 
        string.ascii_letters + string.digits + string.punctuation  
    ]

   
    if 1 <= complexity <= 3:
        chars = char_sets[complexity - 1]
        return ''.join(random.choice(chars) for _ in range(length))
    else:
        print("❌ Invalid complexity. Choose 1, 2, or 3.")
        return None

def main():
    print("🔐 Password Generator 🔐")

    try:
       
        length = int(input("Enter password length: "))
        
        print("\nSelect complexity level:")
        print("1. Letters only (a-z, A-Z)")
        print("2. Letters + digits (a-z, A-Z, 0-9)")
        print("3. Letters + digits + symbols")

        complexity = int(input("Choose complexity (1/2/3): "))

      
        password = generate_password(length, complexity)
        if password:
            print("\n✅ Generated Password:", password)

    except ValueError:
        print("❌ Invalid input. Enter numeric values only.")

if __name__ == "__main__":
    main()
