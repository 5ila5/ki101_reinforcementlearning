from manim import (  # DOWN,; IN,; OUT,; RIGHT,; Create,; FadeIn,; FadeOut,; Arrow3D,; VGroup,; Wait,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    Arrow,
    Create,
    FadeOut,
    GrowArrow,
    Tex,
    Text,
    rate_functions,
)

from ai101_video.default_voice_scene import DefaultMainVoiceScene
from ai101_video.scenes.utils import Elfs, Grid
from ai101_video.text_helper import Text_Helper


class Environment(DefaultMainVoiceScene):
    def construct(self):
        # elfs_group = VGroup(*self.elfs.values()).scale(6)

        # with self.voiceover(
        #     Text_Helper.get_text("Praxis-Environment", "agent")
        # ) as tracker:

        #         elfs.move("down", self.get_center(), play=False)
        #         Text("Agent", color="black")

        grid = Grid()

        grid.add_stool()
        grid.add_present()

        elfs = Elfs(self)

        grid.add_elfs(elfs)

        with self.voiceover(
            Text_Helper.get_text("Praxis-Environment", "start")
        ) as tracker:
            self.add(grid.group)

        with self.voiceover(
            Text_Helper.get_text("Praxis-Environment", "real_start")
            + Text_Helper.get_text("Praxis-Environment", "show_lake")
        ) as tracker:
            time = tracker.duration / 6

            elfs.move("down", grid.env[2][0].get_center(), time * 2)
            elfs.move("right", grid.env[2][2].get_center(), time * 2)
            elfs.move("down", grid.env[3][2].get_center(), time)
            elfs.move("right", grid.env[3][3].get_center(), time)

            p1 = Text("+1", color="black").next_to(elfs.active_elve, UP)
            # put text above active elf
            self.play(Create(p1), FadeOut(grid.present))
            self.play(FadeOut(p1))

        self.add(grid.present)
        elfs.move("down", grid.env[0][0].get_center(), play=False)

        with self.voiceover(
            Text_Helper.get_text("Praxis-Environment", "slippery1")
        ) as tracker:
            n = 32
            time = tracker.duration / n

            self.wait(n // 3 * time)
            n = n - n // 3

            step = (grid.env[1][0].get_center() - grid.env[0][0].get_center()) / n
            post = grid.env[0][0].get_center()
            for i in range(n):
                direction = ["right", "up", "left", "down"][i % 4]
                elfs.move(
                    direction, post := post + step, time, func=rate_functions.linear
                )

        with self.voiceover(
            Text_Helper.get_text("Praxis-Environment", "slippery2")
        ) as tracker:
            time = tracker.duration / 6

            elfs.move("left", grid.env[2][2].get_center(), time)

            arrow_stroke_width = 10
            arrow_font_size = 80

            l_arrow = Arrow(
                grid.env[2][2].get_center(),
                grid.get_edge_center(LEFT)[2][1],
                color="green",
                stroke_width=arrow_stroke_width,
                max_stroke_width_to_length_ratio=100,
            )
            l_arrow_text = Tex(
                r"$\frac{1}{3}$", color="orange", font_size=arrow_font_size
            ).next_to(
                (grid.env[2][2].get_center() + grid.get_edge_center(LEFT)[2][1]) / 2, UP
            )

            u_arrow = Arrow(
                grid.env[2][2].get_center(),
                grid.get_edge_center(UP)[1][2],
                color="orange",
                stroke_width=arrow_stroke_width,
                max_stroke_width_to_length_ratio=100,
            )
            u_arrow_text = Tex(
                r"$\frac{1}{3}$", color="orange", font_size=arrow_font_size
            ).next_to(
                (grid.env[2][2].get_center() + grid.get_edge_center(UP)[1][2]) / 2,
                RIGHT,
            )

            d_arrow = Arrow(
                grid.env[2][2].get_center(),
                grid.get_edge_center(DOWN)[3][2],
                color="orange",
                stroke_width=arrow_stroke_width,
                max_stroke_width_to_length_ratio=100,
            )
            d_arrow_text = Tex(
                r"$\frac{1}{3}$", color="orange", font_size=arrow_font_size
            ).next_to(
                (grid.env[2][2].get_center() + grid.get_edge_center(DOWN)[3][2]) / 2,
                LEFT,
            )

            self.play(
                GrowArrow(l_arrow),
                GrowArrow(u_arrow),
                GrowArrow(d_arrow),
                Create(l_arrow_text),
                Create(u_arrow_text),
                Create(d_arrow_text),
            )
