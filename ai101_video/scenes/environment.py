from manim import (  # DOWN,; IN,; OUT,; RIGHT,; Create,; FadeIn,; FadeOut,; Arrow3D,; VGroup,; Wait,
    DOWN,
    LEFT,
    OUT,
    RIGHT,
    UP,
    Arrow,
    Create,
    FadeOut,
    GrowArrow,
    SurroundingRectangle,
    Tex,
    Text,
    Uncreate,
    VGroup,
    VMobject,
    always_redraw,
    rate_functions,
)

from ai101_video.default_voice_scene import DefaultMainVoiceScene
from ai101_video.scenes.utils import Elfs, Grid
from ai101_video.text_helper import Text_Helper


class Environment(DefaultMainVoiceScene):
    def construct(self):
        helper_text_font_size = 30
        elfs = Elfs(self, z_index=1)
        grid = Grid()
        grid.group.move_to(LEFT * 3)
        texts: list[VMobject] = []
        helper_texts = always_redraw(
            lambda: VGroup()
            if not texts
            else SurroundingRectangle(
                VGroup(*texts).arrange(DOWN, aligned_edge=RIGHT).move_to(RIGHT * 4),
                color="green",
            )
        )
        self.add(helper_texts)

        with self.voiceover(
            Text_Helper.get_text("Praxis-Environment", "agent")
        ) as tracker:
            time = tracker.duration

            elfs.scale(20)
            elfs.to_edge(DOWN)
            elfs.reskin("down", force=True)
            agent_text = Tex("Agent", color="orange", font_size=80).next_to(
                elfs.active_elve, UP * 0.5
            )
            self.play(Create(agent_text), run_time=1)
            time -= 1
            time -= 2

            n = 32

            for i in range(n):
                elfs.reskin(["down", "right", "up", "left"][i % 4])
                self.wait(time / n)

            elfs.reskin("down")

            t = Tex(r"Agent $\approx$ Spielfigur", font_size=helper_text_font_size)
            texts.append(t)
            self.play(
                FadeOut(agent_text),
                Create(t),
                elfs.active_elve.animate.scale((1 / 20) * 6).move_to(
                    grid.env[0][0].get_center() + OUT
                ),
            )

            for e in elfs.elfs.values():
                if e is not elfs.active_elve:
                    e.scale((1 / 20) * 6).move_to(grid.env[0][0].get_center() + OUT)

        grid.add_stool()
        grid.add_present()

        grid.add_elfs(elfs, scale=1)

        with self.voiceover(
            Text_Helper.get_text("Praxis-Environment", "start")
        ) as tracker:
            self.add(grid.group)

        with self.voiceover(
            Text_Helper.get_text("Praxis-Environment", "real_start")
            + Text_Helper.get_text("Praxis-Environment", "show_lake")
        ) as tracker:
            time = tracker.duration / 6
            texts.extend(
                [
                    Tex(
                        r"Action $\approx$ einzelner Schritt",
                        font_size=helper_text_font_size,
                    ),
                    Tex(
                        r"State $\approx$ Zustand des Szenearios",
                        font_size=helper_text_font_size,
                    ),
                ]
            )
            elfs.move(
                "down",
                x=2,
                y=0,
                time=time * 2,
                add_animation=[Create(texts[-2]), Create(texts[-1])],
            )
            elfs.move("right", x=2, y=2, time=time * 2)
            elfs.move("down", x=3, y=2, time=time)
            elfs.move("right", x=3, y=3, time=time)

            p1 = Text("+1", color="black").next_to(elfs.active_elve, UP)
            # put text above active elf
            self.play(Create(p1), FadeOut(grid.present))
            self.play(FadeOut(p1))

        self.add(grid.present)
        elfs.move("down", x=0, y=0, play=False)

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

            elfs.move("left", x=2, y=2, time=time)

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

        with self.voiceover(
            Text_Helper.get_text("Praxis-Environment", "transtiton_function")
        ) as tracker:
            time = tracker.duration / 6
            self.play(
                Uncreate(l_arrow),
                Uncreate(u_arrow),
                Uncreate(d_arrow),
                Uncreate(l_arrow_text),
                Uncreate(u_arrow_text),
                Uncreate(d_arrow_text),
                run_time=time * 3,
            )

            # self.play(FadeOut(grid.present), FadeOut(grid.stool), run_time=time/2)
            elfs.move(
                "down",
                x=0,
                y=0,
                add_animation=[FadeOut(grid.present), FadeOut(grid.stool)],
                time=time * 2,
            )
            self.play(FadeOut(elfs.elfs["down"]), run_time=time)
