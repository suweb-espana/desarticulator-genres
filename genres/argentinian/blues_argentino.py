"""
Blues Argentino - Pappo's Blues style drum patterns.
Heavy blues with rock attitude and multiple authentic variations.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class BluesArgentinoPattern(BasePattern):
    """Blues Argentino pattern with authentic Pappo's Blues characteristics."""
    
    @property
    def genre_name(self) -> str:
        return "Blues Argentino"
    
    @property
    def description(self) -> str:
        return "Heavy Argentine blues - Pappo's Blues style: shuffle feel, blues rock attitude"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic Blues Argentino pattern - shuffle feel with rock attitude."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Heavy kick pattern - Pappo style blues rock
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))  # Strong on 1
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(90, 5))  # On 3
            
            # Powerful snare - blues rock style
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(100, 3))  # 2
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(98, 3))  # 4
            
            # Shuffle feel on hi-hats - classic blues
            for i in range(4):
                # Shuffle triplet feel (long-short pattern)
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             i * self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(75, 5))  # On beat
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             i * self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'] + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(70, 5))  # Shuffle off-beat
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - With ride cymbal and syncopated kicks."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Syncopated kick pattern
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))
            if bar % 3 == 0:  # Variation every 3rd bar
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(80, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(90, 5))
            
            # Snare
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(100, 3))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(98, 3))
            
            # Ride pattern for variation
            for i in range(4):
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             i * self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(80, 5))
                if i % 2 == 1:  # Bell on 2 and 4
                    self.add_note(midi, self.drum_mapping['ride'], bar, 
                                 i * self.midi_config['ticks_per_beat'], 
                                 self.get_random_velocity(85, 5))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Open hi-hats and ghost notes."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Standard kick
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(90, 5))
            
            # Snare with ghost notes
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(100, 3))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(98, 3))
            
            # Ghost notes for groove
            if bar % 2 == 1:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(55, 10))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(50, 10))
            
            # Mix of closed and open hi-hats
            for i in range(4):
                if i % 2 == 0:  # Closed on 1 and 3
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 i * self.midi_config['ticks_per_beat'], 
                                 self.get_random_velocity(75, 5))
                else:  # Open on 2 and 4
                    self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                                 i * self.midi_config['ticks_per_beat'], 
                                 self.get_random_velocity(80, 5))
                
                # Shuffle off-beats
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             i * self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'] + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(65, 8))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple blues fill - snare and hi-hat."""
        # Basic pattern for first half
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                     self.get_random_velocity(95, 5))
        self.add_note(midi, self.drum_mapping['snare'], bar, 
                     self.midi_config['ticks_per_beat'], 
                     self.get_random_velocity(95, 5))
        
        # Simple fill in second half
        positions = [
            self.midi_config['ticks_per_beat'] * 2,
            self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'],
            self.midi_config['ticks_per_beat'] * 3,
            self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth']
        ]
        
        for i, pos in enumerate(positions):
            velocity = 85 + i * 3  # Building intensity
            self.add_note(midi, self.drum_mapping['snare'], bar, pos, velocity)
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex blues fill - tom cascade with blues flavor."""
        # Kick on 1
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                     self.get_random_velocity(100, 3))
        
        # Blues-style tom fill
        positions = [
            (self.midi_config['ticks_per_beat'], self.drum_mapping['snare'], 95),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_high'], 90),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['tom_mid'], 95),
            (self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_low'], 100),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['snare'], 100),
            (self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_high'], 85),
        ]
        
        for position, drum, velocity in positions:
            self.add_note(midi, drum, bar, position, 
                         self.get_random_velocity(velocity, 5))
        
        # Final snare roll
        for i in range(4):
            pos = self.midi_config['ticks_per_beat'] * 4 - self.midi_config['ticks_per_sixteenth'] * (4 - i)
            self.add_note(midi, self.drum_mapping['snare'], bar, pos, 
                         self.get_random_velocity(95 + i * 5, 3))
    
    # ========== SONG SECTIONS ==========
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Intro - blues build-up."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Start with just kick and snare
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(85, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(90, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 
                             self.get_random_velocity(88, 5))
            else:
                # Add shuffle feel
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Verse - steady blues groove."""
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1)
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Chorus - more intense blues."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_1(midi, bar, 1)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bridge - different blues feel."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_2(midi, bar, 1)
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Outro - blues ending."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                self.create_variation_1(midi, bar, 1)
            else:
                self.create_fill_complex(midi, bar)
