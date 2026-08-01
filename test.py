from manim import *

class Pith(Scene):
    def construct(self):

        sq = Square(side_length=5).set_stroke(color=GREEN).set_fill(BLUE, opacity=0.75)

        self.play(Create(sq), run_time=3)
        self.wait()
