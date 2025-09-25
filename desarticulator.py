#!/usr/bin/env python3
"""
Desarticulator - Multi-Genre MIDI Drum Pattern Generator
Advanced drum pattern generator with multiple musical styles and variations.
"""

import os
import random
import time
import argparse
from midiutil import MIDIFile

class Desarticulator:
    def __init__(self):
        self.available_genres = {
            'punk_rock': 'Punk Rock',
            'jazz': 'Jazz',
            'metal': 'Metal',
            'funk': 'Funk',
            'latin': 'Latin',
            'blues': 'Blues'
        }
        
        self.midi_config = {
            'track': 0,
            'channel': 9,
            'ppq': 480,
            'ticks_per_bar': 1920,
            'ticks_per_beat': 480,
            'ticks_per_eighth': 240,
            'ticks_per_sixteenth': 120
        }
        
        self.drum_mapping = {
            'kick': 36,
            'snare': 38,
            'closed_hh': 42,
            'open_hh': 46,
            'ride': 51,
            'crash': 49,
            'tom_high': 43,
            'tom_mid': 45,
            'tom_low': 48
        }
    
    def create_midi_file(self, genre, tempo=150, seed=None, bars=150):
        """Create MIDI file for specified genre with given parameters."""
        if seed is None:
            seed = int(time.time())
        
        random.seed(seed)
        
        midi = MIDIFile(1)
        midi.addTempo(self.midi_config['track'], 0, tempo)
        
        if genre == 'punk_rock':
            return self._create_punk_rock_groove(midi, tempo)
        elif genre == 'jazz':
            return self._create_jazz_groove(midi, tempo)
        elif genre == 'metal':
            return self._create_metal_groove(midi, tempo)
        elif genre == 'funk':
            return self._create_funk_groove(midi, tempo)
        elif genre == 'latin':
            return self._create_latin_groove(midi, tempo)
        elif genre == 'blues':
            return self._create_blues_groove(midi, tempo)
        else:
            raise ValueError(f"Unknown genre: {genre}")
    
    def _add_note(self, midi, drum, bar, beat_pos, velocity=85, duration=0.1):
        """Add a MIDI note to the track."""
        time_ticks = (bar * self.midi_config['ticks_per_bar']) + beat_pos
        midi.addNote(
            self.midi_config['track'],
            self.midi_config['channel'],
            drum,
            time_ticks / self.midi_config['ppq'],
            duration,
            velocity
        )
    
    def _create_punk_rock_groove(self, midi, tempo):
        """Create punk rock drum pattern."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 95)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 90)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 100)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 98)
                
                for sixteenth in range(16):
                    if sixteenth % 2 == 0:
                        vel = random.randint(75, 85) if sixteenth % 4 == 0 else random.randint(65, 75)
                        self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                     sixteenth * self.midi_config['ticks_per_sixteenth'], vel)
                    else:
                        if random.random() < 0.3:
                            self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                         sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                         random.randint(40, 55))
        
        def add_fill_simple(bar):
            self._add_note(midi, self.drum_mapping['kick'], bar, 0, 95)
            self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 100)
            
            fill_pattern = [
                (self.midi_config['ticks_per_beat'] * 2, self.drum_mapping['tom_high'], 90),
                (self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], self.drum_mapping['tom_high'], 85),
                (self.midi_config['ticks_per_beat'] * 3, self.drum_mapping['tom_mid'], 92),
                (self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_eighth'], self.drum_mapping['tom_low'], 95)
            ]
            
            for pos, drum, vel in fill_pattern:
                self._add_note(midi, drum, bar, pos, vel)
        
        current_bar = 0
        while current_bar < 149:
            if current_bar == 148:
                add_fill_simple(current_bar)
                current_bar += 1
            elif (current_bar + 1) % 8 == 0:
                add_fill_simple(current_bar)
                current_bar += 1
            else:
                add_basic_pattern(current_bar)
                current_bar += 7
        
        self._add_note(midi, self.drum_mapping['crash'], 149, 0, 100, 2.0)
        self._add_note(midi, self.drum_mapping['kick'], 149, 0, 100)
        
        return midi
    
    def _create_jazz_groove(self, midi, tempo):
        """Create jazz drum pattern with swing feel."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 85)
                self._add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 2, 80)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 90)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 88)
                
                for eighth in range(8):
                    swing_offset = 0 if eighth % 2 == 0 else self.midi_config['ticks_per_sixteenth']
                    self._add_note(midi, self.drum_mapping['ride'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'] + swing_offset, 
                                 random.randint(70, 85))
        
        current_bar = 0
        while current_bar < 149:
            if current_bar == 148:
                add_basic_pattern(current_bar)
                current_bar += 1
            elif (current_bar + 1) % 8 == 0:
                add_basic_pattern(current_bar)
                current_bar += 1
            else:
                add_basic_pattern(current_bar)
                current_bar += 7
        
        self._add_note(midi, self.drum_mapping['crash'], 149, 0, 100, 2.0)
        return midi
    
    def _create_metal_groove(self, midi, tempo):
        """Create metal drum pattern with double bass and blast beats."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 100)
                self._add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'], 100)
                self._add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 2, 100)
                self._add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 3, 100)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 100)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 100)
                
                for sixteenth in range(16):
                    if sixteenth % 4 == 0:
                        self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                     sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                     random.randint(80, 95))
        
        current_bar = 0
        while current_bar < 149:
            if current_bar == 148:
                add_basic_pattern(current_bar)
                current_bar += 1
            elif (current_bar + 1) % 8 == 0:
                add_basic_pattern(current_bar)
                current_bar += 1
            else:
                add_basic_pattern(current_bar)
                current_bar += 7
        
        self._add_note(midi, self.drum_mapping['crash'], 149, 0, 100, 2.0)
        self._add_note(midi, self.drum_mapping['kick'], 149, 0, 100)
        return midi
    
    def _create_funk_groove(self, midi, tempo):
        """Create funk drum pattern with ghost notes and syncopation."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 90)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'], 85)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 95)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 90)
                
                for sixteenth in range(16):
                    if sixteenth % 2 == 0:
                        self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                     sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                     random.randint(70, 85))
                    else:
                        if random.random() < 0.4:
                            self._add_note(midi, self.drum_mapping['snare'], bar, 
                                         sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                         random.randint(40, 60))
        
        current_bar = 0
        while current_bar < 149:
            if current_bar == 148:
                add_basic_pattern(current_bar)
                current_bar += 1
            elif (current_bar + 1) % 8 == 0:
                add_basic_pattern(current_bar)
                current_bar += 1
            else:
                add_basic_pattern(current_bar)
                current_bar += 7
        
        self._add_note(midi, self.drum_mapping['crash'], 149, 0, 100, 2.0)
        return midi
    
    def _create_latin_groove(self, midi, tempo):
        """Create Latin drum pattern with clave rhythm."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 85)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'] * 2, 80)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 90)
                self._add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'], 85)
                
                for eighth in range(8):
                    self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 random.randint(75, 90))
        
        current_bar = 0
        while current_bar < 149:
            if current_bar == 148:
                add_basic_pattern(current_bar)
                current_bar += 1
            elif (current_bar + 1) % 8 == 0:
                add_basic_pattern(current_bar)
                current_bar += 1
            else:
                add_basic_pattern(current_bar)
                current_bar += 7
        
        self._add_note(midi, self.drum_mapping['crash'], 149, 0, 100, 2.0)
        return midi
    
    def _create_blues_groove(self, midi, tempo):
        """Create blues drum pattern with shuffle feel."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 85)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'], 80)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 90)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 88)
                
                for eighth in range(8):
                    shuffle_offset = self.midi_config['ticks_per_sixteenth'] if eighth % 2 == 1 else 0
                    self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'] + shuffle_offset, 
                                 random.randint(70, 85))
        
        current_bar = 0
        while current_bar < 149:
            if current_bar == 148:
                add_basic_pattern(current_bar)
                current_bar += 1
            elif (current_bar + 1) % 8 == 0:
                add_basic_pattern(current_bar)
                current_bar += 1
            else:
                add_basic_pattern(current_bar)
                current_bar += 7
        
        self._add_note(midi, self.drum_mapping['crash'], 149, 0, 100, 2.0)
        return midi
    
    def generate_drum_pattern(self, genre, tempo=150, seed=None, output_dir="output"):
        """Generate drum pattern and save to file."""
        if genre not in self.available_genres:
            raise ValueError(f"Unknown genre: {genre}. Available: {list(self.available_genres.keys())}")
        
        os.makedirs(output_dir, exist_ok=True)
        
        midi_file = self.create_midi_file(genre, tempo, seed)
        
        timestamp = int(time.time())
        filename = f"{genre}_{tempo}bpm_{timestamp}.mid"
        output_path = os.path.join(output_dir, filename)
        
        with open(output_path, "wb") as f:
            midi_file.writeFile(f)
        
        return output_path

def main():
    parser = argparse.ArgumentParser(description="Desarticulator - Multi-Genre MIDI Drum Pattern Generator")
    parser.add_argument("--genre", "-g", choices=['punk_rock', 'jazz', 'metal', 'funk', 'latin', 'blues'],
                       default='punk_rock', help="Musical genre for drum pattern")
    parser.add_argument("--tempo", "-t", type=int, default=150, help="Tempo in BPM")
    parser.add_argument("--seed", "-s", type=int, help="Random seed for reproducible patterns")
    parser.add_argument("--output", "-o", default="output", help="Output directory")
    
    args = parser.parse_args()
    
    generator = Desarticulator()
    
    try:
        output_path = generator.generate_drum_pattern(
            genre=args.genre,
            tempo=args.tempo,
            seed=args.seed,
            output_dir=args.output
        )
        
        print(f"Generated {output_path}")
        print(f"Genre: {generator.available_genres[args.genre]}")
        print(f"Tempo: {args.tempo} BPM")
        if args.seed:
            print(f"Seed: {args.seed}")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
