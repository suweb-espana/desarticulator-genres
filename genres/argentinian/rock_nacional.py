"""
Rock Nacional - Sumo, Los Redonditos de Ricota style drum patterns.
Aggressive, driving, punk-influenced with multiple variations.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class RockNacionalPattern(BasePattern):
    """Rock Nacional pattern with authentic Argentine rock characteristics."""
    
    @property
    def genre_name(self) -> str:
        return "Rock Nacional"
    
    @property
    def description(self) -> str:
        return "Aggressive Argentine rock - Sumo, Los Redonditos style: punk-influenced, driving, powerful"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic Rock Nacional pattern - aggressive and driving."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Strong kick pattern
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(100, 5))  # Strong on 1
            
            if bar % 2 == 0:  # Variation every other bar
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(95, 5))
            
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(98, 5))  # Strong on 3
            
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(90, 5))
            
            # Powerful snare - characteristic of Argentine rock
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(100, 3))  # 2
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(100, 3))  # 4
            
            # Ghost notes for groove (Sumo influence)
            if bar % 4 != 0:  # Add ghost notes in some bars
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(60, 10))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(65, 10))
            
            # Driving hi-hats - punk influenced
            for sixteenth in range(16):
                if sixteenth % 2 == 0:  # On downbeats and upbeats
                    velocity = 85 if sixteenth % 4 == 0 else 75  # Accent on beats
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(velocity, 8))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - More aggressive with double kicks."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Double kick pattern
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(100, 3))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_sixteenth'], 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(100, 3))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'], 
                         self.get_random_velocity(95, 5))
            
            # Snare with extra hits
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 100)
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 100)
            
            # Extra snare for intensity
            if bar % 2 == 1:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(85, 5))
            
            # Intense hi-hats
            for sixteenth in range(16):
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             sixteenth * self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(80, 10))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Ride pattern with crashes."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Standard kick
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))
            
            # Snare
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(98, 5))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(98, 5))
            
            # Ride pattern instead of hi-hats
            for eighth in range(8):
                velocity = 85 if eighth % 2 == 0 else 75
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             eighth * self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(velocity, 8))
            
            # Occasional crashes
            if bar % 4 == 3:
                self.add_note(midi, self.drum_mapping['crash'], bar, 0, 
                             self.get_random_velocity(90, 5))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple fill - snare rolls."""
        # Basic pattern for first half
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 95)
        self.add_note(midi, self.drum_mapping['snare'], bar, 
                     self.midi_config['ticks_per_beat'], 95)
        
        # Snare roll in second half
        for sixteenth in range(8, 16):
            velocity = 90 + (sixteenth - 8) * 2  # Building intensity
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         sixteenth * self.midi_config['ticks_per_sixteenth'], 
                         min(127, velocity))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex fill - tom cascades with crash."""
        # Kick on 1
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 100)
        
        # Tom cascade
        positions = [
            (self.midi_config['ticks_per_beat'], self.drum_mapping['tom_high'], 95),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_mid'], 90),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['tom_low'], 100),
            (self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_high'], 85),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['tom_mid'], 95),
            (self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_low'], 100),
        ]
        
        for position, drum, velocity in positions:
            self.add_note(midi, drum, bar, position, 
                         self.get_random_velocity(velocity, 5))
        
        # Final snare hits
        self.add_note(midi, self.drum_mapping['snare'], bar, 
                     self.midi_config['ticks_per_beat'] * 4 - self.midi_config['ticks_per_sixteenth'], 105)
        
        # Crash on next bar would be handled by the main pattern
