"""
Song structure generator for complete 150-bar compositions.
"""

from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from midiutil import MIDIFile


@dataclass
class SongSection:
    """Represents a section of a song."""
    section_type: str  # intro, verse, chorus, bridge, outro
    bars: int
    start_bar: int = 0


class SongStructure:
    """Defines complete song structures that total exactly 150 bars."""
    
    def __init__(self, name: str, sections: List[Tuple[str, int]]):
        self.name = name
        self.sections = []
        current_bar = 0
        
        for section_type, bars in sections:
            self.sections.append(SongSection(section_type, bars, current_bar))
            current_bar += bars
        
        self.total_bars = current_bar
        
        if self.total_bars != 150:
            raise ValueError(f"Song structure '{name}' totals {self.total_bars} bars, must be exactly 150")
    
    def get_sections(self) -> List[SongSection]:
        """Get all sections in order."""
        return self.sections
    
    def get_section_info(self) -> str:
        """Get formatted section information."""
        info = f"{self.name} ({self.total_bars} bars):\n"
        for section in self.sections:
            info += f"  {section.section_type.title()}: bars {section.start_bar + 1}-{section.start_bar + section.bars} ({section.bars} bars)\n"
        return info


class SongStructureGenerator:
    """Generator for predefined song structures."""
    
    def __init__(self):
        self.structures = self._create_predefined_structures()
    
    def _create_predefined_structures(self) -> Dict[str, SongStructure]:
        """Create predefined song structures that total 150 bars."""
        structures = {}
        
        # Classic Rock Structure (150 bars total)
        structures['classic_rock'] = SongStructure('Classic Rock', [
            ('intro', 8),
            ('verse', 16),
            ('chorus', 16), 
            ('verse', 16),
            ('chorus', 16),
            ('bridge', 8),
            ('chorus', 16),
            ('verse', 16),
            ('chorus', 16),
            ('outro', 22)  # Extended outro
        ])
        
        # Pop Structure (150 bars total)
        structures['pop'] = SongStructure('Pop', [
            ('intro', 8),
            ('verse', 16),
            ('chorus', 16),
            ('verse', 16), 
            ('chorus', 16),
            ('bridge', 8),
            ('chorus', 16),
            ('chorus', 16),  # Double chorus
            ('outro', 38)   # Extended outro with fade
        ])
        
        # Progressive Structure (150 bars total)
        structures['progressive'] = SongStructure('Progressive', [
            ('intro', 12),
            ('verse', 20),
            ('chorus', 16),
            ('verse', 20),
            ('chorus', 16), 
            ('bridge', 16),
            ('verse', 12),
            ('chorus', 16),
            ('outro', 22)
        ])
        
        # Blues Structure (150 bars total)  
        structures['blues'] = SongStructure('Blues', [
            ('intro', 8),
            ('verse', 24),  # 12-bar blues x2
            ('chorus', 12), # 12-bar chorus
            ('verse', 24),  # 12-bar blues x2
            ('chorus', 12), # 12-bar chorus
            ('bridge', 16), # Extended bridge
            ('verse', 24),  # 12-bar blues x2
            ('chorus', 12), # 12-bar chorus
            ('outro', 18)   # Extended blues outro
        ])
        
        # Punk/Hardcore Structure (150 bars total)
        structures['punk'] = SongStructure('Punk', [
            ('intro', 4),   # Short punk intro
            ('verse', 16),
            ('chorus', 8),  # Short punk chorus
            ('verse', 16),
            ('chorus', 8),
            ('bridge', 8),
            ('verse', 16),
            ('chorus', 8),
            ('verse', 16),
            ('chorus', 8),
            ('verse', 16),
            ('chorus', 8),
            ('outro', 18)   # Punk outro
        ])
        
        # Ballad Structure (150 bars total)
        structures['ballad'] = SongStructure('Ballad', [
            ('intro', 12),  # Longer intro
            ('verse', 20),  # Extended verse
            ('chorus', 20), # Extended chorus
            ('verse', 20),  # Extended verse
            ('chorus', 20), # Extended chorus
            ('bridge', 12), 
            ('chorus', 20), # Extended chorus
            ('outro', 26)   # Long ballad outro
        ])
        
        return structures
    
    def get_available_structures(self) -> Dict[str, str]:
        """Get available song structures with descriptions."""
        return {key: structure.name for key, structure in self.structures.items()}
    
    def get_structure(self, structure_name: str) -> SongStructure:
        """Get a specific song structure."""
        if structure_name not in self.structures:
            available = list(self.structures.keys())
            raise ValueError(f"Unknown structure: {structure_name}. Available: {available}")
        
        return self.structures[structure_name]
    
    def generate_complete_song(self, pattern_instance, structure_name: str) -> MIDIFile:
        """Generate a complete song using the specified structure."""
        structure = self.get_structure(structure_name)
        
        # Setup MIDI file
        pattern_instance.setup_randomization()
        midi = MIDIFile(1)
        midi.addTempo(pattern_instance.midi_config['track'], 0, pattern_instance.tempo)
        
        # Generate each section
        for section in structure.get_sections():
            if section.section_type == 'intro':
                pattern_instance.create_intro_section(midi, section.start_bar, section.bars)
            elif section.section_type == 'verse':
                pattern_instance.create_verse_section(midi, section.start_bar, section.bars)
            elif section.section_type == 'chorus':
                pattern_instance.create_chorus_section(midi, section.start_bar, section.bars)
            elif section.section_type == 'bridge':
                pattern_instance.create_bridge_section(midi, section.start_bar, section.bars)
            elif section.section_type == 'outro':
                pattern_instance.create_outro_section(midi, section.start_bar, section.bars)
        
        return midi
    
    def get_structure_info(self, structure_name: str) -> str:
        """Get detailed information about a structure."""
        structure = self.get_structure(structure_name)
        return structure.get_section_info()
    
    def validate_structure(self, sections: List[Tuple[str, int]]) -> bool:
        """Validate that a custom structure totals 150 bars."""
        total = sum(bars for _, bars in sections)
        return total == 150
    
    def create_custom_structure(self, name: str, sections: List[Tuple[str, int]]) -> SongStructure:
        """Create a custom song structure."""
        return SongStructure(name, sections)
