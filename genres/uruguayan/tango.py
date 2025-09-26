"""
Tango - Astor Piazzolla, Gardel style drum patterns.
Dramatic, passionate, with distinctive 2/4 feel adapted to 4/4 and bandoneón influences.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class TangoPattern(BasePattern):
    """Tango pattern with Astor Piazzolla characteristics."""
    
    @property
    def genre_name(self) -> str:
        return "Tango"
    
    @property
    def description(self) -> str:
        return "Dramatic Argentine tango - Astor Piazzolla, Gardel style: passionate, distinctive rhythm"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic tango pattern - distinctive 2/4 feel in 4/4."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Tango kick pattern - strong on 1 and 3
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))  # Strong on 1
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(90, 5))  # On 3
            
            # Characteristic tango syncopation
            if bar % 2 == 1:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(80, 8))
            
            # Tango snare - dramatic and precise
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(90, 5))  # 2
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(88, 5))  # 4
            
            # Subtle ghost notes for expression
            if bar % 4 == 1 or bar % 4 == 3:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(50, 10))
            
            # Tango hi-hats - subtle and sophisticated
            for eighth in range(8):
                if eighth % 3 == 0:  # Sparse pattern for sophistication
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(70, 8))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - More dramatic with accents."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Dramatic kick pattern
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(100, 3))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))
            
            # Add dramatic pauses and accents
            if bar % 2 == 0:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'] * 3, 
                             self.get_random_velocity(85, 8))
            
            # Dramatic snare with rolls
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 100)
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 100)
            
            # Snare rolls for drama
            if bar % 4 == 3:
                for i in range(3):
                    pos = self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'] + i * self.midi_config['ticks_per_sixteenth']
                    self.add_note(midi, self.drum_mapping['snare'], bar, pos, 
                                 self.get_random_velocity(85 + i * 5, 5))
            
            # Ride for sophistication
            for beat in range(4):
                if beat % 2 == 0:
                    self.add_note(midi, self.drum_mapping['ride'], bar, 
                                 beat * self.midi_config['ticks_per_beat'], 
                                 self.get_random_velocity(75, 8))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Piazzolla-style nuevo tango."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Nuevo tango kick - more complex
            kick_positions = [0, 7, 12]  # Irregular pattern
            for pos in kick_positions:
                if pos < 16:
                    self.add_note(midi, self.drum_mapping['kick'], bar, 
                                 pos * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(90, 8))
            
            # Sophisticated snare placement
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'], 
                         self.get_random_velocity(90, 5))
            
            # Nuevo tango ride pattern
            for eighth in range(8):
                if eighth % 3 != 0:
                    self.add_note(midi, self.drum_mapping['ride'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(80, 8))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple tango fill - dramatic pause and accent."""
        # Dramatic start
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 100)
        
        # Pause then dramatic snare
        self.add_note(midi, self.drum_mapping['snare'], bar, 
                     self.midi_config['ticks_per_beat'] * 2, 95)
        self.add_note(midi, self.drum_mapping['snare'], bar, 
                     self.midi_config['ticks_per_beat'] * 3, 100)
        self.add_note(midi, self.drum_mapping['snare'], bar, 
                     self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 90)
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex tango fill - passionate and dramatic."""
        # Dramatic kick
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 100)
        
        # Passionate tom pattern
        positions = [
            (self.midi_config['ticks_per_beat'], self.drum_mapping['snare'], 95),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 
             self.drum_mapping['tom_high'], 85),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_mid'], 90),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['tom_low'], 100),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['snare'], 100),
            (self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['crash'], 95),
        ]
        
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 5))
    
    # ========== SONG SECTIONS ==========
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Intro - dramatic tango entrance."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Dramatic entrance
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(90, 5))
                if bar % 2 == 1:
                    self.add_note(midi, self.drum_mapping['snare'], bar, 
                                 self.midi_config['ticks_per_beat'] * 3, 
                                 self.get_random_velocity(85, 5))
            else:
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Verse - passionate tango rhythm."""
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1)
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Chorus - dramatic tango intensity."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_1(midi, bar, 1)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bridge - nuevo tango sophistication."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_2(midi, bar, 1)
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Outro - dramatic tango finale."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                self.create_variation_1(midi, bar, 1)
            else:
                self.create_fill_complex(midi, bar)
