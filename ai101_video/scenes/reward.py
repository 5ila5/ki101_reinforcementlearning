import numpy as np
from manim import (
    BLACK,
    DOWN,
    GRAY,
    GREEN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    Arrow,
    FadeIn,
    FadeOut,
    Group,
    ImageMobject,
    SVGMobject,
    Text,
    Write,
)

from ai101_video.default_voice_scene import DefaultMainVoiceScene
from ai101_video.scenes.utils import Elfs, Grid, img
from ai101_video.text_helper import Text_Helper


class Reward(DefaultMainVoiceScene):
    def construct(self):
        self.question_mark: list[Text] | None = None
        self.arrows: list[Arrow] | None = None

        def make_question_marks(elf, color=WHITE):
            self.question_mark = [
                Text("?", font_size=30, color=color, stroke_width=2) for _ in range(3)
            ]
            self.add(
                self.question_mark[0].next_to(elf, np.array([0.1, 0.1, 0])),
                self.question_mark[1].next_to(elf, np.array([0, 1, 0])),
                self.question_mark[2].next_to(elf, np.array([-0.1, 0.1, 0])),
            )

        def remove_question_marks(play=True) -> list[FadeOut | None] | None:
            if self.question_mark is None:
                return None

            question_mark_remove_list = [
                FadeOut(self.question_mark[i]) for i in range(3)
            ]

            if play:
                self.play(*(question_mark_remove_list))
                self.question_mark = None
                return None
            else:
                self.question_mark = None
                return question_mark_remove_list

        def make_arrows(elf, color1=BLACK, color2=BLACK, color3=BLACK, color4=BLACK):
            self.arrows = [
                Arrow(
                    elfs.active_elve.get_center() + UP * 0.1,
                    elfs.active_elve.get_center() + UP * 1.5,
                    color=color1,
                ),
                Arrow(
                    elfs.active_elve.get_center() + RIGHT * 0.1,
                    elfs.active_elve.get_center() + RIGHT * 1.5,
                    color=color2,
                ),
                Arrow(
                    elfs.active_elve.get_center() + DOWN * 0.1,
                    elfs.active_elve.get_center() + DOWN * 1.5,
                    color=color3,
                ),
                Arrow(
                    elfs.active_elve.get_center() + LEFT * 0.1,
                    elfs.active_elve.get_center() + LEFT * 1.5,
                    color=color4,
                ),
            ]

            arrows_add_list = [FadeIn(self.arrows[i]) for i in range(4)]

            self.play(*(arrows_add_list))

        def remove_arrows(play=True) -> list[FadeOut | None] | None:
            if self.arrows is None:
                return None

            arrows_remove_list = [FadeOut(self.arrows[i]) for i in range(4)]

            if play:
                self.play(*(arrows_remove_list))
                return None
            else:
                return arrows_remove_list

        title = Text(Text_Helper.get_text("Reward", "title"))
        self.play(Write(title))

        with self.voiceover(Text_Helper.get_text("Reward", "start")):
            pass

        self.play(FadeOut(title))

        grid = Grid()
        grid.add_stool()
        grid.add_present()
        elfs = Elfs(self)

        checkmark = SVGMobject("assets/checkmark.svg").scale(0.6)
        crossmark = SVGMobject("assets/crossmark.svg").scale(0.6)

        reward_text_group = Group()
        with self.voiceover(Text_Helper.get_text("Reward", "rewards")):
            for i in range(grid.count):
                text = "0"
                color = BLACK
                if i == 15:
                    text = "1"

                if i == 5 or i == 7 or i == 11 or i == 12:
                    color = RED

                reward_text_group.add(
                    Text(text, font_size=40, color=color, stroke_width=1).move_to(
                        grid.group[i].get_center()
                    )
                )

            self.play(grid.group.animate, reward_text_group.animate)
        self.play(FadeOut(reward_text_group))

        with self.voiceover(Text_Helper.get_text("Reward", "elf_rewarded")):
            grid.add_elfs(elfs)
            elfs.move("down", grid.env[2][0].get_center())
            elfs.move("right", grid.env[2][2].get_center())
            elfs.move("down", grid.env[3][2].get_center())
            elfs.move("right", grid.env[3][3].get_center())

            self.play(checkmark.move_to(grid.env[3][3].get_center()).animate)

        self.play(FadeOut(checkmark))

        with self.voiceover(Text_Helper.get_text("Reward", "elf_not_rewarded")):
            elfs.move("down", grid.env[0][0].get_center(), play=False)

            elfs.move("down", grid.env[1][0].get_center())
            elfs.move("right", grid.env[1][1].get_center())

            self.play(crossmark.scale(0.6).move_to(grid.env[1][1].get_center()).animate)

        self.play(FadeOut(crossmark))
        elfs.remove()
        self.play(FadeOut(grid.group))

        with self.voiceover(Text_Helper.get_text("Reward", "markov")):
            self.wait(1)

            markov = ImageMobject("assets/markov.jpg").scale(0.6)
            markov_text = Text("Markov Decision Process (MDP)", font_size=40)

            self.play(FadeIn(markov_text.move_to(UP * 3)), FadeIn(markov.move_to(DOWN)))

        self.play(FadeOut(markov), FadeOut(markov_text))

        with self.voiceover(Text_Helper.get_text("Reward", "policy_1")):
            self.wait(1)

            elf = img("assets/elf_down.png").scale(6)

            self.play(FadeIn(elf.move_to(LEFT * 3)))

            self.wait(1)

            make_question_marks(elf)

            self.wait(1)

            arrow_text = Text("findet", font_size=15)
            arrow = Arrow(elf.get_center() + RIGHT, elf.get_center() + RIGHT * 3)

            policy_test = Text("optimale policy", font_size=40)

            self.play(
                FadeIn(arrow),
                FadeIn(arrow_text.move_to(arrow.get_center() + UP * 0.2 + LEFT * 0.1)),
                FadeIn(policy_test.move_to(RIGHT * 3)),
            )

        self.play(
            FadeOut(elf),
            FadeOut(arrow),
            FadeOut(arrow_text),
            FadeOut(policy_test),
            *remove_question_marks(play=False)
        )

        with self.voiceover(Text_Helper.get_text("Reward", "policy_2")):
            self.wait(1)

            policy_text = Text("Policy", font_size=40)

            self.play(FadeIn(policy_text.move_to(UP * 3)))

            self.play(FadeIn(grid.group.move_to(DOWN * 0.5)))
            grid.add_stool()
            grid.add_present()
            elfs.add_after_remove()

            elfs.move("down", grid.env[0][0].get_center(), play=False)

            self.wait(4)

            make_arrows(
                elfs.active_elve, color1=GRAY, color2=GREEN, color3=GREEN, color4=GRAY
            )
            make_question_marks(elfs.active_elve, color=BLACK)
            self.wait(1)
            self.play(*remove_arrows(play=False), *remove_question_marks(play=False))

            elfs.move("down", grid.env[1][0].get_center())
            make_arrows(
                elfs.active_elve, color1=GREEN, color2=RED, color3=GREEN, color4=GRAY
            )
            make_question_marks(elfs.active_elve, color=BLACK)
            self.wait(1)
            self.play(*remove_arrows(play=False), *remove_question_marks(play=False))

            elfs.move("down", grid.env[2][0].get_center())
            make_arrows(
                elfs.active_elve, color1=GREEN, color2=GREEN, color3=RED, color4=GRAY
            )
            make_question_marks(elfs.active_elve, color=BLACK)
            self.wait(1)
            self.play(*remove_arrows(play=False), *remove_question_marks(play=False))

            elfs.move("right", grid.env[2][1].get_center())
            make_arrows(
                elfs.active_elve, color1=RED, color2=GREEN, color3=GREEN, color4=GREEN
            )
            make_question_marks(elfs.active_elve, color=BLACK)
            self.wait(1)
            self.play(*remove_arrows(play=False), *remove_question_marks(play=False))

            elfs.move("right", grid.env[2][2].get_center())
            make_arrows(
                elfs.active_elve, color1=GREEN, color2=RED, color3=GREEN, color4=GREEN
            )
            make_question_marks(elfs.active_elve, color=BLACK)
            self.wait(1)
            self.play(*remove_arrows(play=False), *remove_question_marks(play=False))

            elfs.move("down", grid.env[3][2].get_center())
            make_arrows(
                elfs.active_elve, color1=GREEN, color2=GREEN, color3=GRAY, color4=GREEN
            )
            make_question_marks(elfs.active_elve, color=BLACK)
            self.wait(1)
            self.play(*remove_arrows(play=False), *remove_question_marks(play=False))

            elfs.move("right", grid.env[3][3].get_center())
            elfs.move("down", grid.env[3][3].get_center())
