"""
Jazz Fusion - Vinnie Colaiuta on Joe's Garage (1979).

Central Scrutinizer is the default vamp. Catholic Girls is the other 4/4
groove and the chorus of a complete song. Written for Le Cars: 18" crash
hats, 24" bash ride, Ayotte toms mapped high-to-floor as 48, 47, 43, 41.
"""

from typing import List, Optional

from midiutil import MIDIFile

from core.base_pattern import BasePattern


class JazzFusionPattern(BasePattern):
    """Joe's Garage grooves adapted to the Le Cars kit."""

    def __init__(self, tempo: int = 112, seed: Optional[int] = None):
        super().__init__(tempo=tempo, seed=seed)
        self.drum_mapping.update({
            'tom_high': 48,
            'tom_mid': 47,
            'tom_low': 43,
            'tom_floor': 41,
            'sidestick': 37,
            'rimshot': 40,
            'ride_bell': 53,
            'crash_2': 57,
        })

    @property
    def genre_name(self) -> str:
        return "Jazz Fusion"

    @property
    def description(self) -> str:
        return (
            "Vinnie Colaiuta on Joe's Garage: Central Scrutinizer vamp plus "
            "Catholic Girls 4/4 groove. Mapped for Le Cars."
        )

    def _sixteenth(self, index: int) -> int:
        return index * self.midi_config['ticks_per_sixteenth']

    def _add_hats(self, midi: MIDIFile, bar: int, energy: int = 0) -> None:
        for eighth in range(8):
            pos = eighth * self.midi_config['ticks_per_eighth']
            if eighth == 0 or eighth == 6:
                velocity = 82 + energy
            elif eighth == 4:
                velocity = 94 + energy
            else:
                velocity = 68 + energy
            self.add_note(
                midi, self.drum_mapping['closed_hh'], bar, pos,
                self.get_random_velocity(velocity, 4)
            )

    def _add_catholic_hats(self, midi: MIDIFile, bar: int, energy: int = 0) -> None:
        for eighth in range(8):
            pos = eighth * self.midi_config['ticks_per_eighth']
            if eighth % 2 == 0:
                velocity = 80 + energy
            else:
                velocity = 70 + energy
            self.add_note(
                midi, self.drum_mapping['closed_hh'], bar, pos,
                self.get_random_velocity(velocity, 4)
            )

    def _add_backbeat(
        self,
        midi: MIDIFile,
        bar: int,
        snare_note: Optional[int] = None,
        energy: int = 0,
        ghost_chance: float = 0.35,
    ) -> None:
        snare = snare_note or self.drum_mapping['snare']
        self.add_note(
            midi, snare, bar, self._sixteenth(4),
            self.get_random_velocity(98 + energy, 3)
        )
        self.add_note(
            midi, snare, bar, self._sixteenth(12),
            self.get_random_velocity(100 + energy, 3)
        )
        if self.should_add_variation(bar, ghost_chance):
            self.add_note(
                midi, self.drum_mapping['snare'], bar, self._sixteenth(7),
                self.get_random_velocity(26, 6)
            )
        if self.should_add_variation(bar, ghost_chance - 0.1):
            self.add_note(
                midi, self.drum_mapping['snare'], bar, self._sixteenth(13),
                self.get_random_velocity(24, 6)
            )
        if ghost_chance >= 0.5 and self.should_add_variation(bar, 0.4):
            self.add_note(
                midi, self.drum_mapping['snare'], bar, self._sixteenth(3),
                self.get_random_velocity(22, 5)
            )
        if ghost_chance >= 0.5 and self.should_add_variation(bar, 0.3):
            self.add_note(
                midi, self.drum_mapping['snare'], bar, self._sixteenth(11),
                self.get_random_velocity(22, 5)
            )

    def _add_tom_melody(self, midi: MIDIFile, bar: int, dense: bool = False) -> None:
        self.add_note(
            midi, self.drum_mapping['tom_mid'], bar, self._sixteenth(2),
            self.get_random_velocity(78, 5)
        )
        self.add_note(
            midi, self.drum_mapping['tom_mid'], bar, self._sixteenth(3),
            self.get_random_velocity(74, 5)
        )
        self.add_note(
            midi, self.drum_mapping['tom_high'], bar, self._sixteenth(8),
            self.get_random_velocity(80, 5)
        )
        if dense:
            self.add_note(
                midi, self.drum_mapping['tom_high'], bar, self._sixteenth(6),
                self.get_random_velocity(72, 5)
            )
            self.add_note(
                midi, self.drum_mapping['tom_low'], bar, self._sixteenth(11),
                self.get_random_velocity(76, 5)
            )

    def _catholic_kick_positions(self, bar: int) -> List[int]:
        patterns = [
            [0, 6, 8, 14],
            [0, 6, 8, 10, 14],
            [0, 3, 6, 8, 14],
            [0, 6, 8, 14, 15],
        ]
        return patterns[bar % len(patterns)]

    def _kick_positions(self, bar: int, mutated: bool) -> List[int]:
        patterns = [
            [0, 6, 7, 10, 14, 15],
            [0, 1, 6, 7, 8, 10, 14, 15],
            [0, 2, 6, 7, 9, 10, 14],
            [0, 6, 7, 8, 10, 11, 14, 15],
        ]
        if mutated:
            extra = [
                [0, 1, 2, 6, 7, 10, 12, 14, 15],
                [0, 6, 7, 9, 10, 11, 13, 14],
            ]
            patterns.extend(extra)
        return patterns[bar % len(patterns)]

    def _add_kick(self, midi: MIDIFile, bar: int, mutated: bool = False) -> None:
        for pos in self._kick_positions(bar, mutated):
            velocity = 96 if pos == 0 else 86
            self.add_note(
                midi, self.drum_mapping['kick'], bar, self._sixteenth(pos),
                self.get_random_velocity(velocity, 5)
            )

    def _vamp(
        self,
        midi: MIDIFile,
        bar: int,
        with_toms: bool = True,
        mutated: bool = False,
        dense_toms: bool = False,
        energy: int = 0,
        snare_note: Optional[int] = None,
        crash: bool = False,
    ) -> None:
        self._add_hats(midi, bar, energy)
        self._add_backbeat(midi, bar, snare_note=snare_note, energy=energy)
        self._add_kick(midi, bar, mutated=mutated)
        if with_toms:
            self._add_tom_melody(midi, bar, dense=dense_toms)
        if crash:
            self.add_note(
                midi, self.drum_mapping['crash'], bar, 0,
                self.get_random_velocity(96, 4)
            )

    def _catholic_groove(
        self,
        midi: MIDIFile,
        bar: int,
        energy: int = 0,
        snare_note: Optional[int] = None,
        crash: bool = False,
    ) -> None:
        self._add_catholic_hats(midi, bar, energy)
        self._add_backbeat(
            midi, bar, snare_note=snare_note, energy=energy, ghost_chance=0.55
        )
        for pos in self._catholic_kick_positions(bar):
            velocity = 98 if pos == 0 else 88
            self.add_note(
                midi, self.drum_mapping['kick'], bar, self._sixteenth(pos),
                self.get_random_velocity(velocity + energy, 4)
            )
        if crash:
            self.add_note(
                midi, self.drum_mapping['crash'], bar, 0,
                self.get_random_velocity(98, 4)
            )

    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Central Scrutinizer vamp with Closed Accent and tom melody."""
        for bar in range(start_bar, start_bar + bars):
            self._vamp(midi, bar, with_toms=True, mutated=False)

    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Catholic Girls 4/4 groove: driving hats, rock kick, ghosts, no tom ostinato."""
        for bar in range(start_bar, start_bar + bars):
            self._catholic_groove(midi, bar)

    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Denser toms, louder hats, crash 2 on phrase starts."""
        for bar in range(start_bar, start_bar + bars):
            crash = bar % 8 == 0
            self._vamp(
                midi, bar, with_toms=True, mutated=True, dense_toms=True, energy=6
            )
            if crash:
                self.add_note(
                    midi, self.drum_mapping['crash_2'], bar, 0,
                    self.get_random_velocity(90, 4)
                )
            if bar % 8 == 7:
                self.add_note(
                    midi, self.drum_mapping['ride_bell'], bar, self._sixteenth(12),
                    self.get_random_velocity(84, 4)
                )

    def create_fill_simple(
        self, midi: MIDIFile, bar: int, closed_accent: bool = True
    ) -> None:
        """Short snare and tom setup into the next groove."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 95)
        if closed_accent:
            self._add_hats(midi, bar)
        else:
            self._add_catholic_hats(midi, bar)
        self.add_note(
            midi, self.drum_mapping['snare'], bar, self._sixteenth(4),
            self.get_random_velocity(96, 3)
        )
        hits = [
            (8, self.drum_mapping['tom_high'], 84),
            (10, self.drum_mapping['tom_mid'], 86),
            (12, self.drum_mapping['tom_low'], 88),
            (14, self.drum_mapping['snare'], 100),
        ]
        for pos, drum, velocity in hits:
            self.add_note(midi, drum, bar, self._sixteenth(pos),
                          self.get_random_velocity(velocity, 4))

    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Linear sixteenth fill across Le Cars toms into crash."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 100)
        toms = [
            self.drum_mapping['tom_high'],
            self.drum_mapping['tom_mid'],
            self.drum_mapping['tom_low'],
            self.drum_mapping['tom_floor'],
        ]
        for i in range(12):
            drum = toms[i % 4] if i % 5 != 0 else self.drum_mapping['snare']
            velocity = 78 + (i % 4) * 5
            self.add_note(
                midi, drum, bar, self._sixteenth(i + 2),
                self.get_random_velocity(velocity, 5)
            )
            if i in (3, 7, 11):
                self.add_note(
                    midi, self.drum_mapping['kick'], bar, self._sixteenth(i + 2),
                    self.get_random_velocity(88, 4)
                )
        self.add_note(
            midi, self.drum_mapping['snare'], bar, self._sixteenth(14), 104
        )
        self.add_note(
            midi, self.drum_mapping['crash'], bar, self._sixteenth(14), 98
        )

    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Spoken-word intro: vamp without toms, sidestick then snare."""
        for bar in range(start_bar, start_bar + bars):
            if bar == start_bar + bars - 1:
                self.create_fill_simple(midi, bar)
                continue
            use_stick = bar < start_bar + max(2, bars // 2)
            snare = self.drum_mapping['sidestick'] if use_stick else None
            self._vamp(midi, bar, with_toms=False, snare_note=snare, energy=-8)

    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Central Scrutinizer vamp; fill into the Catholic Girls chorus."""
        for bar in range(start_bar, start_bar + bars):
            if bar == start_bar + bars - 1:
                self.create_fill_simple(midi, bar)
                continue
            mutated = ((bar - start_bar) // 2) % 2 == 1
            self._vamp(midi, bar, with_toms=True, mutated=mutated)

    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Catholic Girls chorus: driving groove, rimshot, crash every 8 bars."""
        for bar in range(start_bar, start_bar + bars):
            if bar == start_bar + bars - 1:
                self.create_fill_simple(midi, bar, closed_accent=False)
                continue
            crash = (bar - start_bar) % 8 == 0
            self._catholic_groove(
                midi, bar,
                energy=8,
                snare_note=self.drum_mapping['rimshot'],
                crash=crash,
            )

    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """B-section: kick mutations, no tom ostinato."""
        for bar in range(start_bar, start_bar + bars):
            if bar == start_bar + bars - 1:
                self.create_fill_simple(midi, bar)
            else:
                self._vamp(midi, bar, with_toms=False, mutated=True, energy=-4)

    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Mutated vamp into Vinnie-style fills."""
        for bar in range(start_bar, start_bar + bars):
            remaining = start_bar + bars - bar
            if remaining <= 2:
                self.create_fill_complex(midi, bar)
            elif remaining == 3:
                self.create_fill_simple(midi, bar)
            else:
                self._vamp(midi, bar, with_toms=True, mutated=True, energy=4)
