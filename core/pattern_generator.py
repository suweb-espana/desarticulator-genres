"""
Main pattern generator with modular genre support and variation system.
"""

import os
import time
import importlib
from typing import Dict, Type, Optional, Tuple, List
from core.base_pattern import BasePattern
from core.song_structure import SongStructureGenerator
from core.output_manager import OrganizedOutputManager


class PatternGenerator:
    """Main generator that manages all genre patterns with variation system."""
    
    def __init__(self):
        self.patterns: Dict[str, Type[BasePattern]] = {}
        self.song_structure_generator = SongStructureGenerator()
        self.output_manager = OrganizedOutputManager()
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
        
        try:
            from genres.experimental.prog_rock import ProgRockPattern
            self.patterns['prog_rock'] = ProgRockPattern
        except ImportError:
            pass
        
        try:
            from genres.madchester.madchester import MadchesterPattern
            self.patterns['madchester'] = MadchesterPattern
        except ImportError:
            pass
        
        try:
            from genres.argentinian.post_punk_argentino import PostPunkArgentinoPattern
            self.patterns['post_punk_argentino'] = PostPunkArgentinoPattern
        except ImportError:
            pass
        
        # TODO: Add remaining 95 patterns as they're implemented
    
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
                         output_dir: str = "output", bars: int = 150, section: Optional[str] = None,
                         structure: Optional[str] = None) -> Tuple[str, List[str]]:
        """Generate pattern and save organized output."""
        # Update output manager base directory
        self.output_manager.base_output_dir = output_dir
        
        # Generate pattern instance
        pattern_instance = self.generate_pattern(genre, tempo, seed, bars)
        
        if structure:
            # Generate complete song with all individual sections
            song_structure = self.song_structure_generator.get_structure(structure)
            session_folder, file_paths = self.output_manager.generate_complete_song_organized(
                pattern_instance, song_structure, genre, tempo, seed
            )
            return session_folder, file_paths
        elif section:
            # Generate single section
            session_folder, section_path = self.output_manager.generate_single_section_organized(
                pattern_instance, section, bars, genre, tempo, seed
            )
            return session_folder, [section_path]
        else:
            # Generate traditional pattern
            session_folder, pattern_path = self.output_manager.generate_traditional_pattern_organized(
                pattern_instance, bars, genre, tempo, seed
            )
            return session_folder, [pattern_path]
    
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
    
    def get_available_structures(self) -> Dict[str, str]:
        """Get available song structures."""
        return self.song_structure_generator.get_available_structures()
    
    def get_structure_info(self, structure_name: str) -> str:
        """Get detailed information about a song structure."""
        return self.song_structure_generator.get_structure_info(structure_name)
