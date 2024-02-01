from manim import (  # DOWN,; IN,; OUT,; RIGHT,; Create,; FadeIn,; FadeOut,; Arrow3D,; VGroup,; Wait,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    Arrow,
    Create,
    FadeOut,
    Group,
    ImageMobject,
    Tex,
    Text,
    rate_functions,
)

from ai101_video.default_voice_scene import DefaultMainVoiceScene
from ai101_video.text_helper import Text_Helper


class Environment(DefaultMainVoiceScene):
    def construct(self):
        def move_elf(direction, coordinates, time=1, play=True, func=None):
            if self.elfs[direction] != self.active_elve:
                self.remove(self.active_elve)
                self.active_elve = self.elfs[direction]
                self.add(self.active_elve)

            for e in self.elfs.values():
                if e == self.active_elve and play:
                    self.play(
                        self.elfs[direction].animate.move_to(coordinates),
                        run_time=time,
                        rate_func=rate_functions.linear,
                    )
                else:
                    e.move_to(coordinates)

        env = [
            [
                ImageMobject("assets/ice.png"),
                ImageMobject("assets/ice.png"),
                ImageMobject("assets/ice.png"),
                ImageMobject("assets/ice.png"),
            ],
            [
                ImageMobject("assets/ice.png"),
                ImageMobject("assets/cracked_hole.png"),
                ImageMobject("assets/ice.png"),
                ImageMobject("assets/cracked_hole.png"),
            ],
            [
                ImageMobject("assets/ice.png"),
                ImageMobject("assets/ice.png"),
                ImageMobject("assets/ice.png"),
                ImageMobject("assets/cracked_hole.png"),
            ],
            [
                ImageMobject("assets/cracked_hole.png"),
                ImageMobject("assets/ice.png"),
                ImageMobject("assets/ice.png"),
                ImageMobject("assets/ice.png"),
            ],
        ]
        for row in env:
            for col in row:
                col.scale(6)

        g = Group(*[e for row in env for e in row]).arrange_in_grid(4, 4, buff=0.1)

        stool = (
            ImageMobject("assets/stool.png").move_to(env[0][0].get_center()).scale(6)
        )
        g.add(stool)
        present = (
            ImageMobject("assets/goal.png").move_to(env[3][3].get_center()).scale(6)
        )
        g.add(present)

        self.elfs = {
            "down": ImageMobject("assets/elf_down.png"),
            "left": ImageMobject("assets/elf_left.png"),
            "right": ImageMobject("assets/elf_right.png"),
            "up": ImageMobject("assets/elf_up.png"),
        }

        for e in self.elfs.values():
            e.scale(6).move_to(env[0][0].get_center())
        self.active_elve = self.elfs["down"]

        g.add(stool)

        with self.voiceover(
            Text_Helper.get_text("Praxis-Environment", "start")
        ) as tracker:
            self.play(g.animate, run_time=tracker.duration)

        with self.voiceover(
            Text_Helper.get_text("Praxis-Environment", "real_start")
            + Text_Helper.get_text("Praxis-Environment", "show_lake")
        ) as tracker:
            time = tracker.duration / 6

            move_elf("down", env[2][0].get_center(), time * 2)
            move_elf("right", env[2][2].get_center(), time * 2)
            move_elf("down", env[3][2].get_center(), time)
            move_elf("right", env[3][3].get_center(), time)

            p1 = Text("+1", color="black").next_to(self.active_elve, UP)
            # put text above active elf
            self.play(Create(p1), FadeOut(present))
            self.play(FadeOut(p1))

        self.add(present)
        move_elf("down", env[0][0].get_center(), play=False)

        with self.voiceover(
            Text_Helper.get_text("Praxis-Environment", "slippery1")
        ) as tracker:
            n = 32
            time = tracker.duration / n

            self.wait(n // 3 * time)
            n = n - n // 3

            step = (env[1][0].get_center() - env[0][0].get_center()) / n
            post = env[0][0].get_center()
            for i in range(n):
                direction = ["right", "up", "left", "down"][i % 4]
                move_elf(
                    direction, post := post + step, time, func=rate_functions.linear
                )

        with self.voiceover(
            Text_Helper.get_text("Praxis-Environment", "slippery2")
        ) as tracker:
            time = tracker.duration / 6

            move_elf("left", env[2][2].get_center(), time)

            arrow_stroke_width = 10
            arrow_font_size = 80

            l_arrow = Arrow(
                env[2][2].get_center(),
                env[2][1].get_edge_center(LEFT),
                color="green",
                stroke_width=arrow_stroke_width,
                max_stroke_width_to_length_ratio=100,
            )
            l_arrow_text = Tex(
                r"$\frac{1}{3}$", color="orange", font_size=arrow_font_size
            ).next_to(
                (env[2][2].get_center() + env[2][1].get_edge_center(LEFT)) / 2, UP
            )

            u_arrow = Arrow(
                env[2][2].get_center(),
                env[1][2].get_edge_center(UP),
                color="orange",
                stroke_width=arrow_stroke_width,
                max_stroke_width_to_length_ratio=100,
            )
            u_arrow_text = Tex(
                r"$\frac{1}{3}$", color="orange", font_size=arrow_font_size
            ).next_to(
                (env[2][2].get_center() + env[1][2].get_edge_center(UP)) / 2, RIGHT
            )

            d_arrow = Arrow(
                env[2][2].get_center(),
                env[3][2].get_edge_center(DOWN),
                color="orange",
                stroke_width=arrow_stroke_width,
                max_stroke_width_to_length_ratio=100,
            )
            d_arrow_text = Tex(
                r"$\frac{1}{3}$", color="orange", font_size=arrow_font_size
            ).next_to(
                (env[2][2].get_center() + env[3][2].get_edge_center(DOWN)) / 2, LEFT
            )

            self.add(
                # l_arrow,
                # u_arrow,
                # d_arrow,
                Group(l_arrow, u_arrow, d_arrow),
                l_arrow_text,
                u_arrow_text,
                d_arrow_text,
            )
