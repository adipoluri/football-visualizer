# Football Visualizer Package Structure

This document describes the organized package structure of the football visualizer application.

## Directory Structure

```
football-visualizer/
├── football_visualizer/           # Main package directory
│   ├── __init__.py               # Package initialization and exports
│   ├── main.py                   # Main application class
│   ├── core/                     # Core business logic and data models
│   │   ├── __init__.py
│   │   ├── models.py             # Data structures and configuration
│   │   └── playback_controller.py # Playback logic and controls
│   ├── rendering/                # All rendering components
│   │   ├── __init__.py
│   │   ├── pitch_renderer.py     # Football field rendering
│   │   └── entity_renderer.py    # Player and ball rendering
│   ├── data/                     # Data management
│   │   ├── __init__.py
│   │   └── data_loader.py        # Data loading and validation
│   └── ui/                       # User interface
│       ├── __init__.py
│       └── ui_renderer.py        # UI elements and controls
├── main.py                       # Command-line entry point
├── setup.py                      # Package installation script
├── requirements.txt              # Dependencies
├── README.md                     # Project documentation
├── ARCHITECTURE.md               # Architecture documentation
├── PACKAGE_STRUCTURE.md          # This file
├── football_visualizer.py        # Original monolithic version
├── generate_sample_data.py       # Sample data generator
├── test_visualizer.py           # Test suite
└── sample_data.json             # Sample position data
```

## Package Organization

### **Core Module (`football_visualizer/core/`)**
Contains fundamental business logic and data structures.

- **`models.py`**: Data structures, enums, and configuration classes
- **`playback_controller.py`**: Playback logic, timing, and state management

**Purpose**: Core business logic that doesn't depend on external libraries.

### **Rendering Module (`football_visualizer/rendering/`)**
Contains all visual rendering components.

- **`pitch_renderer.py`**: Football field and markings rendering
- **`entity_renderer.py`**: Players and ball rendering with interpolation

**Purpose**: All visual rendering logic separated from business logic.

### **Data Module (`football_visualizer/data/`)**
Contains data management and I/O operations.

- **`data_loader.py`**: JSON file loading, parsing, and validation

**Purpose**: Data persistence and external data format handling.

### **UI Module (`football_visualizer/ui/`)**
Contains user interface components.

- **`ui_renderer.py`**: UI elements, status displays, and controls

**Purpose**: User interface rendering and interaction.

### **Main Application (`football_visualizer/main.py`)**
The main application class that orchestrates all components.

**Purpose**: Application lifecycle and component coordination.

## Benefits of Package Structure

### **1. Logical Organization**
- Related functionality is grouped together
- Clear separation of concerns
- Easy to locate specific functionality

### **2. Scalability**
- Easy to add new modules to appropriate subdirectories
- Clear boundaries for new features
- Supports team development

### **3. Maintainability**
- Each module has a focused responsibility
- Changes are isolated to specific areas
- Easy to understand and modify

### **4. Reusability**
- Components can be imported individually
- Clear public APIs through `__init__.py` files
- Easy to use in other projects

### **5. Testing**
- Each module can be tested independently
- Clear test boundaries
- Easy to mock dependencies

## Import Patterns

### **Internal Package Imports**
```python
# Within the package
from .core import Position, Frame
from .rendering import PitchRenderer
from .data import DataLoader
```

### **External Package Imports**
```python
# From outside the package
from football_visualizer import FootballVisualizer
from football_visualizer.core import Position, Frame
from football_visualizer.rendering import PitchRenderer
```

### **Relative Imports**
```python
# Within submodules
from ..core.models import Frame, Position
from .pitch_renderer import PitchRenderer
```

## Usage Examples

### **Basic Usage**
```python
from football_visualizer import FootballVisualizer

app = FootballVisualizer("data.json")
app.run()
```

### **Component-Level Usage**
```python
from football_visualizer.core import Position, Frame, PlaybackController
from football_visualizer.rendering import PitchRenderer, EntityRenderer
from football_visualizer.data import DataLoader

# Load data
frames = DataLoader.load_data("data.json")

# Create components
pitch_renderer = PitchRenderer()
playback_controller = PlaybackController(frames)
```

### **Command Line Usage**
```bash
# Run the application
python main.py sample_data.json

# Install as package
pip install -e .

# Run as installed command
football-visualizer sample_data.json
```

## Development Guidelines

### **Adding New Features**
1. **Core Logic**: Add to `core/` module
2. **Rendering**: Add to `rendering/` module  
3. **Data**: Add to `data/` module
4. **UI**: Add to `ui/` module

### **Module Dependencies**
- **Core**: No external dependencies (pure Python)
- **Rendering**: Depends on `core` and `arcade`
- **Data**: Depends on `core` and standard library
- **UI**: Depends on `core` and `arcade`
- **Main**: Depends on all modules

### **Testing Strategy**
- Unit tests for each module
- Integration tests for component interactions
- End-to-end tests for complete workflows

## Migration from Flat Structure

The package structure is backward compatible:

1. **Original files**: Still available in root directory
2. **New structure**: Available through package imports
3. **Gradual migration**: Can migrate incrementally
4. **Same functionality**: No behavioral changes

## Future Enhancements

The package structure supports easy addition of:

- **New rendering engines**: Add to `rendering/`
- **Additional data formats**: Add to `data/`
- **Advanced UI components**: Add to `ui/`
- **Plugin system**: Add to `core/`
- **Configuration management**: Add to `core/`

This organized structure provides a solid foundation for the football visualizer's continued development and maintenance.
