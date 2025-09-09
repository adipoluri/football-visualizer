"""
Data models for the football visualizer application.

This module contains all the data structures and enums used throughout the application.
"""

from dataclasses import dataclass
from enum import Enum
from typing import List


class PlaybackState(Enum):
    """Enumeration for playback states"""
    PLAYING = "playing"
    PAUSED = "paused"


@dataclass
class Position:
    """Represents a 2D position with normalized coordinates (0.0 to 1.0)"""
    x: float
    y: float


@dataclass
class BallPosition:
    """Represents a 3D position for the ball with normalized coordinates (0.0 to 1.0) and height (0.0 to 1.0)"""
    x: float
    y: float
    z: float  # Height: 0.0 = ground level, 1.0 = maximum height


@dataclass
class Frame:
    """Represents a single frame of position data"""
    time: float
    ball: BallPosition
    players: List[Position]


@dataclass
class PitchDimensions:
    """Pitch dimensions and layout configuration"""
    # FIFA standard: 105m x 68m, aspect ratio ~1.54:1
    # Increased size to better utilize window space
    width: int = 800
    height: int = 520
    x_offset: int = 50
    y_offset: int = 50
    
    # Goal areas (FIFA standard: 5.5m from goal line, 18.32m wide)
    goal_area_width: int = None
    goal_area_height: int = None
    
    # Penalty areas (FIFA standard: 16.5m from goal line, 40.32m wide)
    penalty_area_width: int = None
    penalty_area_height: int = None
    
    def __post_init__(self):
        """Calculate derived dimensions based on FIFA standards"""
        if self.goal_area_height is None:
            self.goal_area_height = int(self.width * 18.32 / 105)  # ~122px
        if self.goal_area_width is None:
            self.goal_area_width = int(self.height * 5.5 / 68)   # ~37px
        if self.penalty_area_height is None:
            self.penalty_area_height = int(self.width * 40.32 / 105)  # ~269px
        if self.penalty_area_width is None:
            self.penalty_area_width = int(self.height * 16.5 / 68)  # ~110px


@dataclass
class EntityProperties:
    """Properties for rendering entities (players and ball)"""
    # Increased sizes to match larger field
    player_radius: int = 14
    ball_radius: int = 6
    ball_max_radius: int = 20  # Maximum radius when ball is at maximum height
    team_colors: List[tuple] = None
    
    def __post_init__(self):
        """Set default team colors if not provided"""
        if self.team_colors is None:
            import arcade
            self.team_colors = [
                arcade.color.ALABAMA_CRIMSON,       # Team 1
                arcade.color.DARK_POWDER_BLUE       # Team 2
            ]


@dataclass
class PlaybackConfig:
    """Configuration for playback behavior"""
    data_fps: float = 30.0
    fast_forward_speed: float = 5.0
    rewind_speed: float = 5.0
    key_press_buffer_time: float = 0.3  # 300ms buffer before starting continuous
