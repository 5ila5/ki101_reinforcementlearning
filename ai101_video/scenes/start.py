from manim import DOWN, LEFT, RIGHT, UP, FadeOut, ImageMobject, Write
from manim.mobject.graphing.number_line import Tex

from ai101_video.default_voice_scene import DefaultMainVoiceScene
from ai101_video.text_helper import Text_Helper


class Start(DefaultMainVoiceScene):
    def construct(self):
        text = Tex(Text_Helper.get_text("Start", "title"), font_size=50)

        with self.voiceover(Text_Helper.get_text("Start", "title")) as tracker:
            self.play(Write(text), run_time=tracker.duration)

        self.wait(1)
        self.play(FadeOut(text))

        car = ImageMobject("assets/car.jpg").scale(0.3).to_edge(LEFT).to_edge(DOWN)
        schach = (
            ImageMobject("assets/schach_ki.png").scale(1).to_edge(RIGHT).to_edge(UP)
        )

        with self.voiceover(Text_Helper.get_text("Start", "start_1")) as tracker:
            self.wait(1)
            self.play(car.animate, run_time=tracker.duration)

        with self.voiceover(Text_Helper.get_text("Start", "start_2")) as tracker:
            self.wait(1)
            self.play(schach.animate, run_time=tracker.duration)

        with self.voiceover(Text_Helper.get_text("Start", "start_3")) as tracker:
            pass
