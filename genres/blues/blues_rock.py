"""
Blues Rock - Cream, Led Zeppelin, Pappo style drum patterns.
Heavy blues with rock power, driving rhythms, and aggressive attitude.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class BluesRockPattern(BasePattern):
    """Blues Rock pattern with Pappo's Blues rock attitude."""
    
    @property
    def genre_name(self) -> str:
        return "Blues Rock"
    
    @property
    def description(self) -> str:
        return "Heavy blues rock - Cream, Led Zeppelin, Pappo style: driving, aggressive, rock power"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic blues rock pattern - driving and powerful."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Driving rock kick with blues feel
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(100, 3))  # Powerful on 1
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))  # Strong on 3
            
            # Add rock-influenced kicks
            if bar % 2 == 1:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(85, 8))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(80, 8))
            
            # Rock snare - powerful and driving
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(100, 3))  # 2
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(100, 3))  # 4
            
            # Blues rock hi-hats - mix of shuffle and straight
            if bar % 4 < 2:  # Shuffle feel in some bars
                for i in range(4):
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 i * self.midi_config['ticks_per_beat'], 
                                 self.get_random_velocity(80, 8))
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 i * self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'] + self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(75, 10))
            else:  # Straight rock feel in others
                for eighth in range(8):
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(80, 8))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - Maximum rock power with crashes."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Aggressive double kicks
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
            
            # Powerful snare
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 100)
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 100)
            
            # Rock hi-hats - straight and driving
            for sixteenth in range(16):
                if sixteenth % 2 == 0:
                    velocity = 90 if sixteenth % 4 == 0 else 80
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(velocity, 8))
            
            # Crashes for rock power
            if bar % 4 == 0:
                self.add_note(midi, self.drum_mapping['crash'], bar, 0, 
                             self.get_random_velocity(95, 5))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Tom work with blues rock attitude."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Standard kick
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(90, 5))
            
            # Snare
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(95, 5))
            
            # Tom work for blues rock flavor
            if bar % 2 == 1:
                self.add_note(midi, self.drum_mapping['tom_high'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(85, 8))
                self.add_note(midi, self.drum_mapping['tom_mid'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(80, 8))
                self.add_note(midi, self.drum_mapping['tom_low'], bar, 
                             self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(90, 8))
            
            # Ride with blues rock feel
            for eighth in range(8):
                velocity = 85 if eighth % 2 == 0 else 75
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             eighth * self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(velocity, 8))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple blues rock fill - driving."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 100)
        
        # Driving snare pattern
        positions = [
            self.midi_config['ticks_per_beat'],
            self.midi_config['ticks_per_beat'] * 2,
            self.midi_config['ticks_per_beat'] * 3,
            self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth']
        ]
        
        for i, pos in enumerate(positions):
            velocity = 90 + i * 5
            self.add_note(midi, self.drum_mapping['snare'], bar, pos, 
                         min(127, velocity))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex blues rock fill - maximum power."""
        # Powerful kick
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 100)
        
        # Power tom cascade
        positions = [
            (self.midi_config['ticks_per_beat'], self.drum_mapping['crash'], 95),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 
             self.drum_mapping['tom_high'], 90),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_mid'], 95),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['tom_low'], 100),
            (self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['snare'], 100),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['tom_high'], 85),
            (self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['crash'], 100),
        ]
        
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 5))
    
    # ========== SONG SECTIONS ==========
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Intro - blues rock power build-up."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Start with blues foundation
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(85, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2, 
                             self.get_random_velocity(80, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(90, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 
                             self.get_random_velocity(88, 5))
            else:
                # Build to full power
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Verse - blues rock groove."""
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1)
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Chorus - maximum blues rock power."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_1(midi, bar, 1)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bridge - tom-heavy blues rock."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_2(midi, bar, 1)
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Outro - epic blues rock ending."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                self.create_variation_1(midi, bar, 1)
            else:
                self.create_fill_complex(midi, bar)
