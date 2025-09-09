"""
Football Replay Visualizer

Architecture:
- models.py: Data structures and configuration
- pitch_renderer.py: Football field rendering
- entity_renderer.py: Player and ball rendering
- playback_controller.py: Playback logic and controls
- ui_renderer.py: User interface elements
- data_loader.py: Data loading and validation
"""

import arcade
import sys
from typing import List

from .core import PitchDimensions, EntityProperties, PlaybackConfig, PlaybackController
from .rendering import PitchRenderer, EntityRenderer
from .ui import UIRenderer
from .data import DataLoader


class FootballVisualizer(arcade.Window):
    """Main application class for the football replay visualizer"""
    
    def __init__(self, data_file: str):
        # Window sized to match field aspect ratio (1.54:1) with UI padding
        # Field: 700x454, so window should be larger to accommodate UI
        super().__init__(900, 700, "Football Replay Visualizer")
        
        # Window properties
        self.set_update_rate(1/60)  # 60 FPS rendering
        
        # Configuration
        self.pitch_dimensions = PitchDimensions()
        self.entity_properties = EntityProperties()
        self.playback_config = PlaybackConfig()
        
        # Initialize components
        self.pitch_renderer = PitchRenderer(self.pitch_dimensions)
        self.entity_renderer = EntityRenderer(self.pitch_renderer, self.entity_properties)
        self.ui_renderer = UIRenderer(self.width, self.height)
        
        # Load data and initialize playback controller
        self.frames = DataLoader.load_data(data_file)
        if not DataLoader.validate_data(self.frames):
            print("Warning: Data validation failed, but continuing...")
        
        self.playback_controller = PlaybackController(self.frames, self.playback_config)
        
        # Initialize application
        self.setup()
    
    def setup(self):
        """Initialize the application"""
        # Use a more realistic grass green color (RGB: 34, 139, 34)
        arcade.set_background_color((34, 139, 34))
    
    def on_draw(self):
        """Render the current frame"""
        self.clear()
        
        if not self.frames:
            self.ui_renderer.draw_no_data_message()
            return
        
        # Draw pitch
        self.pitch_renderer.draw_pitch()
        
        # Draw entities with interpolation
        current_frame = self.playback_controller.get_current_frame()
        next_frame = self.playback_controller.get_next_frame()
        interpolation_factor = self.playback_controller.interpolation_factor
        is_playing = self.playback_controller.playback_state.value == "playing"
        
        self.entity_renderer.draw_entities(
            current_frame, next_frame, interpolation_factor, is_playing
        )
        
        # Draw UI
        playback_info = self.playback_controller.get_playback_info()
        self.ui_renderer.draw_ui(playback_info)
    
    def on_update(self, delta_time: float):
        """Update the application state"""
        self.playback_controller.update(delta_time)
    
    def on_key_press(self, key, modifiers):
        """Handle key press events"""
        if key == arcade.key.SPACE:
            self.playback_controller.toggle_play_pause()
        
        elif key == arcade.key.R:
            self.playback_controller.restart()
        
        elif key == arcade.key.LEFT:
            self.playback_controller.start_left_key_press()
        
        elif key == arcade.key.RIGHT:
            self.playback_controller.start_right_key_press()
    
    def on_key_release(self, key, modifiers):
        """Handle key release events"""
        if key == arcade.key.LEFT:
            self.playback_controller.release_left_key()
        
        elif key == arcade.key.RIGHT:
            self.playback_controller.release_right_key()


def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        print("Usage: python football_visualizer_refactored.py <data_file.json>")
        print("Example: python football_visualizer_refactored.py sample_data.json")
        return
    
    data_file = sys.argv[1]
    app = FootballVisualizer(data_file)
    arcade.run()


if __name__ == "__main__":
    main()
