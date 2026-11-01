"""Psychedelic rock drum performance for Superior Drummer 3."""

from typing import Optional

from midiutil import MIDIFile

from core.base_pattern import BasePattern


class PsychedelicRockPattern(BasePattern):
    """Hypnotic psychedelic rock groove with shifting accents and tom motifs."""

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
        return "Psychedelic Rock"

    @property
    def description(self) -> str:
        return (
            f"{self.tempo} BPM psychedelic rock performance for Rock Foundry: "
            "hypnotic ostinatos, spacious backbeats, displaced accents, "
            "tom motifs, and expanding crash phrases."
        )

    def _sixteenth(self, position: int) -> int:
        return position * self.midi_config['ticks_per_sixteenth']

    def _eighth(self, position: int) -> int:
        return position * self.midi_config['ticks_per_eighth']

    def _velocity(self, base: int, spread: int = 4) -> int:
        return self.get_random_velocity(base, spread)

    def _hypnotic_hat(self, midi: MIDIFile, bar: int, energy: int = 0) -> None:
        accents = (62, 48, 55, 46, 66, 50, 57, 45)
        for eighth, base in enumerate(accents):
            note = self.drum_mapping['closed_hh']
            if eighth == 7 and bar % 4 == 3:
                note = self.drum_mapping['open_hh']
            self.add_note(
                midi, note, bar, self._eighth(eighth),
                self._velocity(base + energy, 4)
            )

    def _ride_pulse(self, midi: MIDIFile, bar: int, energy: int = 0,
                    bell: bool = False) -> None:
        for eighth in range(8):
            note = self.drum_mapping['ride']
            if bell and eighth in (2, 6):
                note = self.drum_mapping['ride_bell']
            base = 74 if eighth % 2 == 0 else 58
            self.add_note(
                midi, note, bar, self._eighth(eighth),
                self._velocity(base + energy, 5)
            )

    def _backbeat(self, midi: MIDIFile, bar: int, energy: int = 0,
                  half_time: bool = False, rimshot: bool = False) -> None:
        snare = self.drum_mapping['rimshot'] if rimshot else self.drum_mapping['snare']
        positions = (12,) if half_time else (4, 12)
        for position in positions:
            self.add_note(
                midi, snare, bar, self._sixteenth(position),
                self._velocity(96 + energy, 3)
            )
        if self.should_add_variation(bar, 0.7):
            ghost_position = 3 if bar % 2 == 0 else 11
            self.add_note(
                midi, self.drum_mapping['snare'], bar,
                self._sixteenth(ghost_position), self._velocity(26, 5)
            )

    def _kick(self, midi: MIDIFile, bar: int, dense: bool = False,
              energy: int = 0) -> None:
        patterns = (
            (0, 6, 8, 14),
            (0, 3, 6, 10, 14),
            (0, 6, 10, 13, 14),
            (0, 2, 6, 8, 11, 14),
        )
        positions = list(patterns[bar % len(patterns)])
        if dense:
            positions.extend((7, 15) if bar % 2 else (8,))
        for position in positions:
            base = 94 if position == 0 else 72
            self.add_note(
                midi, self.drum_mapping['kick'], bar,
                self._sixteenth(position), self._velocity(base + energy, 5)
            )

    def _tom_motif(self, midi: MIDIFile, bar: int, energy: int = 0) -> None:
        motif = (
            (2, 'tom_high', 68),
            (5, 'tom_mid', 72),
            (8, 'tom_low', 76),
            (11, 'tom_floor', 80),
        )
        for position, drum, base in motif:
            self.add_note(
                midi, self.drum_mapping[drum], bar,
                self._sixteenth(position), self._velocity(base + energy, 4)
            )

    def _groove(self, midi: MIDIFile, bar: int, energy: int = 0,
                ride: bool = False, dense: bool = False,
                half_time: bool = False, rimshot: bool = False) -> None:
        if ride:
            self._ride_pulse(midi, bar, energy, bell=bar % 8 == 7)
        else:
            self._hypnotic_hat(midi, bar, energy)
        self._kick(midi, bar, dense=dense, energy=energy)
        self._backbeat(midi, bar, energy, half_time=half_time, rimshot=rimshot)

    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            self._groove(midi, bar, ride=False, dense=bar % 4 == 3)
            if bar % 4 == 3:
                self._tom_motif(midi, bar, energy=-4)

    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            self._groove(midi, bar, energy=4, ride=True,
                         dense=bar % 4 == 1, rimshot=bar % 4 == 3)
            if bar % 4 == 3:
                self._tom_motif(midi, bar, energy=4)

    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            self._groove(midi, bar, energy=6, ride=True, dense=True,
                         half_time=bar % 2 == 0, rimshot=True)
            if bar % 4 == 0:
                self.add_note(
                    midi, self.drum_mapping['crash_2'], bar, 0,
                    self._velocity(88, 4)
                )
            if bar % 2 == 1:
                self._tom_motif(midi, bar, energy=5)

    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        self._groove(midi, bar, energy=2, ride=False, dense=False)
        for position, drum, base in (
            (8, 'tom_high', 70),
            (10, 'tom_mid', 74),
            (12, 'tom_low', 80),
            (14, 'snare', 88),
        ):
            self.add_note(
                midi, self.drum_mapping[drum], bar,
                self._sixteenth(position), self._velocity(base, 4)
            )

    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        self._groove(midi, bar, energy=5, ride=False, dense=True, rimshot=True)
        cascade = (
            ('snare', 8, 72),
            ('tom_high', 9, 76),
            ('tom_mid', 10, 80),
            ('tom_low', 11, 84),
            ('tom_floor', 13, 90),
            ('crash', 15, 94),
        )
        for drum, position, base in cascade:
            self.add_note(
                midi, self.drum_mapping[drum], bar,
                self._sixteenth(position), self._velocity(base, 4)
            )

    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 3:
                self.add_note(
                    midi, self.drum_mapping['kick'], bar, 0,
                    self._velocity(72, 5)
                )
                self.add_note(
                    midi, self.drum_mapping['tom_floor'], bar,
                    self._eighth(4), self._velocity(58, 5)
                )
            elif bar == start_bar + bars - 1:
                self.create_fill_simple(midi, bar)
            else:
                self._groove(midi, bar, energy=-8, ride=False)

    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        for bar in range(start_bar, start_bar + bars):
            if bar == start_bar + bars - 1:
                self.create_fill_simple(midi, bar)
            else:
                self._groove(midi, bar, ride=bar % 8 >= 4,
                             dense=bar % 8 == 7)
                if bar % 8 == 3:
                    self._tom_motif(midi, bar, energy=-6)

    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        for bar in range(start_bar, start_bar + bars):
            if bar == start_bar + bars - 1:
                self.create_fill_complex(midi, bar)
            else:
                self._groove(midi, bar, energy=7, ride=True,
                             dense=bar % 4 == 1, rimshot=True)
                if (bar - start_bar) % 4 == 0:
                    self.add_note(
                        midi, self.drum_mapping['crash'], bar, 0,
                        self._velocity(92, 4)
                    )

    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            if bar == start_bar + bars - 1:
                self.create_fill_complex(midi, bar)
            else:
                self._groove(midi, bar, energy=-2, ride=False,
                             dense=bar % 3 == 0, half_time=True)
                if bar % 2 == 0:
                    self._tom_motif(midi, bar, energy=-2)

    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        for bar in range(start_bar, start_bar + bars):
            remaining = start_bar + bars - bar
            if remaining == 1:
                self.create_fill_complex(midi, bar)
            elif remaining == 2:
                self.create_fill_simple(midi, bar)
            else:
                self._groove(
                    midi, bar, energy=2, ride=remaining % 2 == 0,
                    dense=remaining <= 4, rimshot=True
                )
