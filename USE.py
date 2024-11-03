from manim import *
from manimextra import *
from scipy.optimize import fsolve

config.max_files_cached = 4096


class Task_1_planimetry(Scene):
    def construct(self):
        task_text = Tex(r"The quadrilateral $ABCD$ is inscribed in a circle. The angle $\angle{ABC}$ is $110^{\circ}$. " +
                        r"The angle $\angle{ABD}$ is $70^{\circ}$. Find the angle $\angle{CAD}$. Give the answer in degrees", width=250)
        rectangle = SurroundingRectangle(task_text, buff=0.3)
        task_label = Tex("Task 1. Planimetry").scale(1.2).to_edge(UP)
        
        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text), run_time=5)
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.3 * UP).scale(0.6),
        ))
        self.wait()

        circle = Circle(radius=2.5, color=BLUE).shift(0.5 * DOWN)

        A = Dot(circle.point_at_angle(-0.92 * PI)).set_z_index(1)
        B = Dot(circle.point_at_angle(0.42 * PI)).set_z_index(1)
        C = Dot(circle.point_at_angle(0.12 * PI)).set_z_index(1)
        D = Dot(circle.point_at_angle(-0.3 * PI)).set_z_index(1)

        A_label = MathTex("A", font_size=42).move_to(A.get_center() + 0.3 * LEFT)
        B_label = MathTex("B", font_size=42).move_to(B.get_center() + 0.29 * RIGHT + 0.29 * UP)
        C_label = MathTex("C", font_size=42).move_to(C.get_center() + 0.36 * RIGHT)
        D_label = MathTex("D", font_size=42).move_to(D.get_center() + 0.25 * RIGHT + 0.26 * DOWN)

        AB = Line(A, B, color=GREEN)
        BC = Line(B, C, color=GREEN)
        CD = Line(C, D, color=GREEN)
        DA = Line(D, A, color=GREEN)
        AC = Line(A, C, color=YELLOW).set_opacity(0.55)
        BD = Line(B, D, color=YELLOW).set_opacity(0.55)


        ALL = VGroup(
            circle,
            A, B, C, D,
            A_label, B_label, C_label, D_label,
            AB, BC, CD, DA,
            AC, BD,
        )


        self.play(Create(circle))
        self.play(LaggedStart(
            FadeIn(VGroup(A, A_label)), FadeIn(VGroup(B, B_label)),
            FadeIn(VGroup(C, C_label)), FadeIn(VGroup(D, D_label)),
            run_time=2, lag_ratio=0.6
        ))

        self.play(LaggedStart(
            Create(AB), Create(BC), Create(CD), Create(DA),
            run_time=2, lag_ratio=0.8
        ))
        self.play(LaggedStart(
            Create(AC), Create(BD),
            run_time=1.3, lag_ratio=0.8
        ))
        self.wait()

        self.play(ALL.animate.shift(2.5 * LEFT))

        
        angle_ABC = Angle.from_three_points(A, B, C, radius=0.35).set_z_index(-1)
        angle_ABD = Angle.from_three_points(A, B, D, radius=0.43).set_z_index(-1)
        angle_DBC = Angle.from_three_points(D, B, C, radius=0.52).set_z_index(-1)
        angle_CAD = Angle.from_three_points(C, A, D, radius=0.52).set_z_index(-1)

        angle_ABC_label = MathTex("110^{\circ}", font_size=28).move_to(angle_ABC.get_label_center())
        angle_ABD_label = MathTex("70^{\circ}", font_size=22).move_to(angle_ABD.get_label_center())
        angle_DBC_label = MathTex("40^{\circ}", font_size=22).move_to(angle_DBC.get_label_center())
        angle_CAD_label = MathTex("40^{\circ}", font_size=22).move_to(angle_CAD.get_label_center())
        


        info_1 = Tex(r"$\angle{DBC} = \angle{ABC} - \angle{ABD}$", font_size=38).shift(3.5 * RIGHT + 0.35 * UP)
        info_2 = Tex(r"$\angle{DBC} = 110^{\circ} - 70^{\circ} = 40^{\circ}$", font_size=38).shift(3.5 * RIGHT + 0.35 * DOWN)
        info_3 = Tex(r"Answer: $\angle{CAD} = 40^{\circ}$", font_size=38).shift(3.5 * RIGHT + 1.05 * DOWN)


        B_animation = B.copy()
        BD_animation = always_redraw(lambda: Line(B_animation.get_center(), D.get_center(), color=RED))
        BC_animation = always_redraw(lambda: Line(B_animation.get_center(), C.get_center(), color=RED))
        angle_DBC_animation = always_redraw(lambda: Angle.from_three_points(D.get_center(), B_animation.get_center(), C.get_center(), radius=0.52).set_z_index(-1))

        self.play(Create(angle_ABC), FadeIn(angle_ABC_label))
        self.wait(0.6)
        self.play(FadeOut(VGroup(angle_ABC, angle_ABC_label)))
        self.wait(0.4)
        self.play(Create(angle_ABD), FadeIn(angle_ABD_label))
        self.wait(0.2)
        self.play(Create(angle_DBC))
        self.wait(0.2)
        self.play(Write(info_1))
        self.wait(0.2)
        self.play(Write(info_2))
        self.wait(0.2)
        self.play(FadeIn(angle_DBC_label))
        self.wait(1.5)
        
        B_animation = B.copy()
        self.add(B_animation)
        
        BD_animation = always_redraw(lambda: Line(B_animation.get_center(), D.get_center(), color=RED))
        BC_animation = always_redraw(lambda: Line(B_animation.get_center(), C.get_center(), color=RED))
        angle_DBC_animation = always_redraw(lambda: Angle.from_three_points(D.get_center(), B_animation.get_center(), C.get_center(), radius=0.52).set_z_index(-1))


        self.play(
            Create(BC_animation), Create(BD_animation), Create(angle_DBC_animation),
            run_time=1.5
        )
        
        self.play(MoveAlongPath(B_animation, ArcBetweenPoints(B.get_center(), A.get_center(), angle=0.66*PI)), run_time=2)
        self.play(FadeIn(angle_CAD), FadeIn(angle_CAD_label))
        self.remove(angle_DBC_animation)
        self.wait(2)
        self.play(FadeOut(VGroup(B_animation, BC_animation, BD_animation)))
        self.wait()
        self.play(Wiggle(angle_CAD_label), run_time=1.5)

        infos = VGroup(info_1, info_2, info_3)
        info_3.set_opacity(0)
        self.play(infos.animate.move_to(3.5 * RIGHT))
        self.play(info_3.animate.set_opacity(1))
        self.wait(0.5)
        answer_box = SurroundingRectangle(info_3, buff=0.1)
        self.play(Create(answer_box))





        self.wait(3)
        

class Task_2_vectors(Scene):
    def construct(self):
        task_text = Tex(r"Given the vectors $\vec{a}(3; -2)$ and $\vec{b}(0; 1)$. " +
                        r"Find the value of $\vec{a} \cdot \vec{b}$", width=250).set_z_index(2)
        rectangle = SurroundingRectangle(task_text, buff=0.3).set_z_index(2)
        task_label = Tex("Task 2. Vectors").scale(1.2).to_edge(UP).set_z_index(2)
        black_rectangle = Rectangle(width=50, height=1.5, color=BLACK, fill_opacity=1).to_edge(UP).shift(0.55 * UP).set_z_index(1)
    
        self.add(black_rectangle)
        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text), run_time=5)        
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.3 * UP).scale(0.6),
        ))
        self.wait()

        plane = NumberPlane(x_range=[-5, 5], y_range=[-4, 4], axis_config={"color": WHITE}).scale(0.65).shift(2.4 * LEFT)
        plane.add_coordinates([-4, -3, -2, -1, 1, 2, 3, 4], [-3, -2, -1, 1, 2, 3])
        self.play(Create(plane))


        info_1 = Tex(r"$\vec{u}(x_1; y_1)$", font_size=38).shift(4 * RIGHT + 1.8 * UP).set_opacity(0.6)
        info_2 = Tex(r"$\vec{v}(x_2; y_2)$", font_size=38).shift(4 * RIGHT + 1.1 * UP).set_opacity(0.6)
        info_3 = Tex(r"$\vec{u} \cdot \vec{v} = x_1 \cdot x_2 + y_1 \cdot y_2$", font_size=38).shift(4 * RIGHT + 0.4 * UP).set_opacity(0.6)
        
        info_4 = Tex(r"$\vec{a} \cdot \vec{b} = 3 \cdot 0 + (-2) \cdot 1 = -2$", font_size=42).shift(4 * RIGHT + 0.55 * DOWN)
        info_4[0][0:2].set_color(RED)
        info_4[0][3:5].set_color(GREEN)
        info_4[0][6].set_color(RED)
        info_4[0][8].set_color(GREEN)
        info_4[0][10:14].set_color(RED)
        info_4[0][15].set_color(GREEN)

        info_5 = Tex(r"Answer: $\vec{a} \cdot \vec{b} = -2$", font_size=42).shift(4 * RIGHT + 1.3 * DOWN)
        answer_rectangle = SurroundingRectangle(info_5, buff=0.15).shift(0.035 * DOWN)
    

        vector_a = Arrow(start=plane.coords_to_point(0, 0, 0), end=plane.coords_to_point(3, -2, 0), color=RED, buff=0, 
                         max_stroke_width_to_length_ratio=2.45, max_tip_length_to_length_ratio=0.12)
        vector_b = Arrow(start=plane.coords_to_point(0, 0, 0), end=plane.coords_to_point(0, 1, 0), color=GREEN, buff=0, 
                         max_stroke_width_to_length_ratio=8.65, max_tip_length_to_length_ratio=0.28)

        self.play(Create(vector_a)) 
        self.wait(0.8)
        self.play(Create(vector_b))
        self.wait(0.8)


        self.play(Write(info_1))
        self.wait(0.2)
        self.play(Write(info_2))
        self.wait(0.2)
        self.play(Write(info_3))

        self.wait(1.5)
        self.play(Write(info_4))
        self.wait(0.8)

        self.play(Write(info_5))
        self.wait(0.5)
        self.play(Create(answer_rectangle))

        self.wait(3)

        

class Task_3_stereometry(ThreeDScene):
    def construct(self):
        task_text = Tex(r"Find the volume of a polyhedron whose vertices are $A, B, C, B_1$" +
                        r"of a rectangular parallelepiped $ABCDA_1B_1C_1D_1$, where $AB=3, AD=3$ and $AA_1=4$", 
                        width=250).set_z_index(2)
        rectangle = SurroundingRectangle(task_text, buff=0.3).set_z_index(2)
        task_label = Tex("Task 3. Stereometry").scale(1.2).to_edge(UP).set_z_index(2)
        black_rectangle = Rectangle(width=50, height=1.5, color=BLACK, fill_opacity=1).to_edge(UP).shift(0.55 * UP).set_z_index(1)
    
        self.add(black_rectangle)
        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text), run_time=5)        
        self.wait()
        
        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.3 * UP).scale(0.6),
        ))
        self.wait()
        
        
        A = Dot3D([-1.5, -2.4, 1.5]).set_z_index(10)
        B = Dot3D([1.5, -2.4, 1.5]).set_z_index(10)
        C = Dot3D([1.5, -2.4, -1.5]).set_z_index(10)
        D = Dot3D([-1.5, -2.4, -1.5]) .set_z_index(10)
        A_1 = Dot3D([-1.5, 1.6, 1.5]).set_z_index(10)
        B_1 = Dot3D([1.5, 1.6, 1.5]).set_z_index(10)
        C_1 = Dot3D([1.5, 1.6, -1.5]).set_z_index(10)
        D_1 = Dot3D([-1.5, 1.6, -1.5]).set_z_index(10)
        
        parallelepiped = VGroup(A, B, C, D, A_1, B_1, C_1, D_1)
        parallelepiped.scale(0.9)
        parallelepiped.rotate(13 * DEGREES, axis=RIGHT).rotate(-38 * DEGREES, axis=UP).rotate(8 * DEGREES, axis=IN)
        
        A_label = MathTex("A", font_size=32).move_to(A.get_center() + 0.3 * LEFT)
        B_label = MathTex("B", font_size=32).move_to(B.get_center() + 0.3 * DOWN)
        C_label = MathTex("C", font_size=32).move_to(C.get_center() + 0.36 * RIGHT)
        D_label = MathTex("D", font_size=32).move_to(D.get_center() + 0.25 * LEFT + 0.25 * UP)
        A_1_label = MathTex("A_1", font_size=32).move_to(A_1.get_center() + 0.33 * LEFT)
        B_1_label = MathTex("B_1", font_size=32).move_to(B_1.get_center() + 0.2 * DOWN + 0.35 * RIGHT)
        C_1_label = MathTex("C_1", font_size=32).move_to(C_1.get_center() + 0.36 * RIGHT)
        D_1_label = MathTex("D_1", font_size=32).move_to(D_1.get_center() + 0.29 * UP + 0.04 * LEFT)
        
        labels = VGroup(A_label, B_label, C_label, D_label, A_1_label, B_1_label, C_1_label, D_1_label)

        AB = Line3D(A.get_center(), B.get_center(), color=BLUE)
        BC = Line3D(B.get_center(), C.get_center(), color=BLUE)
        CD = Line(C.get_center(), D.get_center(), color=BLUE).set_opacity(0.5).set_z_index(-1)
        DA = Line(D.get_center(), A.get_center(), color=BLUE).set_opacity(0.5).set_z_index(-1)
        AA_1 = Line3D(A.get_center(), A_1.get_center(), color=BLUE)
        BB_1 = Line3D(B.get_center(), B_1.get_center(), color=BLUE)
        CC_1 = Line3D(C.get_center(), C_1.get_center(), color=BLUE)
        DD_1 = Line(D.get_center(), D_1.get_center(), color=BLUE).set_opacity(0.5).set_z_index(-1)
        A_1B_1 = Line3D(A_1.get_center(), B_1.get_center(), color=BLUE)
        B_1C_1 = Line3D(B_1.get_center(), C_1.get_center(), color=BLUE)
        C_1D_1 = Line3D(C_1.get_center(), D_1.get_center(), color=BLUE)
        D_1A_1 = Line3D(D_1.get_center(), A_1.get_center(), color=BLUE)
        
        AB_label = MathTex("3", font_size=52, color=YELLOW).move_to(AB.get_center() + 0.32 * DOWN).shift(0.08 * LEFT + 0.03 * UP)
        BC_label = MathTex("3", font_size=52, color=YELLOW).move_to(BC.get_center() + 0.32 * DOWN).shift(0.075 * UP + 0.13 * RIGHT)
        AA_1_label = MathTex("4", font_size=52, color=YELLOW).move_to(AA_1.get_center() + 0.23 * LEFT).set_z_index(9)
        
        AC = Line(A.get_center(), C.get_center(), color=RED)
        AB_1 = Line(A.get_center(), B_1.get_center(), color=RED)
        CB_1 = Line(C.get_center(), B_1.get_center(), color=RED)
        
        pyramid = VGroup(
            Polygon(A.get_center(), B.get_center(), C.get_center(), color=RED).set_stroke(opacity=0).set_fill(RED, 0.3),
            Polygon(A.get_center(), C.get_center(), B_1.get_center(), color=RED).set_stroke(opacity=0).set_fill(RED, 0.3),
            Polygon(B.get_center(), B_1.get_center(), A.get_center(), color=RED).set_stroke(opacity=0).set_fill(RED, 0.3),
            Polygon(B.get_center(), B_1.get_center(), C.get_center(), color=RED).set_stroke(opacity=0).set_fill(RED, 0.3)
        )
        
        A_sq = Dot(4 * RIGHT + UP).set_z_index(9)
        B_sq = Dot(4 * RIGHT + 0.7 * DOWN).set_z_index(9)
        C_sq = Dot(5.7 * RIGHT + 0.7 * DOWN).set_z_index(9)
        D_sq = Dot(5.7 * RIGHT + UP).set_z_index(9)
        
        A_sq_label = Tex("A", font_size=30).move_to(A_sq.get_center() + 0.2 * UL)
        B_sq_label = Tex("B", font_size=30).move_to(B_sq.get_center() + 0.2 * DL)
        C_sq_label = Tex("C", font_size=30).move_to(C_sq.get_center() + 0.2 * DR)
        D_sq_label = Tex("D", font_size=30).move_to(D_sq.get_center() + 0.2 * UR)
        
        AB_sq = Line(A_sq, B_sq, color=BLUE)
        BC_sq = Line(B_sq, C_sq, color=BLUE)
        CD_sq = Line(C_sq, D_sq, color=BLUE)
        DA_sq = Line(D_sq, A_sq, color=BLUE)
        
        AC_sq = Line(A_sq, C_sq, color=RED)
        
        ABC_sq = Polygon(A_sq.get_center(), B_sq.get_center(), C_sq.get_center(), color=RED).set_stroke(opacity=0).set_fill(RED, 0.5)
        
    
        self.play(LaggedStart(
            FadeIn(A), FadeIn(B), FadeIn(C), FadeIn(D),
            run_time=0.8, lag_ratio=0.3
        ))
        self.play(LaggedStart(
            Create(AB), Create(BC), Create(CD), Create(DA),
            run_time=1.4, lag_ratio=0.2
        ))
        self.play(LaggedStart(
            FadeIn(A_label), FadeIn(B_label), FadeIn(C_label), FadeIn(D_label),
            run_time=1.4, lag_ratio=0.3
        ))
        self.play(LaggedStart(
            FadeIn(A_1), FadeIn(B_1), FadeIn(C_1), FadeIn(D_1),
            run_time=0.8, lag_ratio=0.3 
        ))
        self.play(LaggedStart(
            Create(AA_1), Create(BB_1), Create(CC_1), Create(DD_1),
            run_time=1.4, lag_ratio=0.2 
        ))
        self.play(LaggedStart(
            Create(A_1B_1), Create(B_1C_1), Create(C_1D_1), Create(D_1A_1),
            run_time=1.4, lag_ratio=0.2
        ))
        self.play(LaggedStart(
            FadeIn(A_1_label), FadeIn(B_1_label), FadeIn(C_1_label), FadeIn(D_1_label),
            run_time=0.8, lag_ratio=0.3 
        ))
        
        self.wait()
        
        self.play(LaggedStart(
            Write(AB_label), Write(BC_label), Write(AA_1_label),
            run_time=1.5, lag_ratio=0.3
        ))
        
        self.wait(2)
        
        self.play(
            AB.animate.set_color(RED), BC.animate.set_color(RED), BB_1.animate.set_color(RED),
            Create(AC), Create(AB_1), Create(CB_1)
        )
        
        self.play(FadeIn(pyramid), run_time=1.5)
        
        self.wait(2)
        
        self.play(AA_1_label.animate.move_to(BB_1.get_center() + 0.2 * LEFT))
        self.wait(1.5)
        
        formula_1 = MathTex('V', '=', r'\dfrac{1}{3}', '\cdot', 'h', '\cdot', 'S').shift(5 * LEFT + 1.15 *  UP)
        formula_2 = MathTex('V', '=', r'\dfrac{1}{3}', '\cdot', '4', '\cdot', 'S').shift(5 * LEFT + 1.15 *  UP)
        formula_3 = MathTex('V', '=', r'\dfrac{1}{3}', '\cdot', '4', '\cdot', '4.5').shift(5 * LEFT + 1.15 *  UP)
        formula_4 = MathTex('V', '=', r'\dfrac{1}{3}', '\cdot', '18').shift(5 * LEFT + 1.15 *  UP)
        formula_5 = MathTex('V', '=', r'\dfrac{18}{3}').shift(5 * LEFT + 1.15 *  UP)
        formula_5 = MathTex('V', '=', '6').shift(5 * LEFT + 1.15 *  UP)
        
        
        
        info_1 = MathTex('h', '=', 'BB_1').shift(5 * LEFT).set_opacity(0.65)
        info_2 = MathTex('h', '=', '4').shift(5 * LEFT).set_opacity(0.65)
        info_3 = MathTex('S', '=', '\, ?').shift(5 * LEFT + 0.8 * DOWN).set_opacity(0.65)
        info_4 = MathTex('S', '=', '4.5').shift(5 * LEFT + 0.8 * DOWN).set_opacity(0.65)
        
        
        self.play(Write(formula_1))
        self.wait(0.5)
        self.play(Write(info_1))
        self.wait(0.5)
        self.play(Transform(info_1, info_2))
        self.wait(0.7)
        self.play(TransformMatchingTex(formula_1, formula_2))
        self.wait(0.7)
        self.play(Write(info_3))
    
        
        self.play(LaggedStart(
            FadeIn(VGroup(A_sq, A_sq_label)), 
            FadeIn(VGroup(B_sq, B_sq_label)),
            FadeIn(VGroup(C_sq, C_sq_label)), 
            FadeIn(VGroup(D_sq, D_sq_label)), 
            lag_ratio=0.4 
        ))
        
        self.play(LaggedStart(
            Create(AB_sq),
            Create(BC_sq),
            Create(CD_sq),
            Create(DA_sq),
        ))
        
        self.wait(0.1)
        
        self.play(
            AB_sq.animate.set_color(RED),
            BC_sq.animate.set_color(RED),
            Create(AC_sq),
            FadeIn(ABC_sq)
        )
        
        info_sq = MathTex('S', '=', r'\dfrac{1}{2}', '\cdot', '3', '\cdot', '3').move_to(BC_sq.get_center() + 0.9 * DOWN).scale(0.7)
        info_sq_1 = MathTex('S', '=', r'\dfrac{1}{2}', '\cdot', '9').move_to(BC_sq.get_center() + 0.9 * DOWN).scale(0.7)
        info_sq_2 = MathTex('S', '=', r'\dfrac{9}{2}').move_to(BC_sq.get_center() + 0.9 * DOWN).scale(0.7)
        info_sq_3 = MathTex('S', '=', '4.5').move_to(BC_sq.get_center() + 0.9 * DOWN).scale(0.7)
        
        
        self.play(Write(info_sq))
        self.wait(1.3)
        self.play(TransformMatchingTex(info_sq, info_sq_1), run_time=0.7)
        self.wait(0.8)
        self.play(TransformMatchingTex(info_sq_1, info_sq_2), run_time=0.7)
        self.wait(0.6)
        self.play(TransformMatchingTex(info_sq_2, info_sq_3), run_time=0.7)
        
        self.wait()
        
        self.play(TransformMatchingTex(info_3, info_4))
        self.wait(0.8)
        self.play(TransformMatchingTex(formula_2, formula_3))
        self.wait(0.8)
        self.play(TransformMatchingTex(formula_3, formula_4))
        self.wait(0.8)
        self.play(TransformMatchingTex(formula_4, formula_5))
        self.wait()
        
        self.wait(0.5)
        self.play(LaggedStart(
            FadeOut(ABC_sq),
            FadeOut(VGroup(
                AB_sq, BC_sq, CD_sq, DA_sq, AC_sq
            )),
            FadeOut(VGroup(
                A_sq, B_sq, C_sq, D_sq,
                A_sq_label, B_sq_label, C_sq_label, D_sq_label
            )),
            FadeOut(info_sq_3),
            lag_ratio=0.08
        ))
        self.wait(0.2)
        
        ans = Tex("Answer: $6$").shift(5 * LEFT + 1.9 * DOWN).scale(1.2)
        box = SurroundingRectangle(ans, buff=0.15)
        
        self.play(Write(ans))
        self.wait(0.4)
        self.play(ShowPassingFlash(box))
        self.wait()

        
        self.wait(3)
            

class PeopleGroup(VGroup):
    def __init__(self, names):
        super().__init__()
        self.rectangle = Rectangle(width=1.5, height=0.75).set_stroke(color=WHITE, width=2)
        self.names = VGroup()
        for name in names:
            self.names.add(Tex(name, font_size=24))
        self.names.arrange_in_grid(1, len(names), buff=0.1)
        self.add(self.rectangle, self.names)


class Task_4_probability(Scene):
    def construct(self):
        task_text = Tex(r"There are 20 people in the group of tourists. They are thrown into a hard to reach area by " + 
                        r"a helicopter of several dates of 5 people per flight. The order in which the helicopter transports " + 
                        r"tourists is random. Find the probability that the tourist Alex will fly the second flight of the helicopter."
                       , width=250)
        rectangle = SurroundingRectangle(task_text, buff=0.3)
        task_label = Tex("Task 4. Probability").scale(1.2).to_edge(UP)

        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text, run_time=5))
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.3 * UP).scale(0.6),
        ))

        groups_label = Tex("Groups", font_size=38).shift(1.2 * UP)
        groups = VGroup(
            PeopleGroup(["*" for _ in range(5)]),
            PeopleGroup(["*", "A", "*", "*", "*"]),
            PeopleGroup(["*", "*", "*", "*", "*"]),
            PeopleGroup(["*", "*", "*", "*", "*"]),
        ).arrange(RIGHT, buff=0.35).shift(0.1 * UP)


        self.play(Write(groups_label))
        self.wait(0.2)
        for group in groups:
            self.play(FadeIn(group))
            self.wait(0.3)
        
        alex_here_label = Tex("Alex is here", font_size=26).shift(0.5 * DOWN + groups[1].get_center()[0] * RIGHT).set_opacity(0.5)
        self.play(Write(alex_here_label))
        self.wait(0.6)
        self.play(FadeOut(alex_here_label))
        self.wait(3)

        info = Tex(r'P(\text{“Alex will fly the second flight"}) = $\frac{1}{4}$', font_size=38).shift(DOWN)
        info[0][2:28].set_color(BLUE)
        self.play(Write(info))
        self.wait(0.5)
        
        answer = Tex(r"Answer: $\frac{1}{4}$", font_size=42).shift(1.8 * DOWN)
        answer_rectangle = SurroundingRectangle(answer, buff=0.15).shift(0.035 * DOWN)
        self.play(Write(answer))
        self.wait(0.3)
        self.play(Create(answer_rectangle))


        self.wait(3)
        

class Task_5_probability(Scene):
    def construct(self):
        task_text = Tex(r"The room is illuminated by three lamps. The probability of burning out each lamp " +
                        r"is 0.4. The lamps are burned independently of each other. Find the " +
                        r"probability that at least one lamp will not burn.",
                        width=250)
        rectangle = SurroundingRectangle(task_text, buff=0.3)
        task_label = Tex("Task 5. Probability").scale(1.2).to_edge(UP)

        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text, run_time=5))
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.3 * UP).scale(0.6),
        ))

        info_1 = Tex(r"P(\text{“At least one will not burn out”}) $= 1 - $ P(\text{“Everyone will burn out”})", font_size=38).shift(1.2 * UP)
        info_2 = Tex(r"P(\text{“Everyone will burn out”}) $= 0.4^3 = 0.064$", font_size=38).shift(0.5 * UP)
        info_3 = Tex(r"P(\text{“At least one will not burn out”}) $= 1 - 0.064 = 0.936$", font_size=38).shift(0.2 * DOWN)

        info_1[0][2:28].set_color(BLUE)
        info_1[0][34:55].set_color(RED)
        info_2[0][2:23].set_color(RED)
        info_3[0][2:28].set_color(BLUE)

        answer = Tex(r"Answer: $0.936$", font_size=42).shift(DOWN)  
        answer_rectangle = SurroundingRectangle(answer, buff=0.15).shift(0.035 * DOWN)

        self.play(Write(info_1))
        self.wait()
        self.play(Write(info_2))
        self.wait()
        self.play(Write(info_3))
        self.wait()
        self.play(Write(answer))
        self.wait(0.3)
        self.play(Create(answer_rectangle))

        self.wait(3)
        self.play(FadeOut(VGroup(
            info_1, info_2, info_3, answer, answer_rectangle,
            task_text, rectangle
        )))


class Task_6_equation(Scene):
    def construct(self):
        task_text = Tex(r"Solve the equation $\sqrt{2x + 37} = 7$ in real numbers.", width=250)
        rectangle = SurroundingRectangle(task_text, buff=0.3)
        task_label = Tex("Task 6. Equation").scale(1.2).to_edge(UP)

        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text, run_time=5))
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.3 * UP).scale(0.6),
        ))

        solution_1 = MathTex(r"\sqrt{2x + 37} = 7", substrings_to_isolate="x", font_size=38).shift(2 * UP)
        solution_2 = MathTex(r"2x + 37 = 49", substrings_to_isolate="x", font_size=38).shift(1.2 * UP)
        solution_3 = MathTex(r"2x = 12", substrings_to_isolate="x", font_size=38).shift(0.6 * UP)
        solution_4 = MathTex(r"x = 6", substrings_to_isolate="x", font_size=38).shift(0.1 * DOWN)

        solution_1.set_color_by_tex("x", BLUE)
        solution_2.set_color_by_tex("x", BLUE)
        solution_3.set_color_by_tex("x", BLUE)
        solution_4.set_color_by_tex("x", BLUE)
        
        answer = Tex(r"Answer: $x = 6$", font_size=42).shift(DOWN)
        answer_rectangle = SurroundingRectangle(answer, buff=0.15).shift(0.035 * DOWN)

        self.play(Write(solution_1))
        self.wait()
        self.play(Write(solution_2))
        self.wait()
        self.play(Write(solution_3))
        self.wait()
        self.play(Write(solution_4))
        self.wait(1.5)

        self.play(Write(answer))
        self.wait(0.3)
        self.play(Create(answer_rectangle))

        self.wait(3)


class Task_7_calculations(Scene):
    def construct(self):
        task_text = Tex(r"Find the value of $2\sqrt{3} \cos^2{\dfrac{13 \pi}{12}} - \sqrt{3}$", width=250)
        rectangle = SurroundingRectangle(task_text, buff=0.3)
        task_label = Tex("Task 7. Calculations").scale(1.2).to_edge(UP)

        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text, run_time=5))
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.3 * UP).scale(0.6),
        ))

        task_1 = MathTex(r"2", r"\sqrt{3}", r"\cos^2{\left(", r"\dfrac{13 \pi}{12}", r"\right)}", r"-", r"\sqrt{3}").scale(
            1.2).shift(0.2 * DOWN)
        task_1.set_color_by_tex("\pi", BLUE)


        self.play(Write(task_1))
        self.wait(0.3)
        self.play(task_1.animate.shift(3.2 * LEFT))

        info_1 = Tex(r"$\cos{(\pi + x)} = -\cos{x}$", font_size=32).shift(3.8 * RIGHT + 0.3 * UP).set_opacity(0.75)
        info_2 = Tex(r"$\cos^2{(\pi + x)} = \cos^2{x}$", font_size=32).shift(3.8 * RIGHT + 0.6 * DOWN).set_opacity(0.75)

        self.play(Write(info_1))
        self.wait(0.2)
        self.play(Write(info_2))
        self.wait(0.5)

        task_2 = MathTex(r"2", r"\sqrt{3}", r"\cos^2{\left(", r"\pi + \dfrac{\pi}{12}", r"\right)}", r"-", r"\sqrt{3}").scale(
            1.2).move_to(task_1.get_center())
        task_2.set_color_by_tex("\pi", BLUE)

        self.play(TransformMatchingTex(task_1, task_2))
        self.wait(0.5)

        task_3 = MathTex(r"2", r"\sqrt{3}", r"\cos^2{", r"\dfrac{\pi}{12}", r"}", r"-", r"\sqrt{3}").scale(
            1.2).move_to(task_2.get_center())
        task_3.set_color_by_tex("\pi", BLUE)

        self.play(TransformMatchingTex(task_2, task_3))
        self.wait(0.5)

        self.play(FadeOut(VGroup(info_1, info_2)))

        info_3 = Tex("$\cos^2{x} = \dfrac{1 + \cos{2x}}{2}$", font_size=32).shift(3.8 * RIGHT + 0.1 * DOWN).set_opacity(0.75)
        self.play(Write(info_3))
        self.wait(0.5)

        task_4 = MathTex(r"2", r"\sqrt{3}", r"\left(", r"\dfrac{1 + \cos{\left(2 \cdot \dfrac{\pi}{12}\right)}}{2}", 
                         r"\right)", r"-", r"\sqrt{3} + 1").scale(
            1.1).move_to(task_3.get_center()).shift(0.15 * RIGHT)
        task_4[3][1:].set_color(BLUE)
        task_4[4][0].set_color(BLUE)

        self.play(TransformMatchingTex(task_3, task_4))
        self.wait(.5)

        task_5 = MathTex(r"2", r"\sqrt{3}", r"\left(", r"\dfrac{1 + \cos{\dfrac{\pi}{6}}}{2}",
                         r"\right)", r"- \sqrt{3}", "1", "1").scale(
            1.1).move_to(task_3.get_center()).shift(0.15 * RIGHT)
        task_5[3][1:].set_color(BLUE)
        task_5[4][0].set_color(BLUE)

        self.play(TransformMatchingTex(task_4, task_5))
        self.wait(1.5)

        self.play(FadeOut(info_3))
        self.wait(0.5)

        info_4 = Tex(r"$\cos{\dfrac{\pi}{6}} = \dfrac{\sqrt{3}}{2}$").set_opacity(0.75).shift(3.8 * RIGHT + 0.1 * DOWN)
        self.play(Write(info_4))
        self.wait(0.5)

        task_6 = MathTex(r"2", r"\sqrt{3}", r"\left(", r"\dfrac{1 + \dfrac{\sqrt{3}}{2}}{2}", r"\right) - \sqrt{3}", "111111").scale(
                1.1).move_to(task_5.get_center()).shift(0.15 * RIGHT)
        
        self.play(TransformMatchingTex(task_5, task_6))
        self.wait(1.5)

        self.play(FadeOut(info_4))
        self.play(task_6.animate.move_to(0.1 * DOWN))

        task_7 = MathTex(r"2", r"\sqrt{3}", r"\left(", r"\dfrac{\dfrac{2 + \sqrt{3}}{2}}{2}", r"\right) - \sqrt{3}", "111111").scale(
                1.1).move_to(task_6.get_center()).shift(0.15 * RIGHT)
        
        self.play(ReplacementTransform(task_6, task_7))
        self.wait(1.5)

        task_8 = MathTex(r"2", r"\sqrt{3}", r"\left(", r"\dfrac{2 + \sqrt{3}}{4}", r"\right) - \sqrt{3}").scale(
                1.1).move_to(task_7.get_center()).shift(0.15 * RIGHT)
        
        self.play(ReplacementTransform(task_7, task_8))
        self.wait(1.5)

        task_9 = MathTex(r"\sqrt{3}", r"\left(\dfrac{2 + \sqrt{3}}{2}\right) - \sqrt{3}").scale(
                1.1).move_to(task_7.get_center()).shift(0.15 * RIGHT)
        
        self.play(ReplacementTransform(task_8, task_9))
        self.wait(1.5)

        task_10 = MathTex(r"\dfrac{2\sqrt{3} + 3}{2}", "" r"- \sqrt{3}").scale(1.1).move_to(task_7.get_center()).shift(0.15 * RIGHT)
        
        self.play(ReplacementTransform(task_9, task_10))
        self.wait(1.5)

        task_11 = MathTex(r"\dfrac{2\sqrt{3}}{2}", "+", r"\dfrac{3}{2}", r"-\sqrt{3}").scale(1.1).move_to(task_7.get_center()).shift(0.15 * RIGHT)

        self.play(ReplacementTransform(task_10, task_11))
        self.wait(1.5)

        task_12 = MathTex(r"\sqrt{3}", "+", r"\dfrac{3}{2}", r"-\sqrt{3}").scale(1.1).move_to(task_7.get_center()).shift(0.15 * RIGHT)

        self.play(TransformMatchingTex(task_11, task_12))
        self.wait(1.5)

        task_13 = MathTex("\dfrac{3}{2}").scale(1.1).move_to(task_7.get_center()).shift(0.15 * RIGHT)

        self.play(TransformMatchingTex(task_12, task_13))
        self.wait(1.5)

        task_14 = MathTex("1.5").scale(1.1).move_to(task_7.get_center()).shift(0.15 * RIGHT)

        self.play(ReplacementTransform(task_13, task_14))
        self.wait(1.5)

        rectangle = SurroundingRectangle(task_14, buff=0.15).shift(0.035 * DOWN)
        self.play(Create(rectangle))

        self.wait(3)
        

class Task_8_derivative(Scene):
    def construct(self):
        task_text = Tex(
                        'The figure shows a graph of the $f\'(x)$ — derivative of the function $f(x)$ ' +
                        'defined in the interval $(-4; 7)$. At what point in the segment $[-2; 3]$ does the function $f(x)$ take on the greatest value?',
                        width=250)
        rectangle = SurroundingRectangle(task_text, buff=0.3)
        task_label = Tex("Task 8. Derivative").scale(1.2).to_edge(UP)

        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text, run_time=8))
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.6 * UP).scale(0.6),
        ))
        self.wait(1.5)
        
        path = VGroup(
            CubicBezier(
                [237.985, -211.8672, 0], [241.697, -202.8288, 0], [245.5038, -198.2608, 0], [249.3242, -198.2608, 0]
            ),
            CubicBezier(
                [249.3242, -198.2608, 0], [253.1763, -198.2608, 0], [256.8116, -216.4026, 0], [260.6635, -216.4026, 0]
            ),
            CubicBezier(
                [260.6635, -216.4026, 0], [264.4632, -216.4026, 0], [268.3007, -218.4026, 0], [272.0029, -209.5992, 0]
            ),
            CubicBezier(
                [272.0029, -209.5992, 0], [275.825, -200.5104, 0], [279.3963, -180.1192, 0], [283.3419, -180.1192, 0]
            ),
            CubicBezier(
                [283.3419, -180.1192, 0], [287.2216, -180.1192, 0], [290.8495, -197.3496, 0], [294.6813, -202.796, 0]
            ),
            CubicBezier(
                [294.6813, -202.796, 0], [298.4342, -208.1304, 0], [302.2452, -201.9848, 0], [306.0204, -205.064, 0]
            ),
            CubicBezier(
                [306.0204, -205.064, 0], [309.9604, -208.2776, 0], [313.726, -221.3257, 0], [317.3596, -236.812, 0]
            ),
            CubicBezier(
                [317.3596, -236.812, 0], [321.0292, -252.4501, 0], [324.6988, -270.8276, 0], [328.6988, -270.8276, 0]
            ),
            CubicBezier(
                [328.6988, -270.8276, 0], [332.5916, -270.8276, 0], [336.146, -248.1504, 0], [340.038, -248.1504, 0]
            ),
            CubicBezier(
                [340.038, -248.1504, 0], [343.8284, -248.1504, 0], [347.5876, -254.9539, 0], [351.3772, -254.9539, 0]
            ),
            CubicBezier(
                [351.3772, -254.9539, 0], [355.1676, -254.9539, 0], [358.954, -252.682, 0], [362.7172, -248.1504, 0]
            )
        )
        path.move_to(ORIGIN)
        path.scale(0.05)
        path.set_stroke(YELLOW, width=5)
        
        plane = NumberPlane(
            x_range=[-5, 8],
            y_range=[-5, 7], 
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 1.5,
                "stroke_opacity": 0.5
            },
            ).scale(0.65)
        plane.shift(0.12 * RIGHT + 0.32 * DOWN)
        plane.set_z_index(-1)
        
        path.scale(1.144, about_point=plane.coords_to_point(0, 5))
        
        VGroup(plane, path).scale(0.65)
        
        y_axis = plane.get_axes()[1]
        y_axis.add_tip(tip_width=0.15, tip_length=0.15)

        x_axis = plane.get_axes()[0]
        x_axis.add_tip(tip_width=0.15, tip_length=0.15)
        

        plane_labels = plane.get_axis_labels(
            Tex("x").scale(0.7), Text("y").scale(0.45)
        )
        plane_labels[0].shift(0.2 * LEFT)
        plane_labels[1].shift(0.2 * DOWN)
        
        number_labels = VGroup(
            MathTex("0", font_size=30).move_to(plane.coords_to_point(0, 0, 0) + 0.2 * DL),
            MathTex("1", font_size=30).move_to(plane.coords_to_point(1, 0, 0) + 0.2 * DOWN),
            MathTex("-4", font_size=30).move_to(plane.coords_to_point(-4, 0, 0) + 0.2 * DOWN),
            MathTex("7", font_size=30).move_to(plane.coords_to_point(7, 0, 0) + 0.2 * UP),
        )
        
        dots = VGroup(
            Dot(plane.coords_to_point(-4, 2.1, 0), color=BLACK, radius=0.05).set_stroke(YELLOW, width=3),
            Dot(plane.coords_to_point(7, -1, 0), color=BLACK, radius=0.05).set_stroke(YELLOW, width=3),
        ).set_z_index(1)
        
        partial_path = VGroup(
            path[0].copy().pointwise_become_partial(path[5], 0.4, 1),
            path[0].copy().pointwise_become_partial(path[6], 0, 1),
            path[0].copy().pointwise_become_partial(path[7], 0, 1),
            path[0].copy().pointwise_become_partial(path[8], 0, 0.75),
        )
        partial_path.set_stroke(YELLOW, width=5)
        
        partial_axis = plane.axes[0].copy().shift(2.7 * RIGHT)
        partial_axis.scale(0.5, about_point=partial_axis.get_end())
        partial_axis.tip.scale(2)
        x_copy = plane_labels[0].copy().shift(2.7 * RIGHT)
        
        dot = Dot(plane.coords_to_point(3, 0, 0), color=YELLOW).shift(3.6 * RIGHT)  
        dot_label = MathTex("3", font_size=36).next_to(dot, UR, buff=0.1)
        
        
        dashed_line = DashedLine(Perpendicular(partial_axis, dot, length=2).get_end(),
                                 Perpendicular(partial_axis, dot, length=2, rotate=True).get_end(), 
                                 color=RED, dash_length=0.3).set_z_index(-1)
        
        self.play(FadeIn(VGroup(plane, y_axis, x_axis, plane_labels)), run_time=1.5)
        self.wait(0.7)
        self.play(FadeIn(number_labels))
        self.wait(0.5)
        self.play(FadeIn(dots[0]), run_time=0.7)
        self.play(LaggedStart(
            *[Create(curve) for curve in path],
            lag_ratio=0.9,
            run_time=1.2
        ))
        self.play(FadeIn(dots[1]), run_time=0.7)
        self.wait(1.5)
        self.play(Flash(plane.coords_to_point(3, 0, 0)))
        

        self.add(partial_path)
        self.play(
            VGroup(plane, y_axis, x_axis, plane_labels, number_labels, dots, path).animate.shift(2.7 * LEFT),
            partial_path.animate.shift(3.6 * RIGHT),
            FadeIn(VGroup(x_copy, partial_axis))
        )
        self.wait(2)
        
        self.play(FadeIn(VGroup(dot, dot_label)))
        self.wait()
        self.play(Create(dashed_line))
        self.wait(0.5)
        
        plus = MathTex("+", font_size=58).move_to(dashed_line.get_start() + 0.9 * LEFT + 0.2 * DOWN)
        minus = MathTex("-", font_size=58).move_to(dashed_line.get_start() + 0.9 * RIGHT + 0.2 * DOWN)  
        
        self.play(LaggedStart(
            FadeIn(plus),
            FadeIn(minus),
        ))
        self.wait(3)
        
        info = Tex("Answer: $3$").shift(3.45 * DOWN)
        box = SurroundingRectangle(info, buff=0.15)
        
        self.play(Write(info))
        self.play(ShowPassingFlash(box))
        self.wait(2)
                

class Task_9_calculations(Scene):
    def construct(self):
        task_text = Tex(r"To determine the effective temperature of stars, the Stefan-Boltzmann law is used, according to which $P=\sigma S T^4$, " +
                        r"where $P$ is the radiation power of the star (in Watts), " +  
                        r"$\sigma = 5.7 \cdot 10^{-8} \frac{W}{m^2 \cdot K^4}$ - constant. " +
                        r"$S$ is the surface area of the star (in square meters), and $T$ is the temperature (in Kelvins). " +
                        r"It is known that the surface area of a certain star is $\frac{1}{729} \cdot 10^{20} \, m^2$, " +
                        r"and its radiation power is $5.13 \cdot 10^{25}$ watts. Find the temperature of this star in Kelvins.",
                        width=250)
        rectangle = SurroundingRectangle(task_text, buff=0.3)
        task_label = Tex("Task 9. Calculations").scale(1.2).to_edge(UP)

        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text, run_time=8))
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.6 * UP).scale(0.6),
        ))
        self.wait(1.5)


        formula_1 = MathTex(r"P", r"=", r"\sigma", r"S", r"T^4", font_size=52).move_to(0.2 * DOWN)
        formula_1[4][0].set_color(BLUE)

        formula_2 = MathTex(r"P", r"=", r"5.7 \cdot 10^{-8} \frac{W}{m^2 \cdot K^4}", r"S", r"T^4", font_size=52).move_to(0.2 * DOWN)
        formula_2[4][0].set_color(BLUE)
        
        formula_3 = MathTex(r"P", r"=", r"5.7 \cdot 10^{-8} \frac{W}{m^2 \cdot K^4}", r"\frac{1}{729} \cdot 10^{20} \, m^2", r"T^4", font_size=52).move_to(0.2 * DOWN)
        formula_3[4][0].set_color(BLUE)

        formula_4 = MathTex(r"5.13 \cdot 10^{25}\, W", r"=", r"5.7 \cdot 10^{-8} \frac{W}{m^2 \cdot K^4}", r"\frac{1}{729} \cdot 10^{20} \, m^2", r"T^4", font_size=52).move_to(0.2 * DOWN)
        formula_4[4][0].set_color(BLUE)

        formula_5 = MathTex(
            r"5.13",
            r"\cdot",
            r"10^{25}\,",
            r"W",
            r"=",
            r"5.7",
            r"\cdot",
            r"10^{-8}"
            r"\frac{W}{m^2 \cdot K^4}",
            r"\frac{1}{729}",
            r"\cdot",
            r"10^{20} \,"
            r"m^2",
            r"T^4",
            font_size=52).move_to(0.2 * DOWN)
        formula_5[-1][0].set_color(BLUE)
        
        formula_6 = MathTex(
            r"5.13",
            r"\cdot",
            r"10^{25}\,",
            r"=",
            r"5.7",
            r"\cdot",
            r"10^{-8}"
            r"\frac{1}{K^4}",
            r"\frac{1}{729}",
            r"\cdot",
            r"10^{20} \,"
            r"T^4",
            font_size=52).move_to(0.2 * DOWN)
        formula_6[-1][0].set_color(BLUE)

        formula_7 = MathTex(
            r"5.13",
            r"\cdot",
            r"10^{25}\,",
            r"=",
            r"5.7",
            r"\cdot",
            r"10^{-8}"
            r"\frac{1}{K^4}",
            r"\frac{1}{729}",
            r"\cdot",
            r"10^{20} \,"
            r"T^4",
            font_size=52).move_to(0.2 * DOWN)
        formula_7[-1][0].set_color(BLUE)
        
        formula_8 = MathTex(
            r"5.13",
            r"\cdot",
            r"10^{25}\,",
            r"=",
            r"5.7",
            r"\cdot",
            r"\frac{1}{K^4}",
            r"\frac{1}{729}",
            r"\cdot",
            r"10^{12} \,"
            r"T^4",
            font_size=52).move_to(0.2 * DOWN)
        formula_8[-1][0].set_color(BLUE)
        formula_8[-2][0:].set_color(RED)
        formula_8[2][0:].set_color(RED)
        

        sigma = Tex(r"$\sigma = 5.7 \cdot 10^{-8} \frac{W}{m^2 \cdot K^4}$", font_size=42).move_to(2.3 * DOWN + 4.4 * LEFT).set_opacity(0.75)
        s = Tex(r"$S = \frac{1}{729} \cdot 10^{20} \, m^2$", font_size=42).move_to(2.3 * DOWN).set_opacity(0.75)
        p = Tex(r"$P = 5.13 \cdot 10^{25}\, W$", font_size=42).move_to(2.3 * DOWN + 4.4 * RIGHT).set_opacity(0.75)

        self.play(Write(formula_1))
        self.wait(2)

        self.play(Write(sigma))
        self.wait()
        self.play(Write(s))
        self.wait()
        self.play(Write(p))
        self.wait()

        self.wait()
        self.play(TransformMatchingTex(formula_1, formula_2))
        self.wait()
        self.play(TransformMatchingTex(formula_2, formula_3))
        self.wait()
        self.play(TransformMatchingTex(formula_3, formula_4))
        self.wait(2)

        self.play(FadeOut(VGroup(sigma, s, p)))
        self.wait()

        self.remove(formula_4)
        self.add(formula_5)

        self.play(TransformMatchingTex(formula_5, formula_6))
        self.wait()
        self.play(TransformMatchingTex(formula_6, formula_7))
        self.wait(0.75)
        self.play(formula_7[-2][0:].animate.set_color(RED), 
                  formula_7[2][0:].animate.set_color(RED),
                  formula_7[5][0:].animate.set_color(RED),
                  )
        self.wait(0.75)
        self.play(TransformMatchingTex(formula_7, formula_8))

        self.wait(3)


class Empty(Tex):
    def __init__(self):
        super().__init__("nan")
        self.set_color(BLACK)
        self.scale(0.1)


class Task_10_speed(Scene):
    def construct(self):
        task_text = Tex("The first pump fills the tank in 20 minutes, the second in 30 minutes, " +
                        "and the third in 1 hour. In how many minutes will three pumps fill the tank?",
                        font_size=36)
        rectangle = SurroundingRectangle(task_text, buff=0.3)
        task_label = Tex("Task 10. Speed").scale(1.2).to_edge(UP)

        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text, run_time=8))
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.6 * UP).scale(0.6),
        ))
        self.wait(1.5)
        

        
        table = MobjectTable(
            [
                [Empty(), Empty(), Empty()],
                [Empty(), Empty(), Empty()],
                [Empty(), Empty(), Empty()],
            ],
            row_labels=[Tex(r'\MakeUppercase{\romannumeral 1}'), Tex(r'\MakeUppercase{\romannumeral 2}'), Tex(r'\MakeUppercase{\romannumeral 3}')],
            col_labels=[Tex('W'), Tex('T'), Tex('V')],
            include_outer_lines=True
        )
        
        table.get_entries((1, 2)).set_color(RED)
        table.get_entries((1, 3)).set_color(BLUE)
        table.get_entries((1, 4)).set_color(GREEN)
        
        table.get_entries((2, 1)).set_color(YELLOW)
        table.get_entries((3, 1)).set_color(YELLOW)
        table.get_entries((4, 1)).set_color(YELLOW)
        
        
        self.play(FadeIn(table))
        for i in range(2, 5):
            pos = table.get_entries((i, 2)).get_center()
            self.play(
                Transform(
                    table.get_entries((i, 2)),
                    MathTex('1').move_to(pos)
                    )
                )
            self.wait(0.5)
        self.wait()
        
        minutes = ['20', '30', '60']
        for i in range(2, 5):
            pos = table.get_entries((i, 3)).get_center()
            self.play(
                Transform(
                    table.get_entries((i, 3)),
                    MathTex(minutes[i - 2]).move_to(pos)
                    )
                )
            self.wait(0.5)
            
        info_1 = MathTex('V', '=', r'\dfrac{W}{T}').shift(3.4 * DOWN)
        info_1[0].set_color(GREEN)
        info_1[2][:1].set_color(RED)
        info_1[2][2].set_color(BLUE)
        info_2 = MathTex('V', '=', r'\dfrac{1}{T}').shift(3.4 * DOWN)
        info_2[0].set_color(GREEN)
        info_2[2][2].set_color(BLUE)
        
        self.play(Write(info_1))
        self.wait(0.5)
        self.play(TransformMatchingTex(info_1, info_2))
        self.wait(0.5)
        
        speed = [r'\dfrac{1}{20}', r'\dfrac{1}{30}', r'\dfrac{1}{60}']
        for i in range(2, 5):
            pos = table.get_entries((i, 4)).get_center()
            self.play(
                Transform(
                    table.get_entries((i, 4)),
                    MathTex(speed[i - 2]).scale(0.85).move_to(pos)
                    )
                )
            self.wait(0.5)
        self.wait()
            
        info_3 = MathTex('V_{sum}', '=', r'\dfrac{1}{20} + \dfrac{1}{30} + \dfrac{1}{60}').shift(3.4 * DOWN)
        info_3[0].set_color(GREEN)
        info_4 = MathTex('V_{sum}', '=', r'\dfrac{3}{60} + \dfrac{2}{60} + \dfrac{1}{60}').shift(3.4 * DOWN)
        info_4[0].set_color(GREEN)
        info_5 = MathTex('V_{sum}', '=', r'\dfrac{6}{60}').shift(3.4 * DOWN)
        info_5[0].set_color(GREEN)
        info_6 = MathTex('V_{sum}', '=', r'\dfrac{1}{10}').shift(3.4 * DOWN)
        info_6[0].set_color(GREEN)
        
        self.play(Transform(info_2, info_3))
        self.wait(0.5)
        self.play(TransformMatchingTex(info_2, info_4))
        self.wait(0.5)
        self.play(TransformMatchingTex(info_4, info_5))
        self.wait(0.5)
        self.play(TransformMatchingTex(info_5, info_6))
        self.wait()
        self.play(info_6.animate.shift(1.5 * LEFT))
        self.wait(0.8)
        
        info_7 = MathTex('T', '=', '1', ':', '{V_{sum}}').shift(3.4 * DOWN + 1.5 * RIGHT)
        info_7[0].set_color(BLUE)
        info_7[4].set_color(GREEN)
        info_8 = MathTex('T', '=', '1', ':', r'\dfrac{1}{10}').shift(3.4 * DOWN + 1.5 * RIGHT)
        info_8[0].set_color(BLUE)
        info_9 = MathTex('T', '=', '10').shift(3.4 * DOWN + 1.5 * RIGHT)
        info_9[0].set_color(BLUE)
        
        self.play(Write(info_7))
        self.wait(0.5)
        self.play(TransformMatchingTex(info_7, info_8))
        self.wait(0.5)
        self.play(TransformMatchingTex(info_8, info_9))
        self.wait()
        self.play(FadeOut(info_6))
        self.wait(0.2)
        self.play(info_9.animate.shift(1.5 * LEFT))
        
        info_10 = Tex("Answer: $10$ minutes").shift(3.4 * DOWN)
        box = SurroundingRectangle(info_10)
        
        self.play(Transform(info_9, info_10))
        self.wait(0.2)
        self.play(ShowPassingFlash(box))
        self.wait()
        self.wait(3)
                    
          
class Task_11_functions(Scene):
    def construct(self):
        task_text = Tex(r'The figure shows the graph of the function $f(x)=a^x$. find $f(4)$',
                        width=250)
        rectangle = SurroundingRectangle(task_text, buff=0.3)
        task_label = Tex("Task 11. Functions").scale(1.2).to_edge(UP)

        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text, run_time=8))
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.6 * UP).scale(0.6),
        ))
        self.wait(1.5)
        
        plane = NumberPlane(
            x_range=(-5, 5, 1),
            y_range=(-2, 10, 1),
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 1.5,
                "stroke_opacity": 0.5
            },
        ).scale(0.5).shift(0.6 * DOWN)
        
        y_axis = plane.get_axes()[1]
        y_axis.add_tip(tip_width=0.15, tip_length=0.15)

        x_axis = plane.get_axes()[0]
        x_axis.add_tip(tip_width=0.15, tip_length=0.15)
        
        plane_labels = plane.get_axis_labels(
            Tex("x").scale(0.7), Text("y").scale(0.45)
        )
        plane_labels[0].shift(0.2 * LEFT)
        plane_labels[1].shift(0.2 * DOWN)
        
        number_labels = VGroup(
            MathTex("0", font_size=30).move_to(plane.coords_to_point(0, 0, 0) + 0.2 * DL),
            MathTex("1", font_size=30).move_to(plane.coords_to_point(1, 0, 0) + 0.2 * DOWN),
            MathTex("1", font_size=30).move_to(plane.coords_to_point(0, 1, 0) + 0.2 * LEFT),
            MathTex("3", font_size=30).move_to(plane.coords_to_point(0, 3, 0) + 0.2 * LEFT),
        )
        
        number_dots = VGroup(
            Dot(plane.coords_to_point(0, 1, 0)).set_color(YELLOW),
            Dot(plane.coords_to_point(1, 3, 0)).set_color(YELLOW),
        )
        
        graph = plane.plot(lambda x: pow(3, x), x_range=[-5, np.emath.logn(3, 10)]).set_color(YELLOW)
        
        self.play(FadeIn(VGroup(plane, plane_labels)))
        self.play(FadeIn(VGroup(number_labels)))
        self.wait()
        self.play(Create(graph))
        self.play(FadeIn(number_dots, lag_ratio=0.2))
        
        self.wait()
        
        self.play(Flash(number_dots[1]))
        self.wait(0.8)
        
        info_1 = MathTex('f(1)', '=', 'a', '^', '1').shift(5 * LEFT)
        info_2 = MathTex('3', '=', 'a', '^', '1').shift(5 * LEFT)
        info_3 = MathTex('a', '=', '3').shift(5 * LEFT)
        
        self.play(Write(info_1))
        self.wait()
        self.play(TransformMatchingTex(info_1, info_2))
        self.wait()
        self.play(TransformMatchingTex(info_2, info_3))
        self.wait()
        
        info_4 = MathTex('f(x)', '=', '3', '^', 'x').shift(5 * RIGHT)
        info_5 = MathTex('f(4)', '=', '3', '^', '4').shift(5 * RIGHT)
        info_6 = MathTex('f(4)', '=', '81').shift(5 * RIGHT)
        
        
        self.play(Write(info_4))
        self.wait()
        self.play(TransformMatchingTex(info_4, info_5))
        self.wait()
        self.play(TransformMatchingTex(info_5, info_6))
        self.wait(2)     
        
        ans = Tex("Answer: $81$").shift(5 * RIGHT)
        box = SurroundingRectangle(ans)
        
        self.play(TransformMatchingTex(info_6, ans))
        self.wait(0.2)
        self.play(ShowPassingFlash(box))
        self.wait()
        
        
        self.wait(3)
  

class Task_12_derivative(Scene):
    def construct(self):
        task_text = Tex(r'Find the minimum point of the function $y = 5x - \mathrm{ln}(x - 7)$',
                        width=250)
        rectangle = SurroundingRectangle(task_text, buff=0.3)
        task_label = Tex("Task 12. Derivative").scale(1.2).to_edge(UP)

        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text, run_time=8))
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.6 * UP).scale(0.6),
        ))
        self.wait(1.5)
        
        
        label_1 = MathTex('y', '=', '5x', '-', r'\mathrm{ln}(x - 7)').shift(2.7 * UP)
        label_1[0].set_color(YELLOW)
        
        label_res = MathTex('y\'', '=', '5', '-', r'\dfrac{1}{x - 7}').shift(1.75 * UP)
        
        label_2 = MathTex('y\'', '=').shift(1.75 * UP)
        label_2.shift((label_res[1].get_center() - label_2[1].get_center()) * RIGHT)
        label_2[0].set_color(YELLOW)
        
        label_3 = MathTex('y\'', '=', '5', r'\,-').shift(1.75 * UP)
        label_3.shift((label_res[1].get_center() - label_3[1].get_center()) * RIGHT)
        label_3[0].set_color(YELLOW)
        label_3[2].set_color(RED)
                
        label_4 = MathTex('y\'', '=', '5', '-', r'\dfrac{1}{x - 7}').shift(1.75 * UP)
        label_4.shift((label_res[1].get_center() - label_4[1].get_center()) * RIGHT)
        label_4[0].set_color(YELLOW)
        label_4[2].set_color(RED)
        label_4[4].set_color(BLUE)
        
        self.play(Write(label_1))
        self.wait(0.7)
        self.play(Write(label_2))
        self.wait(0.7)
        
        self.play(
            label_1[2].animate.set_color(RED),
            label_1[4].animate.set_color(BLUE),
        )
        
        info_1 = MathTex('(5x)\'', '=', '5', 'x\'')
        info_1[0][1:3].set_color(RED)
        
        info_2 = MathTex('(5x)\'', '=', '5')
        info_2[0][1:3].set_color(RED)
        
        self.play(Write(info_1))
        self.wait(0.7)
        self.play(TransformMatchingTex(info_1, info_2))
        self.wait(0.7)
        
        self.play(TransformMatchingTex(label_2, label_3))
        self.play(FadeOut(info_2))
        self.wait(0.7)
        
        info_3 = MathTex('(\mathrm{ln}(x - 7))\'', '=')
        info_3[0][1:8].set_color(BLUE)
        
        hint = MathTex(
            r"\text{Hint: } (\mathrm{ln}(f(x)))' = \dfrac{1}{f(x)} \cdot f'(x)", 
            substrings_to_isolate=["f(x)"]
        ).shift(2.7 * DOWN)
        hint.set_color_by_tex("f(x)", GREEN)
        hint[0][0:5].set_color(GRAY)
        box = SurroundingRectangle(hint, buff=0.15)

        line = Arrow(2.8 * LEFT, 2.8 * RIGHT, buff=0, stroke_width=4).shift(0.8 * DOWN)
        line.tip.scale(0.7)
        line.tip.shift(0.07 * LEFT)
        x_label = MathTex('x').move_to(line.get_end() + 0.15 * LEFT + 0.35 * UP)
        
        dot = Dot(line.get_center(), color=RED)
        
        graph = FunctionGraph(
            lambda x: 5 - 1 / (x - 7),
            x_range=[7.1, 13],
            color=RED,
        ).move_to(dot.get_center()).scale(0.3, about_point=dot.get_center()).shift(0.86 * RIGHT).set_z_index(-1)
        
        
        info_4 = MathTex('(\mathrm{ln}(x - 7))\'', '=', r'\dfrac{1}{x - 7}', r"\cdot (x - 7)'")
        info_4[0][1:8].set_color(BLUE)
        
        info_5 = MathTex('(\mathrm{ln}(x - 7))\'', '=', r'\dfrac{1}{x - 7}', '\cdot 1')
        info_5[0][1:8].set_color(BLUE)
        
        info_6 = MathTex('(\mathrm{ln}(x - 7))\'', '=', r'\dfrac{1}{x - 7}')
        info_6[0][1:8].set_color(BLUE)
        
        self.play(Write(info_3))
        self.wait(0.7)
        self.play(Write(hint))
        self.wait(0.2)
        self.play(ShowPassingFlash(box))
        self.wait()    
        self.play(TransformMatchingTex(info_3, info_4))
        self.wait(0.5)
        self.play(FadeOut(hint))
        self.wait(0.7)
        self.play(TransformMatchingTex(info_4, info_5))
        self.wait(0.7)
        self.play(TransformMatchingTex(info_5, info_6))
        self.wait(0.7)
        
        self.play(TransformMatchingTex(label_3, label_4))
        self.play(FadeOut(info_6))
        self.wait(2)
        
        info_7 = label_4.copy()
        
        self.add(info_7)
        self.play(info_7.animate.move_to(ORIGIN))
        self.wait()
        
        info_8 = MathTex('0', '=', '5', '-', r'\dfrac{1}{x - 7}')
        info_9 = MathTex(r'\dfrac{1}{x - 7}', '=', '5')
        info_10 = MathTex(r'\dfrac{1}{x - 7}', '=', r'\dfrac{5}{1}')
        info_11 = MathTex('1', '=', '5(x - 7)')
        info_12 = MathTex('1', '=', '5x - 35')
        info_13 = MathTex('36', '=', '5x')
        info_14 = MathTex('x', '=', '\dfrac{36}{5}')
        info_15 = MathTex('x', '=', '7.2')
        
        
        
        self.play(TransformMatchingTex(info_7, info_8))
        self.wait(0.7)
        self.play(TransformMatchingTex(info_8, info_9))
        self.wait(0.7)
        self.play(TransformMatchingTex(info_9, info_10))
        self.wait(1.5)
        self.play(TransformMatchingTex(info_10, info_11))
        self.wait(0.7)
        self.play(TransformMatchingTex(info_11, info_12))
        self.wait(0.7)
        self.play(TransformMatchingTex(info_12, info_13))
        self.wait(0.7)
        self.play(TransformMatchingTex(info_13, info_14))
        self.wait(0.7)
        self.play(TransformMatchingTex(info_14, info_15))
        self.wait()
        self.play(info_15.animate.shift(3 * DOWN))
        self.wait(1.5)
        
        self.play(Create(line))
        self.play(FadeIn(x_label))
        self.play(FadeIn(dot))
        self.play(Create(graph))
        self.wait()
        
        plus = MathTex("+").move_to(dot.get_center() + 1.4 * RIGHT + 1.3 * DOWN)
        minus = MathTex("-").move_to(dot.get_center() + 1.4 * LEFT + 1.3 * DOWN)
        
        self.play(LaggedStart(
            FadeIn(plus),
            FadeIn(minus),
        ))
        self.wait()
        
        info_16 = Tex("Answer: $x = 7.2$").shift(3 * DOWN)
        box = SurroundingRectangle(info_16)
        
        self.play(Transform(info_15, info_16))
        self.play(ShowPassingFlash(box))
        self.wait()

        
        self.wait(3)
        

class Task_13_trigonometry(Scene):
    def construct(self):
        task_text_1 = Tex(r'a) Solve equation $\sin2x - \cos(\pi - x) = 0$.', font_size=36)
        task_text_2 = Tex(r'b) Find all the roots of this equation belonging to the segment $\left[ -3.5\pi ; -2\pi \right]$', font_size=36).move_to(
            task_text_1.get_left() + 0.4 * DOWN)
    
        task_text_2.shift(0.5 * RIGHT * task_text_2.width)
        
        task_text = VGroup(task_text_1, task_text_2).move_to(ORIGIN)
        
        rectangle = SurroundingRectangle(task_text, buff=0.3)
        task_label = Tex("Task 13. Trigonometry").scale(1.2).to_edge(UP)

        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text, run_time=8))
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.6 * UP).scale(0.6),
        ))
        self.wait(1.5)
        
        task_1 = MathTex(r'\sin', '2x', '-', '\cos', '(\pi - x)', '=', '0', substrings_to_isolate="x").shift(0.5 * UP)
        task_2 = MathTex(r'\sin', '2x', '+', '\cos', 'x', '=', '0', substrings_to_isolate="x").shift(0.5 * UP)
        task_3 = MathTex(r'2', '\sin', 'x', '\cos', 'x', '+', '\cos', 'x', '=', '0', substrings_to_isolate="x").shift(0.5 * UP)
        task_4 = MathTex(r'\cos', 'x', '(', '2', '\sin', 'x', '+', '1', ')', '=', '0', substrings_to_isolate="x").shift(0.5 * UP)
        
        task_1.set_color_by_tex("x", YELLOW)
        task_2.set_color_by_tex("x", YELLOW)
        task_3.set_color_by_tex("x", YELLOW)
        task_4.set_color_by_tex("x", YELLOW)
        
        equivalence_1 = MathTex(r'\iff').shift(0.2 * DOWN).rotate(PI / 2).scale(0.8)
        
        task_5 = SystemOfEquations(
            MathTex("\cos", "x", "=", "0", substrings_to_isolate="x"),
            MathTex("2", r"\sin", "x", "+", "1", "=", "0", substrings_to_isolate="x"),
            is_bracket=True,
        ).shift(1.15 * DOWN)
        
        task_5.equations[0].set_color_by_tex("x", YELLOW)
        task_5.equations[1].set_color_by_tex("x", YELLOW)
        
        task_6 = SystemOfEquations(
            MathTex("\cos", "x", "=", "0"),
            MathTex("2", r"\sin", "x", "+", "1", "=", "0"),
            is_bracket=True,
        ).shift(2 * UP)
        
        task_6.equations[0].set_color(BLUE)
        task_6.equations[1].set_color(RED)     
        
        task_7 = MathTex(r'\cos', 'x', '=', '0').shift(UP + 3 * LEFT).set_color(BLUE)
        equivalence_2 = MathTex(r'\iff').rotate(PI / 2).scale(0.8).move_to(0.3 * UP + 3 * LEFT)
        task_8 = MathTex('x', '=', r'\dfrac{\pi}{2}', '+', '\pi k', r', \, k \in \mathbb{Z}').shift(0.6 * DOWN + 3 * LEFT)
        
        task_9 = MathTex(r'2', r'\sin', 'x', '+', '1', '=', '0').shift(UP + 3 * RIGHT).set_color(RED)
        task_10 = MathTex(r'2', r'\sin', 'x', '=', '-1').shift(UP + 3 * RIGHT).set_color(RED)
        task_11 = MathTex(r'\sin', 'x', '=', r'-\dfrac{1}{2}').shift(UP + 3 * RIGHT).set_color(RED)
        equivalence_3 = MathTex(r'\iff').rotate(PI / 2).scale(0.8).move_to(0.3 * UP + 3 * RIGHT)
        task_12 = SystemOfEquations(
            MathTex('x', '=', r'-\dfrac{\pi}{6}', '+', '2\pi k', r', \, k \in \mathbb{Z}'),
            MathTex('x', '=', r'-\dfrac{5\pi}{6}', '+', '2\pi k', r', \, k \in \mathbb{Z}'),
            is_bracket=True,
        ).shift(1.25 * DOWN + 3 * RIGHT)
        
        task_13 = SystemOfEquations(
            MathTex('x', '=', r'\dfrac{\pi}{2}', '+', '\pi k', r', \, k \in \mathbb{Z}'),
            MathTex("2", r"\sin", "x", "+", "1", "=", "0"),
            is_bracket=True,
        ).shift(1.7 * UP)
        
        task_13.equations[1].set_color(RED)    
        
        system = SystemOfEquations(
            MathTex('x', '=', r'\dfrac{\pi}{2}', '+', '\pi k', r', \, k \in \mathbb{Z}'),
            MathTex('x', '=', r'-\dfrac{\pi}{6}', '+', '2\pi k', r', \, k \in \mathbb{Z}'),
            MathTex('x', '=', r'-\dfrac{5\pi}{6}', '+', '2\pi k', r', \, k \in \mathbb{Z}'),
            is_bracket=True,
        ).shift(UP)
        
        
   
                        
        self.play(Write(task_1))
        self.wait()
        self.play(TransformMatchingTex(task_1, task_2))
        self.wait()
        self.play(TransformMatchingTex(task_2, task_3))
        self.wait()
        self.play(TransformMatchingTex(task_3, task_4))
        self.wait()
        self.play(FadeIn(equivalence_1))
        self.wait()
        self.play(FadeIn(task_5))
        self.wait()
        self.play(FadeOut(VGroup(task_4, equivalence_1)))
        self.wait(0.5)
        self.play(task_5.animate.move_to(2 * UP))
        self.wait()
        self.play(TransformSystem(task_5, task_6))
        self.wait(1.5)
        
        self.play(LaggedStart(
            Write(task_7),
            Write(task_9)
        ))
        self.wait()
    
        self.play(FadeIn(equivalence_2))
        self.wait(0.3)
        self.play(Write(task_8))
        self.wait()
        
        self.play(TransformMatchingTex(task_9, task_10))
        self.wait()
        self.play(TransformMatchingTex(task_10, task_11))
        self.wait()
        self.play(FadeIn(equivalence_3))
        self.wait(0.3)
        self.play(FadeIn(task_12))
        self.wait(1.5)
        
        left = VGroup(task_7, equivalence_2, task_8)
        right = VGroup(task_11, equivalence_3, task_12)
        
        self.play(
            left.animate.scale(0.6).shift(2.25 * DOWN),
            right.animate.scale(0.6).shift(2 * DOWN)
        )
        self.wait()
        
        self.play(TransformSystem(task_6, task_13))
        self.wait()
        self.play(TransformSystem(task_13, system))
        self.wait()
        self.play(FadeOut(VGroup(left, right)))
        self.wait(3)
        
        
        circle = UnitCircle(point=-3.5 * PI, fractions=False).move_to(3 * RIGHT).change_right_point()
        arc = circle.get_arc(-3.5 * PI, -2 * PI, color=YELLOW).set_z_index(-1)
        extra_arc = circle.get_arc(-4 * PI, -3.5 * PI, color=BLUE).set_z_index(-1)
        
        self.play(system.animate.move_to(3 * LEFT).scale(0.75))
        self.wait()
        self.play(FadeIn(circle))
        self.play(circle.animate.show_labels())
        self.wait()
        
        info_segment = MathTex("x", "\in", r"\left[ -3.5\pi ; -2\pi \right]").shift(3 * DOWN)
        self.play(Write(info_segment))
        self.wait(0.5)
        self.play(Create(arc))
        self.wait()
        
        circle.circle.set_stroke(opacity=0)
        self.add(extra_arc)
        
        self.play(
            extra_arc.animate.set_stroke(opacity=0.5),
            circle.right_label.animate.set_opacity(0.6),
            circle.left_label.animate.set_opacity(0.6),
            circle.up_label.animate.set_opacity(0.6),
            circle.down_label.animate.set_opacity(0.6),
            circle.up.animate.set_opacity(0.6),
            circle.down.animate.set_opacity(0.6),
            circle.right.animate.set_opacity(0.6),
            circle.left.animate.set_opacity(0.6),
            )    
        
        dots = VGroup()
        labels = VGroup() 
        
        self.play(
            system.equations[1].animate.set_opacity(0.3),
            system.equations[2].animate.set_opacity(0.3),
        )
        
        dots.add(Dot(circle.point_at_angle(-3.5 * PI), color=GREEN))
        self.play(FadeIn(dots[0]), circle.up_label.animate.set_opacity(1))
        self.wait(0.3)
        self.play(Flash(dots[0]), run_time=0.8)
        self.wait(0.35)
        
        dots.add(Dot(circle.point_at_angle(-2.5 * PI), color=GREEN))
        self.play(FadeIn(dots[1]), circle.down_label.animate.set_opacity(1))
        self.wait(0.3)
        self.play(Flash(dots[1]), run_time=0.8)
        self.wait(0.35)
        
        self.wait()
        self.play(
            system.equations[0].animate.set_opacity(0.3),
            system.equations[1].animate.set_opacity(1)
        )
        self.wait(0.5)
        
        dots.add(Dot(circle.point_at_angle(-PI / 6 - 4 * PI), color=GREEN))
        labels.add(MathTex(r'-', '\dfrac{\pi}{6}', '-', '4 \pi', font_size=28).move_to(dots[2].get_center() + 0.7 * RIGHT + 0.1 * DOWN))
        
        self.play(FadeIn(VGroup(dots[2], labels[0])))
        self.wait(0.3)
        self.play(Flash(dots[2]), run_time=0.8)
        self.wait(0.5)
        self.play(Transform(labels[0], 
                            MathTex(r'-', '\dfrac{\pi}{6}', '-', '\dfrac{24 \pi}{6}', font_size=28).move_to(dots[2].get_center() + 0.75 * RIGHT + 0.1 * DOWN)))
        self.wait(0.5)
        self.play(Transform(labels[0], 
                            MathTex(r'-', '\dfrac{25 \pi}{6}', font_size=28).move_to(dots[2].get_center() + 0.45 * RIGHT + 0.1 * DOWN)))
        self.wait(0.5)
        
        self.play(
            system.equations[1].animate.set_opacity(0.3),
            system.equations[2].animate.set_opacity(1)
        )
        self.wait(0.5)
        
        self.wait()
        
        dots.add(Dot(circle.point_at_angle(-5 * PI / 6 - 4 * PI), color=GREEN))
        labels.add(MathTex(r'-', '\dfrac{5 \pi}{6}', '-', '4 \pi', font_size=28).move_to(dots[3].get_center() + 0.8 * LEFT + 0.1 * DOWN))
        
        self.play(FadeIn(VGroup(dots[3], labels[1])))
        self.wait(0.3)
        self.play(Flash(dots[3]), run_time=0.8)
        self.wait(0.5)
        self.play(Transform(labels[1], 
                            MathTex(r'-', '\dfrac{5 \pi}{6}', '-', '\dfrac{24 \pi}{6}', font_size=28).move_to(dots[3].get_center() + 0.85 * LEFT + 0.1 * DOWN)))
        self.wait(0.5)
        self.play(Transform(labels[1], 
                            MathTex(r'-', '\dfrac{29 \pi}{6}', font_size=28).move_to(dots[3].get_center() + 0.55 * LEFT + 0.1 * DOWN)))
        self.wait()
        
        self.play(FadeOut(VGroup(system, info_segment)))
        self.play(VGroup(circle, arc, extra_arc, dots, labels).animate.move_to(ORIGIN))
        self.wait(0.5)
        
        roots_res = MathTex("\Biggl\{", '-3.5 \pi,', '-\dfrac{29 \pi}{6}', '-2.5 \pi', '-\dfrac{25 \pi}{6}', '\Biggr\}', font_size=36).move_to(3 * DOWN)
        roots_1 = MathTex("\Biggl\{", font_size=36)
        roots_2 = MathTex("\Biggl\{",'-3.5 \pi', font_size=36)
        roots_3 = MathTex("\Biggl\{",'-3.5 \pi', '; \, -\dfrac{29 \pi}{6}', font_size=36)
        roots_4 = MathTex("\Biggl\{",'-3.5 \pi', '; \, -\dfrac{29 \pi}{6}', '; \, -2.5 \pi', font_size=36)
        roots_5 = MathTex("\Biggl\{",'-3.5 \pi', '; \, -\dfrac{29 \pi}{6}', '; \, -2.5 \pi', '; \, -\dfrac{25 \pi}{6}', '\Biggr\}', font_size=36)
        
        roots_1.move_to(roots_res.get_center() + (roots_res.width - roots_1.width) * LEFT / 2)
        roots_2.move_to(roots_res.get_center() + (roots_res.width - roots_2.width) * LEFT / 2)
        roots_3.move_to(roots_res.get_center() + (roots_res.width - roots_3.width) * LEFT / 2)
        roots_4.move_to(roots_res.get_center() + (roots_res.width - roots_4.width) * LEFT / 2)
        roots_5.move_to(roots_res.get_center() + (roots_res.width - roots_5.width) * LEFT / 2)
        
        self.play(Write(roots_1))
        self.wait(0.3)
        self.play(Flash(dots[0]), TransformMatchingTex(roots_1, roots_2))
        self.wait(0.3)
        self.play(Flash(dots[3]), TransformMatchingTex(roots_2, roots_3))
        self.wait(0.3)
        self.play(Flash(dots[1]), TransformMatchingTex(roots_3, roots_4))
        self.wait(0.3)
        self.play(Flash(dots[2]), TransformMatchingTex(roots_4, roots_5))
        
        
        answer = Tex("Answer: ", font_size=38).move_to(3 * DOWN)
        answer_res = Tex(r"Answer: $\Biggl\{ -3.5 \pi, \, -\dfrac{29 \pi}{6}, \, -2.5 \pi, \, -\dfrac{25 \pi}{6} \Biggr\}$", font_size=37).next_to(3 * DOWN)
        answer.shift((answer_res.width - answer.width) * LEFT / 2 + 0.2 * RIGHT)
        
        self.play(
            roots_5.animate.shift((answer_res.width - roots_5.width) * RIGHT / 2),
            Write(answer)
        )
        self.wait(0.7)
        
        box = SurroundingRectangle(VGroup(answer, roots_5))
        self.play(ShowPassingFlash(box), run_time=1.3)
        self.wait(3)
        

class Task_14_stereometry(ThreeDScene):
    def construct(self):

        task_text_1 = Tex(r'In a regular tetrahedron $ABCD$ the points $M$ and $N$ are the midpoints of the edges $AB$ and $CD$ ' +
                          r'respectively. The plane $\alpha$ is perpendicular to $MN$ and intersects $BC$ at the point $K$ ',
                            font_size=32)
        task_text_2 = Tex(r'a) Prove that the line $MN$ is perpendicular to the edges $AB$ and $CD$',
                          font_size=32).move_to(task_text_1.get_left() + 0.9 * DOWN)
        task_text_3 = Tex(r'b) Find the cross-sectional area of the tetrahedron $ABCD$ by the plane $\alpha$ if it is known that $BK=1$, $KC=5$',
                          font_size=32).move_to(task_text_1.get_left() + 1.55 * DOWN)
        
        task_text_2.shift(0.5 * RIGHT * task_text_2.width)
        task_text_3.shift(0.5 * RIGHT * task_text_3.width)

        
        task_text = VGroup(task_text_1, task_text_2, task_text_3)   
        
        rectangle = SurroundingRectangle(task_text, buff=0.3)
        task_label = Tex("Task 14. Stereometry").scale(1.2).to_edge(UP)

        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text, run_time=8))
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.8 * UP).scale(0.6),
        ))
        self.wait(1.5)


        
        
        edge = 4.1
        tetrahedron = Tetrahedron(edge).move_to(1.6 * DOWN)
        tetrahedron.rotate(angle=45 * DEGREES, axis=OUT) 
        tetrahedron.rotate(angle=-25 * DEGREES, axis=RIGHT)
        tetrahedron.rotate(angle=15 * DEGREES, axis=UP)
        tetrahedron.shift(0.35 * RIGHT)

        A = Dot3D(tetrahedron.extract_face_coords()[2][1]).set_z_index(9)
        B = Dot3D(tetrahedron.extract_face_coords()[3][2]).set_z_index(9)
        C = Dot3D(tetrahedron.extract_face_coords()[1][0]).set_z_index(9)
        D = Dot3D(tetrahedron.extract_face_coords()[0][0]).set_z_index(9)
        
        A_label = Tex("A", font_size=36).move_to(A.get_center() + 0.15 * DOWN + 0.3 * RIGHT).set_z_index(9)
        B_label = Tex("B", font_size=36).move_to(B.get_center() + 0.15 * DOWN + 0.3 * LEFT).set_z_index(9)
        C_label = Tex("C", font_size=36).move_to(C.get_center() + 0.3 * DOWN + 0.15 * RIGHT).set_z_index(9)
        D_label = Tex("D", font_size=36).move_to(D.get_center() + 0.4 * UP).set_z_index(9)
        
        AB = Line3D(A, B, color=ManimColor('#2e5561'))
        BC = Line3D(B, C, color=BLUE)
        CA = Line3D(C, A, color=BLUE)
        DA = Line3D(D, A, color=BLUE)
        DB = Line3D(D, B, color=BLUE)
        DC = Line3D(D, C, color=BLUE)
        
        M = Dot3D(AB.get_center()).set_z_index(9)
        M_label = Tex("M", font_size=30).move_to(M.get_center() + 0.25 * UP + 0.25 * LEFT).set_z_index(9)
        
        N = Dot3D(DC.get_center()).set_z_index(9)
        N_label = Tex("N", font_size=30).move_to(N.get_center() + 0.25 * UP + 0.2 * RIGHT).set_z_index(9)
        
        MN = Line3D(M, N, color=YELLOW)
    
        CD_equals = VGroup(
            Line(C, N).equal(1),
            Line(N, D).equal(1),
        )
        
        BN = Line(B, N, color=GREEN)
        AN = Line(A, N, color=GREEN)
        
        BN_equal = BN.equal(2)
        AN_equal = AN.equal(2)
        
        
        copy_size = 2.5
        A_copy_1 = Dot([copy_size, 0, 0]).set_z_index(9)
        B_copy_1 = Dot([0, 0, 0]).set_z_index(9)
        N_copy_1 = Dot([copy_size / 2, np.sqrt(3) / 2 * copy_size, 0]).set_z_index(9)
        AB_copy_1 = Line(A_copy_1, B_copy_1, color=BLUE)
        BN_copy_1 = Line(B_copy_1, N_copy_1, color=GREEN)
        AN_copy_1 = Line(A_copy_1, N_copy_1, color=GREEN)
        M_copy_1 = Dot(AB_copy_1.get_center()).set_z_index(9)
        MN_copy_1 = Line(N_copy_1, M_copy_1, color=YELLOW)
        A_label_copy_1 = Tex("A", font_size=34).move_to(A_copy_1.get_center() + 0.24 * DOWN + 0.17 * RIGHT).set_z_index(9)
        B_label_copy_1 = Tex("B", font_size=34).move_to(B_copy_1.get_center() + 0.24 * DOWN + 0.17 * LEFT).set_z_index(9)
        N_label_copy_1 = Tex("N", font_size=34).move_to(N_copy_1.get_center() + 0.3 * UP).set_z_index(9)
        M_label_copy_1 = Tex("M", font_size=34).move_to(M_copy_1.get_center() + 0.3 * DOWN).set_z_index(9)
        BN_equal_copy_1 = BN_copy_1.equal(2)
        AN_equal_copy_1 = AN_copy_1.equal(2)
        
        
        copy_1 = VGroup(
            A_copy_1, B_copy_1, N_copy_1, M_copy_1, AB_copy_1, MN_copy_1, BN_copy_1, AN_copy_1, 
            A_label_copy_1, B_label_copy_1, N_label_copy_1, M_label_copy_1,
            AN_equal_copy_1, BN_equal_copy_1
        ).move_to(4.2 * RIGHT + 0.7 * DOWN)
        
        AB_equals_copy_1 = VGroup(
            Line(A_copy_1, M_copy_1).equal(1),
            Line(M_copy_1, B_copy_1).equal(1),
        )
        
        angle_NMA_copy_1 = Angle.from_three_points(
            np.array([N_copy_1.get_center()[0], N_copy_1.get_center()[1], 0]), 
            np.array([M_copy_1.get_center()[0], M_copy_1.get_center()[1], 0]), 
            np.array([A_copy_1.get_center()[0], A_copy_1.get_center()[1], 0]), 
            elbow=True, radius=0.25).set_stroke(color=YELLOW)
        
        
        copy_size = 2.5
        D_copy_2 = Dot([copy_size, 0, 0]).set_z_index(9)
        C_copy_2 = Dot([0, 0, 0]).set_z_index(9)
        M_copy_2 = Dot([copy_size / 2, np.sqrt(3) / 2 * copy_size, 0]).set_z_index(9)
        DC_copy_2 = Line(D_copy_2, C_copy_2, color=BLUE)
        CM_copy_2 = Line(C_copy_2, M_copy_2, color=GREEN)
        DM_copy_2 = Line(D_copy_2, M_copy_2, color=GREEN)
        N_copy_2 = Dot(DC_copy_2.get_center()).set_z_index(9)
        NM_copy_2 = Line(M_copy_2, N_copy_2, color=YELLOW)
        D_label_copy_2 = Tex("D", font_size=34).move_to(D_copy_2.get_center() + 0.24 * DOWN + 0.17 * RIGHT).set_z_index(9)
        C_label_copy_2 = Tex("C", font_size=34).move_to(C_copy_2.get_center() + 0.24 * DOWN + 0.17 * LEFT).set_z_index(9)
        M_label_copy_2 = Tex("M", font_size=34).move_to(M_copy_2.get_center() + 0.3 * UP).set_z_index(9)
        N_label_copy_2 = Tex("N", font_size=34).move_to(N_copy_2.get_center() + 0.3 * DOWN).set_z_index(9)
        CM_equal_copy_2 = CM_copy_2.equal(2)
        DM_equal_copy_2 = DM_copy_2.equal(2)
        
        
        copy_2 = VGroup(
            D_copy_2, C_copy_2, M_copy_2, N_copy_2, DC_copy_2, NM_copy_2, CM_copy_2, DM_copy_2, 
            D_label_copy_2, C_label_copy_2, M_label_copy_2, N_label_copy_2,
            DM_equal_copy_2, CM_equal_copy_2
        ).move_to(4.2 * LEFT + 0.7 * DOWN)
        
        CD_equals_copy_2 = VGroup(
            Line(C_copy_2, N_copy_2).equal(1),
            Line(N_copy_2, D_copy_2).equal(1),
        )
        
        angle_MNC_copy_2 = Angle.from_three_points(
            np.array([M_copy_2.get_center()[0], M_copy_2.get_center()[1], 0]), 
            np.array([N_copy_2.get_center()[0], N_copy_2.get_center()[1], 0]), 
            np.array([C_copy_2.get_center()[0], C_copy_2.get_center()[1], 0]), 
            elbow=True, radius=0.25).set_stroke(color=YELLOW)
        
        
        
        AB_equals = VGroup(
            Line(A, M).equal(1),
            Line(M, B).equal(1),
        )
        
        CM = Line(C, M, color=GREEN)
        DM = Line(D, M, color=GREEN)
        
        CM_equal = Line(C, M).equal(2)
        DM_equal = Line(D, M).equal(2)
        

        self.play(LaggedStart(
            FadeIn(VGroup(A, A_label)),
            FadeIn(VGroup(B, B_label)),
            FadeIn(VGroup(C, C_label)),
            FadeIn(VGroup(D, D_label)),
            run_time=0.8, lag_ratio=0.4
        ))
        self.wait(0.8)
        self.play(LaggedStart(
            Create(BC),
            Create(CA),
            FadeIn(AB),
            run_time=1.1, lag_ratio=0.4
        ))
        self.wait(0.8)
        self.play(
            Create(DA),
            Create(DB),
            Create(DC),
            run_time=0.9
        )
        self.wait()
        
        self.play(FadeIn(VGroup(M, M_label)), run_time=0.75)
        self.wait(0.3)
        self.play(FadeIn(VGroup(N, N_label)), run_time=0.75)
        self.wait(0.5)
        self.play(Create(MN))
        self.wait(1.5)
        
        self.play(LaggedStart(
            FadeIn(CD_equals[0]),
            FadeIn(CD_equals[1]),
            run_time=0.8, lag_ratio=0.4
        ))
        self.wait(0.8)
        self.play(LaggedStart(
            Create(AN),
            Create(BN),
            run_time=0.9, lag_ratio=0.4
        ))
        
        self.wait()
        self.play(FadeIn(VGroup(AN_equal, BN_equal)))
        self.play(FadeOut(CD_equals), run_time=0.75)
        
        self.play(FadeIn(copy_1))
        self.wait()
        self.play(FadeIn(AB_equals_copy_1))
        self.wait()
        self.play(FadeIn(angle_NMA_copy_1))
        self.wait()
        self.play(FadeOut(VGroup(AB_equals_copy_1, BN_equal_copy_1, AN_equal_copy_1)))
        self.wait()
    
        info_1 = MathTex('AB', r'\perp', 'MN').move_to(M_copy_1.get_center() + 1.5 * DOWN).scale(0.8)
        
        self.play(Write(info_1))
        self.wait()
        self.play(FadeOut(VGroup(BN, BN_equal, AN, AN_equal)))
        self.wait(2)
        
        self.play(FadeIn(AB_equals))
        self.play(LaggedStart(
            Create(CM),
            Create(DM),
            run_time=0.9, lag_ratio=0.4
        ))
        self.wait(0.3)
        self.play(FadeIn(VGroup(CM_equal, DM_equal)))
        self.wait()
        
        self.play(FadeIn(copy_2))
        self.wait()
        self.play(FadeIn(CD_equals_copy_2))
        self.wait()
        self.play(FadeIn(angle_MNC_copy_2))
        self.wait()
        self.play(FadeOut(VGroup(CD_equals_copy_2, CM_equal_copy_2, DM_equal_copy_2)))
        
        info_2 = MathTex('CD', r'\perp', 'MN').move_to(N_copy_2.get_center() + 1.5 * DOWN).scale(0.8)
        
        self.play(Write(info_2))
        self.wait()
        self.play(FadeOut(VGroup(CM, DM, AB_equals, CM_equal, DM_equal)))
        self.wait()
        
        
        box_1 = SurroundingRectangle(info_1, buff=0.3)
        box_2 = SurroundingRectangle(info_2, buff=0.3)
        
        self.play(ShowPassingFlash(box_1), ShowPassingFlash(box_2), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(VGroup(info_1, info_2, copy_1, copy_2, angle_NMA_copy_1, angle_MNC_copy_2)))
        self.wait(2)
        
        
        K = Dot(Line(B, C).point_from_proportion(0.3)).set_z_index(5)
        T = Dot(Line(C, A).point_from_proportion(0.7)).set_z_index(5)
        R = Dot(Line(A, D).point_from_proportion(0.3)).set_z_index(5)
        S = Dot(Line(D, B).point_from_proportion(0.7)).set_z_index(5)
        
        K_label = Tex("K", font_size=32).move_to(K.get_center() + 0.3 * DOWN + 0.13 * LEFT)
        T_label = Tex("T", font_size=32).move_to(T.get_center() + 0.3 * DOWN + 0.13 * RIGHT)
        R_label = Tex("R", font_size=32).move_to(R.get_center() + 0.3 * UP + 0.13 * RIGHT)
        S_label = Tex("S", font_size=32).move_to(S.get_center() + 0.3 * UP + 0.13 * LEFT)
        
        
        KT = Line3D(K, T, color=RED)
        TR = Line3D(T, R, color=RED)
        RS = Line3D(R, S, color=RED)
        SK = Line3D(S, K, color=RED)       
        
        plane = Polygon(K.get_center(), T.get_center(), R.get_center(), S.get_center(), color=RED, fill_opacity=0.4)
        
        A_copy_3 = Dot([0, 0, 0]).set_z_index(5)
        B_copy_3 = Dot([copy_size, 0, 0]).set_z_index(5)
        C_copy_3 = Dot([copy_size / 2, np.sqrt(3) / 2 * copy_size, 0]).set_z_index(5)
        VGroup(A_copy_3, B_copy_3, C_copy_3).rotate(PI, axis=RIGHT)  
        AB_copy_3 = Line(A_copy_3, B_copy_3, color=BLUE)
        BC_copy_3 = Line(B_copy_3, C_copy_3, color=BLUE)
        CA_copy_3 = Line(C_copy_3, A_copy_3, color=BLUE)
        M_copy_3 = Dot(AB_copy_3.get_center()).set_z_index(5)
        D_copy_3 = Dot(VGroup(A_copy_3, B_copy_3, C_copy_3).get_center()).set_z_index(5)
        A_label_copy_3 = Tex("A", font_size=32).move_to(A_copy_3.get_center() + 0.24 * UP + 0.17 * LEFT).set_z_index(5)
        B_label_copy_3 = Tex("B", font_size=32).move_to(B_copy_3.get_center() + 0.24 * UP + 0.17 * RIGHT).set_z_index(5)
        C_label_copy_3 = Tex("C", font_size=32).move_to(C_copy_3.get_center() + 0.3 * DOWN).set_z_index(5)
        M_label_copy_3 = Tex("M", font_size=32).move_to(M_copy_3.get_center() + 0.3 * UP).set_z_index(5)
        D_label_copy_3 = Tex(r"$\mathrm{D_1}$", font_size=32).move_to(D_copy_3.get_center() + 0.1 * UP + 0.35 * RIGHT).set_z_index(5)
        
        copy_3 = VGroup(
            A_copy_3, B_copy_3, C_copy_3, M_copy_3, D_copy_3, AB_copy_3, BC_copy_3, CA_copy_3,
            A_label_copy_3, B_label_copy_3, C_label_copy_3, M_label_copy_3, D_label_copy_3
        ).move_to(4.2 * LEFT + 0.7 * DOWN)
        
        
        
        self.play(FadeIn(VGroup(K, K_label)), MN.animate.set_opacity(0.3))
        self.wait()
        self.play(Create(KT), FadeIn(VGroup(T, T_label)))
        self.wait()
        self.play(Create(TR), FadeIn(VGroup(R, R_label)))
        self.wait()
        self.play(Create(RS), FadeIn(VGroup(S, S_label)))
        self.wait()
        self.play(Create(SK))
        self.wait(0.7)
        self.play(FadeIn(plane))
        self.wait()
        
        info_3 = MathTex('AB', r'\parallel', 'SR', r'\parallel', 'KT').move_to(4 * RIGHT + 0.3 * DOWN).scale(0.85)
        info_4 = MathTex('CD', r'\parallel', 'SK', r'\parallel', 'RT').move_to(4 * RIGHT + 0.9 * DOWN).scale(0.85)
        
        
        self.play(Write(info_3))
        self.play(Write(info_4))        
        self.wait(2)
        
        info_extra_1 = MathTex('MN', r'\perp', 'AB').move_to(4 * LEFT + 0.3 * DOWN).scale(0.85)
        info_extra_2 = MathTex('MN', r'\perp', 'SR').move_to(4 * LEFT + 0.3 * DOWN).scale(0.85)
        info_extra_3 = MathTex('MN', r'\perp', 'CD').move_to(4 * LEFT + 0.9 * DOWN).scale(0.85)
        info_extra_4 = MathTex('MN', r'\perp', 'SK').move_to(4 * LEFT + 0.9 * DOWN).scale(0.85)
        
        self.play(FadeIn(info_extra_1))
        self.wait(1.5)
        self.play(TransformMatchingTex(info_extra_1, info_extra_2))
        self.wait(1)
        self.play(FadeIn(info_extra_3))
        self.wait(1.5)
        self.play(TransformMatchingTex(info_extra_3, info_extra_4))
        self.wait(2)
        self.play(FadeOut(VGroup(info_extra_2, info_extra_4)))
        self.wait()
        
        self.play(FadeIn(copy_3))
        self.wait(1)
        
        tmp_line = Line(C_copy_3, D_copy_3, color=YELLOW)
        self.play(Create(tmp_line))
        self.wait(2)
        self.play(Transform(
            tmp_line,
            tmp_line.copy().set_length_about_point(Line(C_copy_3, M_copy_3).get_length(), C_copy_3.get_center())
        ))
        self.wait(0.4)
        angle_CMA = Angle.from_three_points(
            np.array([C_copy_3.get_center()[0], C_copy_3.get_center()[1], 0]),
            np.array([M_copy_3.get_center()[0], M_copy_3.get_center()[1], 0]),
            np.array([A_copy_3.get_center()[0], A_copy_3.get_center()[1], 0]),
            radius=0.3, color=YELLOW, elbow=True
        )
        self.play(FadeIn(angle_CMA))
        self.wait(0.8)
        
        info_5 = MathTex('AB', r'\perp', 'CD').move_to(4 * RIGHT + 1.5 * DOWN).scale(0.85)
        self.play(Write(info_5))
        self.wait(0.7)
        self.play(FadeOut(VGroup(copy_3, tmp_line, angle_CMA)))
        self.wait(0.8)
        
        box_3 = SurroundingRectangle(VGroup(info_3, info_4, info_5), buff=0.3)
        self.play(ShowPassingFlash(box_3), run_time=1.5)
        self.wait(0.7)
        
        info_6 = MathTex('SK', r'\perp', 'KT').move_to(4 * RIGHT + 1.5 * DOWN).scale(0.85)
        self.play(TransformMatchingTex(info_5, info_6))
        self.wait(1)
        
        
        D_copy_4 = Dot([copy_size, 0, 0]).set_z_index(1)
        C_copy_4 = Dot([0, 0, 0]).set_z_index(1)
        B_copy_4 = Dot([copy_size / 2, np.sqrt(3) / 2 * copy_size, 0]).set_z_index(1)
        VGroup(D_copy_4, C_copy_4, B_copy_4).rotate(-PI / 2, axis=IN).move_to(4.2 * LEFT + 0.2 * DOWN)
        D_label_copy_4 = Tex("D", font_size=32).move_to(D_copy_4.get_center() + 0.24 * UP + 0.17 * RIGHT)
        C_label_copy_4 = Tex("C", font_size=32).move_to(C_copy_4.get_center() + 0.24 * DOWN + 0.17 * RIGHT)
        B_label_copy_4 = Tex("B", font_size=32).move_to(B_copy_4.get_center() + 0.3 * LEFT)
        DC_copy_4  = Line(D_copy_4, C_copy_4, color=BLUE)
        CB_copy_4  = Line(C_copy_4, B_copy_4, color=BLUE)
        BD_copy_4  = Line(B_copy_4, D_copy_4, color=BLUE)
        
        S_copy_4 = Dot(BD_copy_4.point_from_proportion(0.3)).set_z_index(1)
        K_copy_4 = Dot(CB_copy_4.point_from_proportion(0.7)).set_z_index(1)
        S_label_copy_4 = Tex("S", font_size=32).move_to(S_copy_4.get_center() + 0.3 * UP)
        K_label_copy_4 = Tex("K", font_size=32).move_to(K_copy_4.get_center() + 0.3 * DOWN)
        SK_copy_4 = Line(S_copy_4, K_copy_4, color=RED)
        
        BK_label_copy_4 = MathTex('1', font_size=30).move_to(Line(B_copy_4, K_copy_4).point_from_proportion(0.4) + 0.3 * DOWN)
        KC_label_copy_4 = MathTex('5', font_size=30).move_to(Line(K_copy_4, C_copy_4).point_from_proportion(0.4) + 0.3 * DOWN)
        SK_label_copy_4 = MathTex('x', font_size=30).move_to(SK_copy_4.get_center() + 0.25 * RIGHT)
        DC_label_copy_4 = MathTex('6', font_size=30).move_to(DC_copy_4.get_center() + 0.25 * RIGHT)
        
        copy_4 = VGroup(
            D_copy_4, C_copy_4, B_copy_4,
            D_label_copy_4, C_label_copy_4, B_label_copy_4,
            S_copy_4, K_copy_4, S_label_copy_4, K_label_copy_4,
            DC_copy_4, CB_copy_4, BD_copy_4, SK_copy_4
        )
        
        
        self.play(FadeIn(copy_4))
        self.wait()
        self.play(LaggedStart(
            FadeIn(BK_label_copy_4),
            FadeIn(KC_label_copy_4),
            FadeIn(SK_label_copy_4),
            FadeIn(DC_label_copy_4),
            run_time=1.3, lag_ratio=0.4
        ))
        self.wait(2)
        
        info_7 = MathTex(r'\triangle{BKS}', r'\sim', r'\triangle{BCD}').move_to(4.2 * LEFT + 2.5 * DOWN).scale(0.85)
        info_8 = MathTex('\dfrac{BK}{BC}', '=', '\dfrac{SK}{DC}',).move_to(4.2 * LEFT + 2.5 * DOWN).scale(0.85)
        info_9 = MathTex('\dfrac{1}{6}', '=', '\dfrac{x}{6}').move_to(4.2 * LEFT + 2.5 * DOWN).scale(0.85)
        info_10 = MathTex('x', '=', '1').move_to(4.2 * LEFT + 2.5 * DOWN).scale(0.85)
        info_11 = MathTex('SK', '=', '1').move_to(4 * RIGHT + 1 * DOWN).scale(0.85)
        
        self.play(Write(info_7))
        self.wait(2)
        self.play(TransformMatchingTex(info_7, info_8))
        self.wait(1)
        self.play(TransformMatchingTex(info_8, info_9))
        self.wait(1)
        self.play(TransformMatchingTex(info_9, info_10))
        self.wait(0.7)
        self.play(VGroup(info_3, info_4, info_6).animate.set_opacity(0.5).scale(0.7).shift(UP))
        self.play(Write(info_11))
        self.wait(1.5)
        
        BS_label_copy_4 = MathTex('1', font_size=30).move_to(Line(B_copy_4, S_copy_4).point_from_proportion(0.4) + 0.3 * UP)
        SD_label_copy_4 = MathTex('5', font_size=30).move_to(Line(S_copy_4, D_copy_4).point_from_proportion(0.4) + 0.3 * UP)
        
        info_12 = MathTex('BS', '=', '1').move_to(4.2 * LEFT + 2.1 * DOWN).scale(0.85)
        info_13 = MathTex('SD', '=', '5').move_to(4.2 * LEFT + 2.7 * DOWN).scale(0.85)
        
        self.play(LaggedStart(
            FadeIn(BS_label_copy_4),
            FadeIn(SD_label_copy_4),
            run_time=1, lag_ratio=0.4
        ))
        self.wait(0.3)
        self.play(FadeOut(info_10))
        self.play(LaggedStart(
            Write(info_12),
            Write(info_13),
            run_time=1, lag_ratio=0.4
        ))
        self.wait()
        
        self.play(FadeOut(VGroup(copy_4, BS_label_copy_4, SD_label_copy_4, BK_label_copy_4, KC_label_copy_4, SK_label_copy_4, DC_label_copy_4)))
        self.wait()
        
        
        B_copy_5 = Dot([0, 0, 0]).set_z_index(9)
        A_copy_5 = Dot([copy_size, 0, 0]).set_z_index(9)
        D_copy_5 = Dot([copy_size / 2, np.sqrt(3) / 2 * copy_size, 0]).set_z_index(9)
        VGroup(B_copy_5, A_copy_5, D_copy_5).move_to(4.2 * LEFT + 0.2 * DOWN)
        
        B_label_copy_5 = Tex("B", font_size=32).move_to(B_copy_5.get_center() + 0.24 * DOWN + 0.17 * LEFT)
        A_label_copy_5 = Tex("A", font_size=32).move_to(A_copy_5.get_center() + 0.24 * DOWN + 0.17 * RIGHT)
        D_label_copy_5 = Tex("D", font_size=32).move_to(D_copy_5.get_center() + 0.3 * UP)
        
        BA_copy_5 = Line(B_copy_5, A_copy_5, color=BLUE)
        AD_copy_5 = Line(A_copy_5, D_copy_5, color=BLUE)
        DB_copy_5 = Line(D_copy_5, B_copy_5, color=BLUE)
        
        S_copy_5 = Dot(DB_copy_5.point_from_proportion(0.65)).set_z_index(9)
        R_copy_5 = Dot(AD_copy_5.point_from_proportion(0.35)).set_z_index(9)
        
        S_label_copy_5 = Tex("S", font_size=32).move_to(S_copy_5.get_center() + 0.3 * LEFT)
        R_label_copy_5 = Tex("R", font_size=32).move_to(R_copy_5.get_center() + 0.3 * RIGHT)
        
        SR_copy_5 = Line(S_copy_5, R_copy_5, color=RED)
        
        copy_5 = VGroup(
            B_copy_5, A_copy_5, D_copy_5,
            B_label_copy_5, A_label_copy_5, D_label_copy_5,
            S_copy_5, R_copy_5, S_label_copy_5, R_label_copy_5,
            BA_copy_5, AD_copy_5, DB_copy_5, SR_copy_5
        )
        
        BS_label_copy_5 = MathTex('1', font_size=30).move_to(Line(B_copy_5, S_copy_5).point_from_proportion(0.5) + 0.3 * LEFT)
        SD_label_copy_5 = MathTex('5', font_size=30).move_to(Line(S_copy_5, D_copy_5).point_from_proportion(0.5) + 0.3 * LEFT)
        SR_label_copy_5 = MathTex('x', font_size=30).move_to(SR_copy_5.get_center() + 0.25 * DOWN)
        BA_label_copy_5 = MathTex('6', font_size=30).move_to(BA_copy_5.get_center() + 0.25 * DOWN)
        
        self.play(FadeIn(copy_5))
        self.wait()
        
        self.play(LaggedStart(
            FadeIn(BS_label_copy_5),
            FadeIn(SD_label_copy_5),
            run_time=1, lag_ratio=0.4
        ))
        self.wait(0.6)
        self.play(LaggedStart(
            FadeIn(SR_label_copy_5),
            FadeIn(BA_label_copy_5),
            run_time=1, lag_ratio=0.4
        ))
        self.wait()
        
        info_14 = MathTex(r'\dfrac{DS}{DB}', '=', r'\dfrac{SR}{BA}').move_to(4.2 * LEFT + 2.5 * DOWN).scale(0.85)
        info_15 = MathTex(r'\dfrac{5}{6}', '=', r'\dfrac{x}{6}').move_to(4.2 * LEFT + 2.5 * DOWN).scale(0.85)
        info_16 = MathTex('x', '=', '5').move_to(4.2 * LEFT + 2.5 * DOWN).scale(0.85)
        info_17 = MathTex('SR', '=', '5').move_to(4 * RIGHT + 1.6 * DOWN).scale(0.85)
        
        self.play(FadeOut(VGroup(info_12, info_13)))
        self.play(Write(info_14))
        self.wait(1)
        self.play(TransformMatchingTex(info_14, info_15))
        self.wait(1)
        self.play(TransformMatchingTex(info_15, info_16))
        self.wait()
        self.play(Write(info_17))
        self.wait(1.5)
        self.play(FadeOut(VGroup(info_3, info_4, info_6)))
        self.play(VGroup(info_11, info_17).animate.shift(4 * RIGHT))
        
        self.play(FadeOut(VGroup(copy_5, BS_label_copy_5, SD_label_copy_5, SR_label_copy_5, BA_label_copy_5, info_16)))
        self.wait(1.5)

        info_18 = MathTex('S_{RSKT}', '=', 'SK', r'\cdot', 'SR').move_to(4 * LEFT)
        info_19 = MathTex('S_{RSKT}', '=', '1', r'\cdot', '5').move_to(4 * LEFT)
        info_20 = MathTex('S_{RSKT}', '=', '5').move_to(4 * LEFT)
        
        self.play(Write(info_18))
        self.wait(1)
        self.play(TransformMatchingTex(info_18, info_19))
        self.wait(1)
        self.play(TransformMatchingTex(info_19, info_20))
        self.wait(2)
        
        ans = Tex('Answer: 5').move_to(4 * LEFT + DOWN)
        box = SurroundingRectangle(ans, buff=0.3)
        
        self.play(Write(ans))
        self.play(ShowPassingFlash(box), run_time=1.5)
                
        self.wait(3)
        

class Task_15_inequality(Scene):
    def construct(self):
        task_text = Tex(r'Solve inequality: \\ \vspace{0.2cm} $\dfrac{3^x + 9}{3^x - 9} + \dfrac{3^x - 9}{3^x + 9} \geq \dfrac{4 \cdot 3^{x + 1} + 144}{9^x - 81}$', font_size=36)
      
        
        rectangle = SurroundingRectangle(task_text, buff=0.3)
        task_label = Tex("Task 15. Inequality").scale(1.2).to_edge(UP)

        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text, run_time=8))
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.7 * UP).scale(0.7),
        ))
        self.wait(1.5)

        task_1 = MathTex('\dfrac{3^x + 9}{3^x - 9}', '+', '\dfrac{3^x - 9}{3^x + 9}', '\geq', '\dfrac{4 \cdot 3^{x + 1} + 144}{9^x - 81}')
        task_2 = MathTex('\dfrac{3^x + 9}{3^x - 9}', '+', '\dfrac{3^x - 9}{3^x + 9}', '\geq', '\dfrac{4 \cdot 3 \cdot  3^x + 144}{9^x - 81}')
        task_2[0][0:2].set_color(YELLOW)
        task_2[0][5:7].set_color(YELLOW)
        task_2[2][0:2].set_color(YELLOW)
        task_2[2][5:7].set_color(YELLOW)
        task_2[4][2:6].set_color(RED)
        task_2[4][11:13].set_color(YELLOW)
        
        task_3 = MathTex('\dfrac{3^x + 9}{3^x - 9}', '+', '\dfrac{3^x - 9}{3^x + 9}', '\geq', '\dfrac{4 \cdot 3 \cdot  3^x + 144}{(3^x)^2 - 81}')
        task_3[0][0:2].set_color(YELLOW)
        task_3[0][5:7].set_color(YELLOW)
        task_3[2][0:2].set_color(YELLOW)
        task_3[2][5:7].set_color(YELLOW)
        task_3[4][4:6].set_color(YELLOW)
        task_3[4][11:16].set_color(RED)
        
        task_4 = MathTex('\dfrac{t + 9}{3^x - 9}', '+', '\dfrac{3^x - 9}{3^x + 9}', '\geq', '\dfrac{4 \cdot 3 \cdot  3^x + 144}{(3^x)^2 - 81}')
        task_4[0][0].set_color(YELLOW)
        task_4[0][4:6].set_color(YELLOW)
        task_4[2][0:2].set_color(YELLOW)
        task_4[2][5:7].set_color(YELLOW)
        task_4[4][4:6].set_color(YELLOW)
        task_4[4][11:16].set_color(YELLOW)
        
        task_5 = MathTex('\dfrac{t + 9}{t - 9}', '+', '\dfrac{3^x - 9}{3^x + 9}', '\geq', '\dfrac{4 \cdot 3 \cdot  3^x + 144}{(3^x)^2 - 81}')
        task_5[0][0].set_color(YELLOW)
        task_5[0][4].set_color(YELLOW)
        task_5[2][0:2].set_color(YELLOW)
        task_5[2][5:7].set_color(YELLOW)
        task_5[4][4:6].set_color(YELLOW)
        task_5[4][11:16].set_color(YELLOW)
        
        task_6 = MathTex('\dfrac{t + 9}{t - 9}', '+', '\dfrac{t - 9}{3^x + 9}', '\geq', '\dfrac{4 \cdot 3 \cdot  3^x + 144}{(3^x)^2 - 81}')
        task_6[0][0].set_color(YELLOW)
        task_6[0][4].set_color(YELLOW)
        task_6[2][0].set_color(YELLOW)
        task_6[2][4:6].set_color(YELLOW)
        task_6[4][4:6].set_color(YELLOW)
        task_6[4][11:16].set_color(YELLOW)
        
        task_7 = MathTex('\dfrac{t + 9}{t - 9}', '+', '\dfrac{t - 9}{t + 9}', '\geq', '\dfrac{4 \cdot 3 \cdot  3^x + 144}{(3^x)^2 - 81}')
        task_7[0][0].set_color(YELLOW)
        task_7[0][4].set_color(YELLOW)
        task_7[2][0].set_color(YELLOW)
        task_7[2][4].set_color(YELLOW)
        task_7[4][4:6].set_color(YELLOW)
        task_7[4][11:16].set_color(YELLOW)
        
        task_8 = MathTex('\dfrac{t + 9}{t - 9}', '+', '\dfrac{t - 9}{t + 9}', '\geq', '\dfrac{4 \cdot 3t + 144}{(3^x)^2 - 81}')
        task_8[0][0].set_color(YELLOW)
        task_8[0][4].set_color(YELLOW)
        task_8[2][0].set_color(YELLOW)
        task_8[2][4].set_color(YELLOW)
        task_8[4][3].set_color(YELLOW)
        task_8[4][9:14].set_color(YELLOW)
        
        task_9 = MathTex('\dfrac{t + 9}{t - 9}', '+', '\dfrac{t - 9}{t + 9}', '\geq', '\dfrac{4 \cdot 3t + 144}{t^2 - 81}')
        task_9[0][0].set_color(YELLOW)
        task_9[0][4].set_color(YELLOW)
        task_9[2][0].set_color(YELLOW)
        task_9[2][4].set_color(YELLOW)
        task_9[4][3].set_color(YELLOW)
        task_9[4][9:11].set_color(YELLOW)
        
        task_10 = MathTex(
            '\dfrac{t + 9}{t - 9}',
            '+', 
            '\dfrac{t - 9}{t + 9}',
            '\geq', 
            '\dfrac{12t + 144}{t^2 - 81}'
        )
        
        task_11 = MathTex(
            '\dfrac{(t + 9) \cdot (t + 9)}{(t - 9) \cdot (t + 9)}',
            '+', 
            '\dfrac{(t - 9) \cdot (t - 9)}{(t + 9) \cdot (t - 9)}',
            '\geq', 
            '\dfrac{12t + 144}{t^2 - 81}'
        )
        
        task_12 = MathTex(
            '\dfrac{(t + 9) \cdot (t + 9) + (t - 9) \cdot (t - 9)}{(t - 9) \cdot (t + 9)}',
            '\geq', 
            '\dfrac{12t + 144}{t^2 - 81}'
        )
        
        task_13 = MathTex(
            '\dfrac{t^2 + 9t + 81 + (t - 9) \cdot (t - 9)}{(t - 9) \cdot (t + 9)}',
            '\geq', 
            '\dfrac{12t + 144}{t^2 - 81}'
        )
        task_13[0][0:8].set_color(RED)
        
        
        task_14 = MathTex(
            '\dfrac{t^2 + 9t + 81 + t^2 - 9t + 81}{(t - 9) \cdot (t + 9)}',
            '\geq', 
            '\dfrac{12t + 144}{t^2 - 81}'
        )
        task_14[0][9:18].set_color(BLUE)
        
        task_15 = MathTex(
            '\dfrac{t^2 + 81 + t^2 + 81}{(t - 9) \cdot (t + 9)}',
            '\geq', 
            '\dfrac{12t + 144}{t^2 - 81}'
        )
        
        task_16 = MathTex(
            '\dfrac{2t^2 + 162}{(t - 9) \cdot (t + 9)}',
            '\geq', 
            '\dfrac{12t + 144}{t^2 - 81}'
        )
        
        task_17 = MathTex(
            '\dfrac{2t^2 + 162}{(t - 9) \cdot (t + 9)}',
            '-',
            '\dfrac{12t + 144}{t^2 - 81}',
            '\geq', 
            '0'
        )
        
        task_18 = MathTex(
            '\dfrac{2t^2 + 162}{t^2 - 81}',
            '-',
            '\dfrac{12t + 144}{t^2 - 81}',
            '\geq', 
            '0'
        )
        
        task_19 = MathTex('\dfrac{2t^2 + 162 - 12t - 144}{t^2 - 81}', '\geq', '0')
        task_20 = MathTex('\dfrac{2t^2 - 12t + 162 - 144}{t^2 - 81}', '\geq', '0')
        task_21 = MathTex('\dfrac{2t^2 - 12t + 18}{t^2 - 81}', '\geq', '0')
        task_22 = MathTex('2 \cdot \dfrac{t^2 - 6t + 9}{t^2 - 81}', '\geq', '0')
        task_23 = MathTex('\dfrac{t^2 - 6t + 9}{t^2 - 81}', '\geq', '0')
        
        
        
        
        
        
        
        
        
        
        self.play(Write(task_1))
        self.wait()
        self.play(
            task_1[0][0:2].animate.set_color(YELLOW),
            task_1[0][5:7].animate.set_color(YELLOW),
            
            task_1[2][0:2].animate.set_color(YELLOW),
            task_1[2][5:7].animate.set_color(YELLOW),
            
            task_1[4][2:6].animate.set_color(YELLOW),
            task_1[4][11:13].animate.set_color(YELLOW),
        )
        self.wait(0.8)
        self.play(task_1[4][2:6].animate.set_color(RED))
        self.wait(0.8)
        self.play(TransformMatchingTex(task_1, task_2))
        self.wait(0.5)
        self.play(
            task_2[4][2:4].animate.set_color(WHITE), 
            task_2[4][4:6].animate.set_color(YELLOW)
        )
        self.wait(0.8)
        self.play(task_2[4][11:13].animate.set_color(RED))
        self.wait()
        self.play(TransformMatchingTex(task_2, task_3))
        self.wait(0.5)
        self.play(task_3[4][11:16].animate.set_color(YELLOW))
        
        info_1 = MathTex('t', '=', '3^x').move_to(3.5 * DOWN).set_opacity(0.7)
        self.play(Write(info_1))
        self.wait(0.5)
        self.play(TransformMatchingTex(task_3, task_4), run_time=0.5)
        self.wait(0.15)
        self.play(TransformMatchingTex(task_4, task_5), run_time=0.5)
        self.wait(0.15)
        self.play(TransformMatchingTex(task_5, task_6), run_time=0.5)
        self.wait(0.15)
        self.play(TransformMatchingTex(task_6, task_7), run_time=0.5)
        self.wait(0.15)
        self.play(TransformMatchingTex(task_7, task_8), run_time=0.5)
        self.wait(0.15)
        self.play(TransformMatchingTex(task_8, task_9), run_time=0.5)
        self.wait()
        self.play(
            task_9[0][0].animate.set_color(WHITE),
            task_9[0][4].animate.set_color(WHITE),
            task_9[2][0].animate.set_color(WHITE),
            task_9[2][4].animate.set_color(WHITE),
            task_9[4][3].animate.set_color(WHITE),
            task_9[4][9:11].animate.set_color(WHITE),
            FadeOut(info_1)
        )
        self.wait(2)
        
        self.play(TransformMatchingTex(task_9, task_10))
        self.wait()
        self.play(TransformMatchingTex(task_10, task_11))
        self.wait()
        self.play(TransformMatchingTex(task_11, task_12))
        self.wait()
        self.play(task_12[0][0:11].animate.set_color(RED))
        self.wait()
        self.play(TransformMatchingTex(task_12, task_13))
        self.wait(0.5)
        self.play(task_13[0][0:8].animate.set_color(WHITE))
        self.wait(0.6)
        self.play(task_13[0][9:20].animate.set_color(BLUE))
        self.wait(0.9)
        self.play(TransformMatchingTex(task_13, task_14))
        self.wait(0.9)
        self.play(task_14[0][9:20].animate.set_color(WHITE))
        self.wait()
        self.play(
            task_14[0][3:5].animate.set_color(YELLOW),
            task_14[0][11:13].animate.set_color(YELLOW),
        )
        self.wait(0.4)
        self.play(TransformMatchingTex(task_14, task_15))
        self.wait(0.9)
        self.play(TransformMatchingTex(task_15, task_16))
        self.wait(2)
        self.play(TransformMatchingTex(task_16, task_17))
        self.wait()
        self.play(TransformMatchingTex(task_17, task_18))
        self.wait()
        self.play(TransformMatchingTex(task_18, task_19))
        self.wait(0.7)
        self.play(TransformMatchingTex(task_19, task_20))
        self.wait(0.7)
        self.play(TransformMatchingTex(task_20, task_21))
        self.wait(0.7)
        self.play(TransformMatchingTex(task_21, task_22))
        self.wait(0.9)
        self.play(TransformMatchingTex(task_22, task_23))
        self.wait(2)
        
        info_2 = MathTex('t^2 - 6t + 9 = 0').move_to(4 * LEFT + 2 * UP).set_color(BLUE)
        equivalence_1 = MathTex(r'\iff').move_to(4 * LEFT + 1.2 * UP).rotate(PI / 2).scale(0.8).set_color(BLUE)
        info_3 = MathTex('(t - 3)^2 = 0').move_to(4 * LEFT + 0.4 * UP).set_color(BLUE)
        equivalence_2 = MathTex(r'\iff').move_to(4 * LEFT - 0.4 * UP).rotate(PI / 2).scale(0.8).set_color(BLUE)
        info_4 = MathTex('t = 3').move_to(4 * LEFT - 1.2 * UP).set_color(BLUE)
        
        info_5 = MathTex('t^2 - 81 = 0').move_to(4 * RIGHT + 2 * UP).set_color(RED)
        equivalence_3 = MathTex(r'\iff').move_to(4 * RIGHT + 1.2 * UP).rotate(PI / 2).scale(0.8).set_color(RED)
        info_6 = MathTex('(t - 9)(t + 9) = 0').move_to(4 * RIGHT + 0.4 * UP).set_color(RED)
        equivalence_4 = MathTex(r'\iff').move_to(4 * RIGHT - 0.4 * UP).rotate(PI / 2).scale(0.8).set_color(RED)
        info_7 = SystemOfEquations(
            MathTex('t = 9'),
            MathTex('t = -9'),
            is_bracket=True
        ).move_to(4 * RIGHT - 1.6 * UP).set_color(RED)
        
        line = Arrow(buff=0, stroke_width=2).shift(0.8 * DOWN).scale(2)
        line.tip.scale(0.7)
        line.tip.shift(0.07 * LEFT)
        x_label = MathTex('x').move_to(line.get_end() + 0.15 * LEFT + 0.35 * UP)
        
        self.play(task_23.animate.move_to(1.5 * UP))
        self.wait(0.5)
        self.play(FadeIn(line))
        self.wait(0.4)
        self.play(
            task_23[0][0:7].animate.set_color(BLUE),
            task_23[0][8:13].animate.set_color(RED)
        )
        self.wait(0.8)
        
        self.play(Write(info_2))
        self.wait(0.5)
        self.play(Write(equivalence_1), run_time=0.5)
        self.wait(0.5)
        self.play(Write(info_3))
        self.wait(0.5)
        self.play(Write(equivalence_2), run_time=0.5)
        self.wait(0.5)
        self.play(Write(info_4))
        self.wait(0.8)
        
        self.play(Write(info_5))
        self.wait(0.5)
        self.play(Write(equivalence_3), run_time=0.5)
        self.wait(0.5)
        self.play(Write(info_6))
        self.wait(0.5)
        self.play(Write(equivalence_4), run_time=0.5)
        self.wait(0.5)
        self.play(FadeIn(info_7))
        self.wait(1.5)
        
        self.play(
            FadeOut(VGroup(
                info_2, equivalence_1, info_3, equivalence_2, 
                info_5, equivalence_3, info_6, equivalence_4
            )),
            info_4.animate.shift(1.5 * DOWN),
            info_7.animate.shift(1.5 * DOWN),
        )
        self.wait(0.6)
        
        task_24 = MathTex('\dfrac{(t - 3)^2}{(t - 9) \cdot (t + 9)}', '\geq', '0').move_to(task_23.get_center())
        task_24[0][0:6].set_color(BLUE)
        task_24[0][7:18].set_color(RED)
        
        self.play(TransformMatchingTex(task_23, task_24))
        self.wait(0.6)
        
        self.wait(0.8)
        self.play(line.animate.scale(1.75))
        self.wait(0.8)
        
        dot_9 = Dot(line.point_from_proportion(0.75))
        dot_3 = Dot(line.get_center())
        dot_minus_9 = Dot(line.point_from_proportion(0.285))
        
        dot_9_label = MathTex('9').move_to(dot_9.get_center() + 0.3 * DOWN + 0.3 * RIGHT)
        dot_3_label = MathTex('3').move_to(dot_3.get_center() + 0.5 * UP)
        dot_minus_9_label = MathTex('-9').move_to(dot_minus_9.get_center() + 0.3 * DOWN + 0.4 * LEFT)
        
        
        self.play(FadeIn(VGroup(dot_9, dot_9_label)), run_time=0.75)
        self.wait(0.1)
        self.play(FadeIn(VGroup(dot_3, dot_3_label)), run_time=0.75)
        self.wait(0.1)
        self.play(FadeIn(VGroup(dot_minus_9, dot_minus_9_label)), run_time=0.75)
        self.wait(0.5)
        
        black_1 = Rectangle(height=0.55, width=1.85, color=BLACK, fill_color=BLACK, fill_opacity=1).move_to(
            dot_9.get_center() + 0.45 * UP + 2.75 * RIGHT).set_z_index(90)
        black_2 = Rectangle(height=0.55, width=1.85, color=BLACK, fill_color=BLACK, fill_opacity=1).move_to(
            dot_minus_9.get_center() + 0.45 * UP + 2.75 * LEFT).set_z_index(90)
        self.add(black_1, black_2)
        
        bracket_1 = BracketBetweenPoints(dot_9.get_center(), line.get_end() + RIGHT, direction=UP)
        bracket_1_label = MathTex('+').move_to(Line(dot_9.get_center(), line.get_end() + RIGHT).point_from_proportion(0.30) + 0.22 * UP).set_color(GREEN)
        bracket_2 = BracketBetweenPoints(dot_9.get_center(), dot_3.get_center(), direction=DOWN)
        bracket_2_label = MathTex('-').move_to(Line(dot_9.get_center(), dot_3.get_center()).get_center() + 0.22 * DOWN).set_color(RED)
        bracket_3 = bracket_2.copy().shift(
            Line(Line(dot_3, dot_9).get_center(), Line(dot_3, dot_minus_9).get_center()).get_length() * LEFT
        )
        bracket_3_label = MathTex('-').move_to(Line(dot_3.get_center(), dot_minus_9.get_center()).get_center() + 0.22 * DOWN).set_color(RED)
        bracket_4 = BracketBetweenPoints(dot_minus_9.get_center(), line.get_start() + LEFT, direction=UP)
        bracket_4_label = MathTex('+').move_to(Line(dot_minus_9.get_center(), line.get_start() + LEFT).point_from_proportion(0.35) + 0.22 * UP).set_color(GREEN)
        
        self.play(FadeIn(bracket_1))
        self.wait(0.3)
        self.play(FadeIn(bracket_1_label), run_time=0.5)
        self.wait(1.5)
        self.play(FadeIn(bracket_2))
        self.wait(0.3)
        self.play(FadeIn(bracket_2_label), run_time=0.5)
        self.wait(1.5)
        self.play(FadeIn(bracket_3))
        self.wait(0.3)
        self.play(FadeIn(bracket_3_label), run_time=0.5)
        self.wait(1.5)
        self.play(FadeIn(bracket_4))
        self.wait(0.3)
        self.play(FadeIn(bracket_4_label), run_time=0.5)
        self.wait()
        
        self.play(FadeOut(VGroup(info_4, info_7)))
        self.wait(0.7)
        
        task_25 = SystemOfEquations(
            MathTex('-\infty', '<', 't', '\leq', '-9'),
            MathTex('9', '\leq', 't', '<', '+\infty'),
            MathTex('t', '=', '3'),
            is_bracket=True
        ).move_to(2.5 * DOWN)
        
        task_26 = SystemOfEquations(
            MathTex('-\infty', '<', '3^x', '\leq', '-9'),
            MathTex('9', '\leq', '3^x', '<', '+\infty'),
            MathTex('3^x', '=', '3'),
            is_bracket=True
        )
        
        task_27 = SystemOfEquations(
            MathTex('9', '\leq', '3^x', '<', '+\infty').set_opacity(0.4),
            MathTex('3^x', '=', '3').set_opacity(0.4),
            is_bracket=True
        )
        
        task_28 = SystemOfEquations(
            MathTex('2', '\leq', 'x', '<', '+\infty'),
            MathTex('3^x', '=', '3').set_opacity(0.4),
            is_bracket=True
        )
        
        task_29 = SystemOfEquations(
            MathTex('2', '\leq', 'x', '<', '+\infty').set_opacity(0.4),
            MathTex('x', '=', '1'),
            is_bracket=True
        )
        
        self.play(FadeIn(task_25.brace), run_time=0.8)
        self.wait(0.4)
        self.play(Write(task_25.equations[0]))
        self.wait(0.2)
        self.play(Write(task_25.equations[1]))
        self.wait(0.2)
        self.play(Write(task_25.equations[2]))
        self.wait(2)
        
        self.play(FadeOut(VGroup(
            line, 
            dot_3, dot_3_label,
            dot_9, dot_9_label,
            dot_minus_9, dot_minus_9_label,
            bracket_1, bracket_1_label,
            bracket_2, bracket_2_label,
            bracket_3, bracket_3_label,
            bracket_4, bracket_4_label,
            task_24
        )))
        self.remove(black_1, black_2)
        self.wait(0.7)
        self.play(task_25.animate.move_to(ORIGIN))
        self.wait(0.4)
        self.play(FadeIn(info_1), run_time=0.8)
        self.wait(0.8)
        self.play(TransformSystem(task_25, task_26))
        self.wait(0.3)
        self.play(FadeOut(info_1), run_time=0.6)
        self.wait(0.3)
        
        info_8 = MathTex(r'3^x > 0 \,\, \forall x \in \mathbb{R}').move_to(3.5 * DOWN).set_opacity(0.9)
        self.play(
            task_26.equations[1].animate.set_opacity(0.4),
            task_26.equations[2].animate.set_opacity(0.4),
        )
        self.wait(0.2)
        self.play(Write(info_8))
        self.wait()
        self.play(TransformSystem(task_26, task_27))
        self.play(FadeOut(info_8), run_time=0.7)
        self.play(task_27.equations[0].animate.set_opacity(1))
        self.wait(0.6)
        
        info_9 = MathTex('9', '\leq', '3^x', '<', '+\infty').move_to(2.7 * DOWN)
        info_10 = MathTex('\log_3{9}', '\leq', 'x', '<', '+\infty').move_to(2.7 * DOWN)
        info_11 = MathTex('2', '\leq', 'x', '<', '+\infty').move_to(2.7 * DOWN)
        
        self.play(Write(info_9))
        self.wait()
        self.play(TransformMatchingTex(info_9, info_10))
        self.wait()
        self.play(TransformMatchingTex(info_10, info_11))
        self.wait(0.7)
        
        self.play(TransformSystem(task_27, task_28))
        self.wait(0.7)
        self.play(
            task_28.equations[0].animate.set_opacity(0.4),
            task_28.equations[1].animate.set_opacity(1),
            FadeOut(info_11)
        )
        self.wait(0.7)
        
        info_12 = MathTex('3^x', '=', '3').move_to(2.7 * DOWN)
        info_13 = MathTex('x', '=', '1').move_to(2.7 * DOWN)
        
        self.play(Write(info_12))
        self.wait(0.9)
        self.play(TransformMatchingTex(info_12, info_13))
        self.wait(0.5)
        
        self.play(TransformSystem(task_28, task_29))
        self.play(FadeOut(info_13))
        self.wait(0.8)
        self.play(task_29.equations[0].animate.set_opacity(1))
        
        ans = Tex('Answer: $\{1\} \cup [2; +\infty)$').move_to(2 * DOWN)
        box = SurroundingRectangle(ans, buff=0.2)
        
        self.play(Write(ans))
        self.play(ShowPassingFlash(box), run_time=1.5)
        
        
        
        
        
        
        self.wait(3)
        

class Task_16_economics(Scene):
    def construct(self):
        task_text_1 = Tex(r'In July 2023, it is planned to take out a loan from a bank for a certain amount. ' +
                          r'The conditions for its return are as follows: ',
                            font_size=31)
        task_text_2 = Tex(r'- every January, the debt increases by 25\% compared to the end of the previous year',
                          font_size=31).move_to(task_text_1.get_left() + 0.9 * DOWN)
        task_text_3 = Tex(r'- from February to June of each year, it is necessary to pay part of the debt \,\,\, in one payment.',
                          font_size=31).move_to(task_text_1.get_left() + 1.67 * DOWN)
        task_text_4 = Tex(
            'How many rubles are you planning to borrow from the bank ' +
             'if it is known that the loan will be fully repaid in three equal payments (i.e. in 3 years) ' +
             'and the total amount of payments after full repayment of the loan is 65500 rubles more than the amount borrowed?',
             font_size=32
        ).move_to(2.8 * DOWN)
        
        task_text_2.shift(0.5 * RIGHT * task_text_2.width)
        task_text_3.shift(0.5 * RIGHT * task_text_3.width)

        
        task_text = VGroup(task_text_1, task_text_2, task_text_3, task_text_4).shift(1.5 * UP)
        
        rectangle = SurroundingRectangle(task_text, buff=0.3)
        task_label = Tex("Task 16. Economics").scale(1.2).to_edge(UP)
        
        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text, run_time=8))
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(1.35 * UP).scale(0.5),
        ))
        self.wait(1.5)
        
        info_1 = Tex("$S$ - total amount").move_to(0.4 * UP)
        info_1[0][0].set_color(RED)
        info_2 = Tex('$x$ - annual payment').move_to(0.4 * DOWN)
        info_2[0][0].set_color(BLUE)
        
        self.play(Write(info_1))
        self.wait(0.9)
        self.play(Write(info_2))
        self.wait(0.9)
        
        self.play(
            info_1.animate.move_to(3.5 * DOWN + 4 * LEFT).set_color(WHITE).set_opacity(0.4),
            info_2.animate.move_to(3.5 * DOWN + 4 * RIGHT).set_color(WHITE).set_opacity(0.4),
        )
        
        self.wait(1.5)
        
        solution_1 = MathTex('\mathrm{After \; 1 \; year}\colon \;', '1.25S - x', substrings_to_isolate=['S', 'x']).move_to(0.5 * DOWN)
        solution_1.set_color_by_tex('S', RED)
        solution_1.set_color_by_tex('x', BLUE)
        
        solution_2 = MathTex('\mathrm{After \; 2 \; years}\colon \;', '1.25(1.25S - x) - x', substrings_to_isolate=['S', 'x']).move_to(0.5 * DOWN)
        solution_2.set_color_by_tex('S', RED)
        solution_2.set_color_by_tex('x', BLUE)
        
        solution_3 = MathTex('\mathrm{After \; 3 \; years}\colon \; ', '1.25(1.25(1.25S - x) - x) - x', substrings_to_isolate=['S', 'x']).move_to(0.5 * DOWN)
        solution_3.set_color_by_tex('S', RED)
        solution_3.set_color_by_tex('x', BLUE)
        
        self.play(Write(solution_1))
        self.wait()
        self.play(solution_1.animate.shift(0.75 * UP).set_opacity(0.5).scale(0.7).set_color(WHITE), run_time=0.8)
        self.play(Write(solution_2))
        self.wait()
        self.play(
            FadeOut(solution_1), 
            solution_2.animate.shift(0.75 * UP).set_opacity(0.5).scale(0.7).set_color(WHITE),
            run_time=0.8
        )
        self.play(Write(solution_3))
        self.wait()
        self.play(
            FadeOut(solution_2),
            solution_3.animate.shift(0.75 * UP).set_opacity(0.5).scale(0.7).set_color(WHITE),
            run_time=0.8
        )
        self.wait()
        
        label_1 = MathTex(
            '1.25', '(', '1.25', '(', '1.25', 'S', '-', 'x', ')', '-', 'x', ')', '-', 'x', '=', '0'
        ).shift(DOWN)
        
        label_2 = MathTex(
            '\dfrac{5}{4}', '\Biggl(', '\dfrac{5}{4}', '\Biggl(', '\dfrac{5}{4}', 'S', '-', 'x', '\Biggl)', '-', 'x', '\Biggl)', '-', 'x', '=', '0'
        ).shift(DOWN)
        
        label_3 = MathTex(
            '\dfrac{25}{16}', '\Biggl(', '\dfrac{5}{4}', 'S', '-', 'x', '\Biggl)', '-', '\dfrac{5x}{4}',  '-', 'x', '=', '0'
        ).shift(DOWN)
        
        label_4 = MathTex(
            '\dfrac{125}{64}', 'S', '-', '\dfrac{25x}{16}', '-', '\dfrac{5x}{4}','-', 'x', '=', '0'
        ).shift(DOWN)
        
        label_5 = MathTex(
            '\dfrac{125}{64}', 'S', '=', '\dfrac{25x}{16}', '+', '\dfrac{5x}{4}', '+', 'x'
        ).shift(DOWN)
        
        label_6 = MathTex(
            '\dfrac{125}{64}', 'S', '=', '\dfrac{25x}{16}', '+', '\dfrac{20x}{16}', '+', '\dfrac{16x}{16}'
        ).shift(DOWN)
        
        label_7 = MathTex(
            '\dfrac{125}{64}', 'S', '=', '\dfrac{25x + 20x + 16x}{16}',
        ).shift(DOWN)
        
        label_8 = MathTex(
            '\dfrac{125}{64}', 'S', '=', '\dfrac{61x}{16}',
        ).shift(DOWN)  
        
        label_9 = MathTex(
            '\dfrac{125}{64}', 'S', '=', '\dfrac{244x}{64}',
        ).shift(DOWN)        
        
        label_10 = MathTex(
            '125', 'S', '=', '244', 'x'
        ).shift(DOWN) 
        
        label_11 = MathTex(
           '\dfrac{125}{244} S', '=', 'x'    
        ).shift(DOWN) 
        
        label_12 = MathTex(
           'x', '=', '\dfrac{125}{244} S'    
        ).shift(DOWN) 
        
        

        
        
        self.play(Write(label_1))
        self.wait()
        self.play(TransformMatchingTex(label_1, label_2))
        self.wait()
        self.play(TransformMatchingTex(label_2, label_3))
        self.wait()
        self.play(TransformMatchingTex(label_3, label_4))
        self.wait()
        self.play(TransformMatchingTex(label_4, label_5))
        self.wait()
        self.play(TransformMatchingTex(label_5, label_6))
        self.wait(0.8)
        self.play(TransformMatchingTex(label_6, label_7))
        self.wait(0.8)
        self.play(TransformMatchingTex(label_7, label_8))
        self.wait(0.8)
        self.play(TransformMatchingTex(label_8, label_9))
        self.wait(0.8)
        self.play(TransformMatchingTex(label_9, label_10))
        self.wait(0.8)
        self.play(TransformMatchingTex(label_10, label_11))
        self.wait(0.8)
        self.play(TransformMatchingTex(label_11, label_12))
        self.wait(0.8)
        self.play(FadeOut(solution_3), label_12.animate.shift(0.9 * UP).set_opacity(0.5).scale(0.7))
        self.wait()
        
        label_13 = MathTex('3', 'x', '=', 'S', '+', '65500').shift(DOWN) 
        label_14 = MathTex('3', '\dfrac{125}{244} S', '=', 'S', '+', '65500').shift(DOWN) 
        label_15 = MathTex('\dfrac{3 \cdot 125}{244} S', '=', 'S', '+', '65500').shift(DOWN) 
        label_16 = MathTex('\dfrac{375}{244} S', '=', 'S', '+', '65500').shift(DOWN) 
        label_17 = MathTex('\dfrac{375}{244} S', '-', 'S' '=', '65500').shift(DOWN) 
        label_18 = MathTex('\dfrac{375}{244} S', '-', '\dfrac{244}{244} S' '=', '65500').shift(DOWN) 
        label_19 = MathTex('\dfrac{375 S}{244}', '-', '\dfrac{244 S}{375}' '=', '65500').shift(DOWN) 
        label_20 = MathTex('\dfrac{375 S - 244 S}{244}',  '=', '65500').shift(DOWN) 
        label_21 = MathTex('\dfrac{131S}{244}',  '=', '65500').shift(DOWN) 
        label_22 = MathTex('131S',  '=', '65500', '\cdot', '244').shift(DOWN) 
        label_23 = MathTex('131S',  '=', '15 982 000').shift(DOWN) 
        label_24 = MathTex('S',  '=', '122 000').shift(DOWN) 
        
        self.play(Write(label_13))
        self.wait(0.8)
        self.play(TransformMatchingTex(label_13, label_14))
        self.wait(0.8)
        self.play(TransformMatchingTex(label_14, label_15))
        self.wait(0.8)
        self.play(TransformMatchingTex(label_15, label_16))
        self.wait(0.8)
        self.play(TransformMatchingTex(label_16, label_17))
        self.wait(0.8)
        self.play(TransformMatchingTex(label_17, label_18))
        self.wait(0.8)
        self.play(TransformMatchingTex(label_18, label_19))
        self.wait(0.8)
        self.play(TransformMatchingTex(label_19, label_20))
        self.wait(0.8)
        self.play(TransformMatchingTex(label_20, label_21))
        self.wait(0.8)
        self.play(TransformMatchingTex(label_21, label_22))
        self.wait(0.8)
        self.play(TransformMatchingTex(label_22, label_23))
        self.wait(0.8)
        self.play(TransformMatchingTex(label_23, label_24))
        self.wait(2)
        self.play(FadeOut(label_12), label_24.animate.shift(0.7 * UP).set_opacity(0.5).scale(0.7))
        self.wait(0.8)
        
        ans = Tex('Answer: 122000').move_to(1.5 * DOWN)
        box = SurroundingRectangle(ans)
        
        self.play(Write(ans))
        self.play(ShowPassingFlash(box))
        
        
        
        
        
        self.wait(3)

         
class Task_17_planimetry(Scene):
    def construct(self):
        task_text_1 = Tex(r'The circle centered at point $O$ touches the sides of the corner with vertex $N$ at points $A$ and $B$. ' +
                        r'Line BC is the diameter of this circle. ',
                        font_size=36)
        task_text_2 = Tex(r'a) Prove that the line $AC$ is parallel to the bisector of the angle $\angle{ANB}$.',
                          font_size=36).move_to(task_text_1.get_left() + 0.75 * DOWN)
        task_text_3 = Tex(r'b) Find $NO$ if $AB = 24$, $AC = 10$.',
                          font_size=36).move_to(task_text_1.get_left() + 1.15 * DOWN)
        
        task_text_2.shift(0.5 * RIGHT * task_text_2.width)
        task_text_3.shift(0.5 * RIGHT * task_text_3.width)

        
        task_text = VGroup(task_text_1, task_text_2, task_text_3)   
        
        rectangle = SurroundingRectangle(task_text, buff=0.3)
        task_label = Tex("Task 17. Planimetry").scale(1.2).to_edge(UP)

        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text, run_time=8))
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.6 * UP).scale(0.6),
        ))
        self.wait(1.5)
        
        
        N = Dot(2.5 * LEFT + 1.2 * UP).set_z_index(9)
        N_label = Tex("N", font_size=36).move_to(N.get_center() + 0.25 * UL).set_z_index(9)
        
        X = Dot(0.7 * DOWN + 3.8 * RIGHT)
        Y = Dot(3.2 * DOWN + 1 * LEFT)
        
        line_1 = Line(X, N, color=BLUE).scale(0.7, about_point=N.get_center())
        line_2 = Line(N, Y, color=BLUE).scale(0.9, about_point=N.get_center())
        
        circle = Incircle(N, X, Y, color=RED)
        
        O = Dot(circle.get_center()).set_z_index(9)
        O_label = Tex("O", font_size=36).move_to(O.get_center() + 0.32 * DOWN)
        
        A = Dot(intersection_line_and_circle(line_1, circle)[0]).set_z_index(9)
        B = Dot(intersection_line_and_circle(line_2, circle)[0]).set_z_index(9)
        C = Dot(circle.get_diametrically_opposite_point(B)).set_z_index(9)
        
        A_label = Tex("A", font_size=36).move_to(A.get_center() + 0.32 * UP)
        B_label = Tex("B", font_size=36).move_to(B.get_center() + 0.32 * LEFT)
        C_label = Tex("C", font_size=36).move_to(C.get_center() + 0.29 * RIGHT)
        
        AB = Line(A, B, color=YELLOW)
        BC = Line(B, C, color=YELLOW)
        AC = Line(A, C, color=GREEN)
        
        OB = Line(O, B, color=YELLOW)
        OC = Line(O, C, color=YELLOW)
        OA = Line(O, A, color=YELLOW)
        
        ON = Line(O, N, color=GREEN)
        
        OA_equal = OA.equal(2)
        OB_equal = OB.equal(2)
        OC_equal = OC.equal(2)
        
        AC_label = MathTex('10', font_size=30).move_to(AC.get_center() + 0.11 * UP + 0.18 * RIGHT)
        AB_label = MathTex('24', font_size=30).move_to(AB.point_from_proportion(0.45) + 0.28 * UP + 0.1 * LEFT)
        
        OB_label = MathTex('13', font_size=30).move_to(OB.get_center() + 0.28 * DOWN + 0.1 * RIGHT)
        OC_label = MathTex('13', font_size=30).move_to(OC.get_center() + 0.28 * DOWN + 0.1 * RIGHT)
        
        
        angle_OBN = Angle.from_three_points(O, B, N, color=YELLOW, elbow=True, radius=0.27).set_z_index(-1)
        angle_OAN = Angle.from_three_points(O, A, N, color=YELLOW, elbow=True, radius=0.27).set_z_index(-1)
        
        angle_BON = Angle.from_three_points(B, O, N, color=YELLOW, radius=0.35).set_z_index(-1)
        angle_AON = Angle.from_three_points(A, O, N, color=YELLOW, radius=0.38).set_z_index(-1)
        
        angle_BON_label = MathTex(r'\beta', font_size=32).move_to(angle_BON.get_label_center())
        angle_AON_label = MathTex(r'\beta', font_size=32).move_to(angle_AON.get_label_center())
        
        angle_OAC = Angle.from_three_points(O, A, C, color=YELLOW).set_z_index(-1)
        angle_OCA = Angle.from_three_points(O, C, A, color=YELLOW).set_z_index(-1)
        
        angle_OAC_label = MathTex(r'\gamma', font_size=32).move_to(angle_OAC.get_label_center())
        angle_OCA_label = MathTex(r'\gamma', font_size=32).move_to(angle_OCA.get_label_center())
        
        angle_OAC_label_new = MathTex(r'\beta', font_size=32).move_to(angle_OAC.get_label_center())
        angle_OCA_label_new = MathTex(r'\beta', font_size=32).move_to(angle_OCA.get_label_center())
        
        angle_BAC = Angle.from_three_points(B, A, C, color=YELLOW, elbow=True, radius=0.27).set_z_index(-1)
        
        bisector = Bisector(A, N, B, color=GREEN).scale(1.8, about_point=N.get_center())
        bisected_angles = bisector.get_bisected_angles(color=YELLOW)
        bisected_angles_labels = VGroup(
            MathTex(r'\alpha', font_size=36).move_to(bisected_angles[0].get_label_center()),
            MathTex(r'\alpha', font_size=36).move_to(bisected_angles[1].get_label_center())
        )

        
        self.play(FadeIn(VGroup(N, N_label)))
        self.wait(0.4)
        self.play(LaggedStart(
            Create(line_1),
            Create(line_2),
            lag_ratio=0.15
        ))
        
        self.wait()
        self.play(Create(circle))
        self.wait(0.7)
        self.play(FadeIn(VGroup(O, O_label)))
        self.wait()
        self.play(LaggedStart(
            FadeIn(VGroup(A, A_label)),
            FadeIn(VGroup(B, B_label)),
            run_time=0.9, lag_ratio=0.3
        ))
        self.wait()
        
        self.play(Create(BC))
        self.wait(0.3)
        self.play(FadeIn(VGroup(C, C_label)))
        self.wait(0.8)
        self.play(BC.animate.set_opacity(0.5))
        self.wait(1.5)
        
        self.play(LaggedStart(
            Create(AC),
            Create(bisector),
            run_time=2, lag_ratio=0.1
        ))
        self.play(FadeIn(bisected_angles, lag_ratio=0.4), run_time=0.8)
        self.wait()
        
        self.play(FadeIn(bisected_angles_labels, lag_ratio=0.5), run_time=1.2)
        self.wait(2)
        
        self.play(Flash(O))
        self.wait()
        
        
        
        self.play(FadeIn(OB), run_time=0.7)
        self.play(FadeIn(angle_OBN), run_time=0.9)
        self.wait()
        self.play(Create(OA), run_time=0.7)
        self.play(FadeIn(angle_OAN), run_time=0.9)
        self.wait(2)
        self.play(FadeIn(VGroup(angle_BON, angle_BON_label)), run_time=0.9)
        
        info_1 = MathTex(r'\beta', '=', '90^{\\circ}', '-', '\\alpha').shift(3.5 * DOWN)
        self.play(Write(info_1))
        
        self.wait(2)
        self.play(FadeIn(VGroup(angle_AON, angle_AON_label)), run_time=0.9)
        
        self.wait()
        self.play(
            FadeOut(VGroup(angle_OBN, angle_OAN, OB)),
            FadeIn(OC)
        )
        
        self.wait(3)
        self.play(FadeIn(VGroup(OA_equal, OC_equal), lag_ratio=0.4))
        self.wait(2)
        
        self.play(FadeIn(VGroup(angle_OAC, angle_OAC_label)))
        self.play(FadeIn(VGroup(angle_OCA, angle_OCA_label)))
        self.wait(1.5)
        
        info_2 = MathTex('2', r'\beta', '=', '2', r'\gamma').shift(3.5 * DOWN)
        info_3 = MathTex(r'\beta', '=', r'\gamma').shift(3.5 * DOWN)
        
        self.play(TransformMatchingTex(info_1, info_2))
        self.wait()
        self.play(TransformMatchingTex(info_2, info_3))
        self.wait()
        
        self.play(Transform(angle_OAC_label, angle_OAC_label_new))
        self.play(Transform(angle_OCA_label, angle_OCA_label_new))
        
        self.play(FadeOut(VGroup(OA_equal, OC_equal)), run_time=0.7)
        self.play(FadeOut(VGroup(
            angle_AON, angle_AON_label, angle_OAC, angle_OAC_label, info_3
        )))
        self.play(
            OA.animate.set_opacity(0.5),
            BC.animate.set_opacity(1)
        )
        self.remove(OC)
        self.wait()
        
        self.play(Flash(VGroup(angle_BON, angle_BON_label), flash_radius=0.25))
        self.play(Flash(VGroup(angle_OCA, angle_OCA_label_new), flash_radius=0.25))
        
        
        self.wait(3)
        
        self.play(FadeIn(AC_label))
        self.wait()
        self.play(Create(AB))
        self.play(FadeIn(AB_label))
        self.wait(1.5)
        
        self.play(FadeIn(angle_BAC))
        self.play(circle.animate.set_stroke(opacity=0.5))
        
        info_4 = MathTex('BC', '^2', '=', 'AC', '^2', '+', 'AB', '^2').shift(3.5 * DOWN)
        info_5 = MathTex('BC', '^2', '=', '10', '^2', '+', '24', '^2').shift(3.5 * DOWN)
        info_6 = MathTex('BC', '^2', '=', '100',  '+', '576').shift(3.5 * DOWN)
        info_7 = MathTex('BC', '^2', '=', '676').shift(3.5 * DOWN)
        info_8 = MathTex('BC', '=', '26').shift(3.5 * DOWN)
        
        self.play(FadeIn(info_4))
        self.wait()
        self.play(TransformMatchingTex(info_4, info_5))
        self.wait()
        self.play(TransformMatchingTex(info_5, info_6))
        self.wait()
        self.play(TransformMatchingTex(info_6, info_7))
        self.wait()
        self.play(TransformMatchingTex(info_7, info_8))
        self.wait()
        
        self.play(LaggedStart(
            FadeIn(OB_equal),
            FadeIn(OC_equal),
            lag_ratio=0.4
        ))
        self.wait(0.7)
        self.play(LaggedStart(
            FadeIn(OB_label),
            FadeIn(OC_label),
            lag_ratio=0.4
        ))
        self.play(FadeOut(VGroup(
            info_8, OB_equal, OC_equal
        ), run_time=0.8))
        
        N_copy = N.copy()
        B_copy = B.copy()
        O_copy = O.copy()
        
        N_label_copy = N_label.copy()
        B_label_copy = B_label.copy()
        O_label_copy = O_label.copy()

        NB_copy = Line(N, B, color=BLUE).copy()
        BO_copy = Line(B, O, color=YELLOW).copy()
        ON_copy = Line(O, N, color=GREEN).copy()
        
        angle_BON_copy = angle_BON.copy()
        angle_BON_label_copy = angle_BON_label.copy()
        
        angle_ONB_copy = bisected_angles[1].copy()
        angle_ONB_label_copy = bisected_angles_labels[1].copy()
        
        OB_label_copy = OB_label.copy()
        
        A_copy = A.copy()
        B_copy_2 = B.copy()
        C_copy = C.copy()
        
        A_label_copy = A_label.copy()
        B_label_copy_2 = B_label.copy()
        C_label_copy = C_label.copy()
        
        AB_copy = AB.copy()
        BC_copy = BC.copy()
        AC_copy = AC.copy()
        
        angle_BAC_copy = angle_BAC.copy()
        angle_OCA_copy = angle_OCA.copy()
        
        angle_OCA_label_copy = angle_OCA_label_new.copy()
        
        O_copy_2 = O.copy()
        O_label_copy_2 = O_label.copy()
        
        OB_label_copy_2 = OB_label.copy()
        OC_label_copy = OC_label.copy()
        AC_label_copy = AC_label.copy()
        AB_label_copy = AB_label.copy()
        
        
        self.remove(angle_OCA_label)
        ALL = VGroup(
            A, B, C, N, O,
            A_label, B_label, C_label, N_label, O_label,
            line_1, line_2, circle,
            bisector, bisected_angles, bisected_angles_labels,
            BC, AB, AC, OA,
            angle_BAC, angle_OCA, angle_OCA_label_new, angle_BON, angle_BON_label,
            AB_label, AC_label, OB_label, OC_label,
            
        )
        
        BON_copy = VGroup(
            N_copy, B_copy, O_copy,
            N_label_copy, B_label_copy, O_label_copy,
            NB_copy, BO_copy, ON_copy, 
            angle_BON_copy, angle_BON_label_copy,
            angle_ONB_copy, angle_ONB_label_copy,
            OB_label_copy
        )
        
        ABC_copy = VGroup(
            A_copy, B_copy_2, C_copy,
            A_label_copy, B_label_copy_2, C_label_copy,
            AB_copy, BC_copy, AC_copy,
            angle_BAC_copy, angle_OCA_copy, angle_OCA_label_copy,
            O_copy_2, O_label_copy_2,
            OB_label_copy_2, OC_label_copy, AC_label_copy, AB_label_copy
        )
        
        self.add(BON_copy)
        shift_BON = 4 * RIGHT + 0.3 * UP
        shift_ABC = 5 * RIGHT + 1.8 * DOWN
        shift_ALL = 3.4 * LEFT
        self.play(
            LaggedStart(
                BON_copy.animate.shift(shift_BON),
                O_label_copy.animate.move_to(O.copy().get_center() + shift_BON +  + 0.32 * RIGHT),
                ABC_copy.animate.shift(shift_ABC),
                ALL.animate.shift(shift_ALL),
                lag_ratio=0.1, run_time=1.2
            )
        )
        self.wait(2)

        
        BON_copy_bottom = BON_copy.get_bottom() + DOWN + 0.5 * LEFT
        ABC_copy_bottom = BON_copy_bottom + 3 * RIGHT 
        
        
        ABC_copy = VGroup(
            A_copy, B_copy_2, C_copy,
            AB_copy, BC_copy, AC_copy,
            angle_BAC_copy, angle_OCA_copy, 
            O_copy_2
        )
        
        ABC_copy_labels = VGroup(
            A_label_copy, B_label_copy_2, C_label_copy,
            OB_label_copy_2, OC_label_copy, AC_label_copy, AB_label_copy,
            angle_OCA_label_copy, O_label_copy_2,
        )
        
        BON_copy = VGroup(
            N_copy, B_copy, O_copy,
            ON_copy, NB_copy, BO_copy,
            angle_BON_copy, angle_ONB_copy,
        )
        
        BON_copy_labels = VGroup(
            N_label_copy, B_label_copy, O_label_copy,
            angle_BON_label_copy, angle_ONB_label_copy,
            OB_label_copy
        )
        
        ABC_copy_angle = PI-AC_copy.get_angle()
        BON_copy_angle = -BO_copy.get_angle() 
        
        scale_ABC = 0.95
        scale_BON = 1.05
        
        ABC_copy_labels_tmp = ABC_copy_labels.copy().scale(scale_ABC).rotate(ABC_copy_angle).flip().next_to(ABC_copy_bottom, direction=UP, buff=0)
        BON_copy_labels_tmp = BON_copy_labels.copy().scale(scale_BON).rotate(BON_copy_angle).next_to(BON_copy_bottom, direction=UP, buff=0)
    
        delta_ABC = 0.3 * DOWN + 0.015 * LEFT
        delta_BON = 0.45 * DOWN + 0.015 * LEFT
    
        
        ABC_copy_labels_animations = AnimationGroup(
            *[ABC_copy_labels[i].animate.move_to(ABC_copy_labels_tmp[i].get_center()).shift(delta_ABC) for i in range(len(ABC_copy_labels_tmp))]
        )
        BON_copy_labels_animations = AnimationGroup(
            *[BON_copy_labels[i].animate.move_to(BON_copy_labels_tmp[i].get_center()).shift(delta_BON) for i in range(len(BON_copy_labels_tmp))]
        )
        
        
        
        self.play(LaggedStart(
            ABC_copy.animate.scale(scale_ABC).rotate(ABC_copy_angle).flip().next_to(ABC_copy_bottom, direction=UP, buff=0),
            ABC_copy_labels_animations,
            
            BON_copy.animate.scale(scale_BON).rotate(BON_copy_angle).next_to(BON_copy_bottom, direction=UP, buff=0),
            BON_copy_labels_animations,
            OB_label_copy.animate.move_to(BON_copy_labels_tmp[5].get_center() + 0.25 * DOWN),
            B_label_copy.animate.move_to(BON_copy_labels_tmp[1].get_center() + 0.68 * DOWN + 0.05 * RIGHT),
            
            lag_ratio=0.05, run_time=1.2
        ))
        
        self.wait()
        
        A_copy = A_copy.move_to([A_copy.get_x(), A_copy.get_y(), 0])
        A_copy = A_copy.move_to([A_copy.get_x(), A_copy.get_y(), 0])
        B_copy_2 = B_copy_2.move_to([B_copy_2.get_x(), B_copy_2.get_y(), 0])
        C_copy = C_copy.move_to([C_copy.get_x(), C_copy.get_y(), 0])
        
        angle_OBN_copy = Angle.from_three_points(O_copy, B_copy, N_copy, color=YELLOW, elbow=True, radius=0.3).set_z_index(-1)
        angle_ABC_copy = Angle.from_three_points(A_copy, B_copy_2, C_copy, color=YELLOW).set_z_index(-1)
        angle_ABC_label_copy = MathTex(r'\alpha', font_size=30).move_to(angle_ABC_copy.get_label_center(delta=0.3))
        
        self.wait()
  
        self.play(FadeIn(angle_OBN_copy))
        self.play(FadeIn(VGroup(angle_ABC_copy, angle_ABC_label_copy)))

        self.wait()
        
        BC_copy_label = MathTex('26', font_size=30).move_to(BC_copy.get_center() + 0.3 * RIGHT)
        
        self.play(LaggedStart(
            FadeOut(VGroup(O_copy_2, O_label_copy_2)),
            FadeOut(VGroup(OB_label_copy_2, OC_label_copy)),
            FadeIn(BC_copy_label),
            lag_ratio=0.5, run_time=1.5
        ))
        
        info_9 = MathTex(r'\dfrac{ON}{13}', '=', r'\dfrac{26}{10}').shift(3.5 * DOWN)
        info_10 = MathTex(r'ON', '=', r'\dfrac{26}{10}', '\cdot 13').shift(3.5 * DOWN)
        info_11 = MathTex(r'ON', '=', '33.8').shift(3.5 * DOWN)
        
        info_12 = Tex(r'Answer: $33.8$').shift(3.5 * DOWN)
        rectangle = SurroundingRectangle(info_12)     
        
        
        
        self.play(Write(info_9))
        self.wait()
        self.play(TransformMatchingTex(info_9, info_10))
        self.wait()
        self.play(TransformMatchingTex(info_10, info_11))
        self.wait(2)
        
        self.play(Transform(info_11, info_12))
        self.play(ShowPassingFlash(rectangle))
        self.wait(2)
        

        self.wait(3)
        

class Task_18_parameter(ZoomedScene):
    def _get_roots(self, a):
        def func(x):
            return np.sqrt(x + 4)
        def func_1(x):
            return a - x - np.sqrt(x + 4)
        def func_2(x):
            return a + x - np.sqrt(x + 4)
        
        initial_guesses = [-4, 0, 4]

        roots_1 = []
        roots_2 = []

        for guess in initial_guesses:
            root_1 = fsolve(func_1, x0=[guess])
            root_2 = fsolve(func_2, x0=[guess])
            if (abs(func_1(root_1[0])) <= 0.001):
                roots_1.append(root_1[0])
            if (abs(func_2(root_2[0])) <= 0.001):
                roots_2.append(root_2[0])

        roots_1 = np.unique(np.round(roots_1, 4))
        roots_2 = np.unique(np.round(roots_2, 4))
        roots = np.union1d(roots_1, roots_2)
        
        
        dots = []
        for root in roots:
            dots.append(np.array([root, func(root), 0]))
        return dots
    
        
    def construct(self):
        task_text_1 = Tex(r'Find all the values of parameter a, for each of which the system of equations ', font_size=36)
        task_text_2 = SystemOfEquations(
            MathTex('|x| + |y| = a', font_size=36),
            MathTex('y = \sqrt{x + 4}', font_size=36)
        ).move_to(1.1 * DOWN)
        task_text_3 = Tex(r'has 2 solutions',font_size=36).move_to(task_text_1.get_left() + 1.6 * DOWN)
        
        task_text_3.shift(0.5 * RIGHT * task_text_3.width)


        task_text = VGroup(task_text_1, task_text_2, task_text_3)   
        
        rectangle = SurroundingRectangle(task_text, buff=0.3)
        task_label = Tex("Task 18. Parameter").scale(1.2).to_edge(UP)


        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text, run_time=8))
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.6 * UP).scale(0.6),
        ))
        self.wait(1.5)
        
        
        system = SystemOfEquations(
            MathTex('|x|', '+', '|y|', '=', 'a'),
            MathTex('y', '=', '\sqrt{x + 4}')
        )
        
        plane = NumberPlane(
            x_range=[-6, 6], 
            y_range=[-5, 5],
            axis_config={"color": WHITE},
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 1.5,
                "stroke_opacity": 0.4
            }
        ).scale(0.52).shift(2.4 * LEFT + 1.2 * DOWN)
        
        self.play(Write(system))
        self.wait(1.5)
        self.play(system.animate.shift(4 * RIGHT + UP).scale(0.8))
        self.play(Create(plane))
        
        a = ValueTracker(0)
        a_text = always_redraw(lambda: VGroup(
            Tex('a ='),
            DecimalNumber(0).add_updater(lambda d: d.set_value(a.get_value()))
        ).arrange().move_to(
            np.array([system.get_center()[0], plane.get_center()[1], 0])
        ))
        
        square = always_redraw(lambda: Square(
            side_length=(np.sqrt(2) * a.get_value()) * Line(plane.coords_to_point(0, 0), plane.coords_to_point(1, 0)).get_length(),
            color=YELLOW
        ).rotate(PI / 4).move_to(plane.get_center()))
        
        dot = always_redraw(lambda: Dot(plane.coords_to_point(0, a.get_value())))
        dot_label = always_redraw(lambda: MathTex('(0, a)').move_to(dot.get_center() + 0.3 * UP + 0.5 * RIGHT).scale(0.7))
                
        self.play(system.equations[1].animate.set_opacity(0.4))    
        self.add(square)
        self.play(Write(a_text))
        self.play(FadeIn(VGroup(dot, dot_label)), run_time=0.4)
        self.play(a.animate.set_value(3.5), 
                  run_time=2, 
                  rate_func=rate_functions.ease_in_out_sine)    
        self.wait()
        
        tmp_info_1 = MathTex('|x|', '+', '|y|', '\geq', '0').move_to(a_text.get_center() + 0.7 * DOWN).scale(0.7).set_opacity(0.85)
        tmp_info_2 = MathTex('a', '\geq', '0').move_to(a_text.get_center() + 0.7 * DOWN).scale(0.7).set_opacity(0.85)
        self.play(Write(tmp_info_1))
        self.wait(0.8)
        self.play(TransformMatchingTex(tmp_info_1, tmp_info_2))
        self.wait(0.8)
        self.play(FadeOut(tmp_info_2))
        self.wait(0.5)
        
        self.play(a.animate.set_value(0), 
                  run_time=2, 
                  rate_func=rate_functions.ease_in_out_sine)    
        self.play(FadeOut(a_text, dot, dot_label))
        self.wait(0.8)
        self.play(
            system.equations[0].animate.set_opacity(0.4),
            system.equations[1].animate.set_opacity(1),
        )
        self.wait(0.6)
        
        plot = plane.plot(lambda x: np.sqrt(x + 4), x_range=(-4, 5), use_smoothing=False, color=RED)
        self.play(Create(plot))
        self.wait()
        
        
        ans_1 = MathTex('(', '2', ';').move_to(system.get_center())
        ans_2 = MathTex('(', '2', ';', '4', ')').move_to(system.get_center())
        ans_3 = MathTex('(', '2', ';', '4', ')', '\cup', '\{', '4.25', '\}').move_to(system.get_center())
        
        ans_1.shift((ans_3.width - ans_1.width) / 2 * LEFT)
        ans_2.shift((ans_3.width - ans_2.width) / 2 * LEFT)
        
        
        self.play(FadeIn(a_text))
        self.play(
            system.equations[0].animate.set_opacity(1)
        )
        self.add(square)
        self.wait()
        self.play(a.animate.set_value(2), run_time=2.5)
        intersections = always_redraw(lambda: VGroup(*[Dot(plane.coords_to_point(coords[0], coords[1])) for coords in self._get_roots(a.get_value())]).set_z_index(5))
        self.play(FadeIn(intersections))
        self.wait(0.7)
        
        self.play(FadeOut(system))
        self.wait(0.4)
        self.play(Write(ans_1))
        self.wait(0.3)
        
        self.play(Flash(Dot(plane.coords_to_point(0, 2))))
        self.play(a.animate.set_value(4), run_time=5)
        self.wait(1.5)
        
        self.play(TransformMatchingTex(ans_1, ans_2))
        self.wait(0.4)
        
        self.play(a.animate.set_value(17/4), run_time=2)
        self.wait(6)
        
        line = Line(plane.coords_to_point(-17/4, 0), plane.coords_to_point(0, 17/4), color=GREEN).scale(1.4).set_z_index(1).shift(0.25 * DOWN + 0.25 * LEFT)
        self.play(Create(line))
        
        eq_1 = MathTex('a', '-', 'x', font_size=42).move_to(a_text.get_center() + UP)
        eq_2 = MathTex('a', '-', 'x', '=', '\sqrt{x + 4}', font_size=42).move_to(a_text.get_center() + UP)
        eq_1.shift((eq_2.width - eq_1.width) / 2 * LEFT)
        eq_3 = MathTex('(a', '-', 'x)^2', '=', 'x',  '+',  '4', font_size=42).move_to(eq_2.get_center())
        eq_4 = MathTex('a^2', '-', '2ax', '+', 'x^2', '=', 'x',  '+',  '4', font_size=42).move_to(eq_2.get_center())
        eq_5 = MathTex('x^2', '+', '2ax', '-', 'x', '+', 'a^2', '-', '4' '=', '0', font_size=42).move_to(eq_2.get_center())
        eq_6 = MathTex('x^2', '+', 'x', '(', '2a', '-', '1', ')', '+', '(', 'a^2', '-', '4', ')', '=', '0', font_size=42).move_to(eq_2.get_center())
        
        d_1 = MathTex('D', '=', '(', '2a', '-', '1', ')^2', '-', '4(', 'a^2', '-', '4', ')', font_size=35).move_to(eq_6.get_center() + 0.8 * DOWN).set_opacity(0.7)
        d_2 = MathTex('D', '=', '4a^2', '-', '4a', '+', '1', '-', '4a^2', '+', '16', font_size=35).move_to(eq_6.get_center() + 0.8 * DOWN).set_opacity(0.7)
        d_3 = MathTex('D', '=', '-', '4a', '+', '1', '+', '16',  font_size=35).move_to(eq_6.get_center() + 0.8 * DOWN).set_opacity(0.7)
        d_4 = MathTex('D', '=', '-', '4a', '+', '17', font_size=35).move_to(eq_6.get_center() + 0.8 * DOWN).set_opacity(0.7)
        d_5 = MathTex('0', '=', '-', '4a', '+', '17', font_size=35).move_to(eq_6.get_center() + 0.8 * DOWN).set_opacity(0.7)
        d_6 = MathTex('a', '=', '\dfrac{17}{4}', font_size=35).move_to(eq_6.get_center() + 1 * DOWN).set_opacity(0.7)
        d_7 = MathTex('a', '=', '4.25', font_size=35).move_to(eq_6.get_center() + 1 * DOWN).set_opacity(0.7)
        
        self.play(FadeOut(a_text))
        self.play(Write(eq_1))
        self.wait(0.6)
        self.play(TransformMatchingTex(eq_1, eq_2))
        self.wait(0.8)
        self.play(TransformMatchingTex(eq_2, eq_3))
        self.wait(0.8)
        self.play(TransformMatchingTex(eq_3, eq_4))
        self.wait(0.8)
        self.play(TransformMatchingTex(eq_4, eq_5))
        self.wait(0.8)
        self.play(TransformMatchingTex(eq_5, eq_6))
        self.wait()
        self.play(Write(d_1))
        self.wait(0.8)
        self.play(TransformMatchingTex(d_1, d_2))
        self.wait(0.8)
        self.play(TransformMatchingTex(d_2, d_3))
        self.wait(0.8)
        self.play(TransformMatchingTex(d_3, d_4))
        self.wait(2)
        self.play(TransformMatchingTex(d_4, d_5))
        self.wait(0.8)
        self.play(TransformMatchingTex(d_5, d_6))
        self.wait(0.8)
        self.play(TransformMatchingTex(d_6, d_7))
        self.wait()
        self.play(TransformMatchingTex(ans_2, ans_3))
        self.wait()
        self.play(FadeOut(VGroup(line, d_7, eq_6)), run_time=0.8)
        self.play(FadeIn(a_text), run_time=0.8)
        self.wait()
        
        self.play(a.animate.set_value(5.3), run_time=1.5)
        self.wait(0.8)
        self.play(a.animate.set_value(17/4), run_time=1.5)
        
        ans_text = Tex('Answer: ')
        ans_3_copy = ans_3.copy()
        VGroup(ans_text, ans_3_copy).arrange().move_to(ans_3)
        box = SurroundingRectangle(VGroup(ans_text, ans_3_copy))
        
        self.play(FadeIn(ans_text), ans_3.animate.move_to(ans_3_copy.get_center()))        
        self.play(ShowPassingFlash(box), run_time=1.5)
        
        
        self.wait(3)
        
        
class Coin(VGroup):
    def __init__(self, num=0, radius=0.5, font_size=52, **kwargs):
        self.circle = Circle(radius = radius, **kwargs)
        self.num = MathTex(str(num), font_size=font_size, **kwargs)
        
        super().__init__(self.circle, self.num)
        
        
class Task_19_number_theory(Scene):
    def construct(self):
        task_text_1 = Tex(r'There are 29 coins of 5 rubles and 16 coins of 2 rubles ', font_size=32)
        task_text_2 = Tex(r'a) is it possible to get 175?', font_size=32).move_to(task_text_1.get_center() + 0.65 * DOWN)
        task_text_3 = Tex(r'b) is it possible to get 176?', font_size=32).move_to(task_text_2.get_center() + 0.65 * DOWN)
        task_text_4 = Tex(r'c) how many 1 ruble coins do I need to add so that I can collect any amount from 1 to 180 inclusive?',
                          font_size=32).move_to(task_text_3.get_center() + 0.8 * DOWN)
        
        task_text_1.shift((task_text_4.width - task_text_1.width) / 2 * LEFT)
        task_text_2.shift((task_text_4.width - task_text_2.width) / 2 * LEFT)
        task_text_3.shift((task_text_4.width - task_text_3.width) / 2 * LEFT)

        
        task_text = VGroup(task_text_1, task_text_2, task_text_3, task_text_4)   
        
        rectangle = SurroundingRectangle(task_text, buff=0.3)
        task_label = Tex("Task 19. Number theory").scale(1.2).to_edge(UP)

        self.play(Write(task_label))
        self.wait(0.5)
        self.play(Create(rectangle))
        self.play(Write(task_text, run_time=8))
        self.wait()

        self.play(LaggedStart(
            FadeOut(task_label),
            VGroup(task_text, rectangle).animate.to_edge(UP).shift(0.8 * UP).scale(0.6),
        ))
        self.wait(1.5)
        
        
        coin_5 = Coin(5, color=GREEN)
        coin_2 = Coin(2, color=RED)
        
        coin_5_count = MathTex(r'29 \, \times')
        coin_2_count = MathTex(r'16 \, \times')
        
        coin_5_group = VGroup(coin_5_count, coin_5).arrange()
        coin_2_group = VGroup(coin_2_count, coin_2).arrange()
        
        coins_1 = VGroup(coin_5_group, coin_2_group).arrange(buff=0.45)
        
        self.play(Create(coins_1))
        self.wait(0.5)
        self.play(coins_1.animate.set_stroke(opacity=0.6).shift(3 * DOWN).scale(0.7))
        self.wait()
        
        coins_a = VGroup(
            MathTex(r'29 \, \times'), 
            Coin(5, color=GREEN),
            MathTex(r' + \,\, 15 \, \times'), 
            Coin(2, color=RED),
            MathTex('= 175')
        ).arrange()
        box_a = SurroundingRectangle(coins_a)
        
        self.play(Create(coins_a, lag_ratio=0.5))
        self.play(ShowPassingFlash(box_a), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(coins_a))
        self.wait()
        
        self.play(coins_1.animate.scale(1 / 0.7).move_to(ORIGIN).set_stroke(opacity=1))
        
        coins_2 = VGroup(coin_5_group.copy(), MathTex('+'), coin_2_group.copy(), MathTex('= 177')).arrange(buff=0.25)
        
        self.play(
            coins_1[0].animate.move_to(coins_2[0].get_center()),
            coins_1[1].animate.move_to(coins_2[2].get_center()),
            FadeIn(VGroup(coins_2[1], coins_2[3]))
        )
        self.remove(coins_1, coins_2[1], coins_2[3])
        self.add(coins_2)
        
        info_1 = MathTex("177 - 176 = 1").move_to(0.8 * DOWN).scale(0.7).set_opacity(0.6)
        no_coin = Coin(1, color=BLUE).shift(1.7 * DOWN)
        cross = Cross(no_coin)
        
        self.play(Write(info_1))
        self.wait(0.8)
        self.play(FadeIn(no_coin), run_time=0.8)
        self.play(Create(cross), run_time=0.8)
        
        self.wait(4)
        
        self.play(FadeOut(VGroup(info_1, no_coin, cross)))
        self.play(coins_2.animate.shift(3 * DOWN))
        self.wait()
        
        
        three_1_ruble_coins = VGroup(*[Coin(1, color=BLUE) for _ in range(3)]).arrange(buff=0.4)
        self.play(FadeIn(three_1_ruble_coins, lag_ratio=0.5))
        
        info_2 = MathTex('180 - 177 = 3').move_to(0.8 * DOWN).scale(0.7).set_opacity(0.6)
        self.play(Write(info_2))
        self.wait(3)
        
        
        coin_1 = Coin(1, color=BLUE)
        coin_1_text = MathTex(r'3 \, \times')
        coin_1_group = VGroup(coin_1_text, coin_1).arrange()
        
        coins_3 = VGroup(coin_5_group, coin_2_group, coin_1_group).arrange()
        
        self.play(
            FadeOut(three_1_ruble_coins, info_2), 
            FadeOut(VGroup(coins_2[1], coins_2[3])),
            coins_2[0].animate.move_to(coins_3[0].get_center()),
            coins_2[2].animate.move_to(coins_3[1].get_center()),
            FadeIn(coins_3[2])
        )
        self.remove(coins_2[0], coins_2[2], coins_3[2])
        self.add(coins_3)
        
        
        self.wait(3)
        
        
        big_coins = VGroup(
            MathTex(r'28 \, \times'),
            Coin(5, color=GREEN),
            MathTex(r'15 \, \times'),
            Coin(2, color=RED)
        ).arrange().shift(4 * LEFT).scale(0.85)
        
        big_info = MathTex('28 \cdot 5 + 15 \cdot 2 = 170').move_to(
            big_coins.get_center() + 0.75 * DOWN).set_opacity(0.7).scale(0.7)
        
        small_coins = VGroup(
            MathTex(r'1 \, \times'),
            Coin(5, color=GREEN),
            MathTex(r'1 \, \times'),
            Coin(2, color=RED),
            MathTex(r'3 \, \times'),
            Coin(1, color=BLUE),
        ).arrange().shift(4 * RIGHT).scale(0.85)
        
        small_info = MathTex('1 \cdot 5 + 1 \cdot 2  + 1 \cdot 3 = 10').move_to(
            small_coins.get_center() + 0.75 * DOWN).set_opacity(0.7).scale(0.7)
        
        self.play(FadeOut(coins_3), FadeIn(VGroup(big_coins, small_coins)))
        self.play(LaggedStart(
            Write(big_info),
            Write(small_info),
            run_time=1.4, lag_ratio=0.4
        ))
        
        info_3 = MathTex('a', '=', '10', '\cdot', 'b', '+', 'c').shift(3 * DOWN)
        info_4 = MathTex('58' '=' '10', '\cdot', '5', '+', '8').shift(info_3.get_center() + 0.7 * DOWN).set_opacity(0.6).scale(0.8)
        info_5 = MathTex('179' '=' '10', '\cdot', '17', '+', '9').shift(info_3.get_center() + 0.7 * DOWN).set_opacity(0.6).scale(0.8)
        
        self.play(Write(info_3))
        self.wait(0.4)
        self.play(Write(info_4))
        self.wait(1.5)
        self.play(TransformMatchingTex(info_4, info_5))
        self.wait(1.5)
        self.play(FadeOut(info_5))
        self.wait()
        
        big_brace = Brace(big_coins, direction=DOWN).shift(0.35 * DOWN)
        big_label = MathTex('10 \cdot b').move_to(big_brace.get_center() + 0.5 * DOWN)
        
        self.play(FadeIn(big_brace))
        self.play(Write(big_label))
        self.wait(2)
        
        small_brace = Brace(small_coins, direction=DOWN).shift(0.35 * DOWN)
        small_label = MathTex('c').move_to(small_brace.get_center() + 0.5 * DOWN)
        
        self.play(FadeIn(small_brace))
        self.play(Write(small_label))
        self.wait(3)
        
        
        self.play(FadeOut(info_3))
        
        problem = VGroup(
            MathTex('180 ='),
            MathTex(r'29 \, \times'),
            Coin(5, color=GREEN),
            MathTex(r'+ 16 \, \times'),
            Coin(2, color=RED),
            MathTex(r'+ 3 \, \times'),
            Coin(1, color=BLUE)
        ).arrange().move_to(3 * DOWN).scale(0.8)
        problem_box = SurroundingRectangle(problem)
        
        self.play(FadeIn(problem, lag_ratio=0.7), run_time=2)
        self.wait(0.5)
        self.play(ShowPassingFlash(problem_box))
        self.wait(1.5)
        self.play(FadeOut(problem))
        
        ans = Tex("Answer:").move_to(2 * DOWN + 1.2 * LEFT)
        ans_a = Tex('a) Yes').move_to(2 * DOWN + 0.5 * RIGHT)
        ans_b = Tex('b) No').move_to(2.7 * DOWN + 0.5 * RIGHT)
        ans_c = Tex('c) 3').move_to(3.4 * DOWN + 0.5 * RIGHT)
        
        ans_b.shift((ans_a.width - ans_b.width) / 2 * LEFT)
        ans_c.shift((ans_a.width - ans_c.width) / 2 * LEFT)
        
        ans_group = VGroup(ans, ans_a, ans_b, ans_c).scale(0.9)
        box = SurroundingRectangle(ans_group)


        self.play(Write(ans), run_time=0.6)
        self.wait(0.2)
        self.play(Write(ans_a), run_time=0.6)
        self.wait(0.2)
        self.play(Write(ans_b), run_time=0.6)
        self.wait(0.2)
        self.play(Write(ans_c), run_time=0.6)   
        self.wait(0.6)
        self.play(ShowPassingFlash(box), run_time=2)
        

        
        
        self.wait(5)
        



if __name__ == "__main__":
    config.media_dir = 'media/USE'


    Task_3_stereometry().render()





    

    

