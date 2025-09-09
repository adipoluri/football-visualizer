#!/usr/bin/env python3
"""
Football Visualizer - Main Entry Point

This is the main entry point for the football visualizer application.
It provides a command-line interface for running the visualizer with
position data files.

Usage:
    python main.py <data_file.json>
    python main.py sample_data.json

Examples:
    python main.py sample_data.json
    python main.py match_data.json
"""

import sys
import arcade
from football_visualizer import FootballVisualizer


def main():
    """Main entry point for the football visualizer application"""
    if len(sys.argv) != 2:
        print("Football Visualizer")
        print("=" * 50)
        print("Usage: python main.py <data_file.json>")
        print("")
        print("Examples:")
        print("  python main.py sample_data.json")
        print("  python main.py match_data.json")
        print("")
        print("Controls:")
        print("  SPACE: Play/Pause")
        print("  R: Restart")
        print("  ←/→: Step (Hold for FF/RW)")
        return 1
    
    data_file = sys.argv[1]
    
    try:
        print(f"Starting Football Visualizer with data: {data_file}")
        app = FootballVisualizer(data_file)
        arcade.run()
        return 0
    except FileNotFoundError:
        print(f"Error: Could not find data file '{data_file}'")
        print("Make sure the file exists and the path is correct.")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
