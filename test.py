from manim import *

class Ola(Scene):
    def construct(self):
        texto = Text("Olá, Manim!")
        self.play(Write(texto))
        self.wait()

# no terminal
# manim -pqh teste.py Ola
