Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pygame
... import sys
... 
... # Initialize pygame
... pygame.init()
... 
... # Set up the screen
... screen_width = 800
... screen_height = 600
... screen = pygame.display.set_mode((screen_width, screen_height))
... pygame.display.set_caption("Bouncing Ball")
... 
... # Set up colors
... WHITE = (255, 255, 255)
... RED = (255, 0, 0)
... 
... # Ball settings
... ball_radius = 20
... ball_x = screen_width // 2
... ball_y = screen_height // 2
... ball_x_velocity = 4
... ball_y_velocity = 4
... 
... # Set up the clock to control frame rate
... clock = pygame.time.Clock()
... 
... # Game loop
... while True:
...     screen.fill(WHITE)  # Fill the screen with white
... 
...     # Check for events (like closing the window)
...     for event in pygame.event.get():
...         if event.type == pygame.QUIT:
...             pygame.quit()
...             sys.exit()
... 
...     # Move the ball
    ball_x += ball_x_velocity
    ball_y += ball_y_velocity

    # Check for collision with walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
        ball_x_velocity = -ball_x_velocity  # Reverse direction

    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= screen_height:
        ball_y_velocity = -ball_y_velocity  # Reverse direction

    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.update()

    # Control the frame rate (60 frames per second)
    clock.tick(60)
