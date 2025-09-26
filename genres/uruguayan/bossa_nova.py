"""
Bossa Nova - João Gilberto, Tom Jobim style drum patterns.
Subtle, sophisticated, with gentle swing and understated elegance.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class BossaNovaPattern(BasePattern):
    """Bossa Nova pattern with sophisticated Brazilian characteristics."""
    
    @property
    def genre_name(self) -> str:
        return "Bossa Nova"
    
    @property
    def description(self) -> str:
        return "Sophisticated Brazilian rhythm - João Gilberto, Tom Jobim style: subtle, elegant, gentle swing"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic bossa nova pattern - subtle and sophisticated."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Subtle kick pattern - not too prominent
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(75, 8))  # Gentle on 1
            if bar % 2 == 1:  # Variation every other bar
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(70, 8))
            else:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2, 
                             self.get_random_velocity(75, 8))
            
            # Gentle snare - understated
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(80, 8))  # Soft on 2
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(78, 8))  # Soft on 4
            
            # Bossa nova brush-style hi-hats - very subtle
            for eighth in range(8):
                if eighth % 3 == 0:  # Sparse, sophisticated
                    velocity = 65 if eighth % 2 == 0 else 60
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(velocity, 10))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - With ride and subtle swing."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Gentle kick
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(75, 8))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(75, 8))
            
            # Soft snare
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(80, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(78, 8))
            
            # Bossa nova ride pattern - gentle swing
            for i in range(4):
                # Main beats
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             i * self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(70, 8))
                # Swing off-beats
                if i % 2 == 1:
                    self.add_note(midi, self.drum_mapping['ride'], bar, 
                                 i * self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'] + self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(65, 10))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Brush-style with open hi-hats."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Very subtle kick
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(70, 10))
            if bar % 3 == 0:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'] * 2, 
                             self.get_random_velocity(65, 10))
            
            # Brush-style snare (very soft)
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(75, 10))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(73, 10))
            
            # Mix of open and closed hi-hats - brush style
            for eighth in range(8):
                if eighth % 4 == 0:  # Open for breath
                    self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(60, 12))
                elif eighth % 2 == 0:  # Closed for rhythm
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(55, 12))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple bossa fill - gentle and sophisticated."""
        # Gentle kick
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 75)
        
        # Subtle snare pattern
        positions = [
            self.midi_config['ticks_per_beat'],
            self.midi_config['ticks_per_beat'] * 2,
            self.midi_config['ticks_per_beat'] * 3,
            self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth']
        ]
        
        for i, pos in enumerate(positions):
            velocity = 75 + i * 2
            self.add_note(midi, self.drum_mapping['snare'], bar, pos, 
                         self.get_random_velocity(velocity, 8))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex bossa fill - sophisticated brush work."""
        # Gentle kick
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 80)
        
        # Sophisticated tom pattern
        positions = [
            (self.midi_config['ticks_per_beat'], self.drum_mapping['snare'], 80),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_high'], 70),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['tom_mid'], 75),
            (self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_low'], 80),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['snare'], 85),
            (self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['ride'], 75),
        ]
        
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 8))
    
    # ========== SONG SECTIONS ==========
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Intro - gentle bossa entrance."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Very gentle start
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(65, 8))
                if bar % 2 == 1:
                    self.add_note(midi, self.drum_mapping['snare'], bar, 
                                 self.midi_config['ticks_per_beat'] * 3, 
                                 self.get_random_velocity(70, 8))
                # Minimal hi-hats
                for eighth in range(8):
                    if eighth % 4 == 0:
                        self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                     eighth * self.midi_config['ticks_per_eighth'], 
                                     self.get_random_velocity(55, 10))
            else:
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Verse - gentle bossa groove."""
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1)
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Chorus - slightly more present but still elegant."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_1(midi, bar, 1)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bridge - brush-style sophistication."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_2(midi, bar, 1)
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Outro - gentle bossa ending."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                self.create_variation_2(midi, bar, 1)
            else:
                self.create_fill_simple(midi, bar)  # Gentle ending
