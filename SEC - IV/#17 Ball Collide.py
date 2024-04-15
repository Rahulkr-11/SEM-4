def ball_collide(ball1, ball2):
    """
    Checks if two balls are colliding.

    Args:
        ball1 (tuple): (x1, y1, r1) representing the first ball's position (x1, y1) and radius r1.
        ball2 (tuple): (x2, y2, r2) representing the second ball's position (x2, y2) and radius r2.

    Returns:
        bool: True if the balls are colliding, False otherwise.
    """
    x1, y1, r1 = ball1
    x2, y2, r2 = ball2

    # Calculate the distance between the centers of the two balls
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print (f"Ball 1 (x1, y1, r1): {ball1}")
    print (f"Ball 2 (x1, y1, r1): {ball2}")
    print (f"Distance b/w balls : {distance}")
    # Check if the distance is less than or equal to the sum of the radii
    return distance <= r1 + r2

# Example usage
ball1 = (0, 0, 5)  # Ball with center at (0, 0) and radius 5
ball2 = (3, 4, 3)  # Ball with center at (3, 4) and radius 3


print(f"Are the balls colliding? : {ball_collide(ball1, ball2)}")
