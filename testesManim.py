from manim import *

class Transforms(Scene):
    def construct(self):
        quadrado = Square(color=GREEN, fill_opacity = 0.5)
        self.play(DrawBorderThenFill(quadrado))
        circulo = Circle(color= GREEN, fill_opacity = 0.5)
        self.play(ReplacementTransform(quadrado, circulo))
        self.wait(2)
        self.play(Indicate(circulo))
        self.play(FadeOut(circulo))

class Posicionando(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        red_dot = Dot(color=RED)
        self.add(red_dot)

        #next to
        blue_dot = Dot(color= BLUE)
        blue_dot.next_to(red_dot, RIGHT)
        self.add(blue_dot)

        #shift
        orange_dot = Dot(color = ORANGE)
        orange_dot.shift(RIGHT*2)
        self.add(orange_dot)

        # move_to 
            #purple_dot = Dot(color=PURPLE)
            # self.add(purple_dot)
            # self.play(purple_dot.animate.move_to([1,1,0]))
            # self.wait(1)
            # self.play(purple_dot.animate.move_to([1,-1,0]))
            # self.wait(1)
            # self.play(purple_dot.animate.move_to([-1,-1,0]))
            # self.wait(1)
            # self.play(purple_dot.animate.move_to([-1,1,0]))
            # self.wait(1)
        #move to pode ser usado sem animação:
        white_dot = Dot(color=WHITE)
        white_dot.move_to([0,1,0])
        self.add(white_dot)
   
        #align to
        white_circle = Circle(color = WHITE)
        white_circle.align_to(blue_dot, RIGHT)
        self.add(white_circle)

class PontosCriticos(Scene):
    def construct(self):
        c = Circle(color=WHITE, fill_opacity=0.5)
        self.add(c)

        for d in [[0,0,0], UP, UR, RIGHT, DR, DOWN, DL, LEFT, UL]:
            self.add(Dot().move_to(c.get_critical_point(d)))

        q = Square(color= WHITE, fill_opacity = 0.5)
        q.move_to([1,0,0],aligned_edge=LEFT)
        self.add(q)

from manim.utils.unit import Percent

class UsandoUnidades(Scene):
    def construct(self):
        for porcentagem in range(1,100,5):
            # circulo = Circle(radius=porcentagem * Percent(X_AXIS))
            # circulo.move_to([porcentagem/10,0,0])
            # self.add(circulo)
            circulo_branco = Circle(radius = porcentagem * Percent(Y_AXIS), color= WHITE) #X_AXIS e Y_AXIS são constantes, é possível usar qualquer outro número
            self.play(Create(circulo_branco))
            circulo_cinza = Circle(radius = (porcentagem * Percent(X_AXIS)), color= GRAY)
            self.play(Create(circulo_cinza))
            
