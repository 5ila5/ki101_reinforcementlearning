from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    FadeIn,
    MobjectTable,
    SurroundingRectangle,
)
from manim.mobject.graphing.coordinate_systems import GREEN
from manim.mobject.graphing.number_line import Tex
from manim.mobject.three_d.three_dimensions import Group

from ai101_video.default_voice_scene import DefaultMainVoiceScene
from ai101_video.scenes.utils import Grid
from ai101_video.scenes.utils import QTable as Q
from ai101_video.text_helper import Text_Helper

ZERO_TABLE = [
    [
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
    ],
    [
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
    ],
    [
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
    ],
    [
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
    ],
]


class Training(DefaultMainVoiceScene):
    def construct(self):
        grid = Grid()
        grid_display = grid.group.scale(0.8).move_to(LEFT * 4)

        table = Q(ZERO_TABLE)

        table_m: MobjectTable = table.get_qtable().move_to(LEFT * 4)

        table_m.get_vertical_lines().set_opacity(0)
        table_m.get_horizontal_lines().set_opacity(0)

        table_m.scale_to_fit_height(grid.group.get_height())
        table_m.scale_to_fit_width(grid.group.get_width())

        self.play(FadeIn(grid_display), FadeIn(table_m))

        with self.voiceover(Text_Helper.get_text("Training", "start")):
            pass

        with self.voiceover(Text_Helper.get_text("Training", "active_1")):
            pass

        with self.voiceover(Text_Helper.get_text("Training", "active_2")):
            active_display_text_title = Tex(
                Text_Helper.get_text("Training", "active_text_title"), font_size=35
            )
            active_display_text = Group(
                Tex(Text_Helper.get_text("Training", "active_text_1"), font_size=25),
                Tex(Text_Helper.get_text("Training", "active_text_2"), font_size=25),
                Tex(Text_Helper.get_text("Training", "active_text_3"), font_size=25),
            )

            active_display_text_title.move_to(RIGHT * 4 + UP * 2)
            active_display_text.arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(
                RIGHT * 4 + UP
            )

            box = SurroundingRectangle(active_display_text, buff=0.1).set_stroke(
                color=GREEN
            )

            self.play(
                FadeIn(active_display_text_title),
                FadeIn(active_display_text),
                FadeIn(box),
            )

        with self.voiceover(Text_Helper.get_text("Training", "passive")):
            passive_display_text_title = Tex(
                Text_Helper.get_text("Training", "passive_text_title"), font_size=35
            )
            passive_display_text = Group(
                Tex(Text_Helper.get_text("Training", "passive_text"), font_size=25),
            )

            passive_display_text_title.move_to(RIGHT * 4 + DOWN * 0.9)
            passive_display_text.arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(
                RIGHT * 4 + DOWN * 1.5
            )

            box = SurroundingRectangle(passive_display_text, buff=0.1).set_stroke(
                color=GREEN
            )

            self.play(
                FadeIn(passive_display_text_title),
                FadeIn(passive_display_text),
                FadeIn(box),
            )
