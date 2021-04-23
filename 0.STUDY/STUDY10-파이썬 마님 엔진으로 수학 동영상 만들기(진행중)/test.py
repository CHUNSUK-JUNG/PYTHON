from manim import *

class CoordinateEx2(Scene):
    def construct(self):
        dot = Dot()

        dot.to_edge(LEFT)
        self.add(dot)
        self.wait()

        for i in range(0,5):
            self.move_dot(dot)


    def move_dot(self, dot):
        d1 = dot.copy()
        d2 = dot.copy()
        d3 = dot.copy()

        self.play(
            d1.to_corner, UR,
            d2.to_edge, RIGHT,
            d3.to_corner, DR,
        )
        self.remove(d1, d2, d3)