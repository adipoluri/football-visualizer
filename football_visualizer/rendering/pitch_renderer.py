"""
Pitch rendering module for the football visualizer.

This module handles all aspects of drawing the football field including
the main field, goal areas, penalty areas, center circle, and goal posts.
"""

import arcade
from ..core.models import PitchDimensions


class PitchRenderer:
    """Handles rendering of the football pitch and all field markings"""
    
    def __init__(self, dimensions: PitchDimensions):
        self.dimensions = dimensions
    
    def draw_pitch(self):
        """Draw the complete football pitch with all markings"""
        self._draw_field_outline()
        self._draw_midline()
        self._draw_center_circle()
        self._draw_center_dot()
        self._draw_goal_areas()
        self._draw_penalty_areas()
        self._draw_penalty_arcs()
        self._draw_penalty_spots()
        self._draw_goal_posts()
    
    def _draw_field_outline(self):
        """Draw the main field outline"""
        arcade.draw_rectangle_outline(
            self.dimensions.x_offset + self.dimensions.width // 2,
            self.dimensions.y_offset + self.dimensions.height // 2,
            self.dimensions.width,
            self.dimensions.height,
            arcade.color.WHITE,
            border_width=3
        )
    
    def _draw_midline(self):
        """Draw the center line dividing the field"""
        arcade.draw_line(
            self.dimensions.x_offset + self.dimensions.width // 2,
            self.dimensions.y_offset,
            self.dimensions.x_offset + self.dimensions.width // 2,
            self.dimensions.y_offset + self.dimensions.height,
            arcade.color.WHITE,
            line_width=2
        )
    
    def _draw_center_circle(self):
        """Draw the center circle"""
        arcade.draw_circle_outline(
            self.dimensions.x_offset + self.dimensions.width // 2,
            self.dimensions.y_offset + self.dimensions.height // 2,
            self.dimensions.height // 6,
            arcade.color.WHITE,
            border_width=2
        )
    
    def _draw_center_dot(self):
        """Draw the center dot (same size as penalty spots)"""
        arcade.draw_circle_filled(
            self.dimensions.x_offset + self.dimensions.width // 2,
            self.dimensions.y_offset + self.dimensions.height // 2,
            3,
            arcade.color.WHITE
        )
    
    def _draw_goal_areas(self):
        """Draw the goal areas (6-yard boxes)"""
        # Left goal area
        arcade.draw_rectangle_outline(
            self.dimensions.x_offset + self.dimensions.goal_area_width // 2,
            self.dimensions.y_offset + self.dimensions.height // 2,
            self.dimensions.goal_area_width,
            self.dimensions.goal_area_height,
            arcade.color.WHITE,
            border_width=2
        )
        
        # Right goal area
        arcade.draw_rectangle_outline(
            self.dimensions.x_offset + self.dimensions.width - self.dimensions.goal_area_width // 2,
            self.dimensions.y_offset + self.dimensions.height // 2,
            self.dimensions.goal_area_width,
            self.dimensions.goal_area_height,
            arcade.color.WHITE,
            border_width=2
        )
    
    def _draw_penalty_areas(self):
        """Draw the penalty areas (18-yard boxes)"""
        # Left penalty area
        arcade.draw_rectangle_outline(
            self.dimensions.x_offset + self.dimensions.penalty_area_width // 2,
            self.dimensions.y_offset + self.dimensions.height // 2,
            self.dimensions.penalty_area_width,
            self.dimensions.penalty_area_height,
            arcade.color.WHITE,
            border_width=2
        )
        
        # Right penalty area
        arcade.draw_rectangle_outline(
            self.dimensions.x_offset + self.dimensions.width - self.dimensions.penalty_area_width // 2,
            self.dimensions.y_offset + self.dimensions.height // 2,
            self.dimensions.penalty_area_width,
            self.dimensions.penalty_area_height,
            arcade.color.WHITE,
            border_width=2
        )
    
    def _draw_penalty_arcs(self):
        """Draw the penalty arcs (semi-circles at the top of penalty areas)"""
        # Penalty arc radius: 9.15m from penalty spot
        penalty_arc_radius = int(self.dimensions.width * 9.15 / 105)  # ~70px
        penalty_spot_distance = int(self.dimensions.width * 11 / 105)  # ~84px from goal line
        
        # Left penalty arc (only the part above the penalty area)
        left_penalty_spot_x = self.dimensions.x_offset + penalty_spot_distance
        left_penalty_spot_y = self.dimensions.y_offset + self.dimensions.height // 2
        
        # Draw arc from -52.5 to 52.5 degrees (only the top portion above penalty area)
        arcade.draw_arc_outline(
            left_penalty_spot_x,
            left_penalty_spot_y,
            penalty_arc_radius * 2,
            penalty_arc_radius * 2,
            arcade.color.WHITE,
            -52.5,  # Start angle (top-left)
            52.5,   # End angle (top-right)
            border_width=4,
            tilt_angle=0
        )
        
        # Right penalty arc (only the part above the penalty area)
        right_penalty_spot_x = self.dimensions.x_offset + self.dimensions.width - penalty_spot_distance
        right_penalty_spot_y = self.dimensions.y_offset + self.dimensions.height // 2
        
        # Draw arc from 127.5 to 232.5 degrees (only the top portion above penalty area)
        arcade.draw_arc_outline(
            right_penalty_spot_x,
            right_penalty_spot_y,
            penalty_arc_radius * 2,
            penalty_arc_radius * 2,
            arcade.color.WHITE,
            130,  # Start angle (top-left)
            232.5,  # End angle (top-right)
            border_width=4,
            tilt_angle=0
        )
    
    def _draw_penalty_spots(self):
        """Draw the penalty spots (11m from goal line)"""
        penalty_spot_distance = int(self.dimensions.width * 11 / 105)  # ~73px from goal line
        
        # Left penalty spot
        arcade.draw_circle_filled(
            self.dimensions.x_offset + penalty_spot_distance,
            self.dimensions.y_offset + self.dimensions.height // 2,
            3,
            arcade.color.WHITE
        )
        
        # Right penalty spot
        arcade.draw_circle_filled(
            self.dimensions.x_offset + self.dimensions.width - penalty_spot_distance,
            self.dimensions.y_offset + self.dimensions.height // 2,
            3,
            arcade.color.WHITE
        )
    
    def _draw_goal_posts(self):
        """Draw the goal posts (7.32m wide, 2.44m high)"""
        goal_width = int(self.dimensions.width * 7.32 / 105)  # ~49px
        goal_height = int(self.dimensions.height * 2.44 / 68)  # ~16px
        
        # Left goal
        arcade.draw_rectangle_outline(
            self.dimensions.x_offset - goal_height // 2,  # Position goal slightly outside field
            self.dimensions.y_offset + self.dimensions.height // 2,
            goal_height,  # Width (thickness of goal post)
            goal_width,   # Height (width of goal opening)
            arcade.color.WHITE,
            border_width=2
        )
        
        # Right goal
        arcade.draw_rectangle_outline(
            self.dimensions.x_offset + self.dimensions.width + goal_height // 2,  # Position goal slightly outside field
            self.dimensions.y_offset + self.dimensions.height // 2,
            goal_height,  # Width (thickness of goal post)
            goal_width,   # Height (width of goal opening)
            arcade.color.WHITE,
            border_width=2
        )
    
    def normalize_to_screen(self, normalized_x: float, normalized_y: float) -> tuple:
        """Convert normalized coordinates (0-1) to screen coordinates"""
        screen_x = self.dimensions.x_offset + normalized_x * self.dimensions.width
        screen_y = self.dimensions.y_offset + normalized_y * self.dimensions.height
        return screen_x, screen_y
