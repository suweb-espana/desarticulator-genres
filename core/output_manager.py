"""
Output manager for organized MIDI file generation and folder structure.
"""

import os
import time
from typing import Dict, List, Optional, Tuple
from pathlib import Path
from midiutil import MIDIFile
from core.song_structure import SongStructure


class OutputSession:
    """Manages a single generation session with organized outputs."""
    
    def __init__(self, base_output_dir: str = "output"):
        self.base_output_dir = base_output_dir
        self.timestamp = int(time.time())
        self.session_folder = None
        self.files_generated = []
        
    def create_session_folder(self, genre: str, structure_or_section: str, tempo: int, seed: Optional[int] = None) -> str:
        """Create organized session folder."""
        # Create session folder name
        if seed is not None:
            folder_name = f"{genre}_{structure_or_section}_{tempo}bpm_seed{seed}_{self.timestamp}"
        else:
            folder_name = f"{genre}_{structure_or_section}_{tempo}bpm_{self.timestamp}"
        
        self.session_folder = os.path.join(self.base_output_dir, folder_name)
        os.makedirs(self.session_folder, exist_ok=True)
        
        return self.session_folder
    
    def save_midi_file(self, midi: MIDIFile, filename: str) -> str:
        """Save MIDI file to session folder."""
        if not self.session_folder:
            raise ValueError("Session folder not created. Call create_session_folder first.")
        
        filepath = os.path.join(self.session_folder, filename)
        
        with open(filepath, "wb") as f:
            midi.writeFile(f)
        
        self.files_generated.append(filepath)
        return filepath
    
    def create_session_summary(self, genre: str, genre_description: str, structure_info: str = None, 
                             section_info: str = None, tempo: int = 150, seed: Optional[int] = None) -> str:
        """Create a summary file for the session."""
        if not self.session_folder:
            raise ValueError("Session folder not created.")
        
        summary_path = os.path.join(self.session_folder, "session_info.txt")
        
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write("# Desarticulator Generation Session\n")
            f.write("=" * 40 + "\n\n")
            f.write(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.timestamp))}\n")
            f.write(f"Genre: {genre}\n")
            f.write(f"Description: {genre_description}\n")
            f.write(f"Tempo: {tempo} BPM\n")
            if seed is not None:
                f.write(f"Seed: {seed}\n")
            f.write("\n")
            
            if structure_info:
                f.write("Structure Information:\n")
                f.write("-" * 20 + "\n")
                f.write(structure_info)
                f.write("\n")
            
            if section_info:
                f.write("Section Information:\n")
                f.write("-" * 20 + "\n")
                f.write(section_info)
                f.write("\n")
            
            f.write("Generated Files:\n")
            f.write("-" * 15 + "\n")
            for file_path in self.files_generated:
                filename = os.path.basename(file_path)
                f.write(f"- {filename}\n")
        
        return summary_path


class OrganizedOutputManager:
    """Manages organized output generation for complete songs and sections."""
    
    def __init__(self, base_output_dir: str = "output"):
        self.base_output_dir = base_output_dir
    
    def generate_complete_song_organized(self, pattern_instance, structure: SongStructure, 
                                       genre: str, tempo: int, seed: Optional[int] = None) -> Tuple[str, List[str]]:
        """Generate complete song with all individual sections organized in folder."""
        
        # Create session
        session = OutputSession(self.base_output_dir)
        session_folder = session.create_session_folder(genre, f"{structure.name.lower().replace(' ', '_')}_complete", tempo, seed)
        
        # Generate complete song
        pattern_instance.setup_randomization()
        complete_midi = MIDIFile(1)
        complete_midi.addTempo(pattern_instance.midi_config['track'], 0, tempo)
        
        # Generate each section in the complete song
        for section in structure.get_sections():
            if section.section_type == 'intro':
                pattern_instance.create_intro_section(complete_midi, section.start_bar, section.bars)
            elif section.section_type == 'verse':
                pattern_instance.create_verse_section(complete_midi, section.start_bar, section.bars)
            elif section.section_type == 'chorus':
                pattern_instance.create_chorus_section(complete_midi, section.start_bar, section.bars)
            elif section.section_type == 'bridge':
                pattern_instance.create_bridge_section(complete_midi, section.start_bar, section.bars)
            elif section.section_type == 'outro':
                pattern_instance.create_outro_section(complete_midi, section.start_bar, section.bars)
        
        # Save complete song
        complete_filename = f"fracaso_inminente_COMPLETE_{genre}_{structure.name.lower().replace(' ', '_')}_structure_{tempo}bpm.mid"
        complete_path = session.save_midi_file(complete_midi, complete_filename)
        
        # Generate individual sections
        individual_files = []
        section_counter = {}  # Track multiple instances of same section type
        
        for section in structure.get_sections():
            # Create unique section filename
            if section.section_type in section_counter:
                section_counter[section.section_type] += 1
                section_filename = f"fracaso_inminente_{section.section_type}_{section_counter[section.section_type]}_{section.bars}bars.mid"
            else:
                section_counter[section.section_type] = 1
                section_filename = f"fracaso_inminente_{section.section_type}_{section.bars}bars.mid"
            
            # Generate individual section MIDI
            section_midi = pattern_instance.generate_section(section.section_type, section.bars)
            section_path = session.save_midi_file(section_midi, section_filename)
            individual_files.append(section_path)
        
        # Create session summary
        structure_info = structure.get_section_info()
        session.create_session_summary(
            genre=genre,
            genre_description=pattern_instance.description,
            structure_info=structure_info,
            tempo=tempo,
            seed=seed
        )
        
        return session_folder, [complete_path] + individual_files
    
    def generate_single_section_organized(self, pattern_instance, section_type: str, bars: int,
                                        genre: str, tempo: int, seed: Optional[int] = None) -> Tuple[str, str]:
        """Generate single section organized in folder."""
        
        # Create session
        session = OutputSession(self.base_output_dir)
        session_folder = session.create_session_folder(genre, f"{section_type}_section", tempo, seed)
        
        # Generate section
        section_midi = pattern_instance.generate_section(section_type, bars)
        
        # Save section
        section_filename = f"fracaso_inminente_{section_type}_{bars}bars.mid"
        section_path = session.save_midi_file(section_midi, section_filename)
        
        # Create session summary
        section_info = f"Section: {section_type.title()}\nBars: {bars}\nType: Individual Section"
        session.create_session_summary(
            genre=genre,
            genre_description=pattern_instance.description,
            section_info=section_info,
            tempo=tempo,
            seed=seed
        )
        
        return session_folder, section_path
    
    def generate_traditional_pattern_organized(self, pattern_instance, bars: int,
                                             genre: str, tempo: int, seed: Optional[int] = None) -> Tuple[str, str]:
        """Generate traditional pattern organized in folder."""
        
        # Create session
        session = OutputSession(self.base_output_dir)
        session_folder = session.create_session_folder(genre, f"traditional_{bars}bars", tempo, seed)
        
        # Generate pattern
        pattern_midi = pattern_instance.generate_pattern(bars)
        
        # Save pattern
        pattern_filename = f"fracaso_inminente_traditional_pattern_{bars}bars.mid"
        pattern_path = session.save_midi_file(pattern_midi, pattern_filename)
        
        # Create session summary
        pattern_info = f"Pattern: Traditional\nBars: {bars}\nType: Full Pattern with Variations"
        session.create_session_summary(
            genre=genre,
            genre_description=pattern_instance.description,
            section_info=pattern_info,
            tempo=tempo,
            seed=seed
        )
        
        return session_folder, pattern_path
