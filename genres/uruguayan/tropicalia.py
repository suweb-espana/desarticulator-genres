"""
Tropicalia - Caetano Veloso, Gilberto Gil style drum patterns.
Psychedelic Brazilian movement with experimental arrangements and cultural fusion.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class TropicaliaPattern(BasePattern):
    """Tropicalia pattern with psychedelic Brazilian characteristics."""
    
    @property
    def genre_name(self) -> str:
        return "Tropicalia"
    
    @property
    def description(self) -> str:
        return "Psychedelic Brazilian movement - Caetano Veloso, Gilberto Gil style: experimental, cultural fusion"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic tropicalia pattern - experimental Brazilian fusion."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Experimental kick pattern - tropicalia style
            kick_positions = [0, 6, 11, 14]  # Irregular Brazilian pattern
            for pos in kick_positions:
                if pos < 16:
                    self.add_note(midi, self.drum_mapping['kick'], bar, 
                                 pos * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(80, 10))
            
            # Psychedelic snare placement
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 
                         self.get_random_velocity(85, 8))  # Displaced
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'] * 2, 
                         self.get_random_velocity(83, 8))  # Displaced
            
            # Experimental ghost notes
            if bar % 2 == 1:
                ghost_positions = [
                    self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'],
                    self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'] * 3,
                    self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth']
                ]
                for pos in ghost_positions:
                    self.add_note(midi, self.drum_mapping['snare'], bar, pos, 
                                 self.get_random_velocity(45, 15))
            
            # Psychedelic hi-hats - irregular pattern
            for i in range(16):
                if i % 7 == 0 or i % 5 == 0:  # Overlapping psychedelic cycles
                    velocity = 70 if i % 3 == 0 else 60
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 i * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(velocity, 12))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - More experimental with crashes."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Experimental kick pattern
            kick_positions = [0, 4, 9, 13]  # Different irregular pattern
            for pos in kick_positions:
                if pos < 16:
                    self.add_note(midi, self.drum_mapping['kick'], bar, 
                                 pos * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(85, 10))
            
            # Psychedelic snare with tom accents
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(90, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(88, 8))
            
            # Tom accents for psychedelic flavor
            if bar % 3 == 0:
                self.add_note(midi, self.drum_mapping['tom_high'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(75, 10))
                self.add_note(midi, self.drum_mapping['tom_mid'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(70, 10))
            
            # Experimental hi-hats
            for i in range(16):
                if random.random() < 0.6:  # Random psychedelic pattern
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 i * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(65, 15))
            
            # Psychedelic crashes
            if bar % 8 == 7:
                self.add_note(midi, self.drum_mapping['crash'], bar, 
                             self.midi_config['ticks_per_beat'] * 2, 
                             self.get_random_velocity(85, 10))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Cultural fusion with diverse elements."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Fusion kick pattern
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(80, 8))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(78, 8))
            
            # Cultural fusion snare
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 
                         self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'], 
                         self.get_random_velocity(83, 8))
            
            # Fusion ride pattern
            for eighth in range(8):
                if eighth % 3 != 0:
                    self.add_note(midi, self.drum_mapping['ride'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(75, 10))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple tropicalia fill - experimental."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 80)
        
        # Experimental snare pattern
        positions = [
            self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'],
            self.midi_config['ticks_per_beat'] * 2,
            self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'],
            self.midi_config['ticks_per_beat'] * 3,
            self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth']
        ]
        
        for i, pos in enumerate(positions):
            velocity = 75 + i * 4
            self.add_note(midi, self.drum_mapping['snare'], bar, pos, 
                         self.get_random_velocity(velocity, 8))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex tropicalia fill - psychedelic fusion."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 85)
        
        # Psychedelic tom cascade
        positions = [
            (self.midi_config['ticks_per_sixteenth'] * 3, self.drum_mapping['tom_high'], 80),
            (self.midi_config['ticks_per_sixteenth'] * 7, self.drum_mapping['tom_mid'], 75),
            (self.midi_config['ticks_per_sixteenth'] * 11, self.drum_mapping['tom_low'], 85),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['snare'], 90),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['crash'], 80),
            (self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['open_hh'], 75),
        ]
        
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 10))
    
    # ========== SONG SECTIONS ==========
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Intro - psychedelic Brazilian entrance."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Experimental start
                kick_positions = [0, 10] if bar % 2 == 0 else [6, 14]
                for pos in kick_positions:
                    self.add_note(midi, self.drum_mapping['kick'], bar, 
                                 pos * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(75, 10))
                
                # Sparse snare
                if bar % 2 == 1:
                    self.add_note(midi, self.drum_mapping['snare'], bar, 
                                 self.midi_config['ticks_per_beat'] * 3, 
                                 self.get_random_velocity(80, 8))
            else:
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Verse - experimental Brazilian groove."""
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1)
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Chorus - psychedelic energy."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_1(midi, bar, 1)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bridge - cultural fusion."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_2(midi, bar, 1)
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Outro - experimental Brazilian ending."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                self.create_variation_1(midi, bar, 1)
            else:
                self.create_fill_complex(midi, bar)
