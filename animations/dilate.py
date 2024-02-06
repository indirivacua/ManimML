from manim import *

# This changes the resolution of our rendered videos
config.pixel_height = 900
config.pixel_width = 1900
config.frame_height = 25.0
config.frame_width = 25.0

class DilateMatrix(Scene):
    def construct(self):

        dEdy = [[r"\frac{\partial E}{\partial "+"y_{}".format("{"+f"{i+1}{j+1}"+"}")+"}" for i in range(2)] for j in range(2)]
        dEdy = list(map(list, zip(*dEdy))) #transpose

        dilate_text=[["0" for _ in range(3)] for _ in range(3)]

        filter_matrix = VGroup(*[
            Square().set_fill(DARK_BLUE, opacity=1)
            for i in range(2) for j in range(2)
        ]).arrange_in_grid(2, 2, buff=0.0)

        self.play(Create(filter_matrix))

        for i in range(2):
            for j in range(2):
                eq = MathTex(str(dEdy[i][j]))
                eq = eq.scale(1)
                eq.set_color_by_tex("x", BLACK)
                filter_matrix[2*i+j].add(eq.move_to(np.array([-1,1,0]) + np.array([j*2,-i*2,0])))

        self.wait()

        self.play(filter_matrix.animate.arrange_in_grid(2, 2, buff=2))

        dilate_matrix = VGroup(*[
            Square().set_fill(GRAY, opacity=1)
            for i in range(3) for j in range(3)
        ]).arrange_in_grid(3, 3, buff=0.0)
        
        for i in range(3):
            for j in range(3):
                eq = MathTex(str(dilate_text[i][j]))
                eq = eq.scale(1)
                eq.set_color_by_tex("x", BLACK)
                dilate_matrix[3*i+j].add(eq.move_to(np.array([-2,2,0]) + np.array([j*2,-i*2,0])))

        #https://stackoverflow.com/a/69668382/189270
        dilate_matrix.set_z_index(filter_matrix.z_index-1) #send to the back

        self.play(Create(dilate_matrix))

        dots = VGroup(*[
            Dot(np.array([-1,4,0])),
            Dot(np.array([1,4,0]))
        ])
        # dots.arrange_in_grid(buff=1)
        self.add(dots)
        l= Line(dots[0], dots[1])
        self.play(Create(l))

        tex = Tex(r'dilation=S-1', color=WHITE, font_size=48)
        self.add(tex.move_to(np.array([0,5,0])))

        self.wait()

#manim -pql -i dilate.py