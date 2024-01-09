from manim import *
import numpy as np

class Funcao1(Scene):
    def construct(self):
        ax = Axes(x_range= (-10, 10), y_range= (-10,10))
        funcao = lambda x: (x-3)+pow(x,3)/2
        curva = ax.plot(funcao, color = GREEN, x_range=[-2.5,2.5])
        area = ax.get_area(curva, x_range=(-2,0))
        self.play(Create(ax, run_time = 2), Create(curva, run_time = 3))
        self.wait(1)
        self.play(Create(area))
        self.wait(1)
        valor_area = np.trapz([funcao(x) for x in np.arange(-2, 0, 0.01)], dx=0.01)  # Corrigido
        texto = MathTex(f"Resultado =  {valor_area}").next_to(ax,DOWN)
        texto_funcao = MathTex(r"\int_{-2}^{0} (x-3)+\frac{x^3}{2} dx").next_to(ax, UP).shift(DOWN*0.5)
        self.play(Create(texto),Create(texto_funcao))
        self.wait(6)

class Funcao2(Scene):
    def construct(self):
        ax = Axes(x_range= (-10, 10), y_range= (-1,1))
        funcao = lambda x: np.sin(x)
        curva = ax.plot(funcao, color = GREEN, x_range=[-2*np.pi,2*np.pi])
        area = ax.get_area(curva, x_range=(-np.pi,0))
        self.play(Create(ax, run_time = 2), Create(curva, run_time = 3))
        self.wait(1)
        self.play(Create(area))
        self.wait(1)
        valor_area = np.trapz([funcao(x) for x in np.arange(-np.pi, 0, 0.01)], dx=0.01)
        texto = MathTex(f"Aprox =  {valor_area}").next_to(ax,DOWN)
        texto_funcao = MathTex(r"\int_{-\pi}^{0} \sin(x) dx").next_to(ax, UP).shift(DOWN*0.5)
        self.play(Create(texto),Create(texto_funcao))
        self.wait(6)