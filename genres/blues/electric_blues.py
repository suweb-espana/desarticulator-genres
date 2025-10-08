"""
Electric Blues - B.B. King, Albert King, Pappo style drum patterns.
Heavy electric blues with rock attitude, shuffle feel, and powerful dynamics.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class ElectricBluesPattern(BasePattern):
    """Electric Blues pattern with Pappo-style characteristics."""
    
    @property
    def genre_name(self) -> str:
        return "Electric Blues"
    
    @property
    def description(self) -> str:
        return "Heavy electric blues - B.B. King, Albert King, Pappo style: shuffle feel, rock attitude, powerful"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic electric blues pattern - Pappo-style shuffle with power."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Heavy blues kick - Pappo style
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(90, 5))  # Strong on 1
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(85, 5))  # On 3
            
            # Add Pappo-style syncopated kicks
            if bar % 3 == 0:  # Variation every 3rd bar
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(75, 8))
            
            # Powerful snare - electric blues style
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(95, 5))  # 2
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(93, 5))  # 4
            
            # Classic blues shuffle on hi-hats - Pappo style
            for i in range(4):
                # Shuffle triplet feel (long-short pattern)
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             i * self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(75, 8))  # On beat
                # Shuffle off-beat - characteristic blues feel
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             i * self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'] + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(70, 10))  # Shuffle off-beat
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - Pappo-style with ride and double kicks."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Double kick pattern - Pappo rock influence
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_sixteenth'], 
                         self.get_random_velocity(90, 8))  # Quick double
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))
            
            # Add more syncopated kicks
            if bar % 2 == 1:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(80, 8))
            
            # Powerful snare
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(100, 3))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(98, 3))
            
            # Ride pattern with bell - Pappo influence
            for i in range(4):
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             i * self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(80, 8))
                # Bell on 2 and 4 for emphasis
                if i % 2 == 1:
                    self.add_note(midi, self.drum_mapping['ride'], bar, 
                                 i * self.midi_config['ticks_per_beat'], 
                                 self.get_random_velocity(90, 5))  # Bell accent
                
                # Shuffle off-beat on ride
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             i * self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'] + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(75, 10))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Heavy blues rock with ghost notes."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Heavy kick pattern
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(90, 5))
            
            # Add rock-influenced kicks
            if bar % 4 == 3:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'] * 2, 
                             self.get_random_velocity(85, 8))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(80, 8))
            
            # Snare with ghost notes - Pappo groove
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(100, 3))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(98, 3))
            
            # Ghost notes for groove - signature Pappo feel
            ghost_positions = [
                self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'],
                self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'],
                self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth']
            ]
            for pos in ghost_positions:
                self.add_note(midi, self.drum_mapping['snare'], bar, pos, 
                             self.get_random_velocity(55, 12))
            
            # Open hi-hats for blues rock feel
            for i in range(4):
                if i % 2 == 0:  # Closed on 1 and 3
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 i * self.midi_config['ticks_per_beat'], 
                                 self.get_random_velocity(75, 8))
                else:  # Open on 2 and 4
                    self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                                 i * self.midi_config['ticks_per_beat'], 
                                 self.get_random_velocity(85, 8))
                
                # Shuffle off-beats
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             i * self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'] + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(65, 10))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple Pappo-style blues fill."""
        # Heavy kick
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                     self.get_random_velocity(95, 5))
        
        # Blues snare pattern with attitude
        positions = [
            self.midi_config['ticks_per_beat'],
            self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'],
            self.midi_config['ticks_per_beat'] * 2,
            self.midi_config['ticks_per_beat'] * 3,
            self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth']
        ]
        
        for i, pos in enumerate(positions):
            velocity = 85 + i * 4  # Building intensity
            self.add_note(midi, self.drum_mapping['snare'], bar, pos, 
                         min(127, velocity))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex Pappo-style blues rock fill."""
        # Heavy kick
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 100)
        
        # Pappo-style tom cascade with blues flavor
        positions = [
            (self.midi_config['ticks_per_beat'], self.drum_mapping['snare'], 95),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 
             self.drum_mapping['tom_high'], 85),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_mid'], 90),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['tom_low'], 100),
            (self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['snare'], 90),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['tom_high'], 80),
            (self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'], 
             self.drum_mapping['tom_mid'], 85),
            (self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_low'], 95),
        ]
        
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 5))
        
        # Final crash with attitude
        self.add_note(midi, self.drum_mapping['crash'], bar, 
                     self.midi_config['ticks_per_beat'] * 4 - self.midi_config['ticks_per_sixteenth'], 
                     100)
    
    # ========== SONG SECTIONS ==========
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Intro - electric blues build-up."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Start with basic blues
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(80, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(85, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 
                             self.get_random_velocity(85, 5))
                # Simple shuffle
                for i in range(4):
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 i * self.midi_config['ticks_per_beat'], 
                                 self.get_random_velocity(70, 8))
            else:
                # Full electric blues pattern
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Verse - steady electric blues groove."""
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1)
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Chorus - powerful electric blues with ride."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_1(midi, bar, 1)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bridge - blues rock attitude."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_2(midi, bar, 1)
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Outro - electric blues ending with power."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                self.create_variation_2(midi, bar, 1)
            else:
                self.create_fill_complex(midi, bar)
