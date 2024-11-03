from manim import *
from ManimExtra import *
import sys
import math
import scipy.special

sys.setrecursionlimit(2000)

class Title(Scene):
    def construct(self):
        def snowflake(n=4, length=4, stroke_width=6, color=WHITE):
            x = VGroup(*[Koch_curve(n,length,stroke_width,color).rotate(i) for i in [0, PI / 3, -PI / 3]]
            ).arrange(RIGHT, buff=0, aligned_edge=DOWN)
            x[0].rotate(angle=PI, about_point=x[0].get_end())
            return x.move_to(ORIGIN)
        title = Tex("Fractals",font_size=120).to_edge(UP).shift(0.2*DOWN)
        triangle = Sierpinski_triangle(5).scale(1.4).shift(3*RIGHT).shift(DOWN)
        snowflake_1 = snowflake(color=BLUE).shift(3*LEFT).scale(1).shift(DOWN)
        self.add(title,triangle,snowflake_1)


class Koch(Scene):
    def construct(self):

        def snowflake(n=4, length=4, stroke_width=7.5, color=WHITE):
            x = VGroup(*[Koch_curve(n,length,stroke_width,color).rotate(i) for i in [0, PI / 3, -PI / 3]]
            ).arrange(RIGHT, buff=0, aligned_edge=DOWN)
            x[0].rotate(angle=PI, about_point=x[0].get_end())
            return x.move_to(ORIGIN)

        title = Tex("Fractals",font_size=120)
        self.play(Write(title),run_time=1.5)
        self.wait()
        self.play(FadeOut(title))
        self.wait(0.5)

        line = (Line(color=BLUE,stroke_width=7.5).set_length(9).move_to(ORIGIN).shift(np.array([0,-np.sin(PI/3)*9/6,0])).shift(DOWN))
        label = Tex('Build a line')
        self.play(Fancy_label(label))
        self.play(AnimationGroup(
            Create(line),
            FadeOut(label),
            lag_ratio=0.75
        ))

        label = Tex('Divide the line into 3 parts')
        self.play(Fancy_label(label))
        Dot_1 = Dot(line.get_start())
        Dot_2 = Dot(line.point_from_proportion(1/3))
        Dot_3 = Dot(line.point_from_proportion(2/3))
        Dot_4 = Dot(line.get_end())
        self.play(GrowFromCenter(Dot_1),
                  GrowFromCenter(Dot_2),
                  GrowFromCenter(Dot_3),
                  GrowFromCenter(Dot_4),
                  run_time=0.6)
        self.play(FadeOut(label))
        self.wait(0.5)

        line_1 = Line(Dot_1.get_center(),Dot_2.get_center(),color=BLUE,stroke_width=7.5).set_z_index(-1)
        line_2 = Line(Dot_2.get_center(),Dot_3.get_center(),color=BLUE,stroke_width=7.5).set_z_index(-1)
        line_3 = Line(Dot_3.get_center(),Dot_4.get_center(),color=BLUE,stroke_width=7.5).set_z_index(-1)
        self.remove(line)
        self.add(line_1,line_2,line_3)

        label = Tex("Let's build an equilateral triangle in the middle")
        self.play(Fancy_label(label))
        
        line_4 = line_2.copy().rotate(about_point=Dot_2.get_center(), angle=PI/3)
        line_5 = line_3.copy().rotate(about_point=Dot_3.get_center(), angle=2*PI/3)
        Dot_5 = Dot(Dot_1.get_center()).rotate(about_point=Dot_2.get_center(),angle=-2*PI/3)

        self.play(Create(line_4),Create(line_5),GrowFromCenter(Dot_5))
        self.play(FadeOut(label))

        label = Tex("Remove the middle of the line")
        self.play(Fancy_label(label))
        self.play(FadeOut(line_2),run_time=0.7)
        self.play(FadeOut(Dot_1),FadeOut(Dot_2),FadeOut(Dot_3),FadeOut(Dot_4),FadeOut(Dot_5))
        self.play(FadeOut(label))

        label = Tex("Let's repeat this several times")
        self.play(Fancy_label(label))
        self.remove(line_1,line_2,line_3,line_4,line_5)
        curve_1 = (Koch_curve(n=1,stroke_width=7.5,length=9,color=BLUE).shift(DOWN))
        self.add(curve_1)
        for i in range(2,7):
            self.play(
                curve_1.animate.become(Koch_curve(n=i, stroke_width=7.5-i,length=9,color=BLUE)).shift(DOWN))
            self.wait()
        self.play(FadeOut(label))

        label = Tex("This fractal is called the Koch curve")
        self.play(Fancy_label(label))
        self.play(FadeOut(label))

        label = Tex("The Koch curve is self-similar")
        self.play(Fancy_label(label))
        self.play(curve_1.animate.shift(2*UP))

        curve_size = Line(curve_1.get_start(),curve_1.get_end()).get_length()
        curve_2 = Koch_curve(n=5, stroke_width=1.5,length=9,color=BLUE).move_to(curve_1).set_stroke(opacity=0).shift(curve_size/3*LEFT).shift(0.7*DOWN).scale(0.33)
        self.play(curve_2.animate.shift(3.2*DOWN).set_stroke(opacity=1))
        self.wait()
        self.play(curve_2.animate.become(curve_1.copy().shift(3.2*DOWN)))
        self.play(curve_1.animate.shift(1.6*DOWN),curve_2.animate.shift(1.6*UP))
        self.wait(0.4)
        self.play(FadeOut(VGroup(curve_1,curve_2,label)))

        label = Tex("From such curves, you can make a Koch snowflake")
        a,b,c = snowflake(n=7,stroke_width=1.5,length=4,color=BLUE)
        self.play(Fancy_label(label))
        self.play(AnimationGroup(
            Create(a),
            Create(b),
            Create(c),
            lag_ratio=0.9, run_time=4
        ))
        self.wait()
        self.play(FadeOut(label),FadeOut(a),FadeOut(b),FadeOut(c))


class Dimension(Scene):
    def construct(self):
        label = Tex("The concept of dimension is often used for fractals")
        self.play(Fancy_label(label))
        self.wait(0.7)
        self.play(FadeOut(label))

        label = Tex("Let's define this concept using the formula")
        formula = MathTex(r"\mathrm{Copies\,=\,Scale^{Dimension}}", font_size=96)

        formula[0][0:6].set_color(RED)
        formula[0][7:12].set_color(GREEN)
        formula[0][12:].set_color(BLUE)

        self.play(Fancy_label(label))
        self.play(Write(formula))
        self.wait(1.8)
        self.play(FadeOut(label))

        label = Tex("The same, but in logarithmic form")
        self.play(Fancy_label(label))

        new_formula = MathTex(r"\mathrm{Dimension = \log_{Scale}Copies}", font_size=96)

        new_formula[0][0:9].set_color(BLUE)
        new_formula[0][13:18].set_color(GREEN)
        new_formula[0][18:].set_color(RED)

        new_formula[0][10:13].set_color(YELLOW)

        self.play(Transform(formula,new_formula))
        self.wait(2)
        self.play(FadeOut(label))

        label = Tex("Let's consider this in practice")
        self.play(Fancy_label(label))
        self.wait()
        self.play(FadeOut(formula),FadeOut(label))

class Dimension_line(Scene):
    def construct(self):

        label = Tex("Take a line of length 1")
        line_1 = Line(color=BLUE).set_length(6).move_to(UP)
        line_1_brace = BraceBetweenPoints(line_1.get_start(),line_1.get_end(),direction=UP).shift(0.08*DOWN)
        line_1_label = Tex('1').next_to(line_1_brace.get_center(),UP,buff=0.18)
        self.play(Fancy_label(label))
        self.play(Create(line_1))
        self.play(LaggedStart(
            FadeIn(line_1_brace),
            FadeIn(line_1_label),
            lag_ratio=0.8,run_time=1.5
        ))
        self.play(FadeOut(label))

        label = Tex("Let's take the same line, but with a length 2 times less")
        self.play(Fancy_label(label))
        line_2 = line_1.copy()
        self.play(line_2.animate.set_length(3).shift(np.array([-1.55,-2,0])))
        line_2_brace = BraceBetweenPoints(line_2.get_start(),line_2.get_end(),direction=UP).shift(0.08*DOWN)
        line_2_label = Tex('0.5').next_to(line_2_brace.get_center(),UP,buff=0.18)
        self.play(LaggedStart(
            FadeIn(line_2_brace),
            FadeIn(line_2_label),
            lag_ratio=0.8,run_time=1.5
        ))
        self.play(FadeOut(label))

        label = Tex("We will need 2 such straight lines to restore the original")
        self.play(Fancy_label(label))
        line_3 = line_1.copy()
        self.play(line_3.animate.set_length(3).shift(np.array([1.55,-2,0])))
        line_3_brace = BraceBetweenPoints(line_3.get_start(),line_3.get_end(),direction=UP).shift(0.08*DOWN)
        line_3_label = Tex('0.5').next_to(line_3_brace.get_center(),UP,buff=0.18)
        self.play(LaggedStart(
            FadeIn(line_3_brace),
            FadeIn(line_3_label),
            lag_ratio=0.8,run_time=1.5
        ))
        self.play(FadeOut(label))

        label = Tex(r"That is, the dimension of the line is $\log_22 = 1$")
        self.play(Fancy_label(label))

        self.play(FadeOut(VGroup(
            line_1,line_1_brace,line_1_label,
            line_2,line_2_brace,line_2_label,
            line_3,line_3_brace,line_3_label,
            label
        )))

    
class Dimension_square(Scene):
    def construct(self):

        label = Tex("Let's do the same with the square")
        self.play(Fancy_label(label))

        square = Square(side_length=2,color=BLUE).move_to(1.05*UP).set_opacity(0.6)

        brace_1 = BraceBetweenPoints(square.get_right()+UP,square.get_right()+DOWN,direction=RIGHT).shift(0.1*LEFT)
        brace_2 = BraceBetweenPoints(square.get_right()+UP,square.get_top()+LEFT,direction=UP).shift(0.1*DOWN)

        label_1 = Tex('1').next_to(brace_1,RIGHT,buff=0.1)
        label_2 = Tex('1').next_to(brace_2,UP,buff=0.1)

        
        square_1 = square.copy().set_opacity(0.05)
        square_2 = square.copy().set_opacity(0.05)
        square_3 = square.copy().set_opacity(0.05)
        square_4 = square.copy().set_opacity(0.05)

        self.play(FadeIn(square))

        
        self.play(LaggedStart(
            FadeIn(brace_1),
            FadeIn(label_1),
            lag_ratio=0.8,run_time=1
        ))

        self.play(LaggedStart(
            FadeIn(brace_2),
            FadeIn(label_2),
            lag_ratio=0.8,run_time=1
        ))

        self.play(FadeOut(label))
        label = Tex("For a square, we need 4 copies of the original figure")
        self.play(Fancy_label(label))

        self.play(LaggedStart(
            square_1.animate.scale(0.5).shift(np.array([-0.55,-2,0])).set_opacity(0.6),
            square_2.animate.scale(0.5).shift(np.array([0.55,-2,0])).set_opacity(0.6),
            square_3.animate.scale(0.5).shift(np.array([-0.55,-3.1,0])).set_opacity(0.6),
            square_4.animate.scale(0.5).shift(np.array([0.55,-3.1,0])).set_opacity(0.6),
            lag_ratio=0.7, run_time=3
        ))
        
        brace_3 = BraceBetweenPoints(square_3.get_left()+DOWN/2,square_3.get_right()+DOWN/2,direction=DOWN/1.3).shift(0.1*UP)
        brace_4 = BraceBetweenPoints(square_3.get_left()+UP/2,square_3.get_right()+DOWN/2,direction=LEFT/1.3).shift(0.1*RIGHT)

        label_3 = Tex('0.5').next_to(brace_3,DOWN,buff=0.18)
        label_4 = Tex('0.5').next_to(brace_4,LEFT,buff=0.18)

        self.play(LaggedStart(
            FadeIn(brace_3),
            FadeIn(label_3),
            lag_ratio=0.8,run_time=1
        ))

        self.play(LaggedStart(
            FadeIn(brace_4),
            FadeIn(label_4),
            lag_ratio=0.8,run_time=1
        ))

        self.play(FadeOut(label))

        label = Tex(r"So the dimension of the square is $\log_24=2$")
        self.play(Fancy_label(label))
            
        self.play(FadeOut(VGroup(
            square,square_1,square_2,square_3,square_4,
            brace_3,brace_4,label_3,label_4,
            label,brace_1,brace_2,label_1,label_2
        )))


class Dimension_cube(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes().set_opacity(0.2)
        label = Tex("Now consider the cube as well")     
        self.play(Fancy_label(label))


        cube_size = 1.75
        cube_size_real = 1.6

        cube_0 = Cube(fill_opacity=0.95,side_length=cube_size_real)

        cube_1_shadow = cube_0.copy().shift(cube_size/4*LEFT).shift(cube_size/4*IN).shift(2.2*DOWN).rotate(
            about_point=ORIGIN,angle=-PI/6,axis=UP).rotate(
            about_point=ORIGIN,angle=PI/12,axis=RIGHT).scale(0.5)
        
        cube_2_shadow = cube_0.copy().shift(cube_size/4*LEFT).shift(-cube_size/4*IN).shift(2.2*DOWN).rotate(
            about_point=ORIGIN,angle=-PI/6,axis=UP).rotate(
            about_point=ORIGIN,angle=PI/12,axis=RIGHT).scale(0.5)
        
        cube_3_shadow = cube_0.copy().shift(-cube_size/4*LEFT).shift(cube_size/4*IN).shift(2.2*DOWN).rotate(
            about_point=ORIGIN,angle=-PI/6,axis=UP).rotate(
            about_point=ORIGIN,angle=PI/12,axis=RIGHT).scale(0.5)
        
        cube_4_shadow = cube_0.copy().shift(-cube_size/4*LEFT).shift(-cube_size/4*IN).shift(2.2*DOWN).rotate(
            about_point=ORIGIN,angle=-PI/6,axis=UP).rotate(
            about_point=ORIGIN,angle=PI/12,axis=RIGHT).scale(0.5)
        
        cube_5_shadow = cube_0.copy().shift(cube_size/4*LEFT).shift(cube_size/4*IN).shift((2.2-cube_size/2)*DOWN).rotate(
            about_point=ORIGIN,angle=-PI/6,axis=UP).rotate(
            about_point=ORIGIN,angle=PI/12,axis=RIGHT).scale(0.5)
        
        cube_6_shadow = cube_0.copy().shift(cube_size/4*LEFT).shift(-cube_size/4*IN).shift((2.2-cube_size/2)*DOWN).rotate(
            about_point=ORIGIN,angle=-PI/6,axis=UP).rotate(
            about_point=ORIGIN,angle=PI/12,axis=RIGHT).scale(0.5)
        
        cube_7_shadow = cube_0.copy().shift(-cube_size/4*LEFT).shift(cube_size/4*IN).shift((2.2-cube_size/2)*DOWN).rotate(
            about_point=ORIGIN,angle=-PI/6,axis=UP).rotate(
            about_point=ORIGIN,angle=PI/12,axis=RIGHT).scale(0.5)
        
        cube_8_shadow = cube_0.copy().shift(-cube_size/4*LEFT).shift(-cube_size/4*IN).shift((2.2-cube_size/2)*DOWN).rotate(
            about_point=ORIGIN,angle=-PI/6,axis=UP).rotate(
            about_point=ORIGIN,angle=PI/12,axis=RIGHT).scale(0.5)
        


        cube = cube_0.copy().move_to(1.3*UP).rotate(
            about_point=ORIGIN,angle=-PI/6,axis=UP
            ).rotate(
            about_point=ORIGIN,angle=PI/12,axis=RIGHT
            )
        
        self.play(FadeIn(cube))
        self.wait()
        

        vertices = cube_vertices(cube)
        brace_1 = BraceBetweenPoints(vertices[6]+0.15*UP+0.05*RIGHT,vertices[7]+0.15*UP+0.05*RIGHT,direction=(1.315*DL+DR)/2)
        brace_2 = BraceBetweenPoints(vertices[1]+0.163*UP+0.1*LEFT,vertices[6]+0.163*UP+0.1*LEFT,direction=(1.57*DOWN+0.8*RIGHT)/2)
        brace_3 = BraceBetweenPoints(vertices[1]+0.17*LEFT,vertices[2]+0.17*LEFT,direction=RIGHT)

        label_1 = Tex('1').move_to(brace_1.get_center()+((1.315*DL+DR)/2)*0.38)
        label_2 = Tex('1').move_to(brace_2.get_center()+((1.57*DOWN+0.75*RIGHT)/2)*0.5)
        label_3 = Tex('1').move_to(brace_3.get_center()+0.3*RIGHT)
        
        self.play(FadeIn(brace_1),FadeIn(label_1))
        self.play(FadeIn(brace_2),FadeIn(label_2))
        self.play(FadeIn(brace_3),FadeIn(label_3))

        
        cube_1 = cube.copy()

        self.play(cube_1.animate.move_to(cube_1_shadow.get_center()).scale(0.5))

        vertices_1 = cube_vertices(cube_1)
        brace_1_1 = brace_1.copy().scale(0.48).shift(3*DOWN).shift(0.8*LEFT).rotate(
            about_point=ORIGIN,angle=PI/35,axis=IN).shift(1.1*RIGHT).shift(0.38*UP)
        brace_1_2 = brace_2.copy().scale(0.55).shift(3*DOWN).shift(0.4*LEFT).rotate(
            about_point=ORIGIN,angle=-PI/29,axis=IN).shift(0.38*LEFT+0.35*UP)
        brace_1_3 = brace_3.copy().scale(0.47).shift(3*DOWN).shift(0.785*LEFT).shift(0.15*DOWN)

        label_1_1 = Tex('0.5',font_size=24).move_to(brace_1_1.get_center()+((1.315*DL+DR)/2)*0.2)
        label_1_2 = Tex('0.5',font_size=24).move_to(brace_1_2.get_center()+((1.57*DOWN+0.75*RIGHT)/2)*0.32)
        label_1_3 = Tex('0.5',font_size=24).move_to(brace_1_3.get_center()+0.25*RIGHT)

        
        self.play(FadeIn(brace_1_1),FadeIn(label_1_1))
        self.play(FadeIn(brace_1_2),FadeIn(label_1_2))
        self.play(FadeIn(brace_1_3),FadeIn(label_1_3))

        self.wait(0.5)

        self.play(FadeOut(label))
        label = Tex("Now we will need 8 copies")
        self.play(Fancy_label(label))

        self.play(
            FadeOut(brace_1),FadeOut(label_1),
            FadeOut(brace_2),FadeOut(label_2),
            FadeOut(brace_3),FadeOut(label_3),
            FadeOut(brace_1_1),FadeOut(label_1_1),
            FadeOut(brace_1_2),FadeOut(label_1_2),
            FadeOut(brace_1_3),FadeOut(label_1_3),
        )




        cube_2 = cube.copy()
        cube_3 = cube.copy()
        cube_4 = cube.copy()
        cube_5 = cube.copy()
        cube_6 = cube.copy()
        cube_7 = cube.copy()
        cube_8 = cube.copy()

        self.play(LaggedStart(
            cube_2.animate.move_to(cube_2_shadow.get_center()).scale(0.5),
            cube_3.animate.move_to(cube_3_shadow.get_center()).scale(0.5),
            cube_4.animate.move_to(cube_4_shadow.get_center()).scale(0.5),
            cube_5.animate.move_to(cube_5_shadow.get_center()).scale(0.5),
            cube_6.animate.move_to(cube_6_shadow.get_center()).scale(0.5),
            cube_7.animate.move_to(cube_7_shadow.get_center()).scale(0.5),
            cube_8.animate.move_to(cube_8_shadow.get_center()).scale(0.5),

            lag_ratio=0.8,run_time=8
        ))



        self.wait(0.5)
        self.play(FadeOut(label))

        label = Tex(r"So the dimension of the cube is $\log_28=3$")
        self.play(Fancy_label(label))
        self.wait(1.3)
        self.play(FadeOut(VGroup(
            cube, label,
            cube_1, cube_2,
            cube_3, cube_4,
            cube_5, cube_6,
            cube_7, cube_8,
        )))


class Dimension_square_2(Scene):
    def construct(self):
        label = Tex("But it is not necessary to reduce the figures by 2 times")
        self.play(Fancy_label(label))

        size = 1.8
        buff_1 = 0.025
        buff_2 = 0.023
        buff_3 = 0.018



        square_1 = Square(side_length=size,color=BLUE).move_to(3*LEFT+1.5*UP).set_opacity(0.6)
        square_2 = Square(side_length=size,color=RED).move_to(1.5*UP).set_opacity(0.6)
        square_3 = Square(side_length=size,color=GREEN_B).move_to(3*RIGHT+1.5*UP).set_opacity(0.6)

        self.play(FadeIn(square_1))

        square_1_1 = square_1.copy().set_opacity(0.01)
        square_1_2 = square_1.copy().set_opacity(0.01)
        square_1_3 = square_1.copy().set_opacity(0.01)
        square_1_4 = square_1.copy().set_opacity(0.01)

        self.play(LaggedStart(
            square_1_1.animate.scale(0.48).shift(np.array([-(size/4+buff_1),-3-buff_1,0])).set_opacity(0.6),
            square_1_2.animate.scale(0.48).shift(np.array([(size/4+buff_1),-3-buff_1,0])).set_opacity(0.6),
            square_1_3.animate.scale(0.48).shift(np.array([-(size/4+buff_1),-3+size/2+buff_1,0])).set_opacity(0.6),
            square_1_4.animate.scale(0.48).shift(np.array([(size/4+buff_1),-3+size/2+buff_1,0])).set_opacity(0.6),
            lag_ratio=0.8, run_time=4
        ))

        info_1_1 = Tex("Scale: 2",font_size=30).move_to(square_1.get_center()).shift(3.8*DOWN).set_opacity(0.4)
        info_1_2 = Tex("Copies: 4",font_size=30).move_to(square_1.get_center()).shift(4.15*DOWN).set_opacity(0.4)
        info_2_1 = Tex("Scale: 3",font_size=30).move_to(square_2.get_center()).shift(3.8*DOWN).set_opacity(0.4)
        info_2_2 = Tex("Copies: 9",font_size=30).move_to(square_2.get_center()).shift(4.15*DOWN).set_opacity(0.4)
        info_3_1 = Tex("Scale: 4",font_size=30).move_to(square_3.get_center()).shift(3.8*DOWN).set_opacity(0.4)
        info_3_2 = Tex("Copies: 16",font_size=30).move_to(square_3.get_center()).shift(4.15*DOWN).set_opacity(0.4)


        self.play(FadeIn(VGroup(info_1_1, info_1_2)))

        self.play(FadeIn(square_2))

        square_2_1 = square_2.copy().set_opacity(0.01)
        square_2_2 = square_2.copy().set_opacity(0.01)
        square_2_3 = square_2.copy().set_opacity(0.01)
        square_2_4 = square_2.copy().set_opacity(0.01)
        square_2_5 = square_2.copy().set_opacity(0.01)
        square_2_6 = square_2.copy().set_opacity(0.01)
        square_2_7 = square_2.copy().set_opacity(0.01)
        square_2_8 = square_2.copy().set_opacity(0.01)
        square_2_9 = square_2.copy().set_opacity(0.01)

        self.play(LaggedStart(
            square_2_1.animate.scale(0.31).shift(np.array([-(size/3+2*buff_2),-3.15-buff_2,0])).set_opacity(0.6),
            square_2_2.animate.scale(0.31).shift(np.array([0,-3.15-buff_2,0])).set_opacity(0.6),
            square_2_3.animate.scale(0.31).shift(np.array([(size/3+2*buff_2),-3.15-buff_2,0])).set_opacity(0.6),
            square_2_4.animate.scale(0.31).shift(np.array([-(size/3+2*buff_2),-3.15+size/3+buff_2,0])).set_opacity(0.6),
            square_2_5.animate.scale(0.31).shift(np.array([0,-3.15+size/3+buff_2,0])).set_opacity(0.6),
            square_2_6.animate.scale(0.31).shift(np.array([(size/3+2*buff_2),-3.15+size/3+buff_2,0])).set_opacity(0.6),
            square_2_7.animate.scale(0.31).shift(np.array([-(size/3+2*buff_2),-3.15+2*size/3+3*buff_2,0])).set_opacity(0.6),
            square_2_8.animate.scale(0.31).shift(np.array([0,-3.15+2*size/3+3*buff_2,0])).set_opacity(0.6),
            square_2_9.animate.scale(0.31).shift(np.array([(size/3+2*buff_2),-3.15+2*size/3+3*buff_2,0])).set_opacity(0.6),
            lag_ratio=0.45, run_time=5
        ))

        self.play(FadeIn(VGroup(info_2_1, info_2_2)))

        self.play(FadeIn(square_3))

        square_3_1 = square_3.copy().set_opacity(0.01)
        square_3_2 = square_3.copy().set_opacity(0.01)
        square_3_3 = square_3.copy().set_opacity(0.01)
        square_3_4 = square_3.copy().set_opacity(0.01)
        square_3_5 = square_3.copy().set_opacity(0.01)
        square_3_6 = square_3.copy().set_opacity(0.01)
        square_3_7 = square_3.copy().set_opacity(0.01)
        square_3_8 = square_3.copy().set_opacity(0.01)
        square_3_9 = square_3.copy().set_opacity(0.01)
        square_3_10 = square_3.copy().set_opacity(0.01)
        square_3_11 = square_3.copy().set_opacity(0.01)
        square_3_12 = square_3.copy().set_opacity(0.01)
        square_3_13 = square_3.copy().set_opacity(0.01)
        square_3_14 = square_3.copy().set_opacity(0.01)
        square_3_15 = square_3.copy().set_opacity(0.01)
        square_3_16 = square_3.copy().set_opacity(0.01)

        self.play(LaggedStart(
            square_3_1.animate.scale(0.224).shift(np.array([-(3*size/8+3*buff_3),-3.22,0])).set_opacity(0.6),
            square_3_2.animate.scale(0.224).shift(np.array([-(size/8+buff_3),-3.22,0])).set_opacity(0.6),
            square_3_3.animate.scale(0.224).shift(np.array([(size/8+buff_3),-3.22,0])).set_opacity(0.6),
            square_3_4.animate.scale(0.224).shift(np.array([(3*size/8+3*buff_3),-3.22,0])).set_opacity(0.6),
            square_3_5.animate.scale(0.224).shift(np.array([-(3*size/8+3*buff_3),-3.22+(size/4+2*buff_3),0])).set_opacity(0.6),
            square_3_6.animate.scale(0.224).shift(np.array([-(size/8+buff_3),-3.22+(size/4+2*buff_3),0])).set_opacity(0.6),
            square_3_7.animate.scale(0.224).shift(np.array([(size/8+buff_3),-3.22+(size/4+2*buff_3),0])).set_opacity(0.6),
            square_3_8.animate.scale(0.224).shift(np.array([(3*size/8+3*buff_3),-3.22+(size/4+2*buff_3),0])).set_opacity(0.6),
            square_3_9.animate.scale(0.224).shift(np.array([-(3*size/8+3*buff_3),-3.22+2*(size/4+2*buff_3),0])).set_opacity(0.6),
            square_3_10.animate.scale(0.224).shift(np.array([-(size/8+buff_3),-3.22+2*(size/4+2*buff_3),0])).set_opacity(0.6),
            square_3_11.animate.scale(0.224).shift(np.array([(size/8+buff_3),-3.22+2*(size/4+2*buff_3),0])).set_opacity(0.6),
            square_3_12.animate.scale(0.224).shift(np.array([(3*size/8+3*buff_3),-3.22+2*(size/4+2*buff_3),0])).set_opacity(0.6),
            square_3_13.animate.scale(0.224).shift(np.array([-(3*size/8+3*buff_3),-3.22+3*(size/4+2*buff_3),0])).set_opacity(0.6),
            square_3_14.animate.scale(0.224).shift(np.array([-(size/8+buff_3),-3.22+3*(size/4+2*buff_3),0])).set_opacity(0.6),
            square_3_15.animate.scale(0.224).shift(np.array([(size/8+buff_3),-3.22+3*(size/4+2*buff_3),0])).set_opacity(0.6),
            square_3_16.animate.scale(0.224).shift(np.array([(3*size/8+3*buff_3),-3.22+3*(size/4+2*buff_3),0])).set_opacity(0.6),
            lag_ratio=0.4,run_time=7
        ))

        self.play(FadeIn(VGroup(info_3_1, info_3_2)))

        self.play(FadeOut(label))
        label = Tex(r"The dimension of the square is still $\log_24=\log_39=\log_416=2$",font_size=44)
        self.play(Fancy_label(label))
        self.wait()
        self.play(FadeOut(VGroup(
            square_1,square_2,square_3,
            square_1_1,square_1_2,square_1_3,square_1_4,
            square_2_1,square_2_2,square_2_3,square_2_4,
            square_2_5,square_2_6,square_2_7,square_2_8,square_2_9,
            square_3_1,square_3_2,square_3_3,square_3_4,
            square_3_5,square_3_6,square_3_7,square_3_8,
            square_3_9,square_3_10,square_3_11,square_3_12,
            square_3_13,square_3_14,square_3_15,square_3_16,
            label,
            info_1_1,info_1_2,
            info_2_1,info_2_2,
            info_3_1,info_3_2,
        )))
        self.wait()


class Sierpinski(Scene):
    def construct(self):
        label = Tex("Let's build an equilateral triangle")
        triangle_1 = Triangle(color=BLUE, stroke_color=RED).shift(UP).set_opacity(1).set_stroke(opacity=0)
        triangle_2 = triangle_1.copy().set_opacity(0.05)
        triangle_3 = triangle_1.copy().set_opacity(0.05)


        self.play(Fancy_label(label))
        self.play(FadeIn(triangle_1))
        self.play(FadeOut(label))

        label = Tex("Copy it 2 times and assemble a new similar triangle")
        self.play(Fancy_label(label))
        self.play(LaggedStart(
            triangle_2.animate.set_opacity(1).rotate(about_point=ORIGIN,angle=2*PI/3).set_stroke(opacity=0),
            triangle_3.animate.set_opacity(1).rotate(about_point=ORIGIN,angle=-2*PI/3).set_stroke(opacity=0),
            lag_ratio=0.7,run_time=1.8
        ))
        self.play(FadeOut(label))

        label = Tex("Let's repeat this several times")
        self.play(Fancy_label(label))
        
        v = VGroup(triangle_1,triangle_2,triangle_3)
        self.play(v.animate.scale(0.5).move_to(Triangle().get_center()+UP))
        v1 = v.copy()
        v2 = v.copy()
        self.play(LaggedStart(
            v1.animate.set_opacity(1).rotate(about_point=ORIGIN,angle=2*PI/3).set_stroke(opacity=0),
            v2.animate.set_opacity(1).rotate(about_point=ORIGIN,angle=-2*PI/3).set_stroke(opacity=0),
            lag_ratio=0.7,run_time=2
        ))
        self.wait()

        v = VGroup(v,v1,v2)
        for i in range(3,7):
            self.play(Transform(v,Sierpinski_triangle(i).shift(0.23*UP)))
            self.wait(0.4)
            self.remove(v)
            v = Sierpinski_triangle(i).shift(0.23*UP)
        self.add(v)

        self.play(FadeOut(label))
        label = Tex("This fractal is called the Sierpinski Triangle")
        self.play(Fancy_label(label))
        self.wait()
        self.play(FadeOut(VGroup(
            label,v)))
        self.wait(0.1)


class Pascal_and_Sierpinski(Scene):
    def construct(self):
        label = Tex("Take Pascal's triangle")
        self.play(Fancy_label(label))

        n = 7
        triangle_1 = Pascal_Triangle(n).scale(0.6)
        for i in range(n):
            self.play(FadeIn(triangle_1[i]),run_time=0.5)

        self.play(FadeOut(label))

        label = Tex("Let's paint the cells with odd numbers blue")
        self.play(Fancy_label(label))
        for i in range(n):
            x = VGroup()
            for j in range(i+1):
                if scipy.special.comb(i,j)%2==1:
                    x.add(triangle_1[i][j])
            self.play(x.animate.set_stroke(color=BLUE),run_time=0.2)

        self.play(FadeOut(label))
        label = Tex("Can't you see anything? Let's take a bigger triangle!")
        self.play(Fancy_label(label))
        self.play(FadeOut(triangle_1),run_time=0.6)

        k = 32
        triangle_2 = Pascal_Triangle(k).scale(0.15)
        for i in range(k):
            self.play(FadeIn(triangle_2[i]),run_time=0.2)
        self.wait()
        y = VGroup()
        z = VGroup()
        for i in range(k):
            x = VGroup()
            for j in range(i+1):
                if scipy.special.comb(i,j)%2==1:
                    x.add(triangle_2[i][j])
                    z.add(triangle_2[i][j])
                else:
                    y.add(triangle_2[i][j])
            self.play(x.animate.set_stroke(color=BLUE),run_time=0.1)       
        x = VGroup()
        for i in triangle_2:
            for j in i:
                if isinstance(j,Tex):
                    x.add(j)
        self.play(FadeOut(x),run_time=0.6)
        self.play(FadeOut(y),run_time=0.6)
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex("We got the Sierpinski triangle from Pascal's triangle")
        self.play(Fancy_label(label))
        self.play(FadeOut(VGroup(label,z)))
          

class Carpet(Scene):
        def construct(self):
            label = Tex("There is also a Sierpinski carpet")
            self.play(Fancy_label(label))
            x = Sierpinski_carpet(1)
            self.play(FadeIn(x))
            for i in range(2,6):
                self.play(Transform(x,Sierpinski_carpet(i)))
                self.wait(0.2)
                self.remove(x)
                x = Sierpinski_carpet(i)
            self.add(x)
            self.play(FadeOut(x))


class Dimension_Koch(Scene):
    def construct(self):
        label = Tex("Now we calculate the dimension of the Koch curve")
        self.play(Fancy_label(label))
        curve = Koch_curve(n=6, stroke_width=1.5,length=9,color=BLUE).shift(1.2*UP)
        self.play(FadeIn(curve))

        curve_size = Line(curve.get_start(),curve.get_end()).get_length()
        curve_1 = Koch_curve(n=5, stroke_width=1.5,length=9,color=BLUE).scale(1/3).shift(0.1*DOWN).set_stroke(opacity=0)

        self.play(curve_1.animate.set_stroke(opacity=1).shift(2*DOWN).shift(curve_size/3*LEFT))

        curve_2 = curve_1.copy().set_stroke(opacity=0.1)
        curve_3 = curve_1.copy().set_stroke(opacity=0.1)
        curve_4 = curve_1.copy().set_stroke(opacity=0.1)

        self.play(curve_2.animate.shift(curve_size/3*RIGHT).rotate(about_point=curve_1.get_end(),angle=PI/3).set_stroke(opacity=1))
        self.play(curve_3.animate.shift(curve_size/3*RIGHT).rotate(about_point=curve_1.get_end()+curve_size/3*RIGHT,angle=-PI/3).set_stroke(opacity=1))
        self.play(curve_4.animate.shift(2*curve_size/3*RIGHT).set_stroke(opacity=1))
        
        self.play(Glow(curve_1,color=RED))
        self.play(Glow(curve_2,color=RED))
        self.play(Glow(curve_3,color=RED))
        self.play(Glow(curve_4,color=RED))

        info_1_1 = Tex("Scale: 3",font_size=34).shift(2.5*DOWN).set_opacity(0.4)
        info_1_2 = Tex("Copies: 4",font_size=34).shift(2.95*DOWN).set_opacity(0.4)

        self.play(FadeIn(VGroup(info_1_1,info_1_2)))
        self.play(FadeOut(label))
        label = Tex(r"So the dimension of the Koch curve is $\log_34 \approx 1.262$")
        self.play(Fancy_label(label))

        self.wait(1.5)
        self.play(FadeOut(VGroup(
            curve,curve_1,curve_2,curve_3,curve_4,
            info_1_1,info_1_2,label
        )))
        self.wait(0.5)


class Dimension_Sierpinski(Scene):
    def construct(self):
        label = Tex("Now consider the Sierpinski triangle")
        self.play(Fancy_label(label))


        triangle = Sierpinski_triangle(6).shift(UP).scale(0.7)
        triangle_1 = Sierpinski_triangle(5).shift(UP).scale(0.7)
        self.play(FadeIn(triangle))
        self.play(triangle_1.animate.scale(0.5).shift(2.45/4*LEFT).shift(3*DOWN))
        triangle_2 = triangle_1.copy()
        triangle_3 = triangle_1.copy()
        self.play(triangle_2.animate.shift(2.45/2*RIGHT))
        self.play(triangle_3.animate.shift(2.45/4*RIGHT).shift(2.105/2*UP))

        info_1_1 = Tex("Scale: 2",font_size=34).shift(2.7*DOWN).set_opacity(0.4)
        info_1_2 = Tex("Copies: 3",font_size=34).shift(3.15*DOWN).set_opacity(0.4)

        self.play(FadeIn(VGroup(info_1_1,info_1_2)))
        self.play(FadeOut(label))

        label = Tex(r"So the dimension of the Sierpinski Triangle is $\log_23 \approx 1.585$")
        self.play(Fancy_label(label))
        self.wait()
        self.play(FadeOut(VGroup(
            triangle,triangle_1,triangle_2,triangle_3,
            label,info_1_1,info_1_2
        )))

        self.wait()


        




        

        


        


            

