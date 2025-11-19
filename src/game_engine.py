"""
Game engine module for Air Assault Game.
Contains the main game loop and logic.
"""

import pygame
from typing import Optional
from .config import (
    BLACK, SURFACE_WIDTH, SURFACE_HEIGHT, WINDOW_TITLE, FPS,
    INITIAL_BLOCK_SPEED, INITIAL_GAP_MULTIPLIER, DIFFICULTY_LEVELS,
    HELICOPTER_IMAGE_PATH
)
from .game_objects import Helicopter, Block
from .ui import UI


class GameEngine:
    """Main game engine that manages game state and loop."""
    
    def __init__(self):
        """Initialize the game engine."""
        pygame.init()
        
        # Display setup
        self.surface = pygame.display.set_mode((SURFACE_WIDTH, SURFACE_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        
        # UI manager
        self.ui = UI(self.surface, self.clock)
        
        # Game objects
        self.helicopter: Optional[Helicopter] = None
        self.block: Optional[Block] = None
        
        # Game state
        self.score = 0
        self.running = False
    
    def _reset_game(self):
        """Reset game state for a new game."""
        self.helicopter = Helicopter(HELICOPTER_IMAGE_PATH)
        self.block = Block(INITIAL_GAP_MULTIPLIER)
        self.block.set_speed(INITIAL_BLOCK_SPEED)
        self.score = 0
    
    def _handle_input(self):
        """Handle keyboard and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.helicopter.move_up()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.helicopter.move_down()
        
        return True
    
    def _update_difficulty(self):
        """Update game difficulty based on current score."""
        for level in DIFFICULTY_LEVELS:
            if level["min_score"] <= self.score < level["max_score"]:
                self.block.set_speed(level["speed"])
                self.block.gap = self.helicopter.height * level["gap_multiplier"]
                break
    
    def _check_collisions(self) -> bool:
        """
        Check for all types of collisions.
        
        Returns:
            True if collision detected, False otherwise.
        """
        # Check boundary collision
        if self.helicopter.check_boundary_collision():
            return True
        
        # Check block collision
        if self.block.check_collision(self.helicopter):
            return True
        
        return False
    
    def _update(self):
        """Update game state."""
        # Update positions
        self.helicopter.update()
        self.block.update()
        
        # Check if block passed
        if self.block.is_off_screen():
            self.score += 1
            gap_multiplier = INITIAL_GAP_MULTIPLIER
            
            # Find current difficulty level gap multiplier
            for level in DIFFICULTY_LEVELS:
                if level["min_score"] <= self.score < level["max_score"]:
                    gap_multiplier = level["gap_multiplier"]
                    break
            
            self.block.reset(gap_multiplier)
        
        # Update difficulty
        self._update_difficulty()
        
        # Check collisions
        if self._check_collisions():
            self.ui.show_game_over(callback=self.run)
            return False
        
        return True
    
    def _render(self):
        """Render all game objects."""
        self.surface.fill(BLACK)
        self.helicopter.draw(self.surface)
        self.block.draw(self.surface)
        self.ui.draw_score(self.score)
        pygame.display.update()
    
    def run(self):
        """Main game loop."""
        self._reset_game()
        self.running = True
        
        while self.running:
            # Handle input
            if not self._handle_input():
                break
            
            # Update game state
            if not self._update():
                continue
            
            # Render
            self._render()
            
            # Control frame rate
            self.clock.tick(FPS)
    
    def quit(self):
        """Clean up and quit the game."""
        pygame.quit()
