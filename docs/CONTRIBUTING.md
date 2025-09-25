# Contributing to Desarticulator

Thank you for your interest in contributing to Desarticulator! This guide will help you get started.

## Development Setup

### Prerequisites
- Python 3.7+
- midiutil library
- Git

### Getting Started
```bash
git clone <repository-url>
cd desarticulator
pip install midiutil
```

## Adding New Drum Styles

### 1. Create Style Module
Create a new file in `styles/[style_name].py`:

```python
from midiutil import MIDIFile
import random

def create_[style]_groove():
    # Implementation following the template
    pass
```

### 2. Follow the Template Structure
Every style should include:
- `add_basic_pattern()` - Core rhythm
- `add_variation_1()` - First variation
- `add_fill_simple()` - Simple transitions
- `add_fill_complex()` - Complex fills
- `add_final_fill()` - Epic ending

### 3. Create Example Generator
Create `examples/generate_[style]_file.py`:

```python
from styles.[style] import create_[style]_groove

def main():
    midi = create_[style]_groove()
    with open("[Style]150bars.mid", "wb") as f:
        midi.writeFile(f)

if __name__ == "__main__":
    main()
```

### 4. Update Documentation
- Add style to `styles/__init__.py`
- Update README.md with new style info
- Document style characteristics

## Code Style Guidelines

### General Rules
- No Spanish comments or variable names
- Use English for all documentation
- Follow PEP 8 for Python code style
- No inline comments in generated code

### Naming Conventions
```python
# Functions: snake_case
def add_basic_pattern():

# Variables: snake_case
kick_velocity = 95

# Constants: UPPER_CASE
TICKS_PER_BEAT = 480

# Files: lowercase with underscores
punk_rock.py
```

### MIDI Standards
- Always use channel 9 (MIDI channel 10)
- Use GM drum mapping
- PPQ = 480 for maximum resolution
- Velocities: 1-127 range
- Duration: typically 0.1 beats

## Testing Your Contribution

### Manual Testing
1. Generate MIDI file with your style
2. Import into Superior Drummer 3
3. Verify 150 bars exactly
4. Check fills occur every 8 bars
5. Ensure musical quality

### Code Quality
```python
# Test basic functionality
python examples/generate_[style]_file.py

# Verify file structure
ls -la output/
```

## Submission Process

### 1. Create Feature Branch
```bash
git checkout -b feature/add-[style]-style
```

### 2. Commit Changes
```bash
git add .
git commit -m "Add [Style] drum pattern generator

- Implement basic patterns and variations
- Add fills every 8 bars with complexity variation
- Include realistic velocity humanization
- Create example generator script"
```

### 3. Submit Pull Request
- Clear description of the new style
- Examples of generated MIDI files
- Documentation updates included

## Style-Specific Guidelines

### Rock Styles
- Emphasize backbeat (snare on 2 and 4)
- Use ghost notes sparingly
- Focus on driving rhythm

### Jazz Styles
- Implement swing feel
- Ride cymbal prominence
- Subtle brush techniques
- Complex polyrhythms

### Latin Styles
- Syncopated patterns
- Clave-based rhythms
- Percussion integration
- Cultural authenticity

### Electronic Styles
- Quantized timing
- Synthetic drum sounds
- Loop-based thinking
- BPM considerations

## Documentation Standards

### Code Documentation
- Function docstrings for public APIs
- Clear parameter descriptions
- Usage examples
- Return value specifications

### Style Documentation
- Musical characteristics
- Typical BPM range
- Key pattern elements
- Historical context

## Questions and Support

- Create GitHub issues for bugs
- Use discussions for questions
- Check existing documentation first
- Provide minimal reproducible examples

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and contribute
- Maintain professional communication

---

Thank you for contributing to Desarticulator! Your contributions help musicians and producers worldwide.
