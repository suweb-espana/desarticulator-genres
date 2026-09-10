"""
Seguiriya - Tragic and profound flamenco style.
Deep, emotional flamenco with complex 12-beat compás and tragic character.
"""

from core.base_pattern import BasePattern
from midiutil import MIDIFile


class SeguiriyaPattern(BasePattern):
    """Seguiriya pattern - tragic and profound flamenco style."""
    
    @property
    def genre_name(self) -> str:
        return "Seguiriya"
    
    @property
    def description(self) -> str:
        return "Tragic and profound flamenco style - complex 12-beat compás, slow tempo, deep emotional palmas, most tragic flamenco palo"
    
    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic seguiriya pattern - complex 12-beat compás with tragic character."""
        for bar in range(start_bar, start_bar + bars):
            # Seguiriya compás - complex 12-beat pattern
            # Strong beats: 1, 3, 6, 8, 10, 12 (tragic emphasis)
            # Tragic character: slow, deep, profound
            
            # Kick pattern - seguiriya compás
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(90, 5))  # Beat 1 - tragic strong
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(85, 5))  # Beat 3 - tragic strong
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 5, 
                         self.get_random_velocity(90, 5))  # Beat 6 - tragic strong
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(85, 5))  # Beat 8 - tragic strong
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(90, 5))  # Beat 10 - tragic strong
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(95, 5))  # Beat 12 - tragic strong
            
            # Seguiriya palmas - tragic pattern
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 1, 
                         self.get_random_velocity(80, 8))  # Beat 2 - tragic palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 3, 
                         self.get_random_velocity(75, 8))  # Beat 4 - tragic palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 5, 
                         self.get_random_velocity(80, 8))  # Beat 6 - tragic palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(75, 8))  # Beat 8 - tragic palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(80, 8))  # Beat 10 - tragic palmas
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                         self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(85, 8))  # Beat 12 - tragic palmas
            
            # Tragic hi-hats for seguiriya texture
            for beat in [2, 4, 6, 8, 10, 12]:  # Off-beats for tragic feel
                self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(60, 10))
    
    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Seguiriya variation 1 - more tragic with additional accents."""
        for bar in range(start_bar, start_bar + bars):
            # More tragic seguiriya with additional accents
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))  # Beat 1 - more tragic
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(90, 5))  # Beat 3 - more tragic
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 5, 
                         self.get_random_velocity(95, 5))  # Beat 6 - more tragic
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(90, 5))  # Beat 8 - more tragic
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(95, 5))  # Beat 10 - more tragic
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(100, 5))  # Beat 12 - more tragic
            
            # More tragic palmas
            for beat in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                velocity = 75 + (beat % 3) * 5  # Tragic variation
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(velocity, 8))
            
            # Ride cymbal for tragic feel
            for beat in [3, 6, 9, 12]:  # Tragic emphasis beats
                self.add_note(midi, self.drum_mapping['ride'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(70, 10))
    
    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Seguiriya variation 2 - profound with tragic ornaments."""
        for bar in range(start_bar, start_bar + bars):
            # Profound seguiriya with tragic ornaments
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(85, 5))  # Beat 1 - profound
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 2, 
                         self.get_random_velocity(80, 5))  # Beat 3 - profound
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 5, 
                         self.get_random_velocity(85, 5))  # Beat 6 - profound
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 7, 
                         self.get_random_velocity(80, 5))  # Beat 8 - profound
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 9, 
                         self.get_random_velocity(85, 5))  # Beat 10 - profound
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                         self.midi_config['ticks_per_beat'] * 11, 
                         self.get_random_velocity(90, 5))  # Beat 12 - profound
            
            # Profound palmas with ornaments
            for beat in [2, 4, 6, 8, 10, 12]:  # Off-beats only
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(75, 8))
            
            # Open hi-hats for tragic texture
            for beat in [2, 4, 6, 8, 10, 12]:  # Off-beats
                self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(55, 10))
    
    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple seguiriya fill - tragic palmas and compás accent."""
        # Tragic palmas roll
        for i in range(4):
            self.add_note(midi, self.drum_mapping['snare'], bar, 
                        i * self.midi_config['ticks_per_beat'] * 3, 
                        self.get_random_velocity(85, 10))
        
        # Seguiriya compás accent
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 8, 
                     self.get_random_velocity(110, 5))
        
        # Tragic hi-hat flourish
        self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                     self.midi_config['ticks_per_beat'] * 10, 
                     self.get_random_velocity(75, 10))
    
    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex seguiriya fill - tragic with tom work."""
        # Complex palmas pattern with tragic ornaments
        palmas_pattern = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for i, beat in enumerate(palmas_pattern):
            if beat in [1, 3, 6, 8, 10, 12]:  # Seguiriya emphasis beats
                velocity = 80 + (i % 2) * 10  # Tragic variation
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(velocity, 8))
        
        # Tom work for tragic effect
        toms = [self.drum_mapping['tom_high'], self.drum_mapping['tom_mid'], self.drum_mapping['tom_low']]
        for i, tom in enumerate(toms):
            self.add_note(midi, tom, bar, 
                        self.midi_config['ticks_per_beat'] * (4 + i * 2), 
                        self.get_random_velocity(90, 10))
        
        # Seguiriya compás accent with crash
        self.add_note(midi, self.drum_mapping['kick'], bar, 
                     self.midi_config['ticks_per_beat'] * 8, 
                     self.get_random_velocity(115, 5))
        self.add_note(midi, self.drum_mapping['crash'], bar, 
                     self.midi_config['ticks_per_beat'] * 8, 
                     self.get_random_velocity(105, 10))
    
    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Seguiriya intro - builds up with tragic palmas and compás."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 2:
                # Soft tragic palmas only - building tragedy
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 3, 
                            self.get_random_velocity(60, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(60, 8))
            elif bar < start_bar + 4:
                # Add compás - building tragedy
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(75, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(75, 5))
                # More tragic palmas
                for beat in [3, 6, 9]:
                    self.add_note(midi, self.drum_mapping['snare'], bar, 
                                beat * self.midi_config['ticks_per_beat'], 
                                self.get_random_velocity(70, 8))
            else:
                # Full seguiriya pattern
                self.create_basic_pattern(midi, bar, 1)
    
    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Seguiriya verse - steady compás with tragic palmas."""
        for bar in range(start_bar, start_bar + bars):
            # Steady seguiriya compás
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(85, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(80, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 5, 
                        self.get_random_velocity(85, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 7, 
                        self.get_random_velocity(80, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 9, 
                        self.get_random_velocity(85, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 11, 
                        self.get_random_velocity(90, 5))
            
            # Tragic palmas
            for beat in [2, 4, 6, 8, 10, 12]:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(80, 8))
            
            # Tragic hi-hats
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(70, 10))
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, 
                        self.midi_config['ticks_per_beat'] * 6, 
                        self.get_random_velocity(70, 10))
    
    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Seguiriya chorus - maximum tragic intensity."""
        for bar in range(start_bar, start_bar + bars):
            # Intense seguiriya compás
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 5, 
                        self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 7, 
                        self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 9, 
                        self.get_random_velocity(95, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 11, 
                        self.get_random_velocity(100, 5))
            
            # Intense tragic palmas
            for beat in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(90, 8))
            
            # Ride cymbal for tragedy
            self.add_note(midi, self.drum_mapping['ride'], bar, 
                        self.midi_config['ticks_per_beat'] * 6, 
                        self.get_random_velocity(75, 10))
    
    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Seguiriya bridge - different tragic style with contrast."""
        for bar in range(start_bar, start_bar + bars):
            # Different tragic rhythm (soleá style) for contrast
            self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                         self.get_random_velocity(80, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 2, 
                        self.get_random_velocity(75, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 5, 
                        self.get_random_velocity(80, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 7, 
                        self.get_random_velocity(75, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 9, 
                        self.get_random_velocity(80, 5))
            self.add_note(midi, self.drum_mapping['kick'], bar, 
                        self.midi_config['ticks_per_beat'] * 11, 
                        self.get_random_velocity(85, 5))
            
            # Soleá palmas for contrast
            for beat in [2, 4, 6, 8, 10, 12]:
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(70, 8))
            
            # Open hi-hats for contrast
            for beat in [2, 4, 6, 8, 10, 12]:
                self.add_note(midi, self.drum_mapping['open_hh'], bar, 
                            beat * self.midi_config['ticks_per_beat'], 
                            self.get_random_velocity(65, 10))
    
    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Seguiriya outro - winds down with tragic ending."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                # Full seguiriya
                self.create_basic_pattern(midi, bar, 1)
            elif bar < start_bar + 6:
                # Reduce to essential beats
                self.add_note(midi, self.drum_mapping['kick'], bar, 0, 
                             self.get_random_velocity(80, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(80, 5))
                self.add_note(midi, self.drum_mapping['kick'], bar, 
                            self.midi_config['ticks_per_beat'] * 8, 
                            self.get_random_velocity(80, 5))
                # Essential tragic palmas
                for beat in [3, 6, 9]:
                    self.add_note(midi, self.drum_mapping['snare'], bar, 
                                beat * self.midi_config['ticks_per_beat'], 
                                self.get_random_velocity(70, 8))
            else:
                # Final tragic palmas only
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 3, 
                            self.get_random_velocity(65, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 6, 
                            self.get_random_velocity(65, 8))
                self.add_note(midi, self.drum_mapping['snare'], bar, 
                            self.midi_config['ticks_per_beat'] * 9, 
                            self.get_random_velocity(65, 8))

