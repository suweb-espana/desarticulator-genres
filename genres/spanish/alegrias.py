"""
Alegrías - Joyful flamenco from Cádiz with bright compás patterns.
Bright, joyful flamenco palo with moderate tempo and celebratory rhythms.
"""

from core.base_pattern import BasePattern
from midiutil import MIDIFile


class AlegriasPattern(BasePattern):
    """Alegrías pattern - joyful flamenco from Cádiz."""
    
    @property
    def genre_name(self) -> str:
        return "Alegrías"
    
    @property
    def description(self) -> str:
        return "Joyful flamenco from Cádiz - bright 12-beat compás, moderate tempo, celebratory palmas, uplifting flamenco palo"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic alegrías pattern - joyful 12-beat compás."""
        for bar in range(start_bar, start_bar + bars):
            # Alegrías compás - joyful and bright
            # Strong beats: 1, 3, 5, 8, 10, 12 (alegrías emphasis)
            # Alegrías has special emphasis on beats 1, 3, 5, 8, 10, 12
            
            # Kick pattern - alegrías style with joyful emphasis
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))  # Beat 1 - alegrías emphasis
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(90, 5))  # Beat 3 - alegrías emphasis
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 4, 
                         self.get_random_velocity(90, 5))  # Beat 5 - alegrías emphasis
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(95, 5))  # Beat 8 - alegrías emphasis
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(90, 5))  # Beat 10 - alegrías emphasis
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(95, 5))  # Beat 12 - alegrías emphasis
            
            # Alegrías palmas - bright and joyful
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 1, 
                         self.get_random_velocity(80, 8))  # Beat 2 - bright
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(75, 8))  # Beat 4 - alegrías palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 5, 
                         self.get_random_velocity(80, 8))  # Beat 6 - bright
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 6, 
                         self.get_random_velocity(75, 8))  # Beat 7 - alegrías palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 8, 
                         self.get_random_velocity(80, 8))  # Beat 9 - bright
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 10, 
                         self.get_random_velocity(75, 8))  # Beat 11 - alegrías palmas
            
            # Bright hi-hats for alegrías texture
            for beat in [1, 3, 5, 7, 9, 11]:  # Off-beats for brightness
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(65, 10))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Alegrías variation 1 - more celebratory with additional accents."""
        for bar in range(start_bar, start_bar + bars):
            # Celebratory alegrías with more joyful accents
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(100, 5))  # Beat 1 - celebratory
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))  # Beat 3 - celebratory
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 4, 
                         self.get_random_velocity(95, 5))  # Beat 5 - celebratory
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(100, 5))  # Beat 8 - celebratory
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(95, 5))  # Beat 10 - celebratory
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(100, 5))  # Beat 12 - celebratory
            
            # Bright palmas
            for beat in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
                velocity = 75 + (beat % 2) * 5  # Bright variation
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(velocity, 8))
            
            # Ride cymbal for brightness
            for beat in [1, 3, 5, 8, 10, 12]:  # Alegrías emphasis beats
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(70, 10))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Alegrías variation 2 - moderate tempo with celebratory feel."""
        for bar in range(start_bar, start_bar + bars):
            # Moderate alegrías with celebratory feel
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(90, 5))  # Beat 1 - moderate
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(85, 5))  # Beat 3 - moderate
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 4, 
                         self.get_random_velocity(85, 5))  # Beat 5 - moderate
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(90, 5))  # Beat 8 - moderate
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(85, 5))  # Beat 10 - moderate
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(90, 5))  # Beat 12 - moderate
            
            # Celebratory palmas
            for beat in [2, 4, 6, 8, 10, 12]:  # Even beats for celebration
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(80, 8))
            
            # Closed hi-hats for brightness
            for beat in [1, 3, 5, 7, 9, 11]:  # Off-beats
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(70, 10))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple alegrías fill - bright palmas and compás accent."""
        # Bright palmas roll
        for i in range(4):
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        i * self.midi_config['ticks_per_beat'] * 3, 
                        self.get_random_velocity(85, 10))
        
        # Alegrías compás accent
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 8, 
                     self.get_random_velocity(105, 5))
        
        # Bright hi-hat flourish
        self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                     self.midi_config['ticks_per_beat'] * 10, 
                     self.get_random_velocity(75, 10))
        self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                     self.midi_config['ticks_per_beat'] * 11, 
                     self.get_random_velocity(80, 10))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex alegrías fill - celebratory with tom work."""
        # Complex palmas pattern with celebratory feel
        palmas_pattern = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for i, beat in enumerate(palmas_pattern):
            if beat in [1, 3, 5, 8, 10, 12]:  # Alegrías emphasis beats
                velocity = 80 + (i % 2) * 10  # Celebratory variation
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(velocity, 8))
        
        # Tom work for celebration
        toms = [self.drum_mapping['tom_high'], self.drum_mapping['tom_mid'], self.drum_mapping['tom_low']]
        for i, tom in enumerate(toms):
            self.add_note(midi, tom, bar, 
                        self.midi_config['ticks_per_beat'] * (2 + i * 2), 
                        self.get_random_velocity(90, 10))
        
        # Alegrías compás accent with crash
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 8, 
                     self.get_random_velocity(110, 5))
        self.add_note(midi, self.drum_mapping['crash'], bar, 
                     self.midi_config['ticks_per_beat'] * 8, 
                     self.get_random_velocity(100, 10))
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Alegrías intro - builds up with bright palmas and compás."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 2:
                # Soft bright palmas only - building joy
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 3, 
                            self.get_random_velocity(60, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(60, 8))
            elif bar < start_bar + 4:
                # Add compás - building celebration
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(80, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(80, 5))
                # More palmas
                for beat in [3, 6, 9]:
                    self.add_note(midi, self.drum_mapping['snare'], bar, 
                                beat * self.midi_config['ticks_per_beat'], 
                                self.get_random_velocity(70, 8))
            else:
                # Full alegrías pattern
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Alegrías verse - steady joyful compás with bright palmas."""
        for bar in range(start_bar, start_bar + bars):
            # Steady alegrías compás
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 3, 
                        self.get_random_velocity(85, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 6, 
                        self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 8, 
                        self.get_random_velocity(85, 5))
            
            # Bright palmas
            for beat in [2, 4, 6, 8, 10, 12]:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(80, 8))
            
            # Bright hi-hats
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 1, 
                        self.get_random_velocity(70, 10))
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 5, 
                        self.get_random_velocity(70, 10))
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Alegrías chorus - maximum joy and celebration."""
        for bar in range(start_bar, start_bar + bars):
            # Intense alegrías compás
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(100, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 4, 
                        self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 6, 
                        self.get_random_velocity(100, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 7, 
                        self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 8, 
                        self.get_random_velocity(100, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 9, 
                        self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 10, 
                        self.get_random_velocity(100, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 11, 
                        self.get_random_velocity(100, 5))
            
            # Intense palmas
            for beat in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(90, 8))
            
            # Ride cymbal for celebration
            self.add_note(midi, self.drum_mapping['ride'], bar, 
                        self.midi_config['ticks_per_beat'] * 4, 
                        self.get_random_velocity(75, 10))
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Alegrías bridge - different palo with contrast."""
        for bar in range(start_bar, start_bar + bars):
            # Different palo rhythm (soleá style) for contrast
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(85, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 4, 
                        self.get_random_velocity(85, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 8, 
                        self.get_random_velocity(85, 5))
            
            # Soleá palmas for contrast
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(70, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 6, 
                        self.get_random_velocity(70, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 10, 
                        self.get_random_velocity(70, 8))
            
            # Open hi-hats for contrast
            self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 3, 
                        self.get_random_velocity(65, 10))
            self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 7, 
                        self.get_random_velocity(65, 10))
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Alegrías outro - winds down with joyful ending."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Full alegrías
                self.create_basic_pattern(midi, bar, 1)
            elif bar < start_bar + 6:
                # Reduce to essential beats
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(85, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(85, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'] * 8, 
                            self.get_random_velocity(85, 5))
                # Essential palmas
                for beat in [3, 6, 9]:
                    self.add_note(midi, self.drum_mapping['snare'], bar, 
                                beat * self.midi_config['ticks_per_beat'], 
                                self.get_random_velocity(70, 8))
            else:
                # Final bright palmas only
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 3, 
                            self.get_random_velocity(65, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(65, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 9, 
                            self.get_random_velocity(65, 8))

