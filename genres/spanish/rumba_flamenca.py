"""
Rumba Flamenca - Flamenco rumba with Cuban influences.
Fusion of traditional flamenco with Afro-Cuban rhythms and Latin percussion patterns.
"""

from core.base_pattern import BasePattern
from midiutil import MIDIFile


class RumbaFlamencaPattern(BasePattern):
    """Rumba Flamenca pattern - fusion of flamenco with Cuban influences."""
    
    @property
    def genre_name(self) -> str:
        return "Rumba Flamenca"
    
    @property
    def description(self) -> str:
        return "Flamenco rumba with Cuban influences - fusion of traditional flamenco compás with Afro-Cuban rhythms, Latin percussion, and syncopated patterns"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic rumba flamenca pattern - fusion of flamenco compás with Cuban rhythms."""
        for bar in range(start_bar, start_bar + bars):
            # Rumba flamenca compás - fusion of 12-beat flamenco with Cuban syncopation
            # Strong beats: 1, 3, 5, 8, 10, 12 (flamenco base)
            # Cuban syncopation: 2, 4, 6, 7, 9, 11 (Latin influence)
            
            # Kick pattern - flamenco compás with Cuban syncopation
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))  # Beat 1 - flamenco strong
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(90, 5))  # Beat 3 - flamenco strong
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 4, 
                         self.get_random_velocity(90, 5))  # Beat 5 - flamenco strong
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(95, 5))  # Beat 8 - flamenco strong
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(90, 5))  # Beat 10 - flamenco strong
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(95, 5))  # Beat 12 - flamenco strong
            
            # Cuban syncopated kicks
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 1, 
                         self.get_random_velocity(80, 5))  # Beat 2 - Cuban syncopation
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(75, 5))  # Beat 4 - Cuban syncopation
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 5, 
                         self.get_random_velocity(75, 5))  # Beat 6 - Cuban syncopation
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 6, 
                         self.get_random_velocity(80, 5))  # Beat 7 - Cuban syncopation
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 8, 
                         self.get_random_velocity(75, 5))  # Beat 9 - Cuban syncopation
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 10, 
                         self.get_random_velocity(80, 5))  # Beat 11 - Cuban syncopation
            
            # Rumba flamenca palmas - fusion of flamenco and Cuban patterns
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 1, 
                         self.get_random_velocity(85, 8))  # Beat 2 - rumba palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(80, 8))  # Beat 4 - rumba palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 5, 
                         self.get_random_velocity(80, 8))  # Beat 6 - rumba palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 6, 
                         self.get_random_velocity(85, 8))  # Beat 7 - rumba palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 8, 
                         self.get_random_velocity(80, 8))  # Beat 9 - rumba palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 10, 
                         self.get_random_velocity(85, 8))  # Beat 11 - rumba palmas
            
            # Latin hi-hats for Cuban texture
            for beat in [1, 3, 5, 7, 9, 11]:  # Off-beats for Latin feel
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(70, 10))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Rumba flamenca variation 1 - more Cuban influence with syncopation."""
        for bar in range(start_bar, start_bar + bars):
            # More Cuban syncopation
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(100, 5))  # Beat 1
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 1.5, 
                         self.get_random_velocity(85, 5))  # Cuban syncopation
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
                         self.get_random_velocity(90, 5))  # Beat 10
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(95, 5))  # Beat 12
            
            # Cuban palmas with more syncopation
            for beat in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
                velocity = 80 + (beat % 3) * 5  # Cuban variation
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(velocity, 8))
            
            # Ride cymbal for Cuban feel
            for beat in [1, 3, 5, 8, 10, 12]:  # Flamenco emphasis with Cuban syncopation
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(75, 10))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Rumba flamenca variation 2 - more flamenco with Latin accents."""
        for bar in range(start_bar, start_bar + bars):
            # Flamenco compás with Latin accents
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))  # Beat 1
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(90, 5))  # Beat 3
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 4, 
                         self.get_random_velocity(90, 5))  # Beat 5
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(95, 5))  # Beat 8
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(90, 5))  # Beat 10
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(95, 5))  # Beat 12
            
            # Flamenco palmas with Latin accents
            for beat in [2, 4, 6, 8, 10, 12]:  # Even beats for Latin feel
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(85, 8))
            
            # Open hi-hats for Latin texture
            for beat in [1, 3, 5, 7, 9, 11]:  # Off-beats
                self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(65, 10))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple rumba flamenca fill - Cuban palmas and compás accent."""
        # Cuban palmas roll
        for i in range(4):
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        i * self.midi_config['ticks_per_beat'] * 3, 
                        self.get_random_velocity(90, 10))
        
        # Rumba compás accent
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 8, 
                     self.get_random_velocity(110, 5))
        
        # Latin hi-hat flourish
        self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                     self.midi_config['ticks_per_beat'] * 10, 
                     self.get_random_velocity(80, 10))
        self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                     self.midi_config['ticks_per_beat'] * 11, 
                     self.get_random_velocity(85, 10))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex rumba flamenca fill - fusion with tom work."""
        # Complex palmas pattern with Cuban syncopation
        palmas_pattern = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for i, beat in enumerate(palmas_pattern):
            if beat in [1, 3, 5, 8, 10, 12]:  # Flamenco emphasis beats
                velocity = 85 + (i % 2) * 10  # Cuban variation
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(velocity, 8))
        
        # Tom work for fusion effect
        toms = [self.drum_mapping['tom_high'], self.drum_mapping['tom_mid'], self.drum_mapping['tom_low']]
        for i, tom in enumerate(toms):
            self.add_note(midi, tom, bar, 
                        self.midi_config['ticks_per_beat'] * (4 + i * 2), 
                        self.get_random_velocity(95, 10))
        
        # Rumba compás accent with crash
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 8, 
                     self.get_random_velocity(115, 5))
        self.add_note(midi, self.drum_mapping['crash'], bar, 
                     self.midi_config['ticks_per_beat'] * 8, 
                     self.get_random_velocity(105, 10))
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Rumba flamenca intro - builds up with Cuban palmas and compás."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 2:
                # Soft Cuban palmas only - building fusion
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 3, 
                            self.get_random_velocity(65, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(65, 8))
            elif bar < start_bar + 4:
                # Add compás - building fusion
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(85, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(85, 5))
                # More Cuban palmas
                for beat in [3, 6, 9]:
                    self.add_note(midi, self.drum_mapping['snare'], bar, 
                                beat * self.midi_config['ticks_per_beat'], 
                                self.get_random_velocity(75, 8))
            else:
                # Full rumba flamenca pattern
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Rumba flamenca verse - steady fusion compás with Cuban palmas."""
        for bar in range(start_bar, start_bar + bars):
            # Steady rumba compás
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
            
            # Cuban palmas
            for beat in [2, 4, 6, 8, 10, 12]:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(85, 8))
            
            # Latin hi-hats
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 1, 
                        self.get_random_velocity(75, 10))
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 5, 
                        self.get_random_velocity(75, 10))
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Rumba flamenca chorus - maximum fusion intensity."""
        for bar in range(start_bar, start_bar + bars):
            # Intense rumba compás
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
            
            # Intense Cuban palmas
            for beat in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(95, 8))
            
            # Ride cymbal for fusion
            self.add_note(midi, self.drum_mapping['ride'], bar, 
                        self.midi_config['ticks_per_beat'] * 4, 
                        self.get_random_velocity(80, 10))
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Rumba flamenca bridge - different palo with contrast."""
        for bar in range(start_bar, start_bar + bars):
            # Different palo rhythm (alegrías style) for contrast
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(85, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 4, 
                        self.get_random_velocity(85, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 8, 
                        self.get_random_velocity(85, 5))
            
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
            
            # Closed hi-hats for contrast
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 3, 
                        self.get_random_velocity(70, 10))
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 7, 
                        self.get_random_velocity(70, 10))
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Rumba flamenca outro - winds down with fusion ending."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Full rumba flamenca
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
                # Essential Cuban palmas
                for beat in [3, 6, 9]:
                    self.add_note(midi, self.drum_mapping['snare'], bar, 
                                beat * self.midi_config['ticks_per_beat'], 
                                self.get_random_velocity(75, 8))
            else:
                # Final Cuban palmas only
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 3, 
                            self.get_random_velocity(70, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(70, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 9, 
                            self.get_random_velocity(70, 8))

