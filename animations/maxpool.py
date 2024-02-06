from manim import *

# This changes the resolution of our rendered videos
config.pixel_height = 500
config.pixel_width = 1900
config.frame_height = 30.0
config.frame_width = 50.0

class MaxPoolMatrix(Scene):
    def construct(self):

        dEdx = [[0,r"\frac{\partial E}{\partial "+"y_{}".format("{"+"11"+"}")+"}",0,0],
                [0,0,r"\frac{\partial E}{\partial "+"y_{}".format("{"+"12"+"}")+"}",0],
                [r"\frac{\partial E}{\partial "+"y_{}".format("{"+"21"+"}")+"}",0,0,r"\frac{\partial E}{\partial "+"y_{}".format("{"+"22"+"}")+"}"],
                [0,0,0,0]]
        
        dEdy = [[r"\frac{\partial E}{\partial "+"y_{}".format("{"+f"{i+1}{j+1}"+"}")+"}" for j in range(2)] for i in range(2)]

        dist = 10

        matrix_1 = VGroup(*[
            Square().set_fill(DARK_BLUE, opacity=1)
            for i in range(2) for j in range(2)
        ]).arrange_in_grid(2, 2, buff=0.0).move_to((LEFT + UP)*2+LEFT*dist)

        matrix_2 = VGroup(*[
            Square().set_fill(GOLD, opacity=1)
            for i in range(2) for j in range(2)
        ]).arrange_in_grid(2, 2, buff=0.0).move_to((RIGHT + UP)*2+LEFT*dist)

        matrix_3 = VGroup(*[
            Square().set_fill(RED, opacity=1)
            for i in range(2) for j in range(2)
        ]).arrange_in_grid(2, 2, buff=0.0).move_to((LEFT - UP)*2+LEFT*dist)

        matrix_4 = VGroup(*[
            Square().set_fill(GREEN, opacity=1)
            for i in range(2) for j in range(2)
        ]).arrange_in_grid(2, 2, buff=0.0).move_to((RIGHT - UP)*2+LEFT*dist)

        # 

        dist2 = 0

        result_1 = VGroup(*[
            Square().set_fill(DARK_BLUE, opacity=1)
            for i in range(1) for j in range(1)
        ]).arrange_in_grid(2, 2, buff=0.0).move_to((LEFT + UP)+RIGHT*dist2)

        result_2 = VGroup(*[
            Square().set_fill(GOLD, opacity=1)
            for i in range(1) for j in range(1)
        ]).arrange_in_grid(2, 2, buff=0.0).move_to((RIGHT + UP)+RIGHT*dist2)

        result_3 = VGroup(*[
            Square().set_fill(RED, opacity=1)
            for i in range(1) for j in range(1)
        ]).arrange_in_grid(2, 2, buff=0.0).move_to((LEFT - UP)+RIGHT*dist2)

        result_4 = VGroup(*[
            Square().set_fill(GREEN, opacity=1)
            for i in range(1) for j in range(1)
        ]).arrange_in_grid(2, 2, buff=0.0).move_to((RIGHT - UP)+RIGHT*dist2)

        self.add(matrix_1, matrix_2, matrix_3, matrix_4)
        self.add(result_1, result_2, result_3, result_4)

        # text for big matrix
        tex_matrix = MathTex(r"\frac{\partial E}{\partial x}", color=WHITE, font_size=48)
        tex_matrix.move_to(UP*5+LEFT*dist)
        self.add(tex_matrix)
        for i in range(4):
            for j in range(4):
                eq = MathTex(str(dEdx[i][j]))
                eq = eq.scale(1)
                # eq.set_color_by_tex("x", BLACK)
                self.add(eq.move_to(np.array([-dist-3,3,0]) + np.array([j*2,-i*2,0])))

        # text for small matrix
        tex_matrix = MathTex(r"\frac{\partial E}{\partial y}", color=WHITE, font_size=48)
        tex_matrix.move_to(UP*3+LEFT*dist2)
        self.add(tex_matrix)
        for i in range(2):
            for j in range(2):
                eq = MathTex(str(dEdy[i][j]))
                eq = eq.scale(1)
                # eq.set_color_by_tex("x", BLACK)
                self.add(eq.move_to(np.array([-dist2-1,1,0]) + np.array([j*2,-i*2,0])))

        # eq text
        eqs = [r"y_{11} = \max ( x_{11},x_{12},x_{21},x_{22} )=x_{12}",
        r"y_{12} = \max ( x_{13},x_{14},x_{23},x_{24} )=x_{23}",
        r"y_{21} = \max ( x_{31},x_{32},x_{41},x_{42} )=x_{31}",
        r"y_{22} = \max ( x_{33},x_{34},x_{43},x_{44} )=x_{34}"]
        for i,eq in enumerate(eqs):
            eq = MathTex(eq)
            eq = eq.scale(2)
            self.add(eq.move_to(np.array([-dist2+dist+3,3,0]) + np.array([0,-i*2,0])))
            


#manim -pql -i maxpool.py