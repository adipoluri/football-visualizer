"""
Data loading module for the football visualizer.

This module handles loading and parsing of JSON position data files
and converting them into Frame objects.
"""

import json
from typing import List
from ..core.models import Frame, Position, BallPosition


class DataLoader:
    """Handles loading and parsing of position data files"""
    
    @staticmethod
    def load_data(data_file: str) -> List[Frame]:
        """
        Load position data from JSON file
        
        Args:
            data_file: Path to the JSON data file
            
        Returns:
            List of Frame objects containing position data
            
        Raises:
            FileNotFoundError: If the data file doesn't exist
            json.JSONDecodeError: If the JSON is invalid
            KeyError: If required fields are missing
        """
        try:
            with open(data_file, 'r') as f:
                data = json.load(f)
            
            frames = []
            for frame_data in data:
                # Handle both old format (2D) and new format (3D) ball positions
                if len(frame_data['ball']) == 3:
                    ball_pos = BallPosition(frame_data['ball'][0], frame_data['ball'][1], frame_data['ball'][2])
                else:
                    # Fallback for old format - assume ground level
                    ball_pos = BallPosition(frame_data['ball'][0], frame_data['ball'][1], 0.0)
                
                players = [Position(p[0], p[1]) for p in frame_data['players']]
                frame = Frame(frame_data['time'], ball_pos, players)
                frames.append(frame)
            
            print(f"Loaded {len(frames)} frames from {data_file}")
            return frames
            
        except FileNotFoundError:
            print(f"Error: Could not find data file {data_file}")
            return []
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in data file - {e}")
            return []
        except KeyError as e:
            print(f"Error: Missing required field in data - {e}")
            return []
    
    @staticmethod
    def validate_data(frames: List[Frame]) -> bool:
        """
        Validate that the loaded data is correct
        
        Args:
            frames: List of Frame objects to validate
            
        Returns:
            True if data is valid, False otherwise
        """
        if not frames:
            return False
        
        # Check first few frames for data integrity
        for i, frame in enumerate(frames[:5]):
            if len(frame.players) != 22:
                print(f"Error: Frame {i} has {len(frame.players)} players, expected 22")
                return False
            
            if not (0 <= frame.ball.x <= 1 and 0 <= frame.ball.y <= 1 and 0 <= frame.ball.z <= 1):
                print(f"Error: Frame {i} ball position out of bounds: ({frame.ball.x}, {frame.ball.y}, {frame.ball.z})")
                return False
            
            for j, player in enumerate(frame.players):
                if not (0 <= player.x <= 1 and 0 <= player.y <= 1):
                    print(f"Error: Frame {i} player {j} position out of bounds: ({player.x}, {player.y})")
                    return False
        
        return True
