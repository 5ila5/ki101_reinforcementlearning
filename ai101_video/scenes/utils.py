from manim import Group, ImageMobject, rate_functions
from manim.typing import Point3D, Vector3


class Elfs:
    def __init__(self, scene):
        self.scene = scene
        self.elfs = {
            "down": ImageMobject("assets/elf_down.png"),
            "left": ImageMobject("assets/elf_left.png"),
            "right": ImageMobject("assets/elf_right.png"),
            "up": ImageMobject("assets/elf_up.png"),
        }

        self.active_elve = self.elfs["down"]
        self.grid: Grid = None

    def scale(self, scale: float):
        for e in self.elfs.values():
            e.scale(scale)
        return self

    def reskin(self, direction: str):
        if self.elfs[direction] != self.active_elve:
            self.scene.remove(self.active_elve)
            self.active_elve = self.elfs[direction]
            self.scene.add(self.active_elve)

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
        if self.grid is None:
            raise Exception("Grid not set")
        if coordinates is None:
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
                    self.elfs[direction].animate.move_to(coordinates),
                    run_time=time,
                    rate_func=func,
                )
            else:
                e.move_to(coordinates)

    def remove(self):
        self.scene.remove(self.active_elve)


class Grid:
    def __init__(self):
        self.env = [
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
        self.count = 16
        for row in self.env:
            for col in row:
                col.scale(6)

        self.group = Group(*[e for row in self.env for e in row]).arrange_in_grid(
            4, 4, buff=0.1
        )
        self.animate = self.group.animate

    def get_center(self) -> list[list[Point3D]]:
        return [[e.get_center() for e in row] for row in self.env]

    def get_edge_center(self, direction: Vector3) -> list[list[Point3D]]:
        return [[e.get_edge_center(direction) for e in row] for row in self.env]

    def add_stool(self):
        self.stool = (
            ImageMobject("assets/stool.png").move_to(self.get_center()[0][0]).scale(6)
        )
        self.group.add(self.stool)

    def add_present(self):
        self.present = (
            ImageMobject("assets/goal.png").move_to(self.get_center()[3][3]).scale(6)
        )
        self.group.add(self.present)

    def add_elfs(self, elfs: Elfs):
        for e in elfs.elfs.values():
            e.scale(6).move_to(self.env[0][0].get_center())
        elfs.grid = self
