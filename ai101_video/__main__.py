import argparse
import importlib
import inspect
import multiprocessing
import pkgutil
import subprocess
from multiprocessing import Pool
from pathlib import PosixPath

from manim import FadeOut, Scene, config
from manim.utils.file_ops import open_file

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


def merge_videos(video_files: list[PosixPath], output_file: PosixPath):
    # Erstelle eine temporäre Datei mit den Namen der Videodateien

    tmp_file = video_files[0].parent.joinpath("tmp.txt")
    with open(tmp_file, "w") as f:
        for video_file in video_files:
            f.write(f"file '{video_file}'\n")

    # Führe den ffmpeg-Befehl aus, um die Videos zusammenzuführen
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(tmp_file),
            "-c",
            "copy",
            "-scodec",
            "copy",
            output_file,
        ]
    )
    # Lösche die temporäre Datei
    # os.remove("temp.txt")


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


def render_scene(scene_class: type[DefaultMainVoiceScene]) -> PosixPath:
    scene = scene_class()
    scene.render()
    return scene.renderer.file_writer.movie_file_path


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
argparser.add_argument(
    "--no-multiprocessing",
    action="store_true",
)

args = argparser.parse_args()

config.quality = args.quality

if args.no_multiprocessing:
    MainScene().render(preview=True)
else:
    processes = min(multiprocessing.cpu_count(), len(main_scene_classes))

    print(f"Rendering {len(main_scene_classes)} scenes with {processes} processes")

    with Pool(processes=processes) as pool:
        files = list(pool.map(render_scene, main_scene_classes))

    print(files, [f.absolute() for f in files], type(files), type(files[0].absolute()))
    output_path = files[0].with_name("MainScene.mp4")
    merge_videos(files, output_path)
    open_file(output_path)
