"""
Sample Data Generator for Football Visualizer

Generates realistic football match position data for testing the visualizer.
Creates 22 players (11 per team) and a ball with realistic movement patterns.
"""

import json
import math
import random
from typing import List, Tuple


def generate_football_data(duration_seconds: float = 10.0, fps: float = 30.0) -> List[dict]:
    """
    Generate realistic football position data
    
    Args:
        duration_seconds: Duration of the match in seconds
        fps: Frames per second for the data
    
    Returns:
        List of frame data dictionaries
    """
    frames = []
    total_frames = int(duration_seconds * fps)
    
    # Initialize positions
    # Team 1 (left side, blue) - 11 players
    team1_positions = [
        (0.1, 0.1), (0.15, 0.1), (0.2, 0.1), (0.25, 0.1), (0.3, 0.1),  # Defense
        (0.1, 0.3), (0.15, 0.3), (0.2, 0.3), (0.25, 0.3), (0.3, 0.3),  # Midfield
        (0.1, 0.5)   # Forward
    ]
    
    # Team 2 (right side, red) - 11 players
    team2_positions = [
        (0.9, 0.1), (0.85, 0.1), (0.8, 0.1), (0.75, 0.1), (0.7, 0.1),  # Defense
        (0.9, 0.3), (0.85, 0.3), (0.8, 0.3), (0.75, 0.3), (0.7, 0.3),  # Midfield
        (0.9, 0.5)   # Forward
    ]
    
    # Ball starts in center at ground level
    ball_pos = (0.5, 0.5, 0.0)  # (x, y, z)
    
    # Movement parameters
    ball_speed = 0.02
    player_speed = 0.01
    ball_direction = random.uniform(0, 2 * math.pi)
    ball_height = 0.0  # Current height (0.0 = ground, 1.0 = max height)
    ball_velocity_z = 0.0  # Vertical velocity
    
    for frame in range(total_frames):
        time = frame / fps
        
        # Update ball position with some randomness
        if frame > 0:
            # Add some randomness to ball movement
            ball_direction += random.uniform(-0.1, 0.1)
            ball_x = ball_pos[0] + ball_speed * math.cos(ball_direction)
            ball_y = ball_pos[1] + ball_speed * math.sin(ball_direction)
            
            # Keep ball within bounds
            ball_x = max(0.05, min(0.95, ball_x))
            ball_y = max(0.05, min(0.95, ball_y))
            
            # Update ball height with physics simulation
            # Add gravity and random kicks
            gravity = -0.02  # Gravity pulls ball down
            ball_velocity_z += gravity
            
            # Random chance for ball to be kicked up (simulating headers, kicks, etc.)
            if random.random() < 0.05:  # 5% chance per frame
                ball_velocity_z = random.uniform(0.1, 0.3)  # Kick the ball up
            
            # Update height
            ball_height += ball_velocity_z
            
            # Keep ball above ground
            if ball_height < 0.0:
                ball_height = 0.0
                ball_velocity_z = 0.0
            
            # Cap maximum height
            if ball_height > 1.0:
                ball_height = 1.0
                ball_velocity_z = 0.0
            
            ball_pos = (ball_x, ball_y, ball_height)
        
        # Update player positions with slight movement
        if frame > 0:
            new_team1_positions = []
            for x, y in team1_positions:
                # Players move slightly towards ball or maintain formation
                dx = (ball_pos[0] - x) * 0.01 + random.uniform(-0.005, 0.005)
                dy = (ball_pos[1] - y) * 0.01 + random.uniform(-0.005, 0.005)
                
                new_x = max(0.05, min(0.45, x + dx))
                new_y = max(0.05, min(0.95, y + dy))
                new_team1_positions.append((new_x, new_y))
            team1_positions = new_team1_positions
            
            new_team2_positions = []
            for x, y in team2_positions:
                # Players move slightly towards ball or maintain formation
                dx = (ball_pos[0] - x) * 0.01 + random.uniform(-0.005, 0.005)
                dy = (ball_pos[1] - y) * 0.01 + random.uniform(-0.005, 0.005)
                
                new_x = max(0.55, min(0.95, x + dx))
                new_y = max(0.05, min(0.95, y + dy))
                new_team2_positions.append((new_x, new_y))
            team2_positions = new_team2_positions
        
        # Combine all players
        all_players = team1_positions + team2_positions
        
        # Create frame data
        frame_data = {
            "time": time,
            "ball": [ball_pos[0], ball_pos[1], ball_pos[2]],  # Include z-coordinate
            "players": [[pos[0], pos[1]] for pos in all_players]
        }
        
        frames.append(frame_data)
    
    return frames


def main():
    """Generate sample data and save to file"""
    print("Generating football position data...")
    
    # Generate 30 seconds of data at 30 FPS
    data = generate_football_data(duration_seconds=30.0, fps=30.0)
    
    # Save to file
    with open("sample_data.json", "w") as f:
        json.dump(data, f, indent=2)
    
    print(f"Generated {len(data)} frames of data")
    print("Saved to sample_data.json")
    print("\nTo run the visualizer:")
    print("python football_visualizer.py sample_data.json")


if __name__ == "__main__":
    main()

