"""
UI module for Air Assault Game.
Contains all UI rendering functions and text display.
"""

import pygame
import time
from typing import Tuple
from .config import (
    WHITE, SUNSET, SURFACE_WIDTH, SURFACE_HEIGHT,
    FONT_PATH, FONT_SIZE_SMALL, FONT_SIZE_LARGE, MESSAGE_WAIT_TIME
)


class UI:
    """Handles all UI rendering and display."""
    
    def __init__(self, surface: pygame.Surface, clock: pygame.time.Clock):
        """
        Initialize UI manager.
        
        Args:
            surface: Pygame display surface.
            clock: Pygame clock for timing.
        """
        self.surface = surface
        self.clock = clock
        self.small_font = pygame.font.Font(FONT_PATH, FONT_SIZE_SMALL)
        self.large_font = pygame.font.Font(FONT_PATH, FONT_SIZE_LARGE)
    
    def draw_score(self, score: int):
        """
        Draw the current score on screen.
        
        Args:
            score: Current game score to display.
        """
        text = self.small_font.render(f"Score: {score}", True, WHITE)
        self.surface.blit(text, [0, 0])
    
    def _make_text_objects(self, text: str, font: pygame.font.Font) -> Tuple:
        """
        Create text surface and rect.
        
        Args:
            text: Text to render.
            font: Font to use.
            
        Returns:
            Tuple of (text_surface, text_rect).
        """
        text_surface = font.render(text, True, SUNSET)
        return text_surface, text_surface.get_rect()
    
    def show_message(self, message: str, callback=None) -> None:
        """
        Display a centered message on screen.
        
        Args:
            message: Main message to display.
            callback: Optional callback function to handle user input.
        """
        # Draw main message
        title_surf, title_rect = self._make_text_objects(message, self.large_font)
        title_rect.center = SURFACE_WIDTH / 2, SURFACE_HEIGHT / 2
        self.surface.blit(title_surf, title_rect)
        
        # Draw instruction
        instruction = "Press any key to continue"
        instr_surf, instr_rect = self._make_text_objects(instruction, self.small_font)
        instr_rect.center = SURFACE_WIDTH / 2, (SURFACE_HEIGHT / 2) + 100
        self.surface.blit(instr_surf, instr_rect)
        
        pygame.display.update()
        time.sleep(MESSAGE_WAIT_TIME)
        
        # Wait for user input
        waiting = True
        while waiting:
            for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    waiting = False
                    if callback:
                        callback()
                    break
            self.clock.tick()
    
    def show_game_over(self, callback=None):
        """
        Display game over message.
        
        Args:
            callback: Optional callback function for restart.
        """
        self.show_message("CRASHED!", callback)
