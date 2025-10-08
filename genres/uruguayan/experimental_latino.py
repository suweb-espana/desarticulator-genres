"""
Experimental Latino - Latin American avant-garde drum patterns.
Experimental Latin music with avant-garde influences and unconventional rhythms.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class ExperimentalLatinoPattern(BasePattern):
    """Experimental Latino pattern with avant-garde Latin characteristics."""
    
    @property
    def genre_name(self) -> str:
        return "Experimental Latino"
    
    @property
    def description(self) -> str:
        return "Latin avant-garde - experimental Latin music with unconventional rhythms and avant-garde influences"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic experimental latino pattern - unconventional."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Experimental kick pattern - irregular
            kick_positions = [0, 5, 9, 13, 15]  # Unconventional spacing
            for pos in kick_positions:
                if pos < 16:
                    self.add_note(midi, self.drum_mapping['kick'], bar, 
                                 pos * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(80, 12))
            
            # Avant-garde snare placement
            snare_positions = [3, 7, 11] if bar % 2 == 0 else [2, 8, 14]
            for pos in snare_positions:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             pos * self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(85, 10))
            
            # Experimental hi-hats - chaotic pattern
            for i in range(16):
                if random.random() < 0.5:  # Random experimental pattern
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 i * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(60, 15))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - More chaotic with toms."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Chaotic kick
            if random.random() < 0.7:
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(85, 12))
            if random.random() < 0.5:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2, 
                             self.get_random_velocity(80, 12))
            
            # Experimental snare and tom work
            for i in range(4):
                if random.random() < 0.6:
                    drum = random.choice([self.drum_mapping['snare'], 
                                        self.drum_mapping['tom_high'], 
                                        self.drum_mapping['tom_mid']])
                    self.add_note(midi, drum, bar, 
                                 i * self.midi_config['ticks_per_beat'] + random.randint(0, 3) * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(75, 15))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Polyrhythmic experimental."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Polyrhythmic kick in 7/8 over 4/4
            kick_pattern = [0, 7, 14]  # Creates polyrhythmic feel
            for pos in kick_pattern:
                if pos < 16:
                    self.add_note(midi, self.drum_mapping['kick'], bar, 
                                 pos * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(80, 10))
            
            # Experimental snare in 5/4 feel
            snare_positions = [5, 10, 15]
            for pos in snare_positions:
                if pos < 16:
                    self.add_note(midi, self.drum_mapping['snare'], bar, 
                                 pos * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(85, 10))
            
            # Avant-garde ride pattern
            for eighth in range(8):
                if eighth % 5 == 0:
                    self.add_note(midi, self.drum_mapping['ride'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(70, 12))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple experimental fill."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 80)
        for i in range(5):
            pos = self.midi_config['ticks_per_beat'] * 2 + i * self.midi_config['ticks_per_sixteenth']
            drum = self.drum_mapping['snare'] if i % 2 == 0 else self.drum_mapping['tom_high']
            self.add_note(midi, drum, bar, pos, 75 + i * 3)
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex experimental fill."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 85)
        positions = [
            (self.midi_config['ticks_per_sixteenth'] * 3, self.drum_mapping['tom_high'], 75),
            (self.midi_config['ticks_per_sixteenth'] * 7, self.drum_mapping['tom_mid'], 80),
            (self.midi_config['ticks_per_sixteenth'] * 11, self.drum_mapping['tom_low'], 85),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['crash'], 90),
        ]
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 10))
    
    # Song sections - basic implementations
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1) if bar >= start_bar + 4 else None
    
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
                self.create_fill_complex(midi, bar)

