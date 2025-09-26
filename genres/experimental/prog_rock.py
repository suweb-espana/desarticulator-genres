"""
Prog Rock - Frank Zappa, King Crimson style drum patterns.
Complex, experimental, with irregular time signatures and sophisticated arrangements.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class ProgRockPattern(BasePattern):
    """Prog Rock pattern with Frank Zappa-style complexity."""
    
    @property
    def genre_name(self) -> str:
        return "Prog Rock"
    
    @property
    def description(self) -> str:
        return "Complex progressive rock - Frank Zappa, King Crimson style: irregular patterns, sophisticated"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic prog rock pattern - complex and irregular."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Complex kick patterns - Zappa style
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'] * 3, 
                         self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'], 
                         self.get_random_velocity(85, 5))
            
            # Snare on 2 and 4 with variations
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(100, 3))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(98, 3))
            
            # Irregular hi-hat patterns - complex polyrhythms
            for sixteenth in range(16):
                if sixteenth % 3 == 0 or sixteenth % 5 == 0:  # Irregular spacing
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(75, 8))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - More complex with ride and toms."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Asymmetrical kick pattern
            kick_positions = [0, 5, 11, 14]  # Irregular sixteenths
            for pos in kick_positions:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             pos * self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(90, 5))
            
            # Displaced snare
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 
                         self.get_random_velocity(100, 3))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'] * 2, 
                         self.get_random_velocity(95, 5))
            
            # Ride pattern with complex rhythms
            for eighth in range(8):
                if eighth % 3 != 0:
                    self.add_note(midi, self.drum_mapping['ride'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(80, 8))
            
            # Tom accents for complexity
            if bar % 4 == 3:
                self.add_note(midi, self.drum_mapping['tom_high'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'] * 2, 
                             self.get_random_velocity(85, 5))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Polyrhythmic with crashes."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Polyrhythmic kick in 7/8 feel over 4/4
            kick_pattern = [0, 7, 10, 15]  # Creates 7/8 feel
            for pos in kick_pattern:
                if pos < 16:
                    self.add_note(midi, self.drum_mapping['kick'], bar, 
                                 pos * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(95, 5))
            
            # Snare in overlapping rhythm
            snare_positions = [4, 12] if bar % 2 == 0 else [6, 14]
            for pos in snare_positions:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             pos * self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(100, 3))
            
            # Complex hi-hat polyrhythms
            for i in range(16):
                if i % 5 == 0 or i % 7 == 0:  # Overlapping cycles
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 i * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(70, 8))
            
            # Crashes for emphasis
            if bar % 8 == 7:
                self.add_note(midi, self.drum_mapping['crash'], bar, 0, 
                             self.get_random_velocity(95, 5))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple prog fill - tom work."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 95)
        
        # Progressive tom pattern
        positions = [
            (self.midi_config['ticks_per_beat'], self.drum_mapping['tom_high']),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], self.drum_mapping['tom_mid']),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['tom_low']),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['snare']),
        ]
        
        for pos, drum in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(90, 5))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex prog fill - Zappa-style chaos."""
        # Irregular tom cascade
        positions = [
            (0, self.drum_mapping['kick'], 100),
            (self.midi_config['ticks_per_sixteenth'] * 3, self.drum_mapping['tom_high'], 90),
            (self.midi_config['ticks_per_sixteenth'] * 7, self.drum_mapping['tom_mid'], 95),
            (self.midi_config['ticks_per_sixteenth'] * 10, self.drum_mapping['tom_low'], 100),
            (self.midi_config['ticks_per_sixteenth'] * 13, self.drum_mapping['snare'], 105),
            (self.midi_config['ticks_per_sixteenth'] * 15, self.drum_mapping['crash'], 100),
        ]
        
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 5))
    
    # ========== SONG SECTIONS ==========
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Intro - progressive build-up."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 3:
                # Start minimal and complex
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(85, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(80, 5))
            elif bar < start_bar + 6:
                # Add complexity gradually
                self.create_basic_pattern(midi, bar, 1)
            else:
                # Full complexity
                self.create_variation_1(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Verse - complex but supportive."""
        for bar in range(start_bar, start_bar + bars):
            if bar % 4 < 2:
                self.create_basic_pattern(midi, bar, 1)
            else:
                self.create_variation_1(midi, bar, 1)
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Chorus - maximum complexity."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_2(midi, bar, 1)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bridge - completely different feel."""
        for bar in range(start_bar, start_bar + bars):
            # Completely different pattern for contrast
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_sixteenth'] * 2, 
                         self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'] * 3, 
                         self.get_random_velocity(85, 5))
            
            # Ride-heavy pattern
            for eighth in range(8):
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             eighth * self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(75, 8))
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Outro - epic progressive ending."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                self.create_variation_2(midi, bar, 1)
            else:
                self.create_fill_complex(midi, bar)
