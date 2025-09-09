"""
Football Visualizer Package

A modular Python application for visualizing football match replays with
timestamped position data using the Arcade library.

This package provides a clean, maintainable architecture with separated
concerns for rendering, playback control, and data management.

Modules:
- models: Data structures and configuration
- pitch_renderer: Football field rendering
- entity_renderer: Player and ball rendering
- playback_controller: Playback logic and controls
- ui_renderer: User interface elements
- data_loader: Data loading and validation

Usage:
    from football_visualizer import FootballVisualizer
    app = FootballVisualizer("data.json")
    app.run()
"""

# Core components
from .core import (
    Position,
    Frame,
    PlaybackState,
    PitchDimensions,
    EntityProperties,
    PlaybackConfig,
    PlaybackController
)

# Rendering components
from .rendering import (
    PitchRenderer,
    EntityRenderer
)

# Data components
from .data import DataLoader

# UI components
from .ui import UIRenderer

# Main application class
from .main import FootballVisualizer

__version__ = "1.0.0"
__author__ = "Aditya Poluri"

__all__ = [
    # Data models
    "Position",
    "Frame", 
    "PlaybackState",
    "PitchDimensions",
    "EntityProperties",
    "PlaybackConfig",
    
    # Components
    "PitchRenderer",
    "EntityRenderer", 
    "PlaybackController",
    "UIRenderer",
    "DataLoader",
    
    # Main application
    "FootballVisualizer"
]
