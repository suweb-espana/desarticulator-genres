"""Jazz/blues/rock drum performance for Superior Drummer 3."""

from typing import Optional

from midiutil import MIDIFile

from core.base_pattern import BasePattern


class JazzBluesRockPattern(BasePattern):
    """Breathing fusion groove for fast-moving harmony at a relaxed tempo."""

    def __init__(self, tempo: int = 97, seed: Optional[int] = None):
        super().__init__(tempo=tempo, seed=seed)
        self.drum_mapping.update({
            'tom_floor': 41,
            'ride_bell': 53,
            'sidestick': 37,
            'rimshot': 40,
            'crash_2': 57,
        })

    @property
    def genre_name(self) -> str:
        return "Jazz Blues Rock Fusion"

    @property
    def description(self) -> str:
        return (
            "97 BPM Rock Foundry Default fusion performance for Am6 -> "
            "B diminished -> E7: swung jazz ride, blues drag, restrained rock "
            "weight, and phrase fills."
        )

    def _sixteenth(self, position: int) -> int:
        return position * self.midi_config['ticks_per_sixteenth']

    def _triplet_eighth(self, beat: int, slot: int) -> int:
        """Return the start or swung second half of an eighth-note beat."""
        return (
            beat * self.midi_config['ticks_per_beat']
            + slot * (self.midi_config['ticks_per_beat'] * 2 // 3)
        )

    def _velocity(self, base: int, spread: int = 3) -> int:
        return self.get_random_velocity(base, spread)

    def _ride(self, midi: MIDIFile, bar: int, energy: int = 0, bell: bool = False) -> None:
        """Swinging ride triplets leave space around the harmony."""
        accents = ((78, 62), (72, 64), (76, 60), (70, 58))
        for beat, (downbeat, offbeat) in enumerate(accents):
            for slot, base in enumerate((downbeat, offbeat)):
                note = (
                    self.drum_mapping['ride_bell']
                    if bell and beat == 2 and slot == 0
                    else self.drum_mapping['ride']
                )
                self.add_note(
                    midi, note, bar, self._triplet_eighth(beat, slot),
                    self._velocity(base + energy, 4)
                )

    def _hat_breath(self, midi: MIDIFile, bar: int, energy: int = 0) -> None:
        """Straight closed hats provide a restrained rock contrast."""
        for position, base in ((0, 58), (2, 47), (4, 55), (6, 44),
                               (8, 57), (10, 46), (12, 53)):
            self.add_note(midi, self.drum_mapping['closed_hh'], bar, self._sixteenth(position),
                          self._velocity(base + energy, 4))
        self.add_note(midi, self.drum_mapping['open_hh'], bar, self._sixteenth(14),
                      self._velocity(48 + energy, 4))

    def _snare_pocket(self, midi: MIDIFile, bar: int, energy: int = 0,
                      rimshot: bool = False, ghosts: bool = True) -> None:
        snare = self.drum_mapping['rimshot'] if rimshot else self.drum_mapping['snare']
        for position, base in ((4, 94), (12, 100)):
            self.add_note(midi, snare, bar, self._sixteenth(position),
                          self._velocity(base + energy, 3))
        if ghosts and self.should_add_variation(bar, 0.8):
            self.add_note(midi, self.drum_mapping['snare'], bar, self._sixteenth(3),
                          self._velocity(25, 5))
        if ghosts and bar % 2 == 1:
            self.add_note(midi, self.drum_mapping['snare'], bar, self._sixteenth(11),
                          self._velocity(29, 5))

    def _kick(self, midi: MIDIFile, bar: int, dense: bool = False, energy: int = 0) -> None:
        patterns = ([0, 6, 10, 14], [0, 3, 6, 10, 14], [0, 6, 8, 11, 14], [0, 2, 6, 10, 13, 14])
        positions = patterns[bar % len(patterns)]
        if dense:
            positions = positions + ([7, 15] if bar % 2 else [8])
        for position in positions:
            base = 92 if position == 0 else 75
            self.add_note(midi, self.drum_mapping['kick'], bar, self._sixteenth(position),
                          self._velocity(base + energy, 4))

    def _groove(self, midi: MIDIFile, bar: int, energy: int = 0, ride: bool = True,
                dense: bool = False, rimshot: bool = False) -> None:
        if ride:
            self._ride(midi, bar, energy, bell=bar % 8 == 7)
        else:
            self._hat_breath(midi, bar, energy)
        self._kick(midi, bar, dense=dense, energy=energy)
        self._snare_pocket(midi, bar, energy, rimshot=rimshot)

    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            self._groove(midi, bar, ride=True, dense=False)

    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            self._groove(midi, bar, energy=3, ride=bar % 4 != 3, dense=bar % 4 == 1)

    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            self._groove(midi, bar, energy=6, ride=False, dense=True, rimshot=True)
            if bar % 4 == 0:
                self.add_note(midi, self.drum_mapping['crash_2'], bar, 0,
                              self._velocity(88, 4))

    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        self._groove(midi, bar, energy=2, ride=False, dense=False)
        for position, drum, base in ((8, 'tom_high', 68), (10, 'snare', 72),
                                     (12, 'tom_mid', 76), (14, 'snare', 86)):
            self.add_note(midi, self.drum_mapping[drum], bar, self._sixteenth(position),
                          self._velocity(base, 4))

    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        self._groove(midi, bar, energy=4, ride=False, dense=False)
        for index, drum in enumerate(('snare', 'tom_high', 'tom_mid', 'tom_low',
                                      'snare', 'tom_floor')):
            position = 8 + index
            self.add_note(midi, self.drum_mapping[drum], bar, self._sixteenth(position),
                          self._velocity(68 + index * 5, 4))
        self.add_note(midi, self.drum_mapping['crash'], bar, self._sixteenth(14),
                      self._velocity(92, 3))

    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            if bar == start_bar + bars - 1:
                self.create_fill_simple(midi, bar)
            else:
                self._groove(midi, bar, energy=-10, ride=False, dense=False, rimshot=True)

    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        for bar in range(start_bar, start_bar + bars):
            if bar == start_bar + bars - 1:
                self.create_fill_simple(midi, bar)
            else:
                self._groove(midi, bar, ride=True, dense=bar % 8 == 5)

    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        for bar in range(start_bar, start_bar + bars):
            if bar == start_bar + bars - 1:
                self.create_fill_complex(midi, bar)
            else:
                self._groove(midi, bar, energy=7, ride=True, dense=bar % 4 == 1, rimshot=True)
                if (bar - start_bar) % 8 == 0:
                    self.add_note(midi, self.drum_mapping['crash'], bar, 0,
                                  self._velocity(90, 4))

    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            if bar == start_bar + bars - 1:
                self.create_fill_simple(midi, bar)
            else:
                self._groove(midi, bar, energy=-3, ride=False, dense=bar % 3 == 0)

    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            remaining = start_bar + bars - bar
            if remaining == 1:
                self.create_fill_complex(midi, bar)
            elif remaining == 2:
                self.create_fill_simple(midi, bar)
            else:
                self._groove(midi, bar, energy=4, ride=True, dense=remaining < 5, rimshot=True)
