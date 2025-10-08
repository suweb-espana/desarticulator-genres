"""
Nueva Canción - Latin American folk movement drum patterns.
Political folk music with acoustic influences and protest song characteristics.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class NuevaCancionPattern(BasePattern):
    """Nueva Canción pattern with Latin American folk characteristics."""
    
    @property
    def genre_name(self) -> str:
        return "Nueva Canción"
    
    @property
    def description(self) -> str:
        return "Latin American folk movement - acoustic influenced, protest song characteristics, political"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic nueva canción pattern - folk influenced."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Acoustic-style kick - not too prominent
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(80, 8))
            if bar % 2 == 1:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(75, 10))
            
            # Folk snare - understated
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(83, 8))
            
            # Acoustic hi-hats - simple and supportive
            for eighth in range(8):
                if eighth % 2 == 0:  # Simple folk pattern
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(70, 10))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - With Latin percussion influences."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Standard kick
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(80, 8))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(78, 8))
            
            # Snare with Latin accents
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(85, 8))
            
            # Add Latin percussion feel with toms
            if bar % 3 == 0:
                self.add_note(midi, self.drum_mapping['tom_high'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(70, 10))
            
            # Folk hi-hats with Latin touch
            for eighth in range(8):
                velocity = 75 if eighth % 2 == 0 else 65
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             eighth * self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(velocity, 10))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Protest song energy."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # More driving kick for protest energy
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(83, 8))
            
            # Driving snare
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(88, 5))
            
            # Open hi-hats for folk atmosphere
            for eighth in range(8):
                if eighth % 3 == 0:
                    self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(75, 10))
                else:
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(70, 10))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple nueva canción fill."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 80)
        
        # Folk-style snare pattern
        positions = [
            self.midi_config['ticks_per_beat'],
            self.midi_config['ticks_per_beat'] * 2,
            self.midi_config['ticks_per_beat'] * 3,
            self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth']
        ]
        
        for i, pos in enumerate(positions):
            velocity = 75 + i * 3
            self.add_note(midi, self.drum_mapping['snare'], bar, pos, 
                         self.get_random_velocity(velocity, 8))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex nueva canción fill."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 85)
        
        # Folk tom pattern
        positions = [
            (self.midi_config['ticks_per_beat'], self.drum_mapping['snare'], 80),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_high'], 75),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['tom_mid'], 80),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['tom_low'], 85),
            (self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['snare'], 90),
        ]
        
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 8))
    
    # ========== SONG SECTIONS ==========
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Intro - folk acoustic entrance."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Gentle folk start
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(70, 8))
                if bar % 2 == 1:
                    self.add_note(midi, self.drum_mapping['snare'], bar, 
                                 self.midi_config['ticks_per_beat'] * 3, 
                                 self.get_random_velocity(75, 8))
            else:
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Verse - folk narrative support."""
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1)
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Chorus - protest song energy."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_2(midi, bar, 1)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bridge - Latin percussion influences."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_1(midi, bar, 1)
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Outro - folk ending."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                self.create_basic_pattern(midi, bar, 1)
            else:
                self.create_fill_simple(midi, bar)

