from manim import (  # DOWN,; IN,; OUT,; RIGHT,; Create,; FadeIn,; FadeOut,; Arrow3D,; VGroup,; Wait,
    DOWN,
    LEFT,
    RIGHT,
    UP,
    Circle,
    Create,
    Line,
    MathTex,
    Square,
    Text,
    Transform,
    Triangle,
    VGroup,
    Write,
)

from ai101_video.default_voice_scene import DefaultMainVoiceScene
from ai101_video.text_helper import Text_Helper

MANIM_GREEN = "#87c2a5"
MANIM_BLUE = "#525893"
MANIM_RED = "#e07a5f"
MAINM_BLACK = "#343434"


def get_nn_image() -> VGroup:
    node_radius = 0.5
    node_color = MANIM_GREEN
    h_space = 2.5
    v_space = 1.5

    nodes = [
        [Circle(radius=node_radius, color=node_color).shift(UP * 2 * v_space)],
        [
            Circle(radius=node_radius, color=node_color).shift(
                LEFT * h_space + UP * 1 * v_space
            ),
            Circle(radius=node_radius, color=node_color).shift(UP * 1 * v_space),
            Circle(radius=node_radius, color=node_color).shift(
                RIGHT * 1 * h_space + UP * 1 * v_space
            ),
        ],
        [
            Circle(radius=node_radius, color=node_color).shift(LEFT * 1 * h_space),
            Circle(radius=node_radius, color=node_color),
            Circle(radius=node_radius, color=node_color).shift(RIGHT * 1 * h_space),
        ],
        [Circle(radius=node_radius, color=node_color).shift(DOWN * 1 * v_space)],
    ]
    lines = []

    for prev_idx, layer in enumerate(nodes[1:]):
        for this_node in layer:
            for prev_node in nodes[prev_idx]:
                lines.append(
                    Line(
                        prev_node.get_center(),
                        this_node.get_center(),
                        buff=node_radius,
                        color=MANIM_RED,
                    )
                )

    return VGroup(*[n for layers in nodes for n in layers], *lines)


def get_manim_logo() -> VGroup:
    ds_m = MathTex(r"\mathbb{M}", fill_color=MAINM_BLACK).scale(7)
    ds_m.shift(2.25 * LEFT + 1.5 * UP)
    circle = Circle(color=MANIM_GREEN, fill_opacity=1).shift(LEFT)
    square = Square(color=MANIM_BLUE, fill_opacity=1).shift(UP)
    triangle = Triangle(color=MANIM_RED, fill_opacity=1).shift(RIGHT)
    logo = VGroup(triangle, square, circle, ds_m)  # order matters
    return logo


class Abschluss(DefaultMainVoiceScene):
    def construct(self):
        with self.voiceover(Text_Helper.get_text("End", "NN")) as tracker:
            time = tracker.duration
            nn_image = get_nn_image()
            self.play(Create(nn_image), run_time=time)

        with self.voiceover(Text_Helper.get_text("End", "ending")) as tracker:
            time = tracker.duration
            text = Text(
                Text_Helper.get_text("End", "ending_text"),
                gradient=(MANIM_GREEN, MANIM_BLUE, MANIM_RED),
                font_size=60,
            ).to_edge(UP)
            manim_logo = get_manim_logo().to_corner(DOWN + RIGHT)
            text_made_with = Text("Made with", font_size=20).move_to(
                manim_logo.get_edge_center(LEFT) + LEFT * 1.5
            )

            self.play(
                Create(text),
                Transform(nn_image, manim_logo),
                Write(text_made_with),
            )

            self.wait(time - 1)
