"""
Main pattern generator with modular genre support and variation system.
"""

import os
import time
import importlib
from typing import Dict, Type, Optional
from core.base_pattern import BasePattern


class PatternGenerator:
    """Main generator that manages all genre patterns with variation system."""
    
    def __init__(self):
        self.patterns: Dict[str, Type[BasePattern]] = {}
        self.load_patterns()
    
    def load_patterns(self) -> None:
        """Load all available pattern classes from genre modules."""
        # For now, manually register patterns
        # Later this could be automated with dynamic imports
        
        try:
            from genres.argentinian.rock_nacional import RockNacionalPattern
            self.patterns['rock_nacional'] = RockNacionalPattern
        except ImportError:
            pass
        
        try:
            from genres.argentinian.blues_argentino import BluesArgentinoPattern
            self.patterns['blues_argentino'] = BluesArgentinoPattern
        except ImportError:
            pass
        
        # TODO: Add more patterns as they're implemented
        # from genres.experimental.prog_rock import ProgRockPattern
        # from genres.madchester.madchester import MadchesterPattern
        # etc.
    
    def get_available_genres(self) -> Dict[str, str]:
        """Get dictionary of available genres and their display names."""
        available = {}
        for key, pattern_class in self.patterns.items():
            # Create temporary instance to get genre name
            temp_instance = pattern_class()
            available[key] = temp_instance.genre_name
        return available
    
    def generate_pattern(self, genre: str, tempo: int = 150, seed: Optional[int] = None, 
                        bars: int = 150) -> BasePattern:
        """Generate a pattern for the specified genre."""
        if genre not in self.patterns:
            available = list(self.patterns.keys())
            raise ValueError(f"Unknown genre: {genre}. Available: {available}")
        
        pattern_class = self.patterns[genre]
        pattern_instance = pattern_class(tempo=tempo, seed=seed)
        
        return pattern_instance
    
    def generate_and_save(self, genre: str, tempo: int = 150, seed: Optional[int] = None,
                         output_dir: str = "output", bars: int = 150) -> str:
        """Generate pattern and save to MIDI file."""
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate pattern
        pattern_instance = self.generate_pattern(genre, tempo, seed, bars)
        midi_file = pattern_instance.generate_pattern(bars)
        
        # Create filename
        timestamp = int(time.time())
        filename = f"{genre}_{tempo}bpm_{timestamp}.mid"
        if seed is not None:
            filename = f"{genre}_{tempo}bpm_seed{seed}_{timestamp}.mid"
        
        output_path = os.path.join(output_dir, filename)
        
        # Save MIDI file
        with open(output_path, "wb") as f:
            midi_file.writeFile(f)
        
        return output_path
    
    def get_pattern_info(self, genre: str) -> Dict[str, str]:
        """Get information about a specific pattern."""
        if genre not in self.patterns:
            raise ValueError(f"Unknown genre: {genre}")
        
        pattern_class = self.patterns[genre]
        temp_instance = pattern_class()
        
        return {
            'genre': genre,
            'name': temp_instance.genre_name,
            'description': temp_instance.description,
            'variations': ', '.join(temp_instance.variation_types)
        }
