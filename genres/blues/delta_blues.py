"""
Delta Blues - Robert Johnson, Son House style drum patterns.
Traditional Mississippi Delta blues with minimal, authentic rhythms.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class DeltaBluesPattern(BasePattern):
    """Delta Blues pattern with traditional Mississippi characteristics."""
    
    @property
    def genre_name(self) -> str:
        return "Delta Blues"
    
    @property
    def description(self) -> str:
        return "Traditional Mississippi Delta blues - Robert Johnson, Son House style: minimal, authentic"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic delta blues pattern - minimal and traditional."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Minimal kick pattern - traditional delta
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(80, 8))
            if bar % 2 == 1:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2, 
                             self.get_random_velocity(75, 8))
            
            # Traditional snare - understated
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(83, 8))
            
            # Traditional shuffle hi-hats
            for i in range(4):
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             i * self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(70, 8))
                # Shuffle off-beat
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             i * self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'] + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(65, 10))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - With subtle swing."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(80, 8))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(78, 8))
            
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(83, 8))
            
            # Swing feel
            for i in range(4):
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             i * self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(75, 8))
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             i * self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'] + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(70, 10))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Traditional with brush feel."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(75, 10))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(80, 10))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(80, 10))
            
            # Brush-style hi-hats
            for eighth in range(8):
                if eighth % 2 == 0:
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(65, 12))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple delta fill."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 75)
        for i in range(3):
            pos = self.midi_config['ticks_per_beat'] * 2 + i * self.midi_config['ticks_per_eighth']
            self.add_note(midi, self.drum_mapping['snare'], bar, pos, 75 + i * 3)
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex delta fill."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 80)
        positions = [
            (self.midi_config['ticks_per_beat'], self.drum_mapping['snare'], 80),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['tom_mid'], 75),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['snare'], 85),
        ]
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 8))
    
    # Basic song sections
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1) if bar >= start_bar + 2 else None
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1)
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_1(midi, bar, 1)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_2(midi, bar, 1)
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                self.create_variation_2(midi, bar, 1)
            else:
                self.create_fill_simple(midi, bar)

