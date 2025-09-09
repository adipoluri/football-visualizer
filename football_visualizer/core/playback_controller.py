"""
Playback controller module for the football visualizer.

This module handles all playback logic including play/pause, fast forward,
rewind, and frame-by-frame navigation with proper timing and buffering.
"""

from typing import List
from .models import Frame, PlaybackState, PlaybackConfig


class PlaybackController:
    """Handles all playback control logic and state management"""
    
    def __init__(self, frames: List[Frame], config: PlaybackConfig):
        self.frames = frames
        self.config = config
        
        # Playback state
        self.current_frame_index = 0
        self.playback_state = PlaybackState.PAUSED
        self.last_data_update = 0.0
        self.frame_duration = 1.0 / self.config.data_fps
        self.interpolation_factor = 0.0
        
        # Fast forward/rewind state
        self.is_fast_forwarding = False
        self.is_rewinding = False
        
        # Key press buffer state
        self.left_key_pressed = False
        self.right_key_pressed = False
        self.left_key_press_time = 0.0
        self.right_key_press_time = 0.0
    
    def update(self, delta_time: float):
        """Update playback state and handle timing"""
        if not self.frames:
            return
        
        # Update key press timing
        self._update_key_timing(delta_time)
        
        # Check if we should start continuous fast forward/rewind
        self._check_continuous_playback()
        
        # Handle different playback modes
        self._handle_playback_modes(delta_time)
        
        # Update interpolation factor for smooth rendering
        self.interpolation_factor = self.last_data_update / self.frame_duration
    
    def _update_key_timing(self, delta_time: float):
        """Update timing for key press buffering"""
        if self.left_key_pressed:
            self.left_key_press_time += delta_time
        if self.right_key_pressed:
            self.right_key_press_time += delta_time
    
    def _check_continuous_playback(self):
        """Check if we should start continuous fast forward/rewind"""
        if (self.left_key_pressed and 
            self.left_key_press_time >= self.config.key_press_buffer_time and 
            not self.is_fast_forwarding):
            self.is_rewinding = True
            self.playback_state = PlaybackState.PAUSED
            self.last_data_update = 0.0
        
        if (self.right_key_pressed and 
            self.right_key_press_time >= self.config.key_press_buffer_time and 
            not self.is_rewinding):
            self.is_fast_forwarding = True
            self.playback_state = PlaybackState.PAUSED
            self.last_data_update = 0.0
    
    def _handle_playback_modes(self, delta_time: float):
        """Handle different playback modes (normal, fast forward, rewind)"""
        if self.is_fast_forwarding:
            self._handle_fast_forward(delta_time)
        elif self.is_rewinding:
            self._handle_rewind(delta_time)
        elif self.playback_state == PlaybackState.PLAYING:
            self._handle_normal_playback(delta_time)
    
    def _handle_fast_forward(self, delta_time: float):
        """Handle fast forward playback"""
        self.last_data_update += delta_time * self.config.fast_forward_speed
        if self.last_data_update >= self.frame_duration:
            self.last_data_update = 0.0
            if self.current_frame_index < len(self.frames) - 1:
                self.current_frame_index += 1
            else:
                # End of replay, stop fast forwarding
                self.is_fast_forwarding = False
                self.playback_state = PlaybackState.PAUSED
    
    def _handle_rewind(self, delta_time: float):
        """Handle rewind playback"""
        self.last_data_update += delta_time * self.config.rewind_speed
        if self.last_data_update >= self.frame_duration:
            self.last_data_update = 0.0
            if self.current_frame_index > 0:
                self.current_frame_index -= 1
            else:
                # Beginning of replay, stop rewinding
                self.is_rewinding = False
                self.playback_state = PlaybackState.PAUSED
    
    def _handle_normal_playback(self, delta_time: float):
        """Handle normal playback at configured FPS"""
        self.last_data_update += delta_time
        if self.last_data_update >= self.frame_duration:
            self.last_data_update = 0.0
            if self.current_frame_index < len(self.frames) - 1:
                self.current_frame_index += 1
            else:
                # End of replay, pause
                self.playback_state = PlaybackState.PAUSED
    
    def toggle_play_pause(self):
        """Toggle between play and pause states"""
        if self.playback_state == PlaybackState.PLAYING:
            self.playback_state = PlaybackState.PAUSED
        else:
            self.playback_state = PlaybackState.PLAYING
            self.last_data_update = 0.0
    
    def restart(self):
        """Restart playback from the beginning"""
        self.current_frame_index = 0
        self.playback_state = PlaybackState.PAUSED
        self.last_data_update = 0.0
        self.interpolation_factor = 0.0
        self.is_fast_forwarding = False
        self.is_rewinding = False
        self._reset_key_states()
    
    def step_backward(self):
        """Step backward one frame"""
        if self.current_frame_index > 0:
            self.current_frame_index -= 1
            self.playback_state = PlaybackState.PAUSED
            self.interpolation_factor = 0.0
    
    def step_forward(self):
        """Step forward one frame"""
        if self.current_frame_index < len(self.frames) - 1:
            self.current_frame_index += 1
            self.playback_state = PlaybackState.PAUSED
            self.interpolation_factor = 0.0
    
    def start_left_key_press(self):
        """Handle left key press (start rewind or step back)"""
        self.left_key_pressed = True
        self.left_key_press_time = 0.0
        self.is_fast_forwarding = False
        self.playback_state = PlaybackState.PAUSED
        self.last_data_update = 0.0
        
        # Single step backward immediately
        self.step_backward()
    
    def start_right_key_press(self):
        """Handle right key press (start fast forward or step forward)"""
        self.right_key_pressed = True
        self.right_key_press_time = 0.0
        self.is_rewinding = False
        self.playback_state = PlaybackState.PAUSED
        self.last_data_update = 0.0
        
        # Single step forward immediately
        self.step_forward()
    
    def release_left_key(self):
        """Handle left key release"""
        self.is_rewinding = False
        self.left_key_pressed = False
        self.left_key_press_time = 0.0
    
    def release_right_key(self):
        """Handle right key release"""
        self.is_fast_forwarding = False
        self.right_key_pressed = False
        self.right_key_press_time = 0.0
    
    def _reset_key_states(self):
        """Reset all key press states"""
        self.left_key_pressed = False
        self.right_key_pressed = False
        self.left_key_press_time = 0.0
        self.right_key_press_time = 0.0
    
    def get_current_frame(self) -> Frame:
        """Get the current frame being displayed"""
        if not self.frames or self.current_frame_index >= len(self.frames):
            return None
        return self.frames[self.current_frame_index]
    
    def get_next_frame(self) -> Frame:
        """Get the next frame for interpolation"""
        if (not self.frames or 
            self.current_frame_index >= len(self.frames) - 1 or
            self.playback_state != PlaybackState.PLAYING):
            return None
        return self.frames[self.current_frame_index + 1]
    
    def get_playback_info(self) -> dict:
        """Get current playback information for UI display"""
        return {
            'current_frame': self.current_frame_index + 1,
            'total_frames': len(self.frames),
            'time': self.frames[self.current_frame_index].time if self.frames else 0.0,
            'state': self.playback_state.value.upper(),
            'is_fast_forwarding': self.is_fast_forwarding,
            'is_rewinding': self.is_rewinding,
            'fast_forward_speed': self.config.fast_forward_speed,
            'rewind_speed': self.config.rewind_speed
        }
