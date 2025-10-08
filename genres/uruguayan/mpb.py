"""
MPB - Música Popular Brasileña drum patterns.
Sophisticated Brazilian rhythms with samba influences and contemporary arrangements.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class MPBPattern(BasePattern):
    """MPB pattern with sophisticated Brazilian characteristics."""
    
    @property
    def genre_name(self) -> str:
        return "MPB"
    
    @property
    def description(self) -> str:
        return "Brazilian Popular Music - sophisticated rhythms with samba influences, contemporary arrangements"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic MPB pattern - sophisticated Brazilian rhythm."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # MPB kick pattern - samba influenced
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(85, 8))  # Gentle on 1
            if bar % 2 == 1:  # Samba variation
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'] * 3, 
                             self.get_random_velocity(80, 8))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'], 
                         self.get_random_velocity(75, 10))
            
            # Sophisticated snare - MPB style
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(90, 5))  # 2
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(88, 5))  # 4
            
            # Samba-influenced ghost notes
            if bar % 3 == 0:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(55, 10))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(50, 12))
            
            # Brazilian hi-hats - sophisticated pattern
            for i in range(16):
                if i % 5 == 0 or i % 3 == 0:  # Complex Brazilian rhythm
                    velocity = 75 if i % 4 == 0 else 65
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 i * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(velocity, 10))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - With ride and Brazilian sophistication."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Sophisticated kick
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(80, 8))
            
            # Samba-influenced kick variations
            if bar % 3 == 0:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'] * 2, 
                             self.get_random_velocity(75, 10))
            
            # Snare
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(88, 5))
            
            # Brazilian ride pattern
            for i in range(4):
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             i * self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(75, 8))
                # Sophisticated off-beats
                if i % 2 == 1:
                    self.add_note(midi, self.drum_mapping['ride'], bar, 
                                 i * self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'] + self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(70, 10))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Contemporary MPB with open hi-hats."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Modern MPB kick
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(85, 8))
            if bar % 4 == 3:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(80, 8))
            
            # Snare
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(88, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(88, 8))
            
            # Contemporary hi-hat work
            for eighth in range(8):
                if eighth % 3 == 0:  # Open for breath
                    self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(80, 10))
                else:  # Closed for rhythm
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(70, 10))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple MPB fill - sophisticated."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 85)
        
        # Sophisticated snare pattern
        positions = [
            self.midi_config['ticks_per_beat'],
            self.midi_config['ticks_per_beat'] * 2,
            self.midi_config['ticks_per_beat'] * 3,
            self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth']
        ]
        
        for i, pos in enumerate(positions):
            velocity = 80 + i * 3
            self.add_note(midi, self.drum_mapping['snare'], bar, pos, 
                         self.get_random_velocity(velocity, 8))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex MPB fill - Brazilian sophistication."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 90)
        
        # Brazilian tom pattern
        positions = [
            (self.midi_config['ticks_per_beat'], self.drum_mapping['snare'], 85),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'] * 2, 
             self.drum_mapping['tom_high'], 80),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['tom_mid'], 85),
            (self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_low'], 90),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['snare'], 95),
            (self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['ride'], 80),
        ]
        
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 8))
    
    # ========== SONG SECTIONS ==========
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Intro - sophisticated Brazilian entrance."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Gentle sophisticated start
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(75, 8))
                if bar % 2 == 1:
                    self.add_note(midi, self.drum_mapping['snare'], bar, 
                                 self.midi_config['ticks_per_beat'] * 3, 
                                 self.get_random_velocity(80, 8))
            else:
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Verse - sophisticated MPB groove."""
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1)
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Chorus - contemporary MPB energy."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_1(midi, bar, 1)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bridge - modern MPB sophistication."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_2(midi, bar, 1)
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Outro - Brazilian sophistication."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                self.create_variation_2(midi, bar, 1)
            else:
                self.create_fill_simple(midi, bar)  # Gentle ending
