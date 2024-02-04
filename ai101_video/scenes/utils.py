from manim import (
    OUT,
    RESAMPLING_ALGORITHMS,
    Group,
    ImageMobject,
    Transform,
    rate_functions,
)
from manim.typing import Point3D, Vector3


def img(path: str) -> ImageMobject:
    i = ImageMobject(path)
    i.set_resampling_algorithm(RESAMPLING_ALGORITHMS["nearest"])
    return i


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
        func=rate_functions.ease_in_sine,
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

        for e in self.elfs.values():
            if e == self.active_elve and play:
                self.scene.play(
                    self.elfs[direction].animate.move_to(
                        coordinates + (OUT * e.get_z())
                    ),
                    run_time=time,
                    rate_func=func,
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
