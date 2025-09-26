"""
Murga - Uruguayan carnival drum patterns.
Festive, rhythmic, with marching band influences and celebratory feel.
"""

import random
from midiutil import MIDIFile
from core.base_pattern import BasePattern


class MurgaPattern(BasePattern):
    """Murga pattern with Uruguayan carnival characteristics."""
    
    @property
    def genre_name(self) -> str:
        return "Murga"
    
    @property
    def description(self) -> str:
        return "Uruguayan carnival rhythm - festive, marching band influenced, celebratory"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic murga pattern - marching and festive."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Marching kick pattern - strong and regular
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))  # Strong on 1
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(90, 5))  # On 3
            
            # Add carnival syncopation
            if bar % 2 == 1:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(85, 8))
            
            # Festive snare - carnival style
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(100, 3))  # 2
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(98, 3))  # 4
            
            # Carnival rolls and accents
            if bar % 4 == 3:  # Every 4th bar
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(85, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(80, 8))
            
            # Marching hi-hats - steady and driving
            for eighth in range(8):
                velocity = 85 if eighth % 2 == 0 else 75  # Marching accent
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             eighth * self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(velocity, 8))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - With tom flourishes and crashes."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Marching kick
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(100, 3))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))
            
            # Carnival kick variations
            if bar % 2 == 1:
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(85, 8))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'], 
                             self.get_random_velocity(80, 8))
            
            # Snare with flourishes
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 100)
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 100)
            
            # Tom flourishes for carnival feel
            if bar % 3 == 0:
                self.add_note(midi, self.drum_mapping['tom_high'], bar, 
                             self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(85, 8))
                self.add_note(midi, self.drum_mapping['tom_mid'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                             self.get_random_velocity(80, 8))
            
            # Festive hi-hats
            for sixteenth in range(16):
                if sixteenth % 2 == 0:
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                 self.get_random_velocity(80, 10))
            
            # Crashes for celebration
            if bar % 8 == 7:
                self.add_note(midi, self.drum_mapping['crash'], bar, 0, 
                             self.get_random_velocity(95, 5))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - Open hi-hats and carnival atmosphere."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            # Standard marching kick
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(90, 5))
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
            
            # Mix of open and closed hi-hats for carnival atmosphere
            for eighth in range(8):
                if eighth % 3 == 0:  # Open for celebration
                    self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(85, 8))
                else:  # Closed for rhythm
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(75, 8))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple murga fill - carnival roll."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 95)
        
        # Carnival snare roll
        for i in range(6):
            pos = self.midi_config['ticks_per_beat'] * 2 + i * self.midi_config['ticks_per_sixteenth']
            velocity = 85 + i * 3
            self.add_note(midi, self.drum_mapping['snare'], bar, pos, 
                         min(127, velocity))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex murga fill - carnival celebration."""
        # Kick
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 100)
        
        # Carnival tom celebration
        positions = [
            (self.midi_config['ticks_per_beat'], self.drum_mapping['tom_high'], 90),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_sixteenth'], 
             self.drum_mapping['tom_mid'], 85),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_low'], 95),
            (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['crash'], 100),
            (self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['tom_high'], 80),
            (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['snare'], 100),
            (self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], 
             self.drum_mapping['crash'], 95),
        ]
        
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 5))
    
    # ========== SONG SECTIONS ==========
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Intro - carnival build-up."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Start with simple marching
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(85, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'], 80)
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 80)
                # Simple hi-hats
                for eighth in range(8):
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 self.get_random_velocity(70, 5))
            else:
                # Full carnival pattern
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Verse - steady carnival rhythm."""
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1)
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Chorus - festive carnival energy."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_1(midi, bar, 1)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bridge - different carnival feel."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_2(midi, bar, 1)
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Outro - carnival finale."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                self.create_variation_1(midi, bar, 1)
            else:
                self.create_fill_complex(midi, bar)
