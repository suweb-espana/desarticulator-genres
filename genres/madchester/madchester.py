"""
Madchester - Happy Mondays, Stone Roses style drum patterns.
Danceable, funky, psychedelic with four-on-floor influences.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class MadchesterPattern(BasePattern):
    """Madchester pattern with Happy Mondays characteristics."""
    
    @property
    def genre_name(self) -> str:
        return "Madchester"
    
    @property
    def description(self) -> str:
        return "Danceable Manchester sound - Happy Mondays, Stone Roses style: funky, psychedelic, groove-oriented"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic Madchester pattern - danceable groove."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Four-on-floor kick with funk variations
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))  # 1
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(90, 5))  # 2
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))  # 3
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(90, 5))  # 4
            
            # Backbeat snare - dance oriented
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(100, 3))  # 2
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(100, 3))  # 4
            
            # Dance hi-hats - 16th note patterns
            for sixteenth in range(16):
                if sixteenth % 2 == 0:  # On downbeats and upbeats
                    velocity = 85 if sixteenth % 4 == 0 else 75  # Accent pattern
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(velocity, 8))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - With syncopated kicks and ghost notes."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Four-on-floor with syncopation
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(90, 5))
            
            # Add syncopated kicks for funk feel
            if bar % 2 == 1:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(80, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(75, 5))
            
            # Snare with ghost notes
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 100)
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 100)
            
            # Funky ghost notes (Happy Mondays influence)
            ghost_positions = [
                self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'],
                self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'],
                self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth']
            ]
            for pos in ghost_positions:
                self.add_note(midi, self.drum_mapping['snare'], bar, pos, 
                             self.get_random_velocity(50, 10))
            
            # Intense hi-hats
            for sixteenth in range(16):
                if sixteenth % 2 == 0:
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(80, 8))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Open hi-hats and psychedelic touches."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Standard four-on-floor
            for beat in range(4):
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             beat * self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(90, 5))
            
            # Snare
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(95, 5))
            
            # Mix of open and closed hi-hats for psychedelic feel
            for eighth in range(8):
                if eighth % 3 == 0:  # Open hi-hats
                    self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(85, 8))
                else:  # Closed hi-hats
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(75, 8))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple Madchester fill - dance-oriented."""
        # Basic pattern first half
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 95)
        self.add_note(midi, self.drum_mapping['snare'], bar, 
                     self.midi_config['ticks_per_beat'], 95)
        
        # Dance fill second half
        for i in range(4):
            pos = self.midi_config['ticks_per_beat'] * 2 + i * self.midi_config['ticks_per_sixteenth']
            velocity = 80 + i * 5
            self.add_note(midi, self.drum_mapping['snare'], bar, pos, velocity)
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex Madchester fill - psychedelic dance."""
        # Kick on 1
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 100)
        
        # Psychedelic tom pattern
        positions = [
            (self.midi_config['ticks_per_beat'], self.drum_mapping['tom_high'], 90),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'] * 2, 
             self.drum_mapping['tom_mid'], 85),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['tom_low'], 95),
            (self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'] * 3, 
             self.drum_mapping['snare'], 100),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['open_hh'], 90),
            (self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['crash'], 95),
        ]
        
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 5))
    
    # ========== SONG SECTIONS ==========
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Intro - dance build-up."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Start with just four-on-floor
                for beat in range(4):
                    self.add_note(midi, self.drum_mapping['kick'], bar, 
                                 beat * self.midi_config['ticks_per_beat'], 
                                 self.get_random_velocity(85, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'], 80)
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 80)
            else:
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Verse - groove-oriented."""
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1)
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Chorus - dance energy."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_1(midi, bar, 1)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bridge - psychedelic contrast."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_2(midi, bar, 1)
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Outro - dance ending."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                self.create_variation_1(midi, bar, 1)
            else:
                self.create_fill_complex(midi, bar)
