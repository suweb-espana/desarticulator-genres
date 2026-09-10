"""
Dub drum pattern generator with minimal, spaced-out rhythms.
Based on King Tubby, Lee Perry, and traditional dub production.
"""

from core.base_pattern import BasePattern
from midiutil import MIDIFile


class DubPattern(BasePattern):
    """Dub drum patterns with minimal, spaced-out rhythms and hypnotic repetition."""
    
    @property
    def genre_name(self) -> str:
        return "Dub"
    
    @property
    def description(self) -> str:
        return "Minimal dub rhythms with spaced-out patterns, one drop emphasis, and hypnotic repetition inspired by King Tubby and Lee Perry"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Create basic dub pattern - simple and direct for guitar accompaniment."""
        for bar in range(start_bar, start_bar + bars):
            # One drop - kick on beat 3 (strong, characteristic dub)
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(98, 5))
            
            # Snare on beats 2 and 4 (clear backbeat for guitar)
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(92, 6))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(92, 6))
            
            # Hi-hat skank pattern (off-beat eighth notes, essential dub)
            for beat in [0.5, 1.5, 2.5, 3.5]:
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat), 
                             self.get_random_velocity(75, 6))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Create variation with kick on beat 1 and 3 - more driving for guitar."""
        for bar in range(start_bar, start_bar + bars):
            # Kick on beats 1 and 3 (more driving, works better with guitar chords)
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(92, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(98, 5))
            
            # Snare backbeat (clear and strong)
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(92, 6))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(92, 6))
            
            # Hi-hat skank pattern
            for beat in [0.5, 1.5, 2.5, 3.5]:
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat), 
                             self.get_random_velocity(75, 6))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Create variation with kick on beat 1 - simple and direct."""
        for bar in range(start_bar, start_bar + bars):
            # Kick on beat 1 only (alternative to one drop)
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))
            
            # Snare backbeat (clear)
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(92, 6))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(92, 6))
            
            # Hi-hat skank pattern
            for beat in [0.5, 1.5, 2.5, 3.5]:
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat), 
                             self.get_random_velocity(75, 6))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Create simple dub fill - minimal and direct."""
        # Basic pattern for most of the bar
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 2, 
                     self.get_random_velocity(95, 5))
        self.add_note(midi, self.drum_mapping['snare'], bar, 
                     self.midi_config['ticks_per_beat'], 
                     self.get_random_velocity(90, 6))
        
        # Simple tom fill on beat 4
        self.add_note(midi, self.drum_mapping['tom_high'], bar, 
                     self.midi_config['ticks_per_beat'] * 3.5, 
                     self.get_random_velocity(80, 5))
        self.add_note(midi, self.drum_mapping['snare'], bar, 
                     self.midi_config['ticks_per_beat'] * 3, 
                     self.get_random_velocity(90, 6))
        
        # Hi-hat skank
        for beat in [0.5, 1.5, 2.5]:
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                         int(self.midi_config['ticks_per_beat'] * beat), 
                         self.get_random_velocity(75, 6))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Create complex dub fill with tom rolls and crash."""
        # Basic pattern for first half
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 2, 
                     self.get_random_velocity(95, 5))
        self.add_note(midi, self.drum_mapping['snare'], bar, 
                     self.midi_config['ticks_per_beat'], 
                     self.get_random_velocity(90, 6))
        
        # Tom roll starting beat 3
        self.add_note(midi, self.drum_mapping['tom_low'], bar, 
                     self.midi_config['ticks_per_beat'] * 2.5, 
                     self.get_random_velocity(82, 5))
        self.add_note(midi, self.drum_mapping['tom_mid'], bar, 
                     self.midi_config['ticks_per_beat'] * 2.75, 
                     self.get_random_velocity(82, 5))
        self.add_note(midi, self.drum_mapping['tom_high'], bar, 
                     self.midi_config['ticks_per_beat'] * 3, 
                     self.get_random_velocity(82, 5))
        self.add_note(midi, self.drum_mapping['snare'], bar, 
                     self.midi_config['ticks_per_beat'] * 3.25, 
                     self.get_random_velocity(90, 6))
        self.add_note(midi, self.drum_mapping['tom_high'], bar, 
                     self.midi_config['ticks_per_beat'] * 3.5, 
                     self.get_random_velocity(82, 5))
        self.add_note(midi, self.drum_mapping['tom_mid'], bar, 
                     self.midi_config['ticks_per_beat'] * 3.75, 
                     self.get_random_velocity(82, 5))
        
        # Crash accent
        self.add_note(midi, self.drum_mapping['crash'], bar, 
                     self.midi_config['ticks_per_beat'] * 3.5, 
                     self.get_random_velocity(92, 5), 1.5)
        
        # Hi-hat skank
        for beat in [0.5, 1.5, 2.5]:
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                         int(self.midi_config['ticks_per_beat'] * beat), 
                         self.get_random_velocity(75, 6))
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Create dub intro - simple build up."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 2:
                # Start with just hi-hat
                for beat in [0.5, 1.5, 2.5, 3.5]:
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 int(self.midi_config['ticks_per_beat'] * beat), 
                                 self.get_random_velocity(60, 5))
            elif bar < start_bar + 4:
                # Add snare
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(80, 6))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 
                             self.get_random_velocity(80, 6))
                for beat in [0.5, 1.5, 2.5, 3.5]:
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 int(self.midi_config['ticks_per_beat'] * beat), 
                                 self.get_random_velocity(65, 5))
            elif bar < start_bar + 6:
                # Add kick (one drop)
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2, 
                             self.get_random_velocity(88, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(85, 6))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 
                             self.get_random_velocity(85, 6))
                for beat in [0.5, 1.5, 2.5, 3.5]:
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 int(self.midi_config['ticks_per_beat'] * beat), 
                                 self.get_random_velocity(70, 5))
            else:
                # Full pattern
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Create dub verse - simple and steady for guitar accompaniment."""
        for bar in range(start_bar, start_bar + bars):
            # One drop pattern
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))
            
            # Snare backbeat (clear and strong)
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(90, 6))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(90, 6))
            
            # Hi-hat skank pattern
            for beat in [0.5, 1.5, 2.5, 3.5]:
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat), 
                             self.get_random_velocity(73, 6))
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Create dub chorus - driving pattern for guitar chords."""
        for bar in range(start_bar, start_bar + bars):
            # More driving kick pattern (beats 1 and 3)
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(92, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(98, 5))
            
            # Snare backbeat (strong and clear)
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(95, 5))
            
            # Hi-hat skank pattern
            for beat in [0.5, 1.5, 2.5, 3.5]:
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat), 
                             self.get_random_velocity(78, 6))
            
            # Occasional crash accent
            if bar % 4 == 0:
                self.add_note(midi, self.drum_mapping['crash'], bar, 
                             self.midi_config['ticks_per_beat'] * 3.5, 
                             self.get_random_velocity(90, 5), 0.8)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Create dub bridge - simple variation for contrast."""
        for bar in range(start_bar, start_bar + bars):
            # Kick on beat 1 only (different feel)
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(90, 5))
            
            # Snare backbeat
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(88, 6))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(88, 6))
            
            # Hi-hat skank pattern
            for beat in [0.5, 1.5, 2.5, 3.5]:
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat), 
                             self.get_random_velocity(73, 6))
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Create dub outro - simple fade out."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Full pattern
                self.create_basic_pattern(midi, bar, 1)
            elif bar < start_bar + 6:
                # Reduce to kick and snare
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2, 
                             self.get_random_velocity(80, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(75, 6))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 
                             self.get_random_velocity(75, 6))
                for beat in [0.5, 1.5, 2.5, 3.5]:
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 int(self.midi_config['ticks_per_beat'] * beat), 
                                 self.get_random_velocity(65, 6))
            else:
                # Just hi-hat fading
                for beat in [0.5, 1.5, 2.5, 3.5]:
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 int(self.midi_config['ticks_per_beat'] * beat), 
                                 self.get_random_velocity(55, 5))


