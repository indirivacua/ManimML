from manim import *

# This changes the resolution of our rendered videos
config.pixel_height = 700
config.pixel_width = 1900
config.frame_height = 25.0
config.frame_width = 25.0

class MatrixScene(Scene):
    def construct(self):
        # Define the kernel and input matrices
        x = [[r"\frac{\partial E}{\partial y_{11}}", r" \frac{\partial E}{\partial y_{12}}" ],
             [r"\frac{\partial E}{\partial y_{21}}", r"\frac{\partial E}{\partial y_{22}}"]]
        w = [[r"w_{22}", r"w_{21}"],
             [r"w_{12}", r"w_{11}"]]
        result = [[r"\frac{\partial E}{\partial x_{11}}",r"\frac{\partial E}{\partial x_{12}}",r"\frac{\partial E}{\partial x_{13}}"],
                  [r"\frac{\partial E}{\partial x_{21}}",r"\frac{\partial E}{\partial x_{22}}",r"\frac{\partial E}{\partial x_{23}}"],
                  [r"\frac{\partial E}{\partial x_{31}}",r"\frac{\partial E}{\partial x_{32}}",r"\frac{\partial E}{\partial x_{33}}"]]
        #https://stackoverflow.com/a/6473724/11975664
        result = list(map(list, zip(*result)))

        distance = 4

        conv_matrix = VGroup(*[
            Square().set_fill(DARK_BLUE, opacity=0.5).move_to([i*2 - 1, j*2 - 1, 0])
            for i in range(3) for j in range(3)
        ]).move_to(RIGHT * distance)

        matrix_2x2_input = VGroup(*[
            Square().set_fill(DARK_BLUE, opacity=0.5).move_to([i*2 - 2, j*2 - 2, 0])
            for i in range(2) for j in range(2)
        ]).move_to(LEFT * distance)

        matrix_2x2_filter = VGroup(*[
            Square().set_fill(RED, opacity=0.8).move_to([i*2 - 1, j*2 - 1, 0])
            for i in range(2) for j in range(2)
        ]).move_to(LEFT * distance)

        # Add text to the squares
        for i in range(2):
            for j in range(2):
                matrix_2x2_input.add(MathTex(str(x[i][j])).scale(1).move_to(np.array([-distance-1,1,0]) + np.array([j*2,-i*2,0])))

        for i in range(2):
            for j in range(2):
                matrix_2x2_filter.add(MathTex(str(w[i][j])).scale(1).move_to(np.array([-distance-1,1,0]) + np.array([j*2,-i*2,0])))

        # Animate the matrices
        self.play(*[Create(sq) for sq in conv_matrix], *[Create(sq) for sq in matrix_2x2_input])
        self.wait()

        xi=-distance
        yi=0
        # Animate the convolution
        for j in range(3):
            for i in range(3):
                self.play(matrix_2x2_filter.animate.move_to([xi-2+i*2, yi+2-j*2, 0]))
                self.add(MathTex(str(result[i][j])).scale(1).move_to(np.array([distance-1,1,0]) + np.array([i*2-1,-j*2+1,0])))
                self.wait()

        self.play(FadeOut(matrix_2x2_filter))

#manim -pql -i conv2d_backward.py