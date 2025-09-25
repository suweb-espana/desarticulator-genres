"""
Base pattern class for drum pattern generation with variation system.
"""

import random
from abc import ABC, abstractmethod
from typing import Dict, List, Tuple, Optional
from midiutil import MIDIFile


class BasePattern(ABC):
    """Base class for all drum patterns with variation system."""
    
    def __init__(self, tempo: int = 150, seed: Optional[int] = None):
        self.tempo = tempo
        self.seed = seed
        
        # MIDI Configuration
        self.midi_config = {
            'track': 0,
            'channel': 9,
            'ppq': 480,
            'ticks_per_bar': 1920,
            'ticks_per_beat': 480,
            'ticks_per_eighth': 240,
            'ticks_per_sixteenth': 120
        }
        
        # Drum Mapping (GM Standard)
        self.drum_mapping = {
            'kick': 36,
            'snare': 38,
            'closed_hh': 42,
            'open_hh': 46,
            'ride': 51,
            'crash': 49,
            'tom_high': 43,
            'tom_mid': 45,
            'tom_low': 48
        }
        
        # Variation system
        self.variation_types = ['basic', 'variation_1', 'variation_2', 'fill_simple', 'fill_complex']
        self.current_variation = 'basic'
        
    def setup_randomization(self) -> None:
        """Setup randomization with optional seed."""
        if self.seed is not None:
            random.seed(self.seed)
    
    def add_note(self, midi: MIDIFile, drum: int, bar: int, beat_pos: int, 
                 velocity: int = 85, duration: float = 0.1) -> None:
        """Add a MIDI note to the track."""
        time_ticks = (bar * self.midi_config['ticks_per_bar']) + beat_pos
        midi.addNote(
            self.midi_config['track'],
            self.midi_config['channel'],
            drum,
            time_ticks / self.midi_config['ppq'],
            duration,
            velocity
        )
    
    def get_random_velocity(self, base_velocity: int, variation: int = 10) -> int:
        """Get randomized velocity for humanization."""
        return max(1, min(127, base_velocity + random.randint(-variation, variation)))
    
    def should_add_variation(self, bar: int, probability: float = 0.3) -> bool:
        """Determine if a variation should be added based on probability."""
        return random.random() < probability
    
    def select_variation_type(self, bar: int) -> str:
        """Select variation type based on bar position and randomness."""
        # Fill patterns every 8 bars
        if (bar + 1) % 8 == 0:
            return random.choice(['fill_simple', 'fill_complex'])
        
        # Random variations in other bars
        if self.should_add_variation(bar, 0.25):
            return random.choice(['variation_1', 'variation_2'])
        
        return 'basic'
    
    @abstractmethod
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Create the basic pattern for this genre."""
        pass
    
    @abstractmethod
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Create variation 1 of the pattern."""
        pass
    
    @abstractmethod
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Create variation 2 of the pattern."""
        pass
    
    @abstractmethod
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Create a simple fill for transitions."""
        pass
    
    @abstractmethod
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Create a complex fill for major transitions."""
        pass
    
    def generate_pattern(self, bars: int = 150) -> MIDIFile:
        """Generate complete drum pattern with variations."""
        self.setup_randomization()
        
        midi = MIDIFile(1)
        midi.addTempo(self.midi_config['track'], 0, self.tempo)
        
        current_bar = 0
        while current_bar < bars - 1:
            variation_type = self.select_variation_type(current_bar)
            
            if variation_type == 'fill_simple':
                self.create_fill_simple(midi, current_bar)
                current_bar += 1
            elif variation_type == 'fill_complex':
                self.create_fill_complex(midi, current_bar)
                current_bar += 1
            elif variation_type == 'variation_1':
                bars_to_add = min(8, bars - 1 - current_bar)
                self.create_variation_1(midi, current_bar, bars_to_add)
                current_bar += bars_to_add
            elif variation_type == 'variation_2':
                bars_to_add = min(8, bars - 1 - current_bar)
                self.create_variation_2(midi, current_bar, bars_to_add)
                current_bar += bars_to_add
            else:  # basic
                bars_to_add = min(8, bars - 1 - current_bar)
                self.create_basic_pattern(midi, current_bar, bars_to_add)
                current_bar += bars_to_add
        
        # Final crash on last bar
        self.add_note(midi, self.drum_mapping['crash'], bars - 1, 0, 100, 2.0)
        
        return midi
    
    @property
    @abstractmethod
    def genre_name(self) -> str:
        """Return the name of this genre."""
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        """Return description of this genre's characteristics."""
        pass
