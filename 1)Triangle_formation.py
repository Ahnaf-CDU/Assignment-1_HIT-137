def can_form_triangle(a, b, c):
    """
    Check if three lengths can form a triangle.
    Returns True if they can, False otherwise.
    """
    # Check if all inputs are positive
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # The sum of any two sides must be greater than the third side as per triangle inequality theorem
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False

# Main program
def main():
    # Get three inputs from the user
    try:
        side1 = float(input("User input 1: "))
        side2 = float(input("User input 2: "))
        side3 = float(input("User input 3: "))
        
        # Check if they can form a triangle
        if can_form_triangle(side1, side2, side3):
            print(f"Output: Yes, these three lengths can form a triangle.")
        else:
            print(f"Output: NO, these three lengths CANNOT form a triangle.")
            
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()