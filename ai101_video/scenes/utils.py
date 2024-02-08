from manim import (
    DOWN,
    LEFT,
    OUT,
    RESAMPLING_ALGORITHMS,
    RIGHT,
    UP,
    AnimationGroup,
    Group,
    ImageMobject,
    LabeledArrow,
    MobjectTable,
    ParsableManimColor,
    Scene,
    Transform,
    VGroup,
)
from manim.typing import Point3D, Vector3


def img(path: str) -> ImageMobject:
    i = ImageMobject(path)
    i.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
    return i


class QTable:
    def __init__(
        self,
        values: list[list[list[float | int]]],
        arrow_scale: float = 2,
        arrow_color: ParsableManimColor = "green",
        lable_color: ParsableManimColor = "green",
        frame_fill_color: ParsableManimColor = "black",
        frame_fill_opacity: float = 1,
    ):
        self.values = values
        self.arrow_scale = arrow_scale
        self.arrow_color = arrow_color
        self.l_color, self.r_color, self.u_color, self.d_color = (
            arrow_color for _ in range(4)
        )
        self.lable_color = lable_color
        self.frame_fill_color = frame_fill_color
        self.frame_fill_opacity = frame_fill_opacity

    def label(self, value: float):
        return f"{value:.2f}"

    def get_qtable(self) -> MobjectTable:
        self.objects: list[list[VGroup]] = []
        for row in self.values:
            objects_row = []
            for cell in row:
                if len(cell) != 4:
                    raise Exception("only 4 actions are supported")
                arrows = [
                    LabeledArrow(
                        self.label(cell[0]),
                        start=0.1 * RIGHT,
                        end=LEFT * self.arrow_scale,
                        color=self.l_color,
                        label_frame=False,
                        label_color=self.lable_color,
                        frame_fill_color=self.frame_fill_color,
                        frame_fill_opacity=self.frame_fill_opacity,
                    ),
                    LabeledArrow(
                        self.label(cell[1]),
                        start=0.1 * UP,
                        end=DOWN * self.arrow_scale,
                        color=self.r_color,
                        label_frame=False,
                        label_color=self.lable_color,
                        frame_fill_color=self.frame_fill_color,
                        frame_fill_opacity=self.frame_fill_opacity,
                    ),
                    LabeledArrow(
                        self.label(cell[2]),
                        start=0.1 * LEFT,
                        end=RIGHT * self.arrow_scale,
                        color=self.u_color,
                        label_frame=False,
                        label_color=self.lable_color,
                        frame_fill_color=self.frame_fill_color,
                        frame_fill_opacity=self.frame_fill_opacity,
                    ),
                    LabeledArrow(
                        self.label(cell[3]),
                        start=0.1 * DOWN,
                        end=UP * self.arrow_scale,
                        color=self.d_color,
                        label_frame=False,
                        label_color=self.lable_color,
                        frame_fill_color=self.frame_fill_color,
                        frame_fill_opacity=self.frame_fill_opacity,
                    ),
                ]
                Vgroup = VGroup(*arrows)
                objects_row.append(Vgroup)
                # labels = [Text(f"{cell[0]:.2f}"), Text(f"{cell[1]:.2f}"), Text(f"{cell[2]:.2f}"), Text(f"{cell[3]:.2f}")]
            self.objects.append(objects_row)

        self.table = MobjectTable(
            self.objects, v_buff=0.8, h_buff=0.8, include_outer_lines=True
        ).scale(0.4)

        self.table.z_index = 1
        return self.table

    def get_best_arrow(self, f=max, ignore=lambda b: b == 0) -> list[LabeledArrow]:
        best_arrows = []
        for row_idx, row in enumerate(self.values):
            for cell_idx, cell in enumerate(row):
                best_action = f(cell)
                if ignore(best_action):
                    continue
                best_action_index = cell.index(best_action)
                best_arrow = self.objects[row_idx][cell_idx].submobjects[
                    best_action_index
                ]
                best_arrows.append(best_arrow)
        return best_arrows

    def blink_highest(self, scene: Scene, scale: float = 1, time=1, blinks=2, f=max):
        best_arrows = self.get_best_arrow(f)
        time_part = time / (blinks * 2)
        for _ in range(blinks):
            scene.play(
                *[arrow.animate.scale(scale) for arrow in best_arrows],
                run_time=time_part,
            )
            scene.play(
                *[arrow.animate.scale(1 / scale) for arrow in best_arrows],
                run_time=time_part,
            )


class Elfs:
    def __init__(self, scene, z_index=0):
        self.scene = scene
        self.elfs = {
            "down": img("assets/elf_down.png"),
            "left": img("assets/elf_left.png"),
            "right": img("assets/elf_right.png"),
            "up": img("assets/elf_up.png"),
        }
        for e in self.elfs.values():
            e.z_index = z_index

        self.active_elve = self.elfs["down"]
        self.grid: Grid = None

    def scale(self, scale: float):
        for e in self.elfs.values():
            e.scale(scale)
        return self

    def reskin(self, direction: str, force=False):
        if self.elfs[direction] != self.active_elve or force:
            self.scene.remove(self.active_elve)
            self.active_elve = self.elfs[direction]
            self.scene.add(self.active_elve)

    def reskin_transform(self, direction: str, time: float):
        self.scene.play(Transform(self.active_elve, self.elfs[direction]))
        self.active_elve = self.elfs[direction]

    def move(
        self,
        direction: str,
        coordinates: Point3D = None,
        x: float | None = None,
        y: float | None = None,
        time=1,
        play=True,
        func=None,
        add_animation=[],
    ):
        if coordinates is None:
            if self.grid is None:
                raise Exception("Grid not set")
            if x is None or y is None:
                raise Exception("Either coordinates or x and y must be provided")
            if x >= len(self.grid.env) or y >= len(self.grid.env[0]):
                raise Exception(f"Coordinates ({x}, {y}) out of bounds")
            coordinates = coordinates or self.grid.env[x][y].get_center()
        direction = direction.lower()
        if direction not in self.elfs:
            raise Exception(f"Direction {direction} not in {self.elfs.keys()}")

        self.reskin(direction)

        args = {
            "run_time": time,
        }
        if func is not None:
            args["rate_func"] = func

        for e in self.elfs.values():
            if e == self.active_elve and play:
                self.scene.play(
                    AnimationGroup(
                        self.elfs[direction]
                        .animate.move_to(coordinates + (OUT * e.get_z()))
                        .set_run_time(time),
                        *add_animation,
                        **args,
                    )
                )

            else:
                e.move_to(coordinates + (OUT * e.get_z()))

    def remove(self):
        self.scene.remove(self.active_elve)

    def add_after_remove(self):
        self.scene.add(self.active_elve)

    def center(self):
        for e in self.elfs.values():
            e.center()

    def to_edge(self, edge: Vector3):
        for e in self.elfs.values():
            e.to_edge(edge)


class Grid:
    def __init__(self):
        self.env = [
            [
                img("assets/ice.png"),
                img("assets/ice.png"),
                img("assets/ice.png"),
                img("assets/ice.png"),
            ],
            [
                img("assets/ice.png"),
                img("assets/cracked_hole.png"),
                img("assets/ice.png"),
                img("assets/cracked_hole.png"),
            ],
            [
                img("assets/ice.png"),
                img("assets/ice.png"),
                img("assets/ice.png"),
                img("assets/cracked_hole.png"),
            ],
            [
                img("assets/cracked_hole.png"),
                img("assets/ice.png"),
                img("assets/ice.png"),
                img("assets/ice.png"),
            ],
        ]
        self.count = 16
        for row in self.env:
            for col in row:
                col.scale(6).z_index = 0

        self.group = Group(*[e for row in self.env for e in row]).arrange_in_grid(
            4, 4, buff=0.1
        )
        self.animate = self.group.animate

    def get_center(self) -> list[list[Point3D]]:
        return [[e.get_center() for e in row] for row in self.env]

    def get_edge_center(self, direction: Vector3) -> list[list[Point3D]]:
        return [[e.get_edge_center(direction) for e in row] for row in self.env]

    def add_stool(self):
        self.stool = img("assets/stool.png").move_to(self.get_center()[0][0]).scale(6)
        self.group.add(self.stool)

    def add_present(self):
        self.present = img("assets/goal.png").move_to(self.get_center()[3][3]).scale(6)
        self.group.add(self.present)

    def add_elfs(self, elfs: Elfs, scale=6):
        for e in elfs.elfs.values():
            e.scale(scale).move_to(self.env[0][0].get_center() + OUT * e.get_z())
        elfs.grid = self
