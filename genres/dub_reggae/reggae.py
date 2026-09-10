"""
Reggae drum pattern generator with authentic Jamaican characteristics.
Based on Bob Marley, Peter Tosh, and traditional reggae drumming.
"""

from core.base_pattern import BasePattern
from midiutil import MIDIFile


class ReggaePattern(BasePattern):
    """Reggae drum patterns with one drop, skank, and shuffle feel."""
    
    @property
    def genre_name(self) -> str:
        return "Reggae"
    
    @property
    def description(self) -> str:
        return "Authentic Jamaican reggae with one drop rhythm, skank patterns, shuffle feel, and traditional reggae drumming techniques"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Create basic reggae pattern with one drop rhythm."""
        for bar in range(start_bar, start_bar + bars):
            # One drop - kick on beat 3 (off-beat emphasis)
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))
            
            # Snare on beats 2 and 4 (backbeat)
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(90, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(90, 8))
            
            # Hi-hat skank pattern (off-beat eighth notes)
            for beat in [0.5, 1.5, 2.5, 3.5]:
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat), 
                             self.get_random_velocity(75, 10))
            
            # Ride cymbal on steady eighth notes
            for beat in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]:
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat), 
                             self.get_random_velocity(70, 8))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Create variation with additional kick on beat 1."""
        for bar in range(start_bar, start_bar + bars):
            # Kick on beats 1 and 3 (more driving)
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))
            
            # Snare backbeat
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(90, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(90, 8))
            
            # Hi-hat with ghost notes
            for beat in [0.5, 1.5, 2.5, 3.5]:
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat), 
                             self.get_random_velocity(75, 10))
            
            # Ride with slight shuffle
            for beat in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]:
                shuffle_offset = 5 if beat % 1 == 0.5 else 0
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat) + shuffle_offset, 
                             self.get_random_velocity(70, 8))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Create variation with syncopated kick pattern."""
        for bar in range(start_bar, start_bar + bars):
            # Syncopated kick pattern
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 1.5, 
                         self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2.5, 
                         self.get_random_velocity(95, 5))
            
            # Snare with ghost notes
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(90, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(90, 8))
            
            # Ghost snare on off-beats
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 0.5, 
                         self.get_random_velocity(45, 5))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 2.5, 
                         self.get_random_velocity(45, 5))
            
            # Hi-hat skank with variations
            for beat in [0.5, 1.5, 2.5, 3.5]:
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat), 
                             self.get_random_velocity(75, 10))
            
            # Ride with reggae shuffle
            for beat in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]:
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat), 
                             self.get_random_velocity(70, 8))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Create simple reggae fill with tom rolls."""
        # Basic pattern for most of the bar
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 2, 
                     self.get_random_velocity(95, 5))
        self.add_note(midi, self.drum_mapping['snare'], bar, 
                     self.midi_config['ticks_per_beat'], 
                     self.get_random_velocity(90, 8))
        self.add_note(midi, self.drum_mapping['snare'], bar, 
                     self.midi_config['ticks_per_beat'] * 3, 
                     self.get_random_velocity(90, 8))
        
        # Simple tom fill on beat 4
        self.add_note(midi, self.drum_mapping['tom_high'], bar, 
                     self.midi_config['ticks_per_beat'] * 3.5, 
                     self.get_random_velocity(80, 5))
        self.add_note(midi, self.drum_mapping['tom_mid'], bar, 
                     self.midi_config['ticks_per_beat'] * 3.75, 
                     self.get_random_velocity(80, 5))
        
        # Hi-hat skank throughout
        for beat in [0.5, 1.5, 2.5, 3.5]:
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                         int(self.midi_config['ticks_per_beat'] * beat), 
                         self.get_random_velocity(75, 10))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Create complex reggae fill with tom rolls and crashes."""
        # Basic pattern for first half
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 2, 
                     self.get_random_velocity(95, 5))
        self.add_note(midi, self.drum_mapping['snare'], bar, 
                     self.midi_config['ticks_per_beat'], 
                     self.get_random_velocity(90, 8))
        
        # Complex tom roll starting beat 3
        self.add_note(midi, self.drum_mapping['tom_low'], bar, 
                     self.midi_config['ticks_per_beat'] * 2.5, 
                     self.get_random_velocity(85, 5))
        self.add_note(midi, self.drum_mapping['tom_mid'], bar, 
                     self.midi_config['ticks_per_beat'] * 2.75, 
                     self.get_random_velocity(85, 5))
        self.add_note(midi, self.drum_mapping['tom_high'], bar, 
                     self.midi_config['ticks_per_beat'] * 3, 
                     self.get_random_velocity(85, 5))
        self.add_note(midi, self.drum_mapping['snare'], bar, 
                     self.midi_config['ticks_per_beat'] * 3.25, 
                     self.get_random_velocity(90, 8))
        self.add_note(midi, self.drum_mapping['tom_high'], bar, 
                     self.midi_config['ticks_per_beat'] * 3.5, 
                     self.get_random_velocity(85, 5))
        self.add_note(midi, self.drum_mapping['tom_mid'], bar, 
                     self.midi_config['ticks_per_beat'] * 3.75, 
                     self.get_random_velocity(85, 5))
        
        # Crash on beat 4
        self.add_note(midi, self.drum_mapping['crash'], bar, 
                     self.midi_config['ticks_per_beat'] * 3.5, 
                     self.get_random_velocity(100, 5), 1.5)
        
        # Hi-hat skank with variations
        for beat in [0.5, 1.5, 2.5]:
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                         int(self.midi_config['ticks_per_beat'] * beat), 
                         self.get_random_velocity(75, 10))
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Create reggae intro with building energy."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 2:
                # Very minimal intro - just hi-hat
                for beat in [0.5, 1.5, 2.5, 3.5]:
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 int(self.midi_config['ticks_per_beat'] * beat), 
                                 self.get_random_velocity(60, 5))
            elif bar < start_bar + 4:
                # Add ride cymbal
                for beat in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]:
                    self.add_note(midi, self.drum_mapping['ride'], bar, 
                                 int(self.midi_config['ticks_per_beat'] * beat), 
                                 self.get_random_velocity(65, 5))
                for beat in [0.5, 1.5, 2.5, 3.5]:
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 int(self.midi_config['ticks_per_beat'] * beat), 
                                 self.get_random_velocity(60, 5))
            else:
                # Full pattern
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Create reggae verse with steady groove."""
        for bar in range(start_bar, start_bar + bars):
            # One drop pattern
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(90, 5))
            
            # Snare backbeat
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(85, 8))
            
            # Hi-hat skank
            for beat in [0.5, 1.5, 2.5, 3.5]:
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat), 
                             self.get_random_velocity(70, 8))
            
            # Ride cymbal
            for beat in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]:
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat), 
                             self.get_random_velocity(65, 8))
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Create reggae chorus with more energy and crashes."""
        for bar in range(start_bar, start_bar + bars):
            # More driving kick pattern
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(85, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))
            
            # Snare backbeat with more punch
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(95, 5))
            
            # Hi-hat skank with more presence
            for beat in [0.5, 1.5, 2.5, 3.5]:
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat), 
                             self.get_random_velocity(80, 8))
            
            # Ride cymbal with more energy
            for beat in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]:
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat), 
                             self.get_random_velocity(75, 8))
            
            # Occasional crash accents
            if bar % 4 == 0:
                self.add_note(midi, self.drum_mapping['crash'], bar, 
                             self.midi_config['ticks_per_beat'] * 3.5, 
                             self.get_random_velocity(90, 5), 0.5)
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Create reggae bridge with different feel."""
        for bar in range(start_bar, start_bar + bars):
            # Syncopated kick pattern for bridge
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 1.5, 
                         self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2.5, 
                         self.get_random_velocity(90, 5))
            
            # Snare with ghost notes
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(85, 8))
            
            # Ghost snare accents
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 0.5, 
                         self.get_random_velocity(50, 5))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 2.5, 
                         self.get_random_velocity(50, 5))
            
            # Hi-hat skank
            for beat in [0.5, 1.5, 2.5, 3.5]:
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat), 
                             self.get_random_velocity(70, 8))
            
            # Ride cymbal
            for beat in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]:
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                             int(self.midi_config['ticks_per_beat'] * beat), 
                             self.get_random_velocity(70, 8))
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Create reggae outro with fading energy."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Full pattern
                self.create_basic_pattern(midi, bar, 1)
            elif bar < start_bar + 6:
                # Reduce to basic elements
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2, 
                             self.get_random_velocity(85, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'], 
                             self.get_random_velocity(80, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3, 
                             self.get_random_velocity(80, 8))
                
                for beat in [0.5, 1.5, 2.5, 3.5]:
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 int(self.midi_config['ticks_per_beat'] * beat), 
                                 self.get_random_velocity(65, 8))
            else:
                # Just hi-hat and ride
                for beat in [0.5, 1.5, 2.5, 3.5]:
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 int(self.midi_config['ticks_per_beat'] * beat), 
                                 self.get_random_velocity(60, 5))
                
                for beat in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]:
                    self.add_note(midi, self.drum_mapping['ride'], bar, 
                                 int(self.midi_config['ticks_per_beat'] * beat), 
                                 self.get_random_velocity(60, 5))

