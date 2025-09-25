#!/usr/bin/env python3
"""
Desarticulator v2.0 - Modular Multi-Genre MIDI Drum Pattern Generator
Advanced modular drum pattern generator with variation system and authentic genre implementations.
"""

import argparse
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from core.pattern_generator import PatternGenerator


def main():
    parser = argparse.ArgumentParser(
        description="Desarticulator v2.0 - Modular Multi-Genre MIDI Drum Pattern Generator"
    )
    parser.add_argument("--genre", "-g", 
                       help="Musical genre for drum pattern")
    parser.add_argument("--tempo", "-t", type=int, default=150, 
                       help="Tempo in BPM (default: 150)")
    parser.add_argument("--seed", "-s", type=int, 
                       help="Random seed for reproducible patterns (optional)")
    parser.add_argument("--output", "-o", default="output", 
                       help="Output directory (default: output)")
    parser.add_argument("--bars", "-b", type=int, default=150,
                       help="Number of bars to generate (default: 150)")
    parser.add_argument("--list", "-l", action="store_true", 
                       help="List all available genres")
    parser.add_argument("--info", "-i", 
                       help="Get detailed information about a specific genre")
    
    args = parser.parse_args()
    
    # Initialize generator
    try:
        generator = PatternGenerator()
    except Exception as e:
        print(f"Error initializing pattern generator: {e}")
        return 1
    
    # List available genres
    if args.list:
        available = generator.get_available_genres()
        if not available:
            print("No genres available. Make sure pattern modules are properly installed.")
            return 1
            
        print("Available genres:")
        for key, name in available.items():
            print(f"  {key}: {name}")
        return 0
    
    # Show genre info
    if args.info:
        try:
            info = generator.get_pattern_info(args.info)
            print(f"Genre: {info['name']}")
            print(f"Key: {info['genre']}")
            print(f"Description: {info['description']}")
            print(f"Available variations: {info['variations']}")
        except ValueError as e:
            print(f"Error: {e}")
            return 1
        return 0
    
    # Generate pattern
    if not args.genre:
        available = generator.get_available_genres()
        if available:
            print("Please specify a genre with --genre. Available genres:")
            for key, name in available.items():
                print(f"  {key}: {name}")
        else:
            print("No genres available. Use --list to see available options.")
        return 1
    
    try:
        output_path = generator.generate_and_save(
            genre=args.genre,
            tempo=args.tempo,
            seed=args.seed,
            output_dir=args.output,
            bars=args.bars
        )
        
        # Get pattern info for display
        info = generator.get_pattern_info(args.genre)
        
        print(f"✅ Generated {output_path}")
        print(f"🎵 Genre: {info['name']}")
        print(f"🥁 Description: {info['description']}")
        print(f"⏱️  Tempo: {args.tempo} BPM")
        print(f"📊 Bars: {args.bars}")
        if args.seed:
            print(f"🎲 Seed: {args.seed}")
        print(f"🔄 Variations: {info['variations']}")
        
    except Exception as e:
        print(f"Error generating pattern: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
