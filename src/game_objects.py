"""
Game objects module for Air Assault Game.
Contains Helicopter and Block classes.
"""

from typing import Tuple
import pygame
from random import randint, randrange
from .config import (
    HELICOPTER_WIDTH, HELICOPTER_HEIGHT, HELICOPTER_START_X, 
    HELICOPTER_START_Y, HELICOPTER_SPEED, BLOCK_WIDTH,
    SURFACE_WIDTH, SURFACE_HEIGHT, COLOR_CHOICES
)


class Helicopter:
    """Represents the player's helicopter."""
    
    def __init__(self, image_path: str):
        """
        Initialize the helicopter.
        
        Args:
            image_path: Path to the helicopter image file.
        """
        self.image = pygame.image.load(image_path)
        self.width = HELICOPTER_WIDTH
        self.height = HELICOPTER_HEIGHT
        self.x = HELICOPTER_START_X
        self.y = HELICOPTER_START_Y
        self.y_velocity = 0
    
    def move_up(self):
        """Start moving the helicopter upward."""
        self.y_velocity = -HELICOPTER_SPEED
    
    def move_down(self):
        """Start moving the helicopter downward."""
        self.y_velocity = HELICOPTER_SPEED
    
    def update(self):
        """Update helicopter position based on velocity."""
        self.y += self.y_velocity
    
    def draw(self, surface: pygame.Surface):
        """
        Draw the helicopter on the given surface.
        
        Args:
            surface: Pygame surface to draw on.
        """
        surface.blit(self.image, (self.x, self.y))
    
    def check_boundary_collision(self) -> bool:
        """
        Check if helicopter hit screen boundaries.
        
        Returns:
            True if collision detected, False otherwise.
        """
        return self.y > SURFACE_HEIGHT - 40 or self.y < 0
    
    def get_rect(self) -> Tuple[int, int, int, int]:
        """
        Get helicopter bounding box.
        
        Returns:
            Tuple of (x, y, width, height).
        """
        return (self.x, self.y, self.width, self.height)


class Block:
    """Represents an obstacle block."""
    
    def __init__(self, gap_multiplier: float = 3):
        """
        Initialize a block obstacle.
        
        Args:
            gap_multiplier: Multiplier for gap size between top and bottom blocks.
        """
        self.width = BLOCK_WIDTH
        self.x = SURFACE_WIDTH
        self.height = randint(0, int(SURFACE_HEIGHT / 2))
        self.gap = HELICOPTER_HEIGHT * gap_multiplier
        self.color = COLOR_CHOICES[randrange(0, len(COLOR_CHOICES))]
        self.speed = 4
    
    def update(self):
        """Move block to the left."""
        self.x -= self.speed
    
    def draw(self, surface: pygame.Surface):
        """
        Draw the block on the given surface.
        
        Args:
            surface: Pygame surface to draw on.
        """
        # Top block
        pygame.draw.rect(surface, self.color, 
                        [self.x, 0, self.width, self.height])
        # Bottom block
        pygame.draw.rect(surface, self.color, 
                        [self.x, self.height + self.gap, 
                         self.width, SURFACE_HEIGHT])
    
    def is_off_screen(self) -> bool:
        """
        Check if block has moved completely off screen.
        
        Returns:
            True if off screen, False otherwise.
        """
        return self.x < (-1 * self.width)
    
    def reset(self, gap_multiplier: float = 3):
        """
        Reset block to starting position with new random height.
        
        Args:
            gap_multiplier: Multiplier for gap size.
        """
        self.x = SURFACE_WIDTH
        self.height = randint(0, int(SURFACE_HEIGHT / 2))
        self.gap = HELICOPTER_HEIGHT * gap_multiplier
        self.color = COLOR_CHOICES[randrange(0, len(COLOR_CHOICES))]
    
    def set_speed(self, speed: int):
        """
        Set the movement speed of the block.
        
        Args:
            speed: New speed value.
        """
        self.speed = speed
    
    def check_collision(self, helicopter: Helicopter) -> bool:
        """
        Check if helicopter collides with this block.
        
        Args:
            helicopter: Helicopter object to check collision with.
            
        Returns:
            True if collision detected, False otherwise.
        """
        heli_x, heli_y, heli_w, heli_h = helicopter.get_rect()
        
        # Check if helicopter is in the x-range of the block
        if heli_x + heli_w > self.x and heli_x < self.x + self.width:
            # Check collision with top block
            if heli_y < self.height:
                return True
            # Check collision with bottom block
            if heli_y + heli_h > self.height + self.gap:
                return True
        
        return False
