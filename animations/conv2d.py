from manim import *

# This changes the resolution of our rendered videos
config.pixel_height = 700
config.pixel_width = 1900
config.frame_height = 25.0
config.frame_width = 25.0

class MatrixScene(Scene):
    def construct(self):
        # Define the kernel and input matrices
        w = np.array([[1, 0, 1],
              [0, 1, 0],
              [1, 0, 1]
             ])
        x = np.array ([[1,1,1,0,0],
               [0,1,1,1,0],
               [0,0,1,1,1],
               [0,0,1,1,0],
               [0,1,1,0,0]
              ])
        
        distance = 4

        # Create the 3x3 convolution matrix
        conv_matrix = VGroup(*[
            Square().set_fill(DARK_BLUE, opacity=0.5).move_to([i - 1, j - 1, 0])
            for i in range(2) for j in range(2)
        ]).move_to(RIGHT * distance)

        # Create the 5x5 matrix
        matrix_5x5 = VGroup(*[
            Square().set_fill(DARK_BLUE, opacity=0.5).move_to([i - 2, j - 2, 0])
            for i in range(4) for j in range(4)
        ]).move_to(LEFT * distance)

        # Create the 3x3 matrix
        matrix_3x3 = VGroup(*[
            Square().set_fill(RED, opacity=0.8).move_to([i - 1, j - 1, 0])
            for i in range(2) for j in range(2)
        ]).move_to(LEFT * distance)

        # Add text to the squares
        for i in range(5):
            for j in range(5):
                matrix_5x5.add(Text(str(x[i,j])).scale(0.5).move_to(np.array([-distance-2,2,0]) + np.array([j,-i,0])))

        for i in range(3):
            for j in range(3):
                matrix_3x3.add(Text(str(w[i,j])).scale(0.5).move_to(np.array([-distance-1,1,0]) + np.array([j,-i,0])))

        # Animate the matrices
        self.play(*[Create(sq) for sq in conv_matrix], *[Create(sq) for sq in matrix_5x5])
        self.wait()

        xi=-distance
        yi=0
        # Animate the convolution
        for j in range(3):
            for i in range(3):
                self.play(matrix_3x3.animate.move_to([xi-1+i, yi+1-j, 0]))
                result=np.sum(x[j:j+w.shape[0], i:i+w.shape[1]] * w)
                self.add(Text(str(result)).scale(0.5).move_to(np.array([distance-1,1,0]) + np.array([i,-j,0])))
                self.wait()

        self.play(FadeOut(matrix_3x3))

#manim -pql -i conv2d.py