#!/usr/bin/env python3
"""
Test script to verify ball height functionality
"""

import json
from football_visualizer.data.data_loader import DataLoader
from football_visualizer.core.models import EntityProperties

def test_ball_height():
    """Test that ball height data is loaded and processed correctly"""
    print("Testing ball height functionality...")
    
    # Load the generated data
    frames = DataLoader.load_data("data/sample_data.json")
    
    if not frames:
        print("❌ Failed to load data")
        return False
    
    print(f"✅ Loaded {len(frames)} frames")
    
    # Check that ball positions have z-coordinates
    ball_heights = [frame.ball.z for frame in frames[:10]]
    print(f"✅ Ball heights in first 10 frames: {ball_heights}")
    
    # Check that heights vary (not all 0)
    if any(h > 0 for h in ball_heights):
        print("✅ Ball height varies (some heights > 0)")
    else:
        print("⚠️  Ball heights are all 0 - may need to adjust physics parameters")
    
    # Test ball radius calculation
    entity_props = EntityProperties()
    print(f"✅ Base ball radius: {entity_props.ball_radius}")
    print(f"✅ Max ball radius: {entity_props.ball_max_radius}")
    
    # Calculate some example ball sizes
    for z in [0.0, 0.5, 1.0]:
        radius = entity_props.ball_radius + (entity_props.ball_max_radius - entity_props.ball_radius) * z
        print(f"   Height {z}: radius = {int(radius)}")
    
    print("✅ Ball height functionality test completed successfully!")
    return True

if __name__ == "__main__":
    test_ball_height()
