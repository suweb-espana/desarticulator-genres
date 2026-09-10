"""
Sevillanas - Traditional Andalusian folk dance in 3/4 time.
Traditional Spanish folk dance with waltz-like 3/4 rhythm and festive character.
"""

from core.base_pattern import BasePattern
from midiutil import MIDIFile


class SevillanasPattern(BasePattern):
    """Sevillanas pattern - traditional Andalusian folk dance in 3/4."""
    
    @property
    def genre_name(self) -> str:
        return "Sevillanas"
    
    @property
    def description(self) -> str:
        return "Traditional Andalusian folk dance - waltz-like 3/4 rhythm, festive character, traditional Spanish folk patterns"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic sevillanas pattern - 3/4 waltz rhythm with folk character."""
        for bar in range(start_bar, start_bar + bars):
            # Sevillanas compás - 3/4 waltz rhythm
            # Strong beats: 1, 2, 3 (waltz pattern)
            # Folk emphasis: 1 (strong), 2 (medium), 3 (light)
            
            # Kick pattern - waltz rhythm
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))  # Beat 1 - strong
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(80, 5))  # Beat 2 - medium
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(70, 5))  # Beat 3 - light
            
            # Sevillanas palmas - folk pattern
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(85, 8))  # Off-beat 1
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(80, 8))  # Off-beat 2
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(75, 8))  # Off-beat 3
            
            # Folk hi-hats for sevillanas texture
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(65, 10))  # Off-beat 1
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(65, 10))  # Off-beat 2
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(65, 10))  # Off-beat 3
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Sevillanas variation 1 - more festive with additional accents."""
        for bar in range(start_bar, start_bar + bars):
            # Festive sevillanas with more accents
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(100, 5))  # Beat 1 - festive
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(85, 5))  # Beat 2 - festive
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(75, 5))  # Beat 3 - festive
            
            # Festive palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(90, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(90, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(90, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(85, 8))
            
            # Ride cymbal for festive feel
            for beat in [1, 2, 3]:  # On-beats
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(70, 10))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Sevillanas variation 2 - traditional with folk ornaments."""
        for bar in range(start_bar, start_bar + bars):
            # Traditional sevillanas with folk ornaments
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(90, 5))  # Beat 1 - traditional
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'], 
                         self.get_random_velocity(75, 5))  # Beat 2 - traditional
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(65, 5))  # Beat 3 - traditional
            
            # Traditional palmas with ornaments
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(80, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(80, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                         self.get_random_velocity(80, 8))
            
            # Open hi-hats for folk texture
            self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                        self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(60, 10))
            self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                        self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(60, 10))
            self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(60, 10))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple sevillanas fill - folk palmas and waltz accent."""
        # Folk palmas roll
        for i in range(3):
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        i * self.midi_config['ticks_per_beat'], 
                        self.get_random_velocity(85, 10))
        
        # Waltz accent
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 2, 
                     self.get_random_velocity(105, 5))
        
        # Folk hi-hat flourish
        self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                     self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                     self.get_random_velocity(75, 10))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex sevillanas fill - folk with tom work."""
        # Complex palmas pattern with folk ornaments
        palmas_pattern = [
            (self.midi_config['ticks_per_eighth'], 85),
            (self.midi_config['ticks_per_beat'], 80),
            (self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 85),
            (self.midi_config['ticks_per_beat'] * 2, 80),
            (self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 85),
            (self.midi_config['ticks_per_beat'] * 3, 80)
        ]
        for beat_pos, velocity in palmas_pattern:
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        beat_pos, 
                        self.get_random_velocity(velocity, 8))
        
        # Tom work for folk effect
        toms = [self.drum_mapping['tom_high'], self.drum_mapping['tom_mid'], self.drum_mapping['tom_low']]
        for i, tom in enumerate(toms):
            self.add_note(midi, tom, bar, 
                        self.midi_config['ticks_per_beat'] * (1 + i), 
                        self.get_random_velocity(90, 10))
        
        # Waltz accent with crash
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 2, 
                     self.get_random_velocity(110, 5))
        self.add_note(midi, self.drum_mapping['crash'], bar, 
                     self.midi_config['ticks_per_beat'] * 2, 
                     self.get_random_velocity(100, 10))
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Sevillanas intro - builds up with folk palmas and waltz rhythm."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 2:
                # Soft folk palmas only - building tradition
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                            self.get_random_velocity(60, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                            self.get_random_velocity(60, 8))
            elif bar < start_bar + 4:
                # Add waltz rhythm - building folk
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(75, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(70, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'] * 2, 
                            self.get_random_velocity(65, 5))
                # More folk palmas
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                            self.get_random_velocity(70, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                            self.get_random_velocity(70, 8))
            else:
                # Full sevillanas pattern
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Sevillanas verse - steady waltz rhythm with folk palmas."""
        for bar in range(start_bar, start_bar + bars):
            # Steady waltz rhythm
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'], 
                        self.get_random_velocity(75, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(70, 5))
            
            # Folk palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(80, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(80, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(80, 8))
            
            # Folk hi-hats
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(70, 10))
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(70, 10))
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Sevillanas chorus - maximum folk festivity."""
        for bar in range(start_bar, start_bar + bars):
            # Intense waltz rhythm
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(100, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'], 
                        self.get_random_velocity(85, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(80, 5))
            
            # Intense folk palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(90, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'], 
                        self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(90, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(90, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 3, 
                        self.get_random_velocity(85, 8))
            
            # Ride cymbal for festivity
            self.add_note(midi, self.drum_mapping['ride'], bar, 
                        self.midi_config['ticks_per_beat'], 
                        self.get_random_velocity(75, 10))
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Sevillanas bridge - different folk style with contrast."""
        for bar in range(start_bar, start_bar + bars):
            # Different folk rhythm (fandango style) for contrast
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(80, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'], 
                        self.get_random_velocity(75, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(70, 5))
            
            # Fandango palmas for contrast
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(70, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(70, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(70, 8))
            
            # Open hi-hats for contrast
            self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                        self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(65, 10))
            self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                        self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                        self.get_random_velocity(65, 10))
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Sevillanas outro - winds down with folk ending."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Full sevillanas
                self.create_basic_pattern(midi, bar, 1)
            elif bar < start_bar + 6:
                # Reduce to essential beats
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(80, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(70, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'] * 2, 
                            self.get_random_velocity(65, 5))
                # Essential folk palmas
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                            self.get_random_velocity(70, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                            self.get_random_velocity(70, 8))
            else:
                # Final folk palmas only
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] + self.midi_config['ticks_per_eighth'], 
                            self.get_random_velocity(65, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 
                            self.get_random_velocity(65, 8))