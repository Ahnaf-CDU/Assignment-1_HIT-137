def draw_hollow_square(size):
    """
    Square of the given size using asterisks.
    Only the border is drawn, inside is hollow.
    """
    # Special case for size 1
    if size == 1:
        print("*")
        return
    
    # Draw the square
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size-1:  # First or last row
                print("*", end=" ")
            elif j == 0 or j == size-1:  # First or last column in middle rows
                print("*", end=" ")
            else:  # Inside the square (hollow part)
                print(" ", end=" ")
        print()  # Move to next line after each row

# Main program
def main():
    try:
        # Get input
        size = int(input("Enter the size of the square: "))
        
        # check the input
        if size <= 0:
            print("Error: Size must be a positive integer.")
        else:
            print(f"\nSquare of size {size}:")
            draw_hollow_square(size)
            
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
   
    main()