import numpy as np
from manim import (
    BLACK,
    DOWN,
    LEFT,
    RED,
    RIGHT,
    UP,
    FadeIn,
    FadeOut,
    Group,
    ImageMobject,
    SVGMobject,
    Text,
    Write,
)

from ai101_video.default_voice_scene import DefaultMainVoiceScene
from ai101_video.scenes.utils import Elfs, Grid
from ai101_video.text_helper import Text_Helper


class Reward(DefaultMainVoiceScene):
    def construct(self):
        title = Text(Text_Helper.get_text("Reward", "title"))
        self.play(Write(title))

        with self.voiceover(Text_Helper.get_text("Reward", "start")) as _:
            pass

        self.play(FadeOut(title))

        grid = Grid()
        grid.add_stool()
        grid.add_present()
        elfs = Elfs(self)

        checkmark = SVGMobject("assets/checkmark.svg").scale(0.6)
        crossmark = SVGMobject("assets/crossmark.svg").scale(0.6)

        reward_text_group = Group()
        with self.voiceover(Text_Helper.get_text("Reward", "rewards")) as _:
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

        with self.voiceover(Text_Helper.get_text("Reward", "elf_rewarded")) as _:
            grid.add_elfs(elfs)
            elfs.move("down", grid.env[2][0].get_center())
            elfs.move("right", grid.env[2][2].get_center())
            elfs.move("down", grid.env[3][2].get_center())
            elfs.move("right", grid.env[3][3].get_center())

            self.play(checkmark.move_to(grid.env[3][3].get_center()).animate)

        self.play(FadeOut(checkmark))

        with self.voiceover(Text_Helper.get_text("Reward", "elf_not_rewarded")) as _:
            elfs.move("down", grid.env[0][0].get_center(), play=False)

            elfs.move("down", grid.env[1][0].get_center())
            elfs.move("right", grid.env[1][1].get_center())

            self.play(crossmark.scale(0.6).move_to(grid.env[1][1].get_center()).animate)

        self.play(FadeOut(crossmark))
        elfs.remove()
        self.play(FadeOut(grid.group))

        with self.voiceover(Text_Helper.get_text("Reward", "markov")) as _:
            self.wait(1)

            markov = ImageMobject("assets/markov.jpg").scale(0.6)
            markov_text = Text("Markov Decision Process (MDP)", font_size=40)

            self.play(FadeIn(markov_text.move_to(UP * 3)), FadeIn(markov.move_to(DOWN)))

        self.play(FadeOut(markov), FadeOut(markov_text))

        with self.voiceover(Text_Helper.get_text("Reward", "end")) as _:
            self.wait(1)

            elf = ImageMobject("assets/elf_down.png").scale(6)
            question_mark = [
                Text("?", font_size=30),
                Text("?", font_size=30),
                Text("?", font_size=30),
            ]

            self.play(FadeIn(elf.move_to(LEFT * 3)))

            self.wait(1)

            self.play(
                FadeIn(question_mark[0].next_to(elf, np.array([0.1, 0.1, 0]))),
                FadeIn(question_mark[1].next_to(elf, np.array([0, 1, 0]))),
                FadeIn(question_mark[2].next_to(elf, np.array([-0.1, 0.1, 0]))),
            )

            self.wait(1)

            policy_test = Text("policy? wann wo hin?", font_size=40)

            self.play(FadeIn(policy_test.move_to(RIGHT * 3)))
