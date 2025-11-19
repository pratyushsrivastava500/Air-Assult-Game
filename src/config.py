"""
Configuration module for Air Assault Game.
Contains all game constants, colors, and settings.
"""

# Color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SUNSET = (253, 72, 47)
GREEN_YELLOW = (184, 255, 0)
BRIGHT_BLUE = (47, 228, 253)
ORANGE = (255, 113, 0)
YELLOW = (255, 236, 0)
PURPLE = (252, 67, 255)

# Color choices for blocks
COLOR_CHOICES = [GREEN_YELLOW, BRIGHT_BLUE, ORANGE, YELLOW, PURPLE]

# Display settings
SURFACE_WIDTH = 800
SURFACE_HEIGHT = 500
WINDOW_TITLE = "Air Assault"
FPS = 60

# Helicopter settings
HELICOPTER_WIDTH = 100
HELICOPTER_HEIGHT = 43
HELICOPTER_START_X = 150
HELICOPTER_START_Y = 200
HELICOPTER_SPEED = 5

# Block settings
BLOCK_WIDTH = 75
INITIAL_BLOCK_SPEED = 4
INITIAL_GAP_MULTIPLIER = 3

# Game difficulty progression
DIFFICULTY_LEVELS = [
    {"min_score": 3, "max_score": 5, "speed": 5, "gap_multiplier": 2.9},
    {"min_score": 5, "max_score": 8, "speed": 6, "gap_multiplier": 2.8},
    {"min_score": 8, "max_score": 14, "speed": 7, "gap_multiplier": 2.7},
]

# Asset paths
HELICOPTER_IMAGE_PATH = "images/images.png"
FONT_PATH = "freesansbold.ttf"
FONT_SIZE_SMALL = 20
FONT_SIZE_LARGE = 150

# Message settings
MESSAGE_WAIT_TIME = 1  # seconds
