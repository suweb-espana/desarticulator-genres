from midiutil import MIDIFile
import random
import os

random.seed(42)

def create_punk_rock_groove():
    midi = MIDIFile(1)
    track = 0
    channel = 9
    tempo = 150
    ppq = 480
    
    midi.addTempo(track, 0, tempo)
    
    kick = 36
    snare = 38
    closed_hh = 42
    open_hh = 46
    ride = 51
    crash = 49
    tom_high = 43
    tom_mid = 45
    tom_low = 48
    
    ticks_per_bar = 1920
    ticks_per_beat = 480
    ticks_per_eighth = 240
    ticks_per_sixteenth = 120
    
    def add_note(drum, bar, beat_pos, velocity=85, duration=0.1):
        time_ticks = (bar * ticks_per_bar) + beat_pos
        midi.addNote(track, channel, drum, time_ticks / ppq, duration, velocity)
    
    def add_basic_pattern(start_bar):
        for bar in range(start_bar, start_bar + 8):
            add_note(kick, bar, 0, 95)
            add_note(kick, bar, ticks_per_beat * 2 + ticks_per_eighth, 90)
            
            add_note(snare, bar, ticks_per_beat, 100)
            add_note(snare, bar, ticks_per_beat * 3, 98)
            
            for sixteenth in range(16):
                if sixteenth % 2 == 0:
                    vel = random.randint(75, 85) if sixteenth % 4 == 0 else random.randint(65, 75)
                    add_note(closed_hh, bar, sixteenth * ticks_per_sixteenth, vel)
                else:
                    if random.random() < 0.3:
                        add_note(closed_hh, bar, sixteenth * ticks_per_sixteenth, random.randint(40, 55))
    
    def add_variation_1(start_bar):
        for bar in range(start_bar, start_bar + 8):
            add_note(kick, bar, 0, 95)
            add_note(kick, bar, ticks_per_beat + ticks_per_eighth, 85)
            add_note(kick, bar, ticks_per_beat * 2 + ticks_per_eighth, 90)
            add_note(kick, bar, ticks_per_beat * 3 + ticks_per_sixteenth * 3, 88)
            
            add_note(snare, bar, ticks_per_beat, 100)
            add_note(snare, bar, ticks_per_beat * 3, 98)
            if random.random() < 0.4:
                add_note(snare, bar, ticks_per_beat * 2 - ticks_per_sixteenth, 45)
            
            for eighth in range(8):
                if eighth % 2 == 1 and random.random() < 0.6:
                    add_note(open_hh, bar, eighth * ticks_per_eighth, random.randint(70, 80))
                elif eighth % 2 == 0:
                    add_note(closed_hh, bar, eighth * ticks_per_eighth, random.randint(75, 85))
    
    def add_fill_simple(bar):
        add_note(kick, bar, 0, 95)
        add_note(snare, bar, ticks_per_beat, 100)
        
        fill_pattern = [
            (ticks_per_beat * 2, tom_high, 90),
            (ticks_per_beat * 2 + ticks_per_eighth, tom_high, 85),
            (ticks_per_beat * 2 + ticks_per_eighth + ticks_per_sixteenth, tom_mid, 88),
            (ticks_per_beat * 3, tom_mid, 92),
            (ticks_per_beat * 3 + ticks_per_sixteenth, tom_low, 90),
            (ticks_per_beat * 3 + ticks_per_eighth, tom_low, 95),
            (ticks_per_beat * 3 + ticks_per_eighth + ticks_per_sixteenth, snare, 85)
        ]
        
        for pos, drum, vel in fill_pattern:
            add_note(drum, bar, pos, vel)
    
    def add_fill_complex(bar):
        add_note(kick, bar, 0, 95)
        
        tom_sequence = [
            (ticks_per_sixteenth, tom_high, 80),
            (ticks_per_sixteenth * 2, tom_high, 85),
            (ticks_per_sixteenth * 3, tom_mid, 82),
            (ticks_per_eighth, tom_mid, 88),
            (ticks_per_eighth + ticks_per_sixteenth, tom_low, 90),
            (ticks_per_beat, snare, 95),
            (ticks_per_beat + ticks_per_sixteenth, tom_high, 78),
            (ticks_per_beat + ticks_per_eighth, tom_mid, 85),
            (ticks_per_beat + ticks_per_eighth + ticks_per_sixteenth, tom_low, 90),
            (ticks_per_beat * 2, kick, 90),
            (ticks_per_beat * 2 + ticks_per_sixteenth, tom_high, 82),
            (ticks_per_beat * 2 + ticks_per_sixteenth * 2, tom_high, 85),
            (ticks_per_beat * 2 + ticks_per_eighth, tom_mid, 88),
            (ticks_per_beat * 2 + ticks_per_eighth + ticks_per_sixteenth, tom_low, 92),
            (ticks_per_beat * 3, snare, 100),
            (ticks_per_beat * 3 + ticks_per_sixteenth, tom_low, 88),
            (ticks_per_beat * 3 + ticks_per_sixteenth * 2, tom_low, 90),
            (ticks_per_beat * 3 + ticks_per_eighth, snare, 95),
            (ticks_per_beat * 3 + ticks_per_eighth + ticks_per_sixteenth, snare, 85)
        ]
        
        for pos, drum, vel in tom_sequence:
            add_note(drum, bar, pos, vel)
    
    def add_final_fill(bar):
        fill_sequence = [
            (0, kick, 95),
            (ticks_per_sixteenth, tom_high, 85),
            (ticks_per_sixteenth * 2, tom_high, 88),
            (ticks_per_sixteenth * 3, tom_mid, 85),
            (ticks_per_eighth, tom_mid, 90),
            (ticks_per_eighth + ticks_per_sixteenth, tom_low, 92),
            (ticks_per_eighth + ticks_per_sixteenth * 2, tom_low, 88),
            (ticks_per_beat, snare, 100),
            (ticks_per_beat + ticks_per_sixteenth, tom_high, 80),
            (ticks_per_beat + ticks_per_sixteenth * 2, tom_high, 85),
            (ticks_per_beat + ticks_per_eighth, tom_mid, 88),
            (ticks_per_beat + ticks_per_eighth + ticks_per_sixteenth, tom_low, 90),
            (ticks_per_beat * 2, kick, 92),
            (ticks_per_beat * 2 + ticks_per_sixteenth, tom_high, 82),
            (ticks_per_beat * 2 + ticks_per_sixteenth * 2, tom_mid, 85),
            (ticks_per_beat * 2 + ticks_per_eighth, tom_low, 88),
            (ticks_per_beat * 2 + ticks_per_eighth + ticks_per_sixteenth, snare, 90),
            (ticks_per_beat * 3, snare, 100),
            (ticks_per_beat * 3 + ticks_per_sixteenth, tom_low, 85),
            (ticks_per_beat * 3 + ticks_per_sixteenth * 2, tom_low, 88),
            (ticks_per_beat * 3 + ticks_per_sixteenth * 3, snare, 92),
            (ticks_per_beat * 3 + ticks_per_eighth, snare, 95),
            (ticks_per_beat * 3 + ticks_per_eighth + ticks_per_sixteenth, snare, 88),
            (ticks_per_beat * 3 + ticks_per_eighth + ticks_per_sixteenth * 2, snare, 90),
            (ticks_per_beat * 3 + ticks_per_eighth + ticks_per_sixteenth * 3, snare, 85)
        ]
        
        for pos, drum, vel in fill_sequence:
            add_note(drum, bar, pos, vel)
    
    current_bar = 0
    pattern_type = 0
    
    while current_bar < 149:
        if current_bar == 148:
            add_final_fill(current_bar)
            current_bar += 1
        elif (current_bar + 1) % 8 == 0:
            if random.random() < 0.7:
                add_fill_simple(current_bar)
            else:
                add_fill_complex(current_bar)
            current_bar += 1
        else:
            if pattern_type == 0:
                add_basic_pattern(current_bar)
                pattern_type = 1
            else:
                add_variation_1(current_bar)
                pattern_type = 0
            current_bar += 7
    
    add_note(crash, 149, 0, 100, 2.0)
    add_note(kick, 149, 0, 100)
    
    return midi

def main():
    midi_file = create_punk_rock_groove()
    
    os.makedirs("output", exist_ok=True)
    output_path = "output/PunkRock150bars.mid"
    
    with open(output_path, "wb") as output_file:
        midi_file.writeFile(output_file)
    
    print(f"Generated {output_path} with 150 bars")

if __name__ == "__main__":
    main()
