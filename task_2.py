import math
import turtle


def draw_pythagoras_tree(t, branch_length, level, angle=45):
    """
    Recursively draws a Pythagoras tree.

    Args:
        t: Turtle object used for drawing.
        branch_length: Length of the current branch.
        level: Current recursion level.
        angle: Deviation angle of the branches in degrees.
    """
    if level == 0:
        return

    # Draw the current branch
    t.forward(branch_length)

    # Calculate the length of the child branches
    new_length = branch_length * math.cos(math.radians(angle))

    # Draw the right branch
    t.right(angle)
    draw_pythagoras_tree(t, new_length, level - 1, angle)

    # Draw the left branch
    t.left(2 * angle)
    draw_pythagoras_tree(t, new_length, level - 1, angle)

    # Return to the original position and direction
    t.right(angle)
    t.backward(branch_length)


def get_recursion_level():
    """Gets a valid recursion level from the user."""
    while True:
        try:
            level = int(input("Enter recursion level (recommended: 5-12): "))

            if level < 1:
                print("Recursion level must be a positive integer.")
                continue

            return level

        except ValueError:
            print("Please enter a valid integer.")


def setup_screen(level):
    """Creates and configures the drawing screen."""
    screen = turtle.Screen()
    screen.title(f"Pythagoras Tree - Level {level}")
    screen.bgcolor("white")

    return screen


def setup_turtle(screen):
    """Creates and configures the turtle."""
    t = turtle.Turtle()

    t.speed(0)
    t.hideturtle()
    t.color("brown")
    t.pensize(1)

    # Position the turtle at the bottom center
    t.penup()
    t.goto(0, -screen.window_height() // 2 + 50)
    t.setheading(90)
    t.pendown()

    return t


def main():
    """Main program function."""
    level = get_recursion_level()

    screen = setup_screen(level)
    t = setup_turtle(screen)

    initial_branch_length = 150
    branch_angle = 45

    print(
        f"Drawing Pythagoras tree with recursion level {level}..."
    )

    draw_pythagoras_tree(
        t,
        initial_branch_length,
        level,
        branch_angle
    )

    print("Drawing completed. Close the window to exit.")

    turtle.done()


if __name__ == "__main__":
    main()
