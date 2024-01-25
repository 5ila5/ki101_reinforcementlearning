from manim import *
from ai101_video.text_helper import Text_Helper

from ai101_video.default_voice_scene import DefaultMainVoiceScene


class Start(DefaultMainVoiceScene):
    def construct(self):
        text = Text(Text_Helper.get_text("Start", "title"), font_size=50)

        with self.voiceover(Text_Helper.get_text("Start", "title")) as tracker:
            self.play(Write(text), run_time=tracker.duration)

        self.wait(1)

        car = ImageMobject("assets/car_single.png").scale(2).to_edge(LEFT)
        schach = ImageMobject("assets/schach.png").scale(1).to_edge(RIGHT)
        self.play(car.animate.shift(RIGHT * 10), run_time=1)
        self.play(schach.animate, run_time=1)
