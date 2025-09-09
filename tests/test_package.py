#!/usr/bin/env python3
"""
Test script to verify the package structure works correctly.

This script tests that all modules can be imported and basic functionality works.
"""

import sys
import os

def test_imports():
    """Test that all package components can be imported"""
    print("Testing package imports...")
    
    try:
        # Test main package import
        from football_visualizer import FootballVisualizer
        print("✅ Main package import successful")
        
        # Test core module imports
        from football_visualizer.core import Position, Frame, PlaybackState
        from football_visualizer.core import PitchDimensions, EntityProperties, PlaybackConfig
        from football_visualizer.core import PlaybackController
        print("✅ Core module imports successful")
        
        # Test rendering module imports
        from football_visualizer.rendering import PitchRenderer, EntityRenderer
        print("✅ Rendering module imports successful")
        
        # Test data module imports
        from football_visualizer.data import DataLoader
        print("✅ Data module imports successful")
        
        # Test UI module imports
        from football_visualizer.ui import UIRenderer
        print("✅ UI module imports successful")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality of package components"""
    print("\nTesting basic functionality...")
    
    try:
        from football_visualizer.core import Position, Frame, PitchDimensions
        from football_visualizer.data import DataLoader
        
        # Test Position creation
        pos = Position(0.5, 0.5)
        assert pos.x == 0.5 and pos.y == 0.5
        print("✅ Position creation works")
        
        # Test PitchDimensions
        dims = PitchDimensions()
        assert dims.width == 800 and dims.height == 520
        print("✅ PitchDimensions works")
        
        # Test DataLoader (with non-existent file)
        frames = DataLoader.load_data("nonexistent.json")
        assert frames == []
        print("✅ DataLoader error handling works")
        
        return True
        
    except Exception as e:
        print(f"❌ Functionality test error: {e}")
        return False

def test_package_structure():
    """Test that package structure is correct"""
    print("\nTesting package structure...")
    
    try:
        import football_visualizer
        
        # Check that main components are available
        assert hasattr(football_visualizer, 'FootballVisualizer')
        assert hasattr(football_visualizer, 'Position')
        assert hasattr(football_visualizer, 'Frame')
        assert hasattr(football_visualizer, 'PitchRenderer')
        assert hasattr(football_visualizer, 'DataLoader')
        print("✅ Package structure is correct")
        
        return True
        
    except Exception as e:
        print(f"❌ Package structure test error: {e}")
        return False

def main():
    """Run all tests"""
    print("Football Visualizer Package Test")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_basic_functionality,
        test_package_structure
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All package tests passed! The package structure is working correctly.")
        return 0
    else:
        print("❌ Some tests failed. Please check the package structure.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
