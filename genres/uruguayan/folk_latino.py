"""
Folk Latino - Latin American folk drum patterns.
Traditional acoustic rhythms with regional influences and storytelling support.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class FolkLatinoPattern(BasePattern):
    """Folk Latino pattern with traditional Latin American characteristics."""
    
    @property
    def genre_name(self) -> str:
        return "Folk Latino"
    
    @property
    def description(self) -> str:
        return "Traditional Latin folk - acoustic rhythms, regional influences, storytelling support"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic folk latino pattern - traditional and acoustic."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Traditional kick - simple and supportive
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(75, 10))
            if bar % 3 == 0:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2, 
                             self.get_random_velocity(70, 10))
            
            # Folk snare - gentle and traditional
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(80, 10))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(78, 10))
            
            # Traditional hi-hats - simple and acoustic
            for eighth in range(8):
                if eighth % 2 == 0:
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(65, 12))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - With regional percussion influences."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(75, 10))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(73, 10))
            
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(80, 10))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(80, 10))
            
            # Regional tom accents
            if bar % 4 == 3:
                self.add_note(midi, self.drum_mapping['tom_mid'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(70, 10))
            
            for eighth in range(8):
                if eighth % 3 == 0:
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(65, 12))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Open acoustic feel."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(75, 10))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(80, 10))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(80, 10))
            
            # Open hi-hats for acoustic atmosphere
            for eighth in range(8):
                if eighth % 4 == 0:
                    self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(70, 12))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple folk fill."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 75)
        for i in range(4):
            pos = self.midi_config['ticks_per_beat'] * 2 + i * self.midi_config['ticks_per_eighth']
            self.add_note(midi, self.drum_mapping['snare'], bar, pos, 75 + i * 2)
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex folk fill."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 80)
        positions = [
            (self.midi_config['ticks_per_beat'], self.drum_mapping['snare'], 75),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['tom_high'], 70),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['tom_mid'], 75),
            (self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['snare'], 80),
        ]
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 8))
    
    # Song sections - simple implementations
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(70, 10))
                if bar % 2 == 1:
                    self.add_note(midi, self.drum_mapping['snare'], bar, 
                                 self.midi_config['ticks_per_beat'] * 3, 75)
            else:
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1)
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_2(midi, bar, 1)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_1(midi, bar, 1)
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                self.create_basic_pattern(midi, bar, 1)
            else:
                self.create_fill_simple(midi, bar)

