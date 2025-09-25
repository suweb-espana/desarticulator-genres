#!/usr/bin/env python3
"""
Generate drum patterns for all available genres
Example script showing how to use the multi-genre system
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from desarticulator import Desarticulator

def main():
    generator = Desarticulator()
    
    genres = ['punk_rock', 'jazz', 'metal', 'funk', 'latin', 'blues']
    tempos = {
        'punk_rock': 150,
        'jazz': 120,
        'metal': 180,
        'funk': 110,
        'latin': 130,
        'blues': 100
    }
    
    print("🎵 Desarticulator - Multi-Genre Drum Pattern Generator")
    print("=" * 60)
    
    for genre in genres:
        tempo = tempos[genre]
        print(f"\n🎶 Generating {generator.available_genres[genre]} ({tempo} BPM)...")
        
        try:
            output_path = generator.generate_drum_pattern(
                genre=genre,
                tempo=tempo,
                seed=42  # Fixed seed for reproducible demo
            )
            print(f"✅ Generated: {output_path}")
        except Exception as e:
            print(f"❌ Error generating {genre}: {e}")
    
    print(f"\n🎉 All patterns generated in output/ directory!")
    print("Import these MIDI files into Superior Drummer 3 to hear the results.")

if __name__ == "__main__":
    main()
