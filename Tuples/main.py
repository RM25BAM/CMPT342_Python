import matplotlib.pyplot as plt # plt is alias 
def main():
    # Create lists with the X and Y coordinates.
    x_coords = [1, 2, 3, 4, 5]
    y_coords = [3, 3, 5, 2, 4]

    # Build the line graph.
    plt.plot(x_coords, y_coords)

    # Add a title.
    plt.title('Sample Data')

    # Add labels to the axes.
    plt.xlabel('This is the X axis')
    plt.ylabel('This is the Y axis')

    # Add a grid.
    plt.grid(True) #False by default

    # Display the line graph.
    plt.show()

# Call the main function.
if __name__ == '__main__':
    main()