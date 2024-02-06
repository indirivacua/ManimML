from manim import *

from manim_ml.neural_network import Convolutional2DLayer, FeedForwardLayer, NeuralNetwork

# This changes the resolution of our rendered videos
config.pixel_height = 700
config.pixel_width = 1900
config.frame_height = 7.0
config.frame_width = 7.0

# Here we define our basic scene
class BasicScene(ThreeDScene):

    # The code for generating our scene goes here
    def construct(self):
        # Make the neural network
        nn = NeuralNetwork([
                Convolutional2DLayer(1, 7, 3, show_grid_lines=True, stride=2),
                Convolutional2DLayer(1, 3, 3, show_grid_lines=True, cell_width=0.4),
            ],
            layer_spacing=1.25,
        )
        # Center the neural network
        nn.move_to(ORIGIN)
        self.add(nn)
        # Make a forward pass animation
        forward_pass = nn.make_forward_pass_animation()
        # Play animation
        self.play(forward_pass, run_time=5)

#manim -pql -i strides.py