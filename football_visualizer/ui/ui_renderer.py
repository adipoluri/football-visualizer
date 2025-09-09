"""
UI rendering module for the football visualizer.

This module handles all user interface elements including frame information,
playback state, and control instructions.
"""

import arcade
from typing import Dict, Any


class UIRenderer:
    """Handles rendering of all user interface elements"""
    
    # Replay details offset - adjust this single value to move all replay text
    REPLAY_DETAILS_OFFSET = 70
    
    def __init__(self, window_width: int, window_height: int):
        self.window_width = window_width
        self.window_height = window_height
    
    def draw_ui(self, playback_info: Dict[str, Any]):
        """Draw all UI elements"""
        self._draw_title()
        self._draw_frame_info(playback_info)
        self._draw_time_info(playback_info)
        self._draw_playback_state(playback_info)
        self._draw_controls_help()
    
    def _draw_title(self):
        """Draw the main title using Kenney Blocks font"""
        arcade.draw_text(
            "FOOTBALL VISUALIZER",
            self.window_width // 2,
            self.window_height - 20,
            arcade.color.WHITE,
            font_size=40,
            font_name="Kenney Blocks",
            anchor_x="center",
            anchor_y="center"
        )
    
    def draw_no_data_message(self):
        """Draw message when no data is available"""
        arcade.draw_text(
            "No data available",
            self.window_width // 2,
            self.window_height // 2,
            arcade.color.WHITE,
            font_size=28,
            font_name="Kenney Pixel",
            anchor_x="center",
            anchor_y="center"
        )
    
    def _draw_frame_info(self, playback_info: Dict[str, Any]):
        """Draw frame counter information"""
        frame_text = f"Frame: {playback_info['current_frame']}/{playback_info['total_frames']}"
        arcade.draw_text(
            frame_text,
            10,
            self.window_height - self.REPLAY_DETAILS_OFFSET,
            arcade.color.WHITE,
            font_size=18,
            font_name="Kenney Pixel"
        )
    
    def _draw_time_info(self, playback_info: Dict[str, Any]):
        """Draw time information"""
        time_text = f"Time: {playback_info['time']:.2f}s"
        arcade.draw_text(
            time_text,
            10,
            self.window_height - (self.REPLAY_DETAILS_OFFSET + 25),
            arcade.color.WHITE,
            font_size=18,
            font_name="Kenney Pixel"
        )
    
    def _draw_playback_state(self, playback_info: Dict[str, Any]):
        """Draw playback state information"""
        if playback_info['is_fast_forwarding']:
            state_text = f"State: FAST FORWARD ({playback_info['fast_forward_speed']}x)"
        elif playback_info['is_rewinding']:
            state_text = f"State: REWIND ({playback_info['rewind_speed']}x)"
        else:
            state_text = f"State: {playback_info['state']}"
        
        arcade.draw_text(
            state_text,
            10,
            self.window_height - (self.REPLAY_DETAILS_OFFSET + 50),
            arcade.color.WHITE,
            font_size=18,
            font_name="Kenney Pixel"
        )
    
    def _draw_controls_help(self):
        """Draw control instructions"""
        controls_text = "SPACE: Play/Pause | R: Restart | Arrows: Step/FF/RW"
        arcade.draw_text(
            controls_text,
            10,
            10,
            arcade.color.WHITE,
            font_size=16,
            font_name="Kenney Pixel"
        )
