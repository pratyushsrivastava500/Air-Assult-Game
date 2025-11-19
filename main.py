"""
Air Assault Game - Main Entry Point
A challenging helicopter obstacle avoidance arcade game.

Author: Pratyush Srivastava
Version: 2.0.0
"""

import sys
from src.game_engine import GameEngine


def main():
    """Initialize and run the game."""
    try:
        # Create game engine
        game = GameEngine()
        
        # Run the game
        game.run()
        
        # Clean up
        game.quit()
        sys.exit(0)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
