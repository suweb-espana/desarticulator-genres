"""
Dub Reggae drum pattern generator fusing rocksteady swing with a dub one drop.
Inspired by Prince Buster's rocksteady shuffle and the spaced-out dub production
of Scientist, Prince Far I, and Augustus Pablo.
"""

import random
from typing import Optional
from core.base_pattern import BasePattern
from midiutil import MIDIFile


class DubReggaePattern(BasePattern):
    """Rocksteady-swung one drop with dub-style space, drops, and aggressive breaks."""

    # Offbeat swing ratio range - varies note to note so the shuffle breathes
    # instead of locking to a grid, per Prince Buster's rocksteady feel.
    SWING_MIN = 0.56
    SWING_MAX = 0.63

    def __init__(self, tempo: int = 150, seed: Optional[int] = None):
        super().__init__(tempo, seed)
        # Extend the GM map with the rocksteady rim click and the riddim cowbell.
        self.drum_mapping['side_stick'] = 37
        self.drum_mapping['cowbell'] = 56

    @property
    def genre_name(self) -> str:
        return "Dub Reggae"

    @property
    def description(self) -> str:
        return ("Rocksteady-swung one drop fused with dub space, drops, and "
                "triplet break hits, inspired by Prince Buster's shuffle and "
                "the dub production of Scientist, Prince Far I, and Augustus Pablo")

    def _swung_tick(self, beat: int) -> int:
        """Offbeat tick position with a humanized rocksteady swing ratio."""
        ratio = random.uniform(self.SWING_MIN, self.SWING_MAX)
        return int(self.midi_config['ticks_per_beat'] * (beat + ratio))

    def _hihat_skank(self, midi: MIDIFile, bar: int, base_velocity: int = 76,
                      variation: int = 8, beats: tuple = (0, 1, 2, 3)) -> None:
        """Swung hi-hat skank on the offbeats - the rocksteady half of the fusion,
        and the main pulse of the tune."""
        for beat in beats:
            self.add_note(midi, self.drum_mapping['closed_hh'], bar,
                         self._swung_tick(beat),
                         self.get_random_velocity(base_velocity, variation))

    def _ride_skank(self, midi: MIDIFile, bar: int, base_velocity: int = 82,
                     variation: int = 8, beats: tuple = (0, 1, 2, 3)) -> None:
        """Ride cymbal on the swung offbeats - bigger and more sustained than the hi-hat, for climaxes."""
        for beat in beats:
            self.add_note(midi, self.drum_mapping['ride'], bar,
                         self._swung_tick(beat),
                         self.get_random_velocity(base_velocity, variation))

    def _open_hat_accent(self, midi: MIDIFile, bar: int, beat: int = 3,
                          velocity: int = 85) -> None:
        """Open hi-hat 'chick-aahh' marking a phrase end or a drop return."""
        self.add_note(midi, self.drum_mapping['open_hh'], bar,
                     self._swung_tick(beat),
                     self.get_random_velocity(velocity, 6), 0.3)

    def _section_crash(self, midi: MIDIFile, bar: int, velocity: int = 100) -> None:
        """Crash marking the start of a section, not just a fill accent."""
        self.add_note(midi, self.drum_mapping['crash'], bar, 0,
                     self.get_random_velocity(velocity, 5), 1.2)

    def _rim_ghost(self, midi: MIDIFile, bar: int) -> None:
        """Rocksteady rim click - a defined rim ghost, landing on a different
        offbeat each bar so it doesn't feel programmed."""
        beat = random.choice([0, 2])
        self.add_note(midi, self.drum_mapping['side_stick'], bar,
                     self._swung_tick(beat),
                     self.get_random_velocity(62, 8))

    def _pompe_touch(self, midi: MIDIFile, bar: int, base_velocity: int = 58) -> None:
        """A brief nod to Django Reinhardt's la pompe: two straight, muted
        quarter-note rim hits (beats 3-4), used sparingly as a color, never as
        the main pulse - a full bar of it flattened the groove."""
        for beat in (2, 3):
            self.add_note(midi, self.drum_mapping['side_stick'], bar,
                         self.midi_config['ticks_per_beat'] * beat,
                         self.get_random_velocity(base_velocity, 6), 0.06)

    def _cowbell_accent(self, midi: MIDIFile, bar: int) -> None:
        """Sparse riddim cowbell click on beat 1 - only in the driving sections."""
        self.add_note(midi, self.drum_mapping['cowbell'], bar, 0,
                     self.get_random_velocity(72, 6))

    def _one_drop_kick(self, midi: MIDIFile, bar: int, velocity: int = 105,
                        double_drop: bool = False) -> None:
        """Clear, tight one-drop kick on beat 3. Occasionally a swung double-drop
        pickup on the and-of-2 pushes into it for extra syncopation."""
        if double_drop and random.random() < 0.3:
            self.add_note(midi, self.drum_mapping['kick'], bar,
                         self._swung_tick(1),
                         self.get_random_velocity(velocity - 20, 5))
        self.add_note(midi, self.drum_mapping['kick'], bar,
                     self.midi_config['ticks_per_beat'] * 2,
                     self.get_random_velocity(velocity, 3))

    def _backbeat_snare(self, midi: MIDIFile, bar: int, velocity: int = 100,
                         variation: int = 4, flam: bool = False) -> None:
        """Clear, tight snare backbeat on 2 and 4. Optional flam for a more
        aggressive attack on the climactic sections."""
        for beat_ticks in (self.midi_config['ticks_per_beat'],
                           self.midi_config['ticks_per_beat'] * 3):
            if flam:
                self.add_note(midi, self.drum_mapping['snare'], bar,
                             beat_ticks - 28,
                             self.get_random_velocity(45, 5))
            self.add_note(midi, self.drum_mapping['snare'], bar,
                         beat_ticks,
                         self.get_random_velocity(velocity, variation))

    def _triplet_kick_break(self, midi: MIDIFile, bar: int, beat: int = 3) -> None:
        """Aggressive dubstep/breaks-style triplet kick run - a heavier alternative
        to the tom pickup, used sparingly on climactic bars."""
        third = self.midi_config['ticks_per_beat'] // 3
        base_tick = self.midi_config['ticks_per_beat'] * beat
        for i in range(3):
            self.add_note(midi, self.drum_mapping['kick'], bar,
                         base_tick + i * third,
                         self.get_random_velocity(108 - i * 4, 4))

    def create_basic_pattern(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Classic one drop with occasional double-drop push, swung hi-hat, rim click."""
        for bar in range(start_bar, start_bar + bars):
            self._one_drop_kick(midi, bar, double_drop=True)
            self._backbeat_snare(midi, bar)
            self._hihat_skank(midi, bar)
            self._rim_ghost(midi, bar)

    def create_variation_1(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Rocksteady push with ride, cowbell click, and flammed backbeat - the driving variant."""
        for bar in range(start_bar, start_bar + bars):
            self.add_note(midi, self.drum_mapping['kick'], bar,
                         self._swung_tick(1),
                         self.get_random_velocity(85, 5))
            self._one_drop_kick(midi, bar)
            self._backbeat_snare(midi, bar, flam=True)
            self._ride_skank(midi, bar, base_velocity=80, variation=6)
            self._cowbell_accent(midi, bar)

    def create_variation_2(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Dub drop: beats 1-2 stripped to hi-hat and rim, one drop hits hard on 3
        with an open hat accent marking the return."""
        for bar in range(start_bar, start_bar + bars):
            self._hihat_skank(midi, bar, base_velocity=70, variation=6, beats=(0, 1))
            self._rim_ghost(midi, bar)

            self._one_drop_kick(midi, bar, velocity=112)
            self._backbeat_snare(midi, bar, velocity=105, variation=3)
            self._open_hat_accent(midi, bar, beat=2, velocity=88)
            self._hihat_skank(midi, bar, base_velocity=80, variation=6, beats=(3,))

    def create_fill_simple(self, midi: MIDIFile, bar: int) -> None:
        """Simple fill - one drop plus a swung tom pickup into the next bar."""
        self._one_drop_kick(midi, bar)
        self._backbeat_snare(midi, bar)

        self.add_note(midi, self.drum_mapping['tom_high'], bar,
                     self._swung_tick(3),
                     self.get_random_velocity(85, 5))
        self.add_note(midi, self.drum_mapping['tom_mid'], bar,
                     self.midi_config['ticks_per_beat'] * 3.75,
                     self.get_random_velocity(85, 5))

        self._hihat_skank(midi, bar, beats=(0, 1, 2))

    def create_fill_complex(self, midi: MIDIFile, bar: int) -> None:
        """Complex fill - either a tom roll into a crash, or (30% of the time) an
        aggressive triplet kick break, for the climactic dub-drop moment."""
        self._one_drop_kick(midi, bar)
        self._backbeat_snare(midi, bar)

        if random.random() < 0.3:
            self._triplet_kick_break(midi, bar)
        else:
            self.add_note(midi, self.drum_mapping['tom_low'], bar,
                         self.midi_config['ticks_per_beat'] * 2.5,
                         self.get_random_velocity(88, 5))
            self.add_note(midi, self.drum_mapping['tom_mid'], bar,
                         self.midi_config['ticks_per_beat'] * 2.75,
                         self.get_random_velocity(88, 5))
            self.add_note(midi, self.drum_mapping['tom_high'], bar,
                         self._swung_tick(3),
                         self.get_random_velocity(90, 5))
            self.add_note(midi, self.drum_mapping['tom_mid'], bar,
                         self.midi_config['ticks_per_beat'] * 3.75,
                         self.get_random_velocity(88, 5))

        self.add_note(midi, self.drum_mapping['crash'], bar,
                     self.midi_config['ticks_per_beat'] * 3.5,
                     self.get_random_velocity(100, 5), 1.5)

        self._hihat_skank(midi, bar, beats=(0, 1))

    def create_intro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Build up from bare swung hi-hat to the full swung one drop."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 2:
                self._hihat_skank(midi, bar, base_velocity=55, variation=5)
            elif bar < start_bar + 4:
                self._hihat_skank(midi, bar, base_velocity=62, variation=5)
                self._rim_ghost(midi, bar)
            elif bar < start_bar + 6:
                self._hihat_skank(midi, bar, base_velocity=68, variation=6)
                self._backbeat_snare(midi, bar, velocity=78, variation=6)
            else:
                self.create_basic_pattern(midi, bar, 1)

    def create_verse_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Steady swung one drop - the groove that carries the song."""
        self._section_crash(midi, start_bar, velocity=85)
        self.create_basic_pattern(midi, start_bar, bars)

    def create_chorus_section(self, midi: MIDIFile, start_bar: int, bars: int = 16) -> None:
        """Rocksteady push driving the chorus: ride wash, cowbell, flammed snare,
        crash on every section/phrase start, occasional triplet break for punch."""
        self._section_crash(midi, start_bar, velocity=105)
        for bar in range(start_bar, start_bar + bars):
            phrase_start = (bar - start_bar) % 4 == 0

            if phrase_start and random.random() < 0.25:
                self._triplet_kick_break(midi, bar)
            else:
                self.add_note(midi, self.drum_mapping['kick'], bar,
                             self._swung_tick(1),
                             self.get_random_velocity(88, 5))
                self._one_drop_kick(midi, bar, velocity=110)

            self._backbeat_snare(midi, bar, velocity=105, variation=4, flam=True)
            self._ride_skank(midi, bar, base_velocity=84, variation=6)
            self._cowbell_accent(midi, bar)

            if phrase_start and not (bar == start_bar):
                self.add_note(midi, self.drum_mapping['crash'], bar,
                             self.midi_config['ticks_per_beat'] * 3.5,
                             self.get_random_velocity(95, 5), 0.8)
                self._open_hat_accent(midi, bar, beat=3, velocity=90)

    def create_bridge_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Dub drop for contrast - space up front, hits hard on the return. The
        quiet half nods to la pompe with two straight rim hits instead of the skank."""
        self._section_crash(midi, start_bar, velocity=90)
        for bar in range(start_bar, start_bar + bars):
            self._pompe_touch(midi, bar)

            self._one_drop_kick(midi, bar, velocity=112)
            self._backbeat_snare(midi, bar, velocity=105, variation=3)
            self._open_hat_accent(midi, bar, beat=2, velocity=88)
            self._hihat_skank(midi, bar, base_velocity=80, variation=6, beats=(3,))

    def create_outro_section(self, midi: MIDIFile, start_bar: int, bars: int = 8) -> None:
        """Strip back down to bare swung hi-hat, mirroring the intro build."""
        for bar in range(start_bar, start_bar + bars):
            if bar < start_bar + 4:
                self.create_basic_pattern(midi, bar, 1)
            elif bar < start_bar + 6:
                self._hihat_skank(midi, bar, base_velocity=62, variation=6)
                self._backbeat_snare(midi, bar, velocity=70, variation=6)
            else:
                self._hihat_skank(midi, bar, base_velocity=52, variation=5)
