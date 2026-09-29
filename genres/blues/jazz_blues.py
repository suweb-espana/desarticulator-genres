"""
Jazz Blues - Classic jazz club blues drum patterns.
Swing ride, feathered kick, ghost notes, and brushed dynamics.
"""

from typing import Optional

from midiutil import MIDIFile

from core.base_pattern import BasePattern


class JazzBluesPattern(BasePattern):
    """Jazz blues with swing ride and soft club dynamics."""

    def __init__(self, tempo: int = 92, seed: Optional[int] = None):
        super().__init__(tempo=tempo, seed=seed)
        self.drum_mapping.update({
            'sidestick': 37,
            'ride_bell': 53,
        })

    @property
    def genre_name(self) -> str:
        return "Jazz Blues"

    @property
    def description(self) -> str:
        return (
            "Classic jazz blues - Art Blakey, jazz club shuffle: swing ride, "
            "feathered kick, ghost notes, and soft brushed dynamics"
        )

    def _beat(self, beat: int) -> int:
        return beat * self.midi_config['ticks_per_beat']

    def _shuffle_off(self, beat: int) -> int:
        return (
            self._beat(beat)
            + self.midi_config['ticks_per_eighth']
            + self.midi_config['ticks_per_sixteenth']
        )

    def _add_swing_ride(self, midi: MIDIFile, bar: int, energy: int = 0) -> None:
        accents = [0, 2]
        for beat in range(4):
            vel = 78 + energy if beat in accents else 70 + energy
            self.add_note(
                midi, self.drum_mapping['ride'], bar, self._beat(beat),
                self.get_random_velocity(vel, 6)
            )
            if beat in (1, 3):
                self.add_note(
                    midi, self.drum_mapping['ride'], bar, self._shuffle_off(beat),
                    self.get_random_velocity(62 + energy, 8)
                )

    def _add_feathered_kick(self, midi: MIDIFile, bar: int, syncopated: bool = False) -> None:
        self.add_note(
            midi, self.drum_mapping['kick'], bar, 0,
            self.get_random_velocity(58, 6)
        )
        self.add_note(
            midi, self.drum_mapping['kick'], bar, self._beat(2),
            self.get_random_velocity(52, 6)
        )
        if syncopated and self.should_add_variation(bar, 0.4):
            self.add_note(
                midi, self.drum_mapping['kick'], bar, self._shuffle_off(2),
                self.get_random_velocity(48, 6)
            )

    def _add_jazz_snare(
        self,
        midi: MIDIFile,
        bar: int,
        energy: int = 0,
        use_sidestick: bool = False,
        ghost_dense: bool = False,
    ) -> None:
        snare = self.drum_mapping['sidestick'] if use_sidestick else self.drum_mapping['snare']
        self.add_note(
            midi, snare, bar, self._beat(1),
            self.get_random_velocity(82 + energy, 5)
        )
        self.add_note(
            midi, snare, bar, self._beat(3),
            self.get_random_velocity(80 + energy, 5)
        )

        ghosts = [
            self.midi_config['ticks_per_eighth'],
            self._beat(1) + self.midi_config['ticks_per_eighth'],
            self._beat(2) + self.midi_config['ticks_per_sixteenth'],
            self._shuffle_off(3),
        ]
        if ghost_dense:
            ghosts.extend([
                self._beat(2) + self.midi_config['ticks_per_eighth'],
                self._beat(3) + self.midi_config['ticks_per_sixteenth'],
            ])

        for pos in ghosts:
            if self.should_add_variation(bar, 0.55 if ghost_dense else 0.35):
                self.add_note(
                    midi, self.drum_mapping['snare'], bar, pos,
                    self.get_random_velocity(28, 8)
                )

    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Basic jazz blues - feathered kick with swing ride."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            self._add_feathered_kick(midi, bar, syncopated=False)
            self._add_jazz_snare(midi, bar, energy=0, use_sidestick=False)
            self._add_swing_ride(midi, bar, energy=0)

    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 1 - ride bell accents and denser ghosts."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            self._add_feathered_kick(midi, bar, syncopated=True)
            self._add_jazz_snare(midi, bar, energy=6, ghost_dense=True)
            self._add_swing_ride(midi, bar, energy=4)

            if bar % 2 == 1:
                self.add_note(
                    midi, self.drum_mapping['ride_bell'], bar, self._beat(1),
                    self.get_random_velocity(88, 5)
                )
                self.add_note(
                    midi, self.drum_mapping['ride_bell'], bar, self._beat(3),
                    self.get_random_velocity(86, 5)
                )

            if self.should_add_variation(bar, 0.3):
                self.add_note(
                    midi, self.drum_mapping['open_hh'], bar, self._shuffle_off(3),
                    self.get_random_velocity(55, 8), 0.3
                )

    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Variation 2 - sidestick blues shuffle with soft hats."""
        for bar in range(start_bar, min(start_bar + bars, 149)):
            self._add_feathered_kick(midi, bar, syncopated=True)
            self._add_jazz_snare(midi, bar, energy=-8, use_sidestick=True, ghost_dense=True)

            for beat in range(4):
                self.add_note(
                    midi, self.drum_mapping['closed_hh'], bar, self._beat(beat),
                    self.get_random_velocity(62, 8)
                )
                self.add_note(
                    midi, self.drum_mapping['closed_hh'], bar, self._shuffle_off(beat),
                    self.get_random_velocity(48, 10)
                )

            if bar % 4 == 3:
                self.add_note(
                    midi, self.drum_mapping['tom_mid'], bar, self._shuffle_off(2),
                    self.get_random_velocity(60, 8)
                )

    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple jazz blues fill - snare and soft toms."""
        self.add_note(
            midi, self.drum_mapping['kick'], bar, 0,
            self.get_random_velocity(70, 5)
        )
        self.add_note(
            midi, self.drum_mapping['ride'], bar, 0,
            self.get_random_velocity(72, 6)
        )

        positions = [
            (self._beat(1), self.drum_mapping['snare'], 78),
            (self._shuffle_off(1), self.drum_mapping['snare'], 68),
            (self._beat(2), self.drum_mapping['tom_high'], 72),
            (self._shuffle_off(2), self.drum_mapping['tom_mid'], 76),
            (self._beat(3), self.drum_mapping['snare'], 84),
            (self._shuffle_off(3), self.drum_mapping['tom_low'], 80),
        ]
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 5))

    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex jazz blues fill - triplet tom cascade into crash."""
        self.add_note(midi, self.drum_mapping['kick'], bar, 0, 78)
        self.add_note(midi, self.drum_mapping['ride'], bar, 0, 74)

        positions = [
            (self._beat(1), self.drum_mapping['snare'], 82),
            (self._beat(1) + self.midi_config['ticks_per_sixteenth'],
             self.drum_mapping['tom_high'], 74),
            (self._shuffle_off(1), self.drum_mapping['tom_mid'], 78),
            (self._beat(2), self.drum_mapping['tom_low'], 84),
            (self._beat(2) + self.midi_config['ticks_per_sixteenth'],
             self.drum_mapping['snare'], 80),
            (self._shuffle_off(2), self.drum_mapping['tom_high'], 76),
            (self._beat(3), self.drum_mapping['tom_mid'], 86),
            (self._beat(3) + self.midi_config['ticks_per_sixteenth'],
             self.drum_mapping['tom_low'], 88),
            (self._shuffle_off(3), self.drum_mapping['snare'], 92),
        ]
        for pos, drum, velocity in positions:
            self.add_note(midi, drum, bar, pos, self.get_random_velocity(velocity, 5))

        self.add_note(
            midi, self.drum_mapping['crash'], bar,
            self.midi_config['ticks_per_beat'] * 4 - self.midi_config['ticks_per_sixteenth'],
            95
        )
        self.add_note(
            midi, self.drum_mapping['kick'], bar,
            self.midi_config['ticks_per_beat'] * 4 - self.midi_config['ticks_per_sixteenth'],
            90
        )

    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Intro - soft sidestick into swing ride."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars // 2:
                self._add_feathered_kick(midi, bar)
                self._add_jazz_snare(midi, bar, energy=-12, use_sidestick=True)
                for beat in range(4):
                    self.add_note(
                        midi, self.drum_mapping['closed_hh'], bar, self._beat(beat),
                        self.get_random_velocity(55, 8)
                    )
            else:
                self.create_basic_pattern(midi, bar, 1)

    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Verse - classic jazz blues swing."""
        for bar in range(start_bar, start_bar + bars):
            self.create_basic_pattern(midi, bar, 1)

    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Chorus - ride bell and denser ghosts."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_1(midi, bar, 1)

    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Bridge - sidestick shuffle."""
        for bar in range(start_bar, start_bar + bars):
            self.create_variation_2(midi, bar, 1)

    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Outro - jazz blues wind-down."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + bars - 2:
                self.create_variation_1(midi, bar, 1)
            else:
                self.create_fill_complex(midi, bar)
