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
        return "Aggressive Argentine rock - Sumo, Los Redonditos, Big Manifesto style: punk-influenced, driving, powerful"
    
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
    
    # ========== SONG SECTIONS ==========
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Intro - builds up energy gradually."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 2:
                # Start minimal - just kick and snare
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(90, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(85, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 
                             self.get_random_velocity(85, 5))
            elif bar < start_bar + 4:
                # Add hi-hats
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(95, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2, 
                             self.get_random_velocity(90, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(90, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 
                             self.get_random_velocity(90, 5))
                
                # Simple hi-hats
                for eighth in range(8):
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(70, 5))
            else:
                # Full pattern for last bars
                self.create_basic_pattern(midi, bar, 1)
            
            # Build-up fill on last bar
            if bar == start_bar + bars - 1:
                self.create_fill_simple(midi, bar)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Verse - steady supportive groove, not too busy."""
        for bar in range(start_bar, start_bar + bars):
            # Steady kick pattern
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(90, 3))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(88, 3))
            
            # Consistent snare
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(95, 3))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(93, 3))
            
            # Subtle ghost notes (less than basic pattern)
            if bar % 8 == 7:  # Only every 8th bar
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(50, 8))
            
            # Steady hi-hats
            for eighth in range(8):
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             eighth * self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(75, 5))
            
            # Simple fill every 8 bars
            if (bar + 1) % 8 == 0 and bar < start_bar + bars - 1:
                self.create_fill_simple(midi, bar)
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Chorus - energetic, driving, full intensity."""
        for bar in range(start_bar, start_bar + bars):
            # More aggressive kick pattern
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(100, 3))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(100, 3))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(92, 5))
            
            # Powerful snare
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 100)
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 100)
            
            # More ghost notes for intensity
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(65, 10))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(70, 10))
            
            # Intense hi-hats
            for sixteenth in range(16):
                if sixteenth % 2 == 0:
                    velocity = 90 if sixteenth % 4 == 0 else 80
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(velocity, 8))
            
            # Crashes for emphasis
            if bar % 4 == 0:
                self.add_note(midi, self.drum_mapping['crash'], bar, 0, 
                             self.get_random_velocity(95, 5))
            
            # Complex fills every 8 bars
            if (bar + 1) % 8 == 0 and bar < start_bar + bars - 1:
                self.create_fill_complex(midi, bar)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bridge - different feel, creates contrast."""
        for bar in range(start_bar, start_bar + bars):
            # Different kick pattern - more syncopated
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(85, 5))
            if bar % 2 == 0:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'] * 3, 
                             self.get_random_velocity(80, 5))
            else:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 
                             self.get_random_velocity(85, 5))
            
            # Snare with different placement
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 
                         self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'], 
                         self.get_random_velocity(88, 5))
            
            # Ride instead of hi-hats for different texture
            for eighth in range(8):
                velocity = 80 if eighth % 2 == 0 else 70
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             eighth * self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(velocity, 8))
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Outro - big ending or fade out."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                # Full intensity for most of outro
                self.create_chorus_section(midi, bar, 1)
            elif bar == start_bar + bars - 2:
                # Build up fill
                self.create_fill_complex(midi, bar)
            else:
                # Final bar - big ending
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 100)
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'], 100)
                self.add_note(midi, self.drum_mapping['crash'], bar, 0, 100, 2.0)
                self.add_note(midi, self.drum_mapping['crash'], bar, 
                             self.midi_config['ticks_per_beat'] * 2, 100, 2.0)
