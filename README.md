# Football Replay Visualizer

A Python application using the Arcade library to visualize football match replays with timestamped position data. The visualizer supports smooth 30 FPS data playback with 60 FPS interpolation for fluid rendering.

## Features

- **Real-time Visualization**: Displays 22 players (11 per team) and a ball on a football pitch
- **Smooth Animation**: 30 FPS data updates with 60 FPS interpolation for seamless motion
- **Interactive Controls**: Play/pause, restart, and frame-by-frame navigation
- **Realistic Pitch**: Complete football field with center line, center circle, and goal boxes
- **Team Differentiation**: Blue and red teams with player numbers
- **Performance Optimized**: Designed to run smoothly at 60 FPS

## Requirements

- Python 3.7+
- Arcade library

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Visualizer

```bash
python football_visualizer.py <data_file.json>
```

Example:
```bash
python football_visualizer.py sample_data.json
```

### Generating Sample Data

To generate sample position data for testing:

```bash
python generate_sample_data.py
```

This creates a `sample_data.json` file with 30 seconds of realistic football match data.

## Controls

- **SPACE**: Play/Pause the replay
- **R**: Restart the replay from the beginning
- **Left Arrow**: Step backward one frame
- **Right Arrow**: Step forward one frame

## Data Format

The visualizer expects JSON data in the following format:

```json
[
  {
    "time": 0.0,
    "ball": [0.5, 0.5],
    "players": [
      [0.1, 0.1], [0.2, 0.1], [0.3, 0.1], [0.4, 0.1], [0.5, 0.1],
      [0.1, 0.2], [0.2, 0.2], [0.3, 0.2], [0.4, 0.2], [0.5, 0.2],
      [0.1, 0.3],
      [0.9, 0.1], [0.8, 0.1], [0.7, 0.1], [0.6, 0.1], [0.5, 0.1],
      [0.9, 0.2], [0.8, 0.2], [0.7, 0.2], [0.6, 0.2], [0.5, 0.2],
      [0.9, 0.3]
    ]
  }
]
```

### Data Structure

- **time**: Timestamp in seconds (float)
- **ball**: Ball position as [x, y] coordinates (normalized 0-1)
- **players**: List of 22 player positions as [x, y] coordinates (normalized 0-1)
  - First 11 players: Team 1 (blue)
  - Last 11 players: Team 2 (red)

### Coordinate System

- Coordinates are normalized (0.0 to 1.0)
- (0, 0) is the bottom-left corner of the pitch
- (1, 1) is the top-right corner of the pitch
- (0.5, 0.5) is the center of the pitch

## Technical Details

### Performance

- **Rendering**: 60 FPS for smooth display
- **Data Updates**: 30 FPS for position data
- **Interpolation**: Linear interpolation between data frames
- **Optimized**: Efficient rendering for 22 players + 1 ball

### Architecture

- **Main Class**: `FootballVisualizer` extends `arcade.Window`
- **Data Models**: `Position`, `Frame` dataclasses
- **State Management**: `PlaybackState` enum
- **Interpolation**: Smooth position interpolation between frames

## File Structure

```
football-visualizer/
├── football_visualizer.py    # Main application
├── generate_sample_data.py   # Sample data generator
├── sample_data.json         # Sample position data
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## Customization

### Pitch Appearance

Modify the `draw_pitch()` method to change:
- Field dimensions
- Line colors and thickness
- Goal box sizes
- Center circle radius

### Player Appearance

Modify the `draw_entities()` method to change:
- Player circle sizes
- Team colors
- Player number display
- Ball appearance

### Performance Tuning

Adjust these parameters in the `__init__` method:
- `self.set_update_rate(1/60)`: Rendering FPS
- `self.data_fps = 30.0`: Data update FPS
- `self.player_radius`: Player circle size
- `self.ball_radius`: Ball circle size

## Troubleshooting

### Common Issues

1. **"No data available" message**: Check that the JSON file exists and has valid data
2. **Poor performance**: Reduce the number of players or lower the rendering FPS
3. **Invalid JSON error**: Ensure the data file follows the correct format

### Performance Tips

- Use normalized coordinates (0-1) for better performance
- Keep data files reasonably sized (< 1000 frames for smooth playback)
- Close other applications to free up system resources

## License

This project is open source. See the LICENSE file for details.