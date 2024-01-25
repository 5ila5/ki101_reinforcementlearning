import argparse
import importlib
import inspect
import pkgutil

from manim import FadeOut, Scene, config

import ai101_video.scenes as main_scenes
from ai101_video.default_voice_scene import DefaultMainVoiceScene
from ai101_video.text_helper import ScenesToRender

main_scene_classes: list[type[DefaultMainVoiceScene]] = []

for loader, module_name, is_pkg in pkgutil.walk_packages(main_scenes.__path__):
    module = importlib.import_module("." + module_name, main_scenes.__package__)

    for name, obj in inspect.getmembers(module):
        if (
            inspect.isclass(obj)
            and issubclass(obj, DefaultMainVoiceScene)
            and obj is not DefaultMainVoiceScene
            and obj.__name__ in ScenesToRender
        ):
            main_scene_classes.append(obj)


main_scene_classes.sort(key=lambda x: ScenesToRender.index(x.__name__))


def fade_out(scene: Scene):
    animations = []
    for mobject in scene.mobjects:
        animations.append(FadeOut(mobject))
    if animations:
        scene.play(*animations)


class MainScene(DefaultMainVoiceScene):
    def construct(self):
        for my_scene in main_scene_classes:
            my_scene.construct(self)
            fade_out(self)


argparser = argparse.ArgumentParser()
argparser.add_argument(
    "--quality",
    default="low_quality",
    choices=[
        "fourk_quality",
        "production_quality",
        "high_quality",
        "medium_quality",
        "low_quality",
        "example_quality",
    ],
)
args = argparser.parse_args()

config.quality = args.quality
MainScene().render(preview=True)
