# API Reference - Desarticulator

## Core Functions

### `create_[style]_groove()`
Main function to generate a MIDI groove for a specific style.

**Returns**: `MIDIFile` object ready to be written to disk

**Example**:
```python
from styles.punk_rock import create_punk_rock_groove

midi = create_punk_rock_groove()
with open("output.mid", "wb") as f:
    midi.writeFile(f)
```

### `add_note(drum, bar, beat_pos, velocity=85, duration=0.1)`
Core utility function to add MIDI notes.

**Parameters**:
- `drum` (int): MIDI note number for drum instrument
- `bar` (int): Bar number (0-149)
- `beat_pos` (int): Position within bar in ticks
- `velocity` (int): MIDI velocity (1-127)
- `duration` (float): Note duration in beats

## Pattern Functions

### `add_basic_pattern(start_bar, bars=8)`
Adds the fundamental pattern for the style.

### `add_variation_1(start_bar, bars=8)`
Adds the first variation of the basic pattern.

### `add_fill_simple(bar)`
Adds a simple fill for the style.

### `add_fill_complex(bar)`
Adds a complex fill for the style.

### `add_final_fill(bar)`
Adds the epic final fill before the groove ends.

## Constants

### Timing Constants
```python
TICKS_PER_BAR = 1920        # 4/4 time signature
TICKS_PER_BEAT = 480        # Quarter note
TICKS_PER_EIGHTH = 240      # Eighth note  
TICKS_PER_SIXTEENTH = 120   # Sixteenth note
```

### Drum Mapping (GM Standard)
```python
KICK = 36           # Bass Drum
SNARE = 38          # Acoustic Snare
CLOSED_HH = 42      # Closed Hi-Hat
OPEN_HH = 46        # Open Hi-Hat
RIDE = 51           # Ride Cymbal
CRASH = 49          # Crash Cymbal
TOM_HIGH = 43       # High Tom
TOM_MID = 45        # Mid Tom
TOM_LOW = 48        # Low Tom
```

### Velocity Ranges
```python
VELOCITY_RANGES = {
    'kick_main': (90, 100),
    'kick_ghost': (60, 75),
    'snare_main': (95, 100),
    'snare_ghost': (40, 50),
    'hh_closed_accent': (75, 85),
    'hh_closed_normal': (65, 75),
    'hh_open': (70, 80),
    'crash': (95, 100),
    'tom_fill': (80, 95)
}
```
