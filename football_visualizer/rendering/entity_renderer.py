"""
Entity rendering module for the football visualizer.

This module handles rendering of players and the ball with proper
interpolation for smooth animation.
"""

import arcade
from typing import List, Tuple
from ..core.models import Frame, EntityProperties
from .pitch_renderer import PitchRenderer


class EntityRenderer:
    """Handles rendering of players and ball entities"""
    
    def __init__(self, pitch_renderer: PitchRenderer, entity_props: EntityProperties):
        self.pitch_renderer = pitch_renderer
        self.entity_props = entity_props
    
    def draw_entities(self, current_frame: Frame, next_frame: Frame = None, 
                     interpolation_factor: float = 0.0, is_playing: bool = False):
        """Draw all entities (players and ball) with interpolation"""
        if not current_frame:
            return
        
        # Get interpolated positions
        ball_pos, player_positions = self._get_interpolated_positions(
            current_frame, next_frame, interpolation_factor, is_playing
        )
        
        # Draw ball
        self._draw_ball(ball_pos)
        
        # Draw players
        self._draw_players(player_positions)
    
    def _get_interpolated_positions(self, current_frame: Frame, next_frame: Frame = None,
                                  interpolation_factor: float = 0.0, is_playing: bool = False) -> Tuple[Tuple[float, float, float], List[Tuple[float, float]]]:
        """Calculate interpolated positions for smooth animation"""
        if is_playing and next_frame:
            # Interpolate ball position (including z-coordinate)
            ball_x = self._interpolate(current_frame.ball.x, next_frame.ball.x, interpolation_factor)
            ball_y = self._interpolate(current_frame.ball.y, next_frame.ball.y, interpolation_factor)
            ball_z = self._interpolate(current_frame.ball.z, next_frame.ball.z, interpolation_factor)
            
            # Interpolate player positions
            player_positions = []
            for curr_pos, next_pos in zip(current_frame.players, next_frame.players):
                x = self._interpolate(curr_pos.x, next_pos.x, interpolation_factor)
                y = self._interpolate(curr_pos.y, next_pos.y, interpolation_factor)
                player_positions.append((x, y))
        else:
            # Use current frame positions
            ball_x = current_frame.ball.x
            ball_y = current_frame.ball.y
            ball_z = current_frame.ball.z
            player_positions = [(p.x, p.y) for p in current_frame.players]
        
        return (ball_x, ball_y, ball_z), player_positions
    
    def _interpolate(self, start: float, end: float, factor: float) -> float:
        """Interpolate between two values using the interpolation factor"""
        return start + (end - start) * factor
    
    def _draw_ball(self, ball_pos: Tuple[float, float, float]):
        """Draw the ball as a white circle with size based on height"""
        ball_x, ball_y, ball_z = ball_pos
        screen_x, screen_y = self.pitch_renderer.normalize_to_screen(ball_x, ball_y)
        
        # Calculate ball radius based on height (z-value)
        # When z=0 (ground), use base radius; when z=1 (max height), use max radius
        ball_radius = self.entity_props.ball_radius + (self.entity_props.ball_max_radius - self.entity_props.ball_radius) * ball_z
        
        arcade.draw_circle_filled(
            screen_x,
            screen_y,
            int(ball_radius),
            arcade.color.WHITE
        )
    
    def _draw_players(self, player_positions: List[Tuple[float, float]]):
        """Draw all players with team colors, borders, and numbers"""
        for i, (x, y) in enumerate(player_positions):
            screen_x, screen_y = self.pitch_renderer.normalize_to_screen(x, y)
            
            # Determine team color (first 11 players are team 1, next 11 are team 2)
            team_index = 0 if i < 11 else 1
            color = self.entity_props.team_colors[team_index]
            
            # Draw player circle
            arcade.draw_circle_filled(
                screen_x,
                screen_y,
                self.entity_props.player_radius,
                color
            )
            
            # Draw player border
            arcade.draw_circle_outline(
                screen_x,
                screen_y,
                self.entity_props.player_radius,
                arcade.color.WHITE,
                border_width=2
            )
            
            # Draw player number
            player_num = (i % 11) + 1
            arcade.draw_text(
                str(player_num),
                screen_x,
                screen_y,
                arcade.color.WHITE,
                font_size=14,
                font_name="Kenney Pixel",
                bold=True,
                anchor_x="center",
                anchor_y="center"
            )
