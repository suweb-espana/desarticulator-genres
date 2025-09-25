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
            'pop': 'Pop',
            'rap': 'Rap',
            'rock': 'Rock',
            'hip_hop': 'Hip Hop',
            'indie': 'Indie',
            'country': 'Country',
            'modern_rock': 'Modern Rock',
            'alternative_metal': 'Alternative Metal',
            'classic_rock': 'Classic Rock',
            'r_and_b': 'R&B',
            'dance_pop': 'Dance Pop',
            'pop_rap': 'Pop Rap',
            'soft_rock': 'Soft Rock',
            'reggaeton': 'Reggaetón',
            'hard_rock': 'Hard Rock',
            'pop_punk': 'Pop Punk',
            'nu_metal': 'Nu Metal',
            'post_grunge': 'Post-Grunge',
            'trap': 'Trap',
            'urbano_latino': 'Urbano Latino'
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
        
        if genre == 'pop':
            return self._create_pop_groove(midi, tempo)
        elif genre == 'rap':
            return self._create_rap_groove(midi, tempo)
        elif genre == 'rock':
            return self._create_rock_groove(midi, tempo)
        elif genre == 'hip_hop':
            return self._create_hip_hop_groove(midi, tempo)
        elif genre == 'indie':
            return self._create_indie_groove(midi, tempo)
        elif genre == 'country':
            return self._create_country_groove(midi, tempo)
        elif genre == 'modern_rock':
            return self._create_modern_rock_groove(midi, tempo)
        elif genre == 'alternative_metal':
            return self._create_alternative_metal_groove(midi, tempo)
        elif genre == 'classic_rock':
            return self._create_classic_rock_groove(midi, tempo)
        elif genre == 'r_and_b':
            return self._create_r_and_b_groove(midi, tempo)
        elif genre == 'dance_pop':
            return self._create_dance_pop_groove(midi, tempo)
        elif genre == 'pop_rap':
            return self._create_pop_rap_groove(midi, tempo)
        elif genre == 'soft_rock':
            return self._create_soft_rock_groove(midi, tempo)
        elif genre == 'reggaeton':
            return self._create_reggaeton_groove(midi, tempo)
        elif genre == 'hard_rock':
            return self._create_hard_rock_groove(midi, tempo)
        elif genre == 'pop_punk':
            return self._create_pop_punk_groove(midi, tempo)
        elif genre == 'nu_metal':
            return self._create_nu_metal_groove(midi, tempo)
        elif genre == 'post_grunge':
            return self._create_post_grunge_groove(midi, tempo)
        elif genre == 'trap':
            return self._create_trap_groove(midi, tempo)
        elif genre == 'urbano_latino':
            return self._create_urbano_latino_groove(midi, tempo)
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
    
    def _create_pop_groove(self, midi, tempo):
        """Create pop drum pattern - clean, commercial sound."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 90)
                self._add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 2, 85)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 95)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 90)
                
                for eighth in range(8):
                    self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 random.randint(70, 80))
        
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
    
    def _create_rap_groove(self, midi, tempo):
        """Create rap drum pattern - heavy kick, snare on 2 and 4."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 100)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'], 95)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 100)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 100)
                
                for sixteenth in range(16):
                    if sixteenth % 4 == 0:
                        self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                     sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                     random.randint(75, 85))
        
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
    
    def _create_rock_groove(self, midi, tempo):
        """Create rock drum pattern - classic 4/4 with driving rhythm."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 95)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 90)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 100)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 98)
                
                for eighth in range(8):
                    self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 random.randint(75, 85))
        
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
    
    def _create_hip_hop_groove(self, midi, tempo):
        """Create hip hop drum pattern - syncopated, groove-oriented."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 95)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'] * 2, 90)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 100)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 95)
                
                for sixteenth in range(16):
                    if sixteenth % 2 == 0:
                        self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                     sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                     random.randint(70, 80))
        
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
    
    def _create_indie_groove(self, midi, tempo):
        """Create indie drum pattern - creative, less conventional."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 85)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'], 80)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 90)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 85)
                
                for eighth in range(8):
                    if random.random() < 0.7:
                        self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                     eighth * self.midi_config['ticks_per_eighth'], 
                                     random.randint(65, 75))
        
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
    
    def _create_country_groove(self, midi, tempo):
        """Create country drum pattern - traditional, steady rhythm."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 90)
                self._add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 2, 85)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 95)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 90)
                
                for eighth in range(8):
                    self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 random.randint(70, 80))
        
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
    
    def _create_modern_rock_groove(self, midi, tempo):
        """Create modern rock drum pattern - contemporary sound."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 95)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 90)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 100)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 98)
                
                for eighth in range(8):
                    self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 random.randint(75, 85))
        
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
    
    def _create_alternative_metal_groove(self, midi, tempo):
        """Create alternative metal drum pattern - heavy but melodic."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 100)
                self._add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 2, 95)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 100)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 100)
                
                for sixteenth in range(16):
                    if sixteenth % 4 == 0:
                        self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                     sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                     random.randint(80, 90))
        
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
    
    def _create_classic_rock_groove(self, midi, tempo):
        """Create classic rock drum pattern - timeless sound."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 90)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 85)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 95)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 90)
                
                for eighth in range(8):
                    self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 random.randint(70, 80))
        
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
    
    def _create_r_and_b_groove(self, midi, tempo):
        """Create R&B drum pattern - smooth, groove-oriented."""
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
                                     random.randint(70, 80))
        
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
    
    def _create_dance_pop_groove(self, midi, tempo):
        """Create dance pop drum pattern - electronic, danceable."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 95)
                self._add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 2, 90)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 100)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 95)
                
                for sixteenth in range(16):
                    if sixteenth % 2 == 0:
                        self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                     sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                     random.randint(75, 85))
        
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
    
    def _create_pop_rap_groove(self, midi, tempo):
        """Create pop rap drum pattern - commercial hip hop."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 95)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'], 90)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 100)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 95)
                
                for sixteenth in range(16):
                    if sixteenth % 4 == 0:
                        self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                     sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                     random.randint(70, 80))
        
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
    
    def _create_soft_rock_groove(self, midi, tempo):
        """Create soft rock drum pattern - mellow, melodic."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 85)
                self._add_note(midi, self.drum_mapping['kick'], bar, self.midi_config['ticks_per_beat'] * 2, 80)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 90)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 85)
                
                for eighth in range(8):
                    self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 random.randint(65, 75))
        
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
    
    def _create_reggaeton_groove(self, midi, tempo):
        """Create reggaetón drum pattern - Latin urban rhythm."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 95)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'] * 2, 90)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 100)
                self._add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'], 95)
                
                for sixteenth in range(16):
                    if sixteenth % 2 == 0:
                        self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                     sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                     random.randint(75, 85))
        
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
    
    def _create_hard_rock_groove(self, midi, tempo):
        """Create hard rock drum pattern - aggressive, powerful."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 100)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 95)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 100)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 100)
                
                for eighth in range(8):
                    self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 random.randint(80, 90))
        
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
    
    def _create_pop_punk_groove(self, midi, tempo):
        """Create pop punk drum pattern - energetic, melodic punk."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 95)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 90)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 100)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 98)
                
                for sixteenth in range(16):
                    if sixteenth % 2 == 0:
                        self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                     sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                     random.randint(75, 85))
        
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
    
    def _create_nu_metal_groove(self, midi, tempo):
        """Create nu metal drum pattern - heavy, syncopated."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 100)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'], 95)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 100)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 100)
                
                for sixteenth in range(16):
                    if sixteenth % 4 == 0:
                        self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                     sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                     random.randint(80, 90))
        
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
    
    def _create_post_grunge_groove(self, midi, tempo):
        """Create post-grunge drum pattern - alternative rock sound."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 90)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_eighth'], 85)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 95)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 90)
                
                for eighth in range(8):
                    self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                 eighth * self.midi_config['ticks_per_eighth'], 
                                 random.randint(70, 80))
        
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
    
    def _create_trap_groove(self, midi, tempo):
        """Create trap drum pattern - modern hip hop with hi-hats."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 100)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'] * 2, 95)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 100)
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'] * 3, 100)
                
                for sixteenth in range(16):
                    if sixteenth % 2 == 0:
                        self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                     sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                     random.randint(70, 80))
        
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
    
    def _create_urbano_latino_groove(self, midi, tempo):
        """Create urbano latino drum pattern - Latin urban fusion."""
        def add_basic_pattern(start_bar):
            for bar in range(start_bar, start_bar + 8):
                self._add_note(midi, self.drum_mapping['kick'], bar, 0, 95)
                self._add_note(midi, self.drum_mapping['kick'], bar, 
                             self.midi_config['ticks_per_beat'] * 2 + self.midi_config['ticks_per_sixteenth'], 90)
                
                self._add_note(midi, self.drum_mapping['snare'], bar, self.midi_config['ticks_per_beat'], 100)
                self._add_note(midi, self.drum_mapping['snare'], bar, 
                             self.midi_config['ticks_per_beat'] * 3 + self.midi_config['ticks_per_sixteenth'], 95)
                
                for sixteenth in range(16):
                    if sixteenth % 2 == 0:
                        self._add_note(midi, self.drum_mapping['closed_hh'], bar, 
                                     sixteenth * self.midi_config['ticks_per_sixteenth'], 
                                     random.randint(75, 85))
        
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
    parser.add_argument("--genre", "-g", 
                       choices=['pop', 'rap', 'rock', 'hip_hop', 'indie', 'country', 'modern_rock', 
                               'alternative_metal', 'classic_rock', 'r_and_b', 'dance_pop', 'pop_rap', 
                               'soft_rock', 'reggaeton', 'hard_rock', 'pop_punk', 'nu_metal', 
                               'post_grunge', 'trap', 'urbano_latino'],
                       default='pop', help="Musical genre for drum pattern")
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
