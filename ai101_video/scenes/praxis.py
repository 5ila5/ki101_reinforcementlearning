from manim import (  # DOWN,; IN,; OUT,; RIGHT,; Create,; FadeIn,; FadeOut,
    Group,
    ImageMobject,
    Text,
)

from ai101_video.default_voice_scene import DefaultMainVoiceScene
from ai101_video.text_helper import Text_Helper


class Environment(DefaultMainVoiceScene):
    def construct(self):
        def move_elf(direction, coordinates, time):
            if self.elfs[direction] != self.active_elve:
                self.remove(self.active_elve)
                self.active_elve = self.elfs[direction]
                self.add(self.active_elve)

            for e in self.elfs.values():
                if e == self.active_elve:
                    self.play(
                        self.elfs[direction].animate.move_to(coordinates), run_time=time
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
        ) as tracker:
            time = tracker.duration / 6

            move_elf("down", env[2][0].get_center(), time * 2)
            move_elf("right", env[2][2].get_center(), time * 2)
            move_elf("down", env[3][2].get_center(), time)
            move_elf("right", env[3][3].get_center(), time)

            self.active_elve.add(Text("+1"))

            # self.play(elf.
