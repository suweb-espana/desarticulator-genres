"""
Post-Punk Argentino - Sumo, Soda Stereo style drum patterns.
Dark, angular, with new wave influences and driving rhythms.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class PostPunkArgentinoPattern(BasePattern):
    """Post-Punk Argentino pattern with Sumo/Soda Stereo characteristics."""
    
    @property
    def genre_name(self) -> str:
        return "Post-Punk Argentino"
    
    @property
    def description(self) -> str:
        return "Dark Argentine post-punk - Sumo, Soda Stereo style: angular, new wave influenced, driving"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic post-punk pattern - angular and driving."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Angular kick pattern - post-punk style
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(90, 5))
            if bar % 3 == 0:  # Irregular pattern
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'] * 2, 
                             self.get_random_velocity(85, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(88, 5))
            
            # Sharp snare - post-punk characteristic
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(100, 3))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(98, 3))
            
            # New wave influenced hi-hats - 16th notes with gaps
            for sixteenth in range(16):
                if sixteenth % 3 != 0:  # Skip some for angular feel
                    velocity = 80 if sixteenth % 4 == 0 else 70
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(velocity, 8))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - More aggressive with crashes."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Aggressive kick
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))
            
            # Double snare hits for intensity
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 100)
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 95)
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 100)
            
            # Intense hi-hats
            for sixteenth in range(16):
                if sixteenth % 2 == 0:
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(85, 8))
            
            # Crashes for post-punk intensity
            if bar % 4 == 3:
                self.add_note(midi, self.drum_mapping['crash'], bar, 0, 
                             self.get_random_velocity(90, 5))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Ride pattern with new wave feel."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Steady kick
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(88, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(88, 5))
            
            # Snare
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(95, 5))
            
            # New wave ride pattern
            for eighth in range(8):
                velocity = 85 if eighth % 2 == 0 else 75  # Accent on downbeats
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             eighth * self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(velocity, 8))
            
            # Bell accents
            if bar % 2 == 1:
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             self.midi_config['ticks_per_beat'], 90)  # Bell on 2
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 90)  # Bell on 4
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple post-punk fill."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 95)
        
        # Angular snare pattern
        positions = [
            self.midi_config['ticks_per_beat'],
            self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'],
            self.midi_config['ticks_per_beat'] * 2,
            self.midi_config['ticks_per_beat'] * 3,
            self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth']
        ]
        
        for i, pos in enumerate(positions):
            velocity = 85 + i * 3
            self.add_note(midi, self.drum_mapping['snare'], bar, pos, velocity)
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex post-punk fill - dark and angular."""
        # Kick
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 100)
        
        # Angular tom cascade
        positions = [
            (self.midi_config['ticks_per_beat'], self.drum_mapping['snare'], 95),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'] * 2, 
             self.drum_mapping['tom_high'], 90),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['tom_mid'], 95),
            (self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'] * 3, 
             self.drum_mapping['tom_low'], 100),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['snare'], 100),
            (self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['crash'], 95),
        ]
        
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 5))
    
    # ========== SONG SECTIONS ==========
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Intro - dark post-punk build-up."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Start minimal and dark
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(80, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 
                             self.get_random_velocity(85, 5))
                # Sparse hi-hats
                for eighth in range(8):
                    if eighth % 3 == 0:
                        self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                     eighth * self.midi_config['ticks_per_eighth'], 
                                     self.get_random_velocity(65, 5))
            else:
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Verse - angular and supportive."""
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1)
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Chorus - more aggressive post-punk."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_1(midi, bar, 1)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bridge - new wave contrast."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_2(midi, bar, 1)
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Outro - dark post-punk ending."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                self.create_variation_1(midi, bar, 1)
            else:
                self.create_fill_complex(midi, bar)
