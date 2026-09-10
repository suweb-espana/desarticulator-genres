"""
Soleá - Deep, emotional flamenco style with dramatic compás patterns.
The most profound and emotional flamenco palo with slow, dramatic 12-beat cycles.
"""

from core.base_pattern import BasePattern
from midiutil import MIDIFile


class SoleaPattern(BasePattern):
    """Soleá pattern - deep, emotional flamenco with dramatic compás."""
    
    @property
    def genre_name(self) -> str:
        return "Soleá"
    
    @property
    def description(self) -> str:
        return "Deep, emotional flamenco style - dramatic 12-beat compás, slow tempo, profound palmas, most emotional flamenco palo"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic soleá pattern - slow, dramatic 12-beat compás."""
        for bar in range(start_bar, start_bar + bars):
            # Soleá compás - slow and dramatic
            # Strong beats: 1, 3, 6, 8, 10, 12 (soleá emphasis)
            # Soleá has special emphasis on beats 3, 6, 8, 10, 12
            
            # Kick pattern - soleá style with dramatic emphasis
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(90, 5))  # Beat 1 - strong but not overwhelming
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))  # Beat 3 - soleá emphasis
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 4, 
                         self.get_random_velocity(85, 5))  # Beat 5 - softer
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 5, 
                         self.get_random_velocity(90, 5))  # Beat 6 - soleá emphasis
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(95, 5))  # Beat 8 - soleá emphasis
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(90, 5))  # Beat 10 - soleá emphasis
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(95, 5))  # Beat 12 - soleá emphasis
            
            # Soleá palmas - deep and emotional
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 1, 
                         self.get_random_velocity(70, 8))  # Beat 2 - soft
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(75, 8))  # Beat 4 - soleá palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 5, 
                         self.get_random_velocity(70, 8))  # Beat 6 - soft
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 6, 
                         self.get_random_velocity(75, 8))  # Beat 7 - soleá palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 8, 
                         self.get_random_velocity(70, 8))  # Beat 9 - soft
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 10, 
                         self.get_random_velocity(75, 8))  # Beat 11 - soleá palmas
            
            # Open hi-hats for soleá texture - slow and dramatic
            for beat in [1, 3, 5, 7, 9, 11]:  # Off-beats for dramatic effect
                self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(55, 10))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Soleá variation 1 - more intense with additional accents."""
        for bar in range(start_bar, start_bar + bars):
            # Intense soleá with more dramatic accents
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))  # Beat 1
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(100, 5))  # Beat 3 - intense
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 4, 
                         self.get_random_velocity(90, 5))  # Beat 5
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 5, 
                         self.get_random_velocity(95, 5))  # Beat 6 - intense
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(100, 5))  # Beat 8 - intense
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(95, 5))  # Beat 10 - intense
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(100, 5))  # Beat 12 - intense
            
            # Intense palmas
            for beat in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
                velocity = 70 + (beat % 3) * 5  # Varying intensity
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(velocity, 8))
            
            # Ride cymbal for dramatic effect
            for beat in [3, 6, 8, 10, 12]:  # Soleá emphasis beats
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(65, 10))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Soleá variation 2 - slower with more space and drama."""
        for bar in range(start_bar, start_bar + bars):
            # Slower soleá with more dramatic pauses
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(85, 5))  # Beat 1 - softer
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(90, 5))  # Beat 3 - dramatic
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 5, 
                         self.get_random_velocity(85, 5))  # Beat 6 - dramatic
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(90, 5))  # Beat 8 - dramatic
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(85, 5))  # Beat 10 - dramatic
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(90, 5))  # Beat 12 - dramatic
            
            # Sparse palmas for dramatic effect
            for beat in [2, 4, 6, 8, 10, 12]:  # Only on even beats
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(70, 8))
            
            # Open hi-hats for atmosphere
            for beat in [1, 3, 5, 7, 9, 11]:  # Off-beats
                self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(50, 10))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple soleá fill - dramatic palmas and compás accent."""
        # Dramatic palmas roll
        for i in range(4):
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        i * self.midi_config['ticks_per_beat'] * 3, 
                        self.get_random_velocity(80, 10))
        
        # Soleá compás accent
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 6, 
                     self.get_random_velocity(105, 5))
        
        # Open hi-hat for drama
        self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                     self.midi_config['ticks_per_beat'] * 8, 
                     self.get_random_velocity(70, 10))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex soleá fill - dramatic with tom work."""
        # Complex palmas pattern with dramatic pauses
        palmas_pattern = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for i, beat in enumerate(palmas_pattern):
            if beat in [3, 6, 8, 10, 12]:  # Soleá emphasis beats
                velocity = 80 + (i % 2) * 10  # Dramatic variation
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(velocity, 8))
        
        # Tom work for dramatic effect
        toms = [self.drum_mapping['tom_high'], self.drum_mapping['tom_mid'], self.drum_mapping['tom_low']]
        for i, tom in enumerate(toms):
            self.add_note(midi, tom, bar, 
                        self.midi_config['ticks_per_beat'] * (4 + i * 2), 
                        self.get_random_velocity(85, 10))
        
        # Soleá compás accent with crash
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 6, 
                     self.get_random_velocity(110, 5))
        self.add_note(midi, self.drum_mapping['crash'], bar, 
                     self.midi_config['ticks_per_beat'] * 6, 
                     self.get_random_velocity(100, 10))
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Soleá intro - builds up slowly with dramatic palmas."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 2:
                # Very soft palmas only - building anticipation
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 3, 
                            self.get_random_velocity(50, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(50, 8))
            elif bar < start_bar + 4:
                # Add soft compás - building drama
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(70, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(75, 5))
                # More palmas
                for beat in [3, 6, 9]:
                    self.add_note(midi, self.drum_mapping['snare'], bar, 
                                beat * self.midi_config['ticks_per_beat'], 
                                self.get_random_velocity(60, 8))
            else:
                # Full soleá pattern
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Soleá verse - steady dramatic compás with emotional palmas."""
        for bar in range(start_bar, start_bar + bars):
            # Steady soleá compás
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(85, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 3, 
                        self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 6, 
                        self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 8, 
                        self.get_random_velocity(90, 5))
            
            # Emotional palmas
            for beat in [2, 4, 6, 8, 10, 12]:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(75, 8))
            
            # Open hi-hats for atmosphere
            self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 1, 
                        self.get_random_velocity(60, 10))
            self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 5, 
                        self.get_random_velocity(60, 10))
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Soleá chorus - maximum emotional intensity."""
        for bar in range(start_bar, start_bar + bars):
            # Intense soleá compás
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(100, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 4, 
                        self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 5, 
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
                            self.get_random_velocity(85, 8))
            
            # Ride cymbal for intensity
            self.add_note(midi, self.drum_mapping['ride'], bar, 
                        self.midi_config['ticks_per_beat'] * 3, 
                        self.get_random_velocity(70, 10))
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Soleá bridge - different palo with contrast."""
        for bar in range(start_bar, start_bar + bars):
            # Different palo rhythm (alegrías style) for contrast
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(80, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 4, 
                        self.get_random_velocity(80, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 8, 
                        self.get_random_velocity(80, 5))
            
            # Alegrías palmas for contrast
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(70, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 6, 
                        self.get_random_velocity(70, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 10, 
                        self.get_random_velocity(70, 8))
            
            # Closed hi-hats for contrast
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 3, 
                        self.get_random_velocity(65, 10))
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 7, 
                        self.get_random_velocity(65, 10))
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Soleá outro - winds down with dramatic ending."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Full soleá
                self.create_basic_pattern(midi, bar, 1)
            elif bar < start_bar + 6:
                # Reduce to essential beats
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(80, 5))
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
                                self.get_random_velocity(65, 8))
            else:
                # Final dramatic palmas only
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 3, 
                            self.get_random_velocity(60, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(60, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 9, 
                            self.get_random_velocity(60, 8))

