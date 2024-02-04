import numpy as np
from manim import GrowArrow, MobjectTable

from ai101_video.default_voice_scene import DefaultMainVoiceScene
from ai101_video.scenes.utils import Grid
from ai101_video.scenes.utils import QTable as Q
from ai101_video.text_helper import Text_Helper

# random value between 0 and 1

RANDOM_TABLE = [
    [
        [
            0.54507032,
            0.50480373,
            0.5022681,
            0.5033242,
        ],
        [
            0.39346827,
            0.35613195,
            0.18863932,
            0.491817,
        ],
        [
            0.42860918,
            0.40931135,
            0.4202072,
            0.46005767,
        ],
        [
            0.27750734,
            0.29191303,
            0.3973913,
            0.44343163,
        ],
    ],
    [
        [
            0.55590619,
            0.36304211,
            0.37631394,
            0.35890126,
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
        [
            0.19068687,
            0.14792543,
            0.30038977,
            0.12166222,
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
    ],
    [
        [
            0.44271958,
            0.36661197,
            0.29791931,
            0.57524743,
        ],
        [
            0.43329599,
            0.59033738,
            0.53409583,
            0.42928873,
        ],
        [
            0.59153599,
            0.35249563,
            0.38405557,
            0.29857569,
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
    ],
    [
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
        [
            0.4268005,
            0.57650756,
            0.76955664,
            0.49279255,
        ],
        [
            0.71737489,
            0.90890458,
            0.7274925,
            0.72024403,
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
        ],
    ],
]


def randfloat():
    return np.random.rand()


class QTable(DefaultMainVoiceScene):
    def construct(self):
        grid = Grid()
        self.add(grid.group)

        table = Q(RANDOM_TABLE)

        table_m: MobjectTable = table.get_qtable()

        table_m.get_vertical_lines().set_opacity(0)
        table_m.get_horizontal_lines().set_opacity(0)

        table_m.scale_to_fit_height(grid.group.get_height())
        table_m.scale_to_fit_width(grid.group.get_width())

        with self.voiceover(Text_Helper.get_text("QTabble", "start")) as tracker:
            time = tracker.duration

            self.play(
                *[GrowArrow(t) for row in table.objects for g in row for t in g],
                run_time=time / 3
            )
            self.wait(2 * time / 3)

        with self.voiceover(Text_Helper.get_text("QTabble", "richtig")) as tracker:
            time = tracker.duration
            table.blink_highest(self, 1.5, time=time, blinks=int(time))
