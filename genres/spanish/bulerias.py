"""
Bulerías - Fast flamenco palo with complex compás patterns.
The fastest and most complex flamenco style with intricate 12-beat cycles.
"""

from core.base_pattern import BasePattern
from midiutil import MIDIFile


class BuleriasPattern(BasePattern):
    """Bulerías pattern - fastest flamenco with complex compás."""
    
    @property
    def genre_name(self) -> str:
        return "Bulerías"
    
    @property
    def description(self) -> str:
        return "Fast flamenco palo - complex 12-beat compás, rapid palmas, intricate rhythms, most challenging flamenco style"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic bulerías pattern - fast 12-beat compás with complex syncopation."""
        for bar in range(start_bar, start_bar + bars):
            # Bulerías compás - fast and complex
            # Strong beats: 1, 3, 5, 8, 10, 12 (traditional bulerías emphasis)
            # Additional syncopation: 2, 4, 6, 7, 9, 11
            
            # Kick pattern - bulerías style with syncopation
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(100, 5))  # Beat 1 - strong
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))  # Beat 3 - strong
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 4, 
                         self.get_random_velocity(90, 5))  # Beat 5 - strong
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(100, 5))  # Beat 8 - strong
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(95, 5))  # Beat 10 - strong
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(100, 5))  # Beat 12 - strong
            
            # Bulerías palmas - rapid and complex
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 1, 
                         self.get_random_velocity(85, 8))  # Beat 2
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(80, 8))  # Beat 4
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 5, 
                         self.get_random_velocity(80, 8))  # Beat 6
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 6, 
                         self.get_random_velocity(85, 8))  # Beat 7
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 8, 
                         self.get_random_velocity(80, 8))  # Beat 9
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 10, 
                         self.get_random_velocity(85, 8))  # Beat 11
            
            # Fast hi-hats for bulerías texture
            for beat in range(12):
                if beat not in [1, 3, 5, 8, 10, 12]:  # Not on strong beats
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                beat * self.midi_config['ticks_per_beat'], 
                                self.get_random_velocity(65, 10))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bulerías variation 1 - even faster with more syncopation."""
        for bar in range(start_bar, start_bar + bars):
            # Ultra-fast bulerías with extreme syncopation
            # More kicks for intensity
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(105, 5))  # Beat 1
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 1.5, 
                         self.get_random_velocity(90, 5))  # Syncopated
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(100, 5))  # Beat 3
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 4, 
                         self.get_random_velocity(95, 5))  # Beat 5
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(105, 5))  # Beat 8
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(95, 5))  # Beat 10
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(100, 5))  # Beat 12
            
            # Rapid palmas with ghost notes
            for beat in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
                velocity = 75 + (beat * 2)  # Crescendo through the cycle
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(velocity, 8))
            
            # Ride cymbal for bulerías intensity
            for beat in range(0, 12, 3):  # Every third beat
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(70, 10))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bulerías variation 2 - complex polyrhythmic patterns."""
        for bar in range(start_bar, start_bar + bars):
            # Complex bulerías with polyrhythmic elements
            # Traditional compás with additional complexity
            
            # Main compás kicks
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(100, 5))  # Beat 1
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))  # Beat 3
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 4, 
                         self.get_random_velocity(90, 5))  # Beat 5
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(100, 5))  # Beat 8
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(95, 5))  # Beat 10
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(100, 5))  # Beat 12
            
            # Polyrhythmic palmas
            palmas_pattern = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            for i, beat in enumerate(palmas_pattern):
                # Varying intensities for polyrhythmic effect
                intensity = 70 + (i % 3) * 10
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(intensity, 8))
            
            # Complex hi-hat patterns
            for beat in [1, 3, 5, 7, 9, 11]:  # Off-beats
                self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(60, 10))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple bulerías fill - rapid palmas and compás accent."""
        # Rapid palmas roll
        for i in range(6):
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        i * self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(85, 10))
        
        # Bulerías compás accent
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 8, 
                     self.get_random_velocity(110, 5))
        
        # Hi-hat flourish
        self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                     self.midi_config['ticks_per_beat'] * 10, 
                     self.get_random_velocity(75, 10))
        self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                     self.midi_config['ticks_per_beat'] * 11, 
                     self.get_random_velocity(80, 10))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex bulerías fill - polyrhythmic with tom work."""
        # Complex palmas pattern with polyrhythmic elements
        palmas_pattern = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for i, beat in enumerate(palmas_pattern):
            velocity = 75 + (i * 2)  # Crescendo
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        beat * self.midi_config['ticks_per_beat'], 
                        self.get_random_velocity(velocity, 8))
        
        # Tom cascade (bulerías style)
        toms = [self.drum_mapping['tom_high'], self.drum_mapping['tom_mid'], self.drum_mapping['tom_low']]
        for i, tom in enumerate(toms):
            self.add_note(midi, tom, bar, 
                        self.midi_config['ticks_per_beat'] * (6 + i * 2), 
                        self.get_random_velocity(90, 10))
        
        # Bulerías compás accent with crash
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 8, 
                     self.get_random_velocity(115, 5))
        self.add_note(midi, self.drum_mapping['crash'], bar, 
                     self.midi_config['ticks_per_beat'] * 8, 
                     self.get_random_velocity(105, 10))
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bulerías intro - builds up with rapid palmas and compás."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 2:
                # Soft palmas only - building anticipation
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 3, 
                            self.get_random_velocity(60, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(60, 8))
            elif bar < start_bar + 4:
                # Add compás - building intensity
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(85, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(85, 5))
                # More palmas
                for beat in [3, 6, 9]:
                    self.add_note(midi, self.drum_mapping['snare'], bar, 
                                beat * self.midi_config['ticks_per_beat'], 
                                self.get_random_velocity(70, 8))
            else:
                # Full bulerías pattern
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Bulerías verse - steady fast compás with rapid palmas."""
        for bar in range(start_bar, start_bar + bars):
            # Fast bulerías compás
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 3, 
                        self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 6, 
                        self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 8, 
                        self.get_random_velocity(90, 5))
            
            # Rapid palmas
            for beat in [2, 4, 6, 9, 11]:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(80, 8))
            
            # Fast hi-hats
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 1, 
                        self.get_random_velocity(65, 10))
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 5, 
                        self.get_random_velocity(65, 10))
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Bulerías chorus - maximum intensity with complex patterns."""
        for bar in range(start_bar, start_bar + bars):
            # Intense bulerías compás
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(105, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(100, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 4, 
                        self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 6, 
                        self.get_random_velocity(105, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 8, 
                        self.get_random_velocity(100, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 10, 
                        self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 11, 
                        self.get_random_velocity(105, 5))
            
            # Intense palmas
            for beat in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(90, 8))
            
            # Ride cymbal for intensity
            self.add_note(midi, self.drum_mapping['ride'], bar, 
                        self.midi_config['ticks_per_beat'] * 4, 
                        self.get_random_velocity(75, 10))
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bulerías bridge - different palo with contrast."""
        for bar in range(start_bar, start_bar + bars):
            # Different palo rhythm (alegrías style) for contrast
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 4, 
                        self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 8, 
                        self.get_random_velocity(90, 5))
            
            # Alegrías palmas for contrast
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(75, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 6, 
                        self.get_random_velocity(75, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 10, 
                        self.get_random_velocity(75, 8))
            
            # Open hi-hats for contrast
            self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 3, 
                        self.get_random_velocity(70, 10))
            self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 7, 
                        self.get_random_velocity(70, 10))
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bulerías outro - winds down with traditional ending."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Full bulerías
                self.create_basic_pattern(midi, bar, 1)
            elif bar < start_bar + 6:
                # Reduce to essential beats
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(95, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(95, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'] * 8, 
                            self.get_random_velocity(95, 5))
                # Essential palmas
                for beat in [3, 6, 9]:
                    self.add_note(midi, self.drum_mapping['snare'], bar, 
                                beat * self.midi_config['ticks_per_beat'], 
                                self.get_random_velocity(75, 8))
            else:
                # Final palmas only
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 3, 
                            self.get_random_velocity(65, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(65, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 9, 
                            self.get_random_velocity(65, 8))

