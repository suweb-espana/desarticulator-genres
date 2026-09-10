"""
Fandango - Traditional Andalusian song in 3/4 time.
Traditional Spanish folk song with waltz-like 3/4 rhythm and traditional character.
"""

from core.base_pattern import BasePattern
from midiutil import MIDIFile


class FandangoPattern(BasePattern):
    """Fandango pattern - traditional Andalusian song in 3/4."""
    
    @property
    def genre_name(self) -> str:
        return "Fandango"
    
    @property
    def description(self) -> str:
        return "Traditional Andalusian song - waltz-like 3/4 rhythm, traditional character, classic Spanish folk song patterns"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic fandango pattern - 3/4 waltz rhythm with traditional character."""
        for bar in range(start_bar, start_bar + bars):
            # Fandango compás - 3/4 waltz rhythm
            # Strong beats: 1, 2, 3 (waltz pattern)
            # Traditional emphasis: 1 (strong), 2 (medium), 3 (light)
            
            # Kick pattern - waltz rhythm
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(90, 5))  # Beat 1 - strong
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(75, 5))  # Beat 2 - medium
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(65, 5))  # Beat 3 - light
            
            # Fandango palmas - traditional pattern
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(80, 8))  # Off-beat 1
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(75, 8))  # Off-beat 2
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(70, 8))  # Off-beat 3
            
            # Traditional hi-hats for fandango texture
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(60, 10))  # Off-beat 1
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(60, 10))  # Off-beat 2
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(60, 10))  # Off-beat 3
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Fandango variation 1 - more traditional with additional accents."""
        for bar in range(start_bar, start_bar + bars):
            # Traditional fandango with more accents
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))  # Beat 1 - traditional
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(80, 5))  # Beat 2 - traditional
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(70, 5))  # Beat 3 - traditional
            
            # Traditional palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(80, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(80, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(80, 8))
            
            # Ride cymbal for traditional feel
            for beat in [1, 2, 3]:  # On-beats
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(65, 10))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Fandango variation 2 - classic with folk ornaments."""
        for bar in range(start_bar, start_bar + bars):
            # Classic fandango with folk ornaments
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(85, 5))  # Beat 1 - classic
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(70, 5))  # Beat 2 - classic
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(60, 5))  # Beat 3 - classic
            
            # Classic palmas with ornaments
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(75, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(75, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(75, 8))
            
            # Open hi-hats for folk texture
            self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                        self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(55, 10))
            self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                        self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(55, 10))
            self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(55, 10))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple fandango fill - traditional palmas and waltz accent."""
        # Traditional palmas roll
        for i in range(3):
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        i * self.midi_config['ticks_per_beat'], 
                        self.get_random_velocity(80, 10))
        
        # Waltz accent
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 2, 
                     self.get_random_velocity(100, 5))
        
        # Traditional hi-hat flourish
        self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                     self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                     self.get_random_velocity(70, 10))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex fandango fill - traditional with tom work."""
        # Complex palmas pattern with traditional ornaments
        palmas_pattern = [
            (self.midi_config['ticks_per_eighth'], 80),
            (self.midi_config['ticks_per_beat'], 75),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 80),
            (self.midi_config['ticks_per_beat'] * 2, 75),
            (self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 80),
            (self.midi_config['ticks_per_beat'] * 3, 75)
        ]
        for beat_pos, velocity in palmas_pattern:
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        beat_pos, 
                        self.get_random_velocity(velocity, 8))
        
        # Tom work for traditional effect
        toms = [self.drum_mapping['tom_high'], self.drum_mapping['tom_mid'], self.drum_mapping['tom_low']]
        for i, tom in enumerate(toms):
            self.add_note(midi, tom, bar, 
                        self.midi_config['ticks_per_beat'] * (1 + i), 
                        self.get_random_velocity(85, 10))
        
        # Waltz accent with crash
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 2, 
                     self.get_random_velocity(105, 5))
        self.add_note(midi, self.drum_mapping['crash'], bar, 
                     self.midi_config['ticks_per_beat'] * 2, 
                     self.get_random_velocity(95, 10))
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Fandango intro - builds up with traditional palmas and waltz rhythm."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 2:
                # Soft traditional palmas only - building tradition
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                            self.get_random_velocity(55, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                            self.get_random_velocity(55, 8))
            elif bar < start_bar + 4:
                # Add waltz rhythm - building tradition
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(70, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(65, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'] * 2, 
                            self.get_random_velocity(60, 5))
                # More traditional palmas
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                            self.get_random_velocity(65, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                            self.get_random_velocity(65, 8))
            else:
                # Full fandango pattern
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Fandango verse - steady waltz rhythm with traditional palmas."""
        for bar in range(start_bar, start_bar + bars):
            # Steady waltz rhythm
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(85, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'], 
                        self.get_random_velocity(70, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(65, 5))
            
            # Traditional palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(75, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(75, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(75, 8))
            
            # Traditional hi-hats
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(65, 10))
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(65, 10))
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Fandango chorus - maximum traditional intensity."""
        for bar in range(start_bar, start_bar + bars):
            # Intense waltz rhythm
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'], 
                        self.get_random_velocity(80, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(75, 5))
            
            # Intense traditional palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'], 
                        self.get_random_velocity(80, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(80, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 3, 
                        self.get_random_velocity(80, 8))
            
            # Ride cymbal for tradition
            self.add_note(midi, self.drum_mapping['ride'], bar, 
                        self.midi_config['ticks_per_beat'], 
                        self.get_random_velocity(70, 10))
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Fandango bridge - different traditional style with contrast."""
        for bar in range(start_bar, start_bar + bars):
            # Different traditional rhythm (soleá style) for contrast
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(75, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'], 
                        self.get_random_velocity(70, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(65, 5))
            
            # Soleá palmas for contrast
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(65, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(65, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(65, 8))
            
            # Open hi-hats for contrast
            self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                        self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(60, 10))
            self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                        self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(60, 10))
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Fandango outro - winds down with traditional ending."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Full fandango
                self.create_basic_pattern(midi, bar, 1)
            elif bar < start_bar + 6:
                # Reduce to essential beats
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(75, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(65, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'] * 2, 
                            self.get_random_velocity(60, 5))
                # Essential traditional palmas
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                            self.get_random_velocity(65, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                            self.get_random_velocity(65, 8))
            else:
                # Final traditional palmas only
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                            self.get_random_velocity(60, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                            self.get_random_velocity(60, 8))

