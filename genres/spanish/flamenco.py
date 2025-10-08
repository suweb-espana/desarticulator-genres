"""
Flamenco drum pattern generator - Traditional Spanish flamenco with authentic compás patterns.
"""

from core.base_pattern import BasePattern
from midiutil import MIDIFile


class FlamencoPattern(BasePattern):
    """Flamenco drum patterns with traditional compás and palmas rhythms."""
    
    @property
    def genre_name(self) -> str:
        return "Flamenco"
    
    @property
    def description(self) -> str:
        return "Traditional Spanish flamenco - compás patterns, palmas, bulerías, soleá, and alegrías rhythms"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic flamenco compás pattern - traditional 12-beat cycle."""
        for bar in range(start_bar, start_bar + bars):
            # Traditional flamenco compás (12-beat cycle)
            # Strong beats: 1, 3, 5, 8, 10, 12
            # Weak beats: 2, 4, 6, 7, 9, 11
            
            # Kick on strong beats (compás)
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))  # Beat 1
            self.add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(90, 5))  # Beat 3
            self.add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 4, 
                         self.get_random_velocity(90, 5))  # Beat 5
            self.add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(95, 5))  # Beat 8
            self.add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(90, 5))  # Beat 10
            self.add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(95, 5))  # Beat 12
            
            # Snare on weak beats (palmas)
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 1, 
                         self.get_random_velocity(75, 8))  # Beat 2
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(70, 8))  # Beat 4
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 5, 
                         self.get_random_velocity(70, 8))  # Beat 6
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 6, 
                         self.get_random_velocity(75, 8))  # Beat 7
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 8, 
                         self.get_random_velocity(70, 8))  # Beat 9
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 10, 
                         self.get_random_velocity(75, 8))  # Beat 11
            
            # Hi-hats for rhythm texture
            for beat in range(12):
                if beat not in [1, 3, 5, 8, 10, 12]:  # Not on strong beats
                    self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                beat * self.midi_config['ticks_per_beat'], 
                                self.get_random_velocity(60, 10))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bulerías variation - faster, more complex compás."""
        for bar in range(start_bar, start_bar + bars):
            # Bulerías compás with more syncopation
            # Strong beats with variations
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(100, 5))  # Beat 1
            self.add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))  # Beat 3
            self.add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 4, 
                         self.get_random_velocity(90, 5))  # Beat 5
            self.add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(100, 5))  # Beat 8
            self.add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(90, 5))  # Beat 10
            self.add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(95, 5))  # Beat 12
            
            # More complex palmas pattern
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 1, 
                         self.get_random_velocity(80, 8))  # Beat 2
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(75, 8))  # Beat 4
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 5, 
                         self.get_random_velocity(75, 8))  # Beat 6
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 6, 
                         self.get_random_velocity(80, 8))  # Beat 7
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 8, 
                         self.get_random_velocity(75, 8))  # Beat 9
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 10, 
                         self.get_random_velocity(80, 8))  # Beat 11
            
            # Ride cymbal for bulerías texture
            for beat in range(0, 12, 2):  # Every other beat
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(65, 10))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Soleá variation - slower, more dramatic compás."""
        for bar in range(start_bar, start_bar + bars):
            # Soleá compás - more emphasis on beats 3, 6, 8, 10, 12
            # Strong beats with soleá emphasis
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(90, 5))  # Beat 1
            self.add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(95, 5))  # Beat 3 (soleá emphasis)
            self.add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 4, 
                         self.get_random_velocity(85, 5))  # Beat 5
            self.add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 5, 
                         self.get_random_velocity(90, 5))  # Beat 6 (soleá emphasis)
            self.add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(95, 5))  # Beat 8 (soleá emphasis)
            self.add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(90, 5))  # Beat 10 (soleá emphasis)
            self.add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(95, 5))  # Beat 12 (soleá emphasis)
            
            # Soleá palmas pattern
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 1, 
                         self.get_random_velocity(70, 8))  # Beat 2
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(75, 8))  # Beat 4
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 5, 
                         self.get_random_velocity(70, 8))  # Beat 6
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 6, 
                         self.get_random_velocity(75, 8))  # Beat 7
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 8, 
                         self.get_random_velocity(70, 8))  # Beat 9
            self.add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 10, 
                         self.get_random_velocity(75, 8))  # Beat 11
            
            # Open hi-hats for soleá texture
            for beat in [1, 3, 5, 7, 9, 11]:  # Off-beats
                self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(55, 10))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple flamenco fill - palmas and compás variations."""
        # Palmas roll
        for i in range(4):
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        i * self.midi_config['ticks_per_beat'] * 3, 
                        self.get_random_velocity(80, 10))
        
        # Compás accent
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 6, 
                     self.get_random_velocity(100, 5))
        
        # Hi-hat flourish
        self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                     self.midi_config['ticks_per_beat'] * 8, 
                     self.get_random_velocity(70, 10))
        self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                     self.midi_config['ticks_per_beat'] * 9, 
                     self.get_random_velocity(75, 10))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex flamenco fill - bulerías style with tom work."""
        # Complex palmas pattern
        palmas_pattern = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for i, beat in enumerate(palmas_pattern):
            velocity = 70 + (i * 3)  # Crescendo
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        beat * self.midi_config['ticks_per_beat'], 
                        self.get_random_velocity(velocity, 8))
        
        # Tom cascade (flamenco style)
        toms = [self.drum_mapping['tom_high'], self.drum_mapping['tom_mid'], self.drum_mapping['tom_low']]
        for i, tom in enumerate(toms):
            self.add_note(midi, tom, bar, 
                        self.midi_config['ticks_per_beat'] * (6 + i * 2), 
                        self.get_random_velocity(85, 10))
        
        # Compás accent with crash
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 8, 
                     self.get_random_velocity(110, 5))
        self.add_note(midi, self.drum_mapping['crash'], bar, 
                     self.midi_config['ticks_per_beat'] * 8, 
                     self.get_random_velocity(100, 10))
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Flamenco intro - builds up with palmas and compás."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 2:
                # Soft palmas only
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 3, 
                            self.get_random_velocity(60, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(60, 8))
            elif bar < start_bar + 4:
                # Add compás
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(80, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(80, 5))
            else:
                # Full compás pattern
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Flamenco verse - steady compás with palmas."""
        for bar in range(start_bar, start_bar + bars):
            # Traditional compás
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 6, 
                        self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 8, 
                        self.get_random_velocity(90, 5))
            
            # Palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 3, 
                        self.get_random_velocity(75, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 9, 
                        self.get_random_velocity(75, 8))
            
            # Hi-hats
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(60, 10))
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 5, 
                        self.get_random_velocity(60, 10))
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Flamenco chorus - more intense compás and palmas."""
        for bar in range(start_bar, start_bar + bars):
            # Intense compás
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(100, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 3, 
                        self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 6, 
                        self.get_random_velocity(100, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 8, 
                        self.get_random_velocity(95, 5))
            
            # Strong palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 5, 
                        self.get_random_velocity(85, 8))
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        self.midi_config['ticks_per_beat'] * 9, 
                        self.get_random_velocity(85, 8))
            
            # Ride cymbal
            self.add_note(midi, self.drum_mapping['ride'], bar, 
                        self.midi_config['ticks_per_beat'] * 4, 
                        self.get_random_velocity(70, 10))
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Flamenco bridge - different palo (style) with contrast."""
        for bar in range(start_bar, start_bar + bars):
            # Different palo rhythm (alegrías style)
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(85, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 4, 
                        self.get_random_velocity(85, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 8, 
                        self.get_random_velocity(85, 5))
            
            # Alegrías palmas
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
        """Flamenco outro - winds down with traditional ending."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Full compás
                self.create_basic_pattern(midi, bar, 1)
            elif bar < start_bar + 6:
                # Reduce to essential beats
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(90, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(90, 5))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 3, 
                            self.get_random_velocity(70, 8))
            else:
                # Final palmas only
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 3, 
                            self.get_random_velocity(60, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(60, 8))
