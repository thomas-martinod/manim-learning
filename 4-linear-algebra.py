from manim import *
import random

class Vectors(VectorScene):
    def construct(self):
        plane = self.add_plane(animate=True). add_coordinates()
        vec = self.add_vector([-3, 2], color = BLUE_C)

        basis = self.get_basis_vectors()
        self.add(basis)
        self.vector_to_coords(vector=vec)

        vec2 = self.add_vector([2,2])
        self.write_vector_coordinates(vector=vec2)


class Matrix(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(self, show_coordinates=True, leave_ghost_vectors=True,
                                           show_basis_vectors=True)
    
    def construct(self):
        matrix = [[1, 2], [2, 1]]
        matrix_tex = MathTex("A = \\begin{bmatrix} 1 & 2 \\\ 2 & 1 \\end{bmatrix}").to_edge(UL).add_background_rectangle()

        unit_square = self.get_unit_square()
        text = always_redraw(lambda : Tex("Det(A)").set(width=0.7).move_to(unit_square.get_center()))

        vec = self.get_vector([1, -2], color = PURPLE_B)

        rect1 = Rectangle(height=2, width=1, stroke_color=BLUE_A, fill_color=BLUE_D,
                          fill_opacity=0.6).shift(UP*2 + LEFT*2)
        
        circ1 = Circle(radius=1, stroke_color=BLUE_A, fill_color=BLUE_D, fill_opacity=0.6).shift(DOWN*2 + RIGHT*1)

        self.add_transformable_mobject(vec, unit_square, rect1, circ1)
        self.add_background_mobject(matrix_tex)
        self.add_foreground_mobject(text)
        self.apply_matrix(matrix)

        self.wait()


class AddingVectors(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-5,5,1], y_range=[-4,4,1], x_length=10, y_length=7)
        plane.add_coordinates()
        plane.shift(RIGHT * 2)

        Vec1 = Line(start=plane.coords_to_point(0,0), end=plane.coords_to_point(3,2), stroke_color=YELLOW).add_tip()
        Vec1_label = MathTex(r"\\vec{v}").next_to(Vec1, RIGHT, buff=0.1).set_color(YELLOW)

        Vec2 = Line(start=plane.coords_to_point(0,0), end=plane.coords_to_point(-2,1), stroke_color=RED).add_tip()
        Vec2_label = MathTex(r"\\vec{w}").next_to(Vec2, LEFT, buff=0.1).set_color(RED)

        Vec3 = Line(start=plane.coords_to_point(3,2), end=plane.coords_to_point(-2,1), stroke_color=RED).add_tip()

        Vec4 = Line(start=plane.coords_to_point(0,0), end=plane.coords_to_point(1,3), stroke_color=GREEN).add_tip()
        Vec4_label = MathTex(r"\\vec{v} + \\vec{w}").next_to(Vec4, LEFT, buff=0.1).set_color(YELLOW)

        stuff = VGroup(plane, Vec1, Vec1_label, Vec2, Vec2_label, Vec3, Vec4, Vec4_label)
        box = RoundedRectangle(height = 1.5, width = 1.5, corner_radius=0.1, stroke_color=PINK).toedge(DL)

        self.play(DrawBorderThenFill(plane), run_time=2)
        self.wait()
        self.play(GrowFromPoint(Vec1, point=Vec1.get_start()), Write(Vec1_label), run_time = 2)