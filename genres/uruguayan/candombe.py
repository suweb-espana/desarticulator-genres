"""
Candombe - Traditional Uruguayan drum patterns.
Afro-Uruguayan rhythm with complex polyrhythmic patterns and call-and-response.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class CandonbePattern(BasePattern):
    """Candombe pattern with authentic Uruguayan characteristics."""
    
    @property
    def genre_name(self) -> str:
        return "Candombe"
    
    @property
    def description(self) -> str:
        return "Traditional Uruguayan rhythm - Afro-Uruguayan polyrhythmic patterns, call-and-response"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic candombe pattern - polyrhythmic and syncopated."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Candombe kick pattern - irregular, polyrhythmic
            kick_positions = [0, 6, 10, 14]  # Syncopated pattern in sixteenths
            for pos in kick_positions:
                if pos < 16:
                    self.add_note(midi, self.drum_mapping['kick'], bar, 
                                 pos * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(85, 8))
            
            # Add variation every few bars
            if bar % 3 == 0:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'] * 2, 
                             self.get_random_velocity(80, 8))
            
            # Candombe snare - call and response pattern
            if bar % 2 == 0:  # Call
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(90, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(85, 8))
            else:  # Response
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(88, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 
                             self.get_random_velocity(92, 5))
            
            # Polyrhythmic hi-hats - complex African-influenced pattern
            for i in range(16):
                if i % 5 == 0 or i % 7 == 0:  # Overlapping cycles
                    velocity = 75 if i % 3 == 0 else 65  # Accent pattern
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 i * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(velocity, 10))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - More intense with tom work."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # More aggressive kick pattern
            kick_positions = [0, 3, 7, 11, 15]  # Denser pattern
            for pos in kick_positions:
                if pos < 16:
                    self.add_note(midi, self.drum_mapping['kick'], bar, 
                                 pos * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(90, 8))
            
            # Call and response with toms
            if bar % 2 == 0:
                # Call with snare and high tom
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'], 95)
                self.add_note(midi, self.drum_mapping['tom_high'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(80, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 90)
            else:
                # Response with mid and low toms
                self.add_note(midi, self.drum_mapping['tom_mid'], bar, 
                             self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(85, 8))
                self.add_note(midi, self.drum_mapping['tom_low'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(90, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 95)
            
            # Complex polyrhythmic hi-hats
            for i in range(16):
                if i % 3 == 0 or i % 7 == 0:
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 i * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(70, 12))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Ride pattern with African influences."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Syncopated kick
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(85, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'] * 3, 
                         self.get_random_velocity(80, 8))
            
            # Snare with African feel
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'] * 2, 
                         self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'], 
                         self.get_random_velocity(88, 5))
            
            # Ride with bell accents - African influence
            for eighth in range(8):
                velocity = 80 if eighth % 2 == 0 else 70
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             eighth * self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(velocity, 8))
            
            # Bell accents on complex pattern
            bell_positions = [4, 10, 14]  # Irregular bell pattern
            for pos in bell_positions:
                if pos < 16:
                    self.add_note(midi, self.drum_mapping['ride'], bar, 
                                 pos * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(85, 5))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple candombe fill - tom call and response."""
        # Kick on 1
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 90)
        
        # Call and response tom pattern
        positions = [
            (self.midi_config['ticks_per_beat'], self.drum_mapping['tom_high'], 85),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_mid'], 80),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['tom_low'], 90),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['snare'], 95),
        ]
        
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 8))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex candombe fill - polyrhythmic African-style."""
        # Kick
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 95)
        
        # Complex polyrhythmic tom pattern
        positions = [
            (self.midi_config['ticks_per_sixteenth'] * 3, self.drum_mapping['tom_high'], 85),
            (self.midi_config['ticks_per_sixteenth'] * 7, self.drum_mapping['tom_mid'], 90),
            (self.midi_config['ticks_per_sixteenth'] * 10, self.drum_mapping['tom_low'], 95),
            (self.midi_config['ticks_per_sixteenth'] * 13, self.drum_mapping['tom_high'], 80),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['snare'], 100),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['tom_mid'], 85),
            (self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_low'], 90),
        ]
        
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 8))
    
    # ========== SONG SECTIONS ==========
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Intro - candombe build-up."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Start with basic polyrhythm
                kick_positions = [0, 10]  # Simple start
                for pos in kick_positions:
                    self.add_note(midi, self.drum_mapping['kick'], bar, 
                                 pos * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(80, 5))
                
                # Simple snare
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'], 85)
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 85)
            else:
                # Full candombe pattern
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Verse - steady candombe groove."""
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1)
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Chorus - intense candombe with toms."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_1(midi, bar, 1)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bridge - ride pattern with African influences."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_2(midi, bar, 1)
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Outro - candombe ending with polyrhythmic fills."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                self.create_variation_1(midi, bar, 1)
            else:
                self.create_fill_complex(midi, bar)
