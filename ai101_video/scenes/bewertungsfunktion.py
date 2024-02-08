from manim import (
    DOWN,
    UP,
    WHITE,
    FadeIn,
    FadeOut,
    ImageMobject,
    ParsableManimColor,
    SurroundingRectangle,
    Write,
)
from manim.mobject.graphing.coordinate_systems import Arrow
from manim.mobject.text.tex_mobject import Tex

from ai101_video.default_voice_scene import DefaultMainVoiceScene
from ai101_video.text_helper import Text_Helper


class Bewertungsfunktion(DefaultMainVoiceScene):
    def construct(self):
        def highlight_text(text: Tex, pos1: int, pos2: int, color: ParsableManimColor):
            return [
                text[0][pos1 + i].animate.set_color(color)
                for i in range(0, pos2 - pos1)
            ]

        with self.voiceover(
            Text_Helper.get_text("Bewertungsfunktion", "start")
        ) as tracker:
            title = Tex(
                Text_Helper.get_text("Bewertungsfunktion", "title"), font_size=40
            ).move_to(UP * 3)

            self.play(Write(title))

            bellman_title = Tex(
                Text_Helper.get_text("Bewertungsfunktion", "bellman_title"),
                font_size=30,
            ).next_to(title, DOWN)

            bellman = ImageMobject("assets/Bellman.jpg").scale(0.2).move_to(DOWN * 0.5)

            self.play(
                Write(bellman_title),
            )
            self.play(
                bellman.animate.scale(2),
                run_time=tracker.duration,
            )

        self.play(FadeOut(bellman_title), FadeOut(bellman))

        with self.voiceover(Text_Helper.get_text("Bewertungsfunktion", "formel_start")):
            formel = Tex(
                "\\begin{flalign*} Q-Table(state, action) = ~ &Q-Table(state, action) \\cdot (1 - learning\\_rate) \\\\ \
                &+ learning\\_rate \\cdot (reward + discount\\_rate \\cdot max(Q-Table(new\\_state))) \\end{flalign*}",
                font_size=25,
            )

            desc_text_1_pos = formel[0][25].get_center()
            desc_text_1_arrow = Arrow(
                desc_text_1_pos,
                desc_text_1_pos + UP * 0.8,
                stroke_width=4,
                max_stroke_width_to_length_ratio=100,
                max_tip_length_to_length_ratio=10,
                tip_length=0.15,
            )
            desc_text_1 = Tex(
                Text_Helper.get_text("Bewertungsfunktion", "desc_text_1"),
                font_size=20,
            ).next_to(desc_text_1_pos + UP * 0.5, UP)
            desc_text_1_box = SurroundingRectangle(
                desc_text_1, color=WHITE, stroke_width=1
            )

            desc_text_2_pos = formel[0][111].get_center()
            desc_text_2_arrow = Arrow(
                desc_text_2_pos,
                desc_text_2_pos + DOWN * 0.8,
                stroke_width=4,
                max_stroke_width_to_length_ratio=100,
                max_tip_length_to_length_ratio=10,
                tip_length=0.15,
            )
            desc_text_2 = Tex(
                Text_Helper.get_text("Bewertungsfunktion", "desc_text_2"), font_size=20
            ).next_to(desc_text_2_pos + DOWN * 0.5, DOWN)
            desc_text_2_box = SurroundingRectangle(
                desc_text_2, color=WHITE, stroke_width=1
            )

            self.play(Write(formel))
            self.play(
                FadeIn(desc_text_1_arrow),
                FadeIn(desc_text_1),
                FadeIn(desc_text_1_box),
                FadeIn(desc_text_2_arrow),
                FadeIn(desc_text_2),
                FadeIn(desc_text_2_box),
            )

        with self.voiceover(
            Text_Helper.get_text("Bewertungsfunktion", "formel_learning_rate")
        ):
            for i in range(0, 3):
                if i % 2 == 0:
                    self.play(
                        *highlight_text(formel, 47, 60, "#21acfc"),
                        *highlight_text(formel, 62, 76, "#21acfc"),
                        run_time=0.5,
                    )
                else:
                    self.play(
                        *highlight_text(formel, 47, 60, WHITE),
                        *highlight_text(formel, 62, 76, WHITE),
                        run_time=0.5,
                    )

        self.play(
            *highlight_text(formel, 47, 60, WHITE),
            *highlight_text(formel, 62, 76, WHITE),
        )

        with self.voiceover(
            Text_Helper.get_text("Bewertungsfunktion", "formel_reward")
        ):
            for i in range(0, 3):
                if i % 2 == 0:
                    self.play(
                        *highlight_text(formel, 77, 83, "#21acfc"),
                        run_time=0.5,
                    )
                else:
                    self.play(
                        *highlight_text(formel, 77, 83, WHITE),
                        run_time=0.5,
                    )

        self.play(*highlight_text(formel, 77, 83, WHITE))
