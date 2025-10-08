"""
Latin Jazz - Sophisticated Latin American jazz fusion drum patterns.
Complex rhythms with Afro-Cuban influences and jazz sophistication.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class LatinJazzPattern(BasePattern):
    """Latin Jazz pattern with sophisticated Afro-Cuban characteristics."""
    
    @property
    def genre_name(self) -> str:
        return "Latin Jazz"
    
    @property
    def description(self) -> str:
        return "Sophisticated Latin jazz - Afro-Cuban influences with jazz complexity and Latin rhythms"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic Latin jazz pattern - complex and sophisticated."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Latin jazz kick - clave influenced
            kick_positions = [0, 10, 14]  # Clave-based pattern
            for pos in kick_positions:
                if pos < 16:
                    self.add_note(midi, self.drum_mapping['kick'], bar, 
                                 pos * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(85, 8))
            
            # Add variation every few bars
            if bar % 3 == 0:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'] * 2, 
                             self.get_random_velocity(80, 10))
            
            # Jazz snare with Latin accent
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(90, 5))  # 2
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(88, 5))  # 4
            
            # Latin ghost notes for clave feel
            if bar % 2 == 1:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(60, 12))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(55, 12))
            
            # Jazz ride pattern with Latin feel
            for eighth in range(8):
                if eighth % 3 != 0:  # Skip some for sophistication
                    velocity = 80 if eighth % 2 == 0 else 70
                    self.add_note(midi, self.drum_mapping['ride'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(velocity, 10))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - More complex with polyrhythms."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Complex polyrhythmic kick
            kick_pattern = [0, 5, 9, 12, 15]  # Dense Latin pattern
            for pos in kick_pattern:
                if pos < 16:
                    self.add_note(midi, self.drum_mapping['kick'], bar, 
                                 pos * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(80, 10))
            
            # Jazz snare with Latin complexity
            snare_positions = [4, 8, 12] if bar % 2 == 0 else [6, 10, 14]
            for pos in snare_positions:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             pos * self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(85, 8))
            
            # Tom work for Latin jazz flavor
            if bar % 4 == 3:
                self.add_note(midi, self.drum_mapping['tom_high'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(75, 10))
                self.add_note(midi, self.drum_mapping['tom_mid'], bar, 
                             self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(80, 10))
            
            # Complex ride with bell
            for eighth in range(8):
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             eighth * self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(75, 10))
                # Bell accents on complex pattern
                if eighth % 3 == 0:
                    self.add_note(midi, self.drum_mapping['ride'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(85, 8))  # Bell
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Hi-hat work with Latin sophistication."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Sophisticated kick
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(80, 8))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'], 
                         self.get_random_velocity(75, 10))
            
            # Jazz snare
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(85, 8))
            
            # Sophisticated hi-hat work
            for eighth in range(8):
                if eighth % 4 == 0:  # Open for jazz breath
                    self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(75, 10))
                elif eighth % 2 == 0:  # Closed for rhythm
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(70, 10))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple Latin jazz fill."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 85)
        
        # Jazz snare pattern with Latin accent
        positions = [
            self.midi_config['ticks_per_beat'],
            self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'],
            self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'],
            self.midi_config['ticks_per_beat'] * 3,
            self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth']
        ]
        
        for i, pos in enumerate(positions):
            velocity = 80 + i * 3
            self.add_note(midi, self.drum_mapping['snare'], bar, pos, 
                         self.get_random_velocity(velocity, 8))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex Latin jazz fill - sophisticated."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 90)
        
        # Sophisticated Latin jazz tom pattern
        positions = [
            (self.midi_config['ticks_per_beat'], self.drum_mapping['snare'], 85),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'] * 2, 
             self.drum_mapping['tom_high'], 80),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_mid'], 75),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['tom_low'], 85),
            (self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['snare'], 90),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['ride'], 80),
            (self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['crash'], 85),
        ]
        
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 8))
    
    # ========== SONG SECTIONS ==========
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Intro - Latin jazz sophistication."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Sophisticated jazz start
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(75, 8))
                if bar % 2 == 1:
                    self.add_note(midi, self.drum_mapping['snare'], bar, 
                                 self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(80, 8))
                # Jazz ride
                for eighth in range(8):
                    if eighth % 3 == 0:
                        self.add_note(midi, self.drum_mapping['ride'], bar, 
                                     eighth * self.midi_config['ticks_per_eighth'], 
                                     self.get_random_velocity(70, 10))
            else:
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Verse - Latin jazz groove."""
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1)
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Chorus - complex Latin jazz."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_1(midi, bar, 1)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bridge - jazz sophistication."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_2(midi, bar, 1)
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Outro - Latin jazz ending."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                self.create_variation_2(midi, bar, 1)
            else:
                self.create_fill_complex(midi, bar)

