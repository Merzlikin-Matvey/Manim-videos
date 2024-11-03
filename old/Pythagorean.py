from ManimExtra import * 

class Title(Scene):
    def construct(self):
        title = Tex("Pythagorean theorem",font_size=120).shift(1.5*UP)
        self.add(title)
        label = Tex(r"$a^2+b^2=c^2$", font_size=120, color=YELLOW).shift(DOWN)
        self.add(label)


class Start(Scene):
    def construct(self):
        title = Tex("Pythagorean theorem",font_size=95)
        self.play(Write(title),run_time=2.5)
        self.wait()
        self.play(FadeOut(title))
        self.wait(0.5)

class Theorem(Scene):
    def construct(self):
        A = Dot(2*UP+2*LEFT)
        B = Dot(2*DOWN+3*RIGHT)
        C = Dot(2*DOWN+2*LEFT)

        A_label = Tex("A").next_to(A.get_center(),UL)
        B_label = Tex("B").next_to(B.get_center(),DR)
        C_label = Tex("C").next_to(C.get_center(),DL)
        

        AB = Line(A.get_center(), B.get_center(), color=BLUE)
        BC = Line(B.get_center(), C.get_center(), color=BLUE)
        CA = Line(C.get_center(), A.get_center(), color=BLUE)

        label = Tex("Given a right triangle ABC")
        self.play(Fancy_label(label))
        self.play(LaggedStart(
            Create(AB),
            Create(BC),
            Create(CA),
            lag_ratio=0.99, run_time=3
        ))
        self.play(GrowFromCenter(A),
                  GrowFromCenter(B),
                  GrowFromCenter(C),
                  FadeIn(A_label),
                  FadeIn(B_label),
                  FadeIn(C_label),
                  run_time=1)
        
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex(r"$\angle{C} = 90^{\circ}$")
        self.play(Fancy_label(label, 'normal'))

        C_angle = Angle().from_three_points(
            A.get_center(), C.get_center(), B.get_center(), 
            elbow=True, radius=0.25, color=YELLOW).set_z_index(-1)
        
        self.play(FadeIn(C_angle))
        self.wait(0.05)
        self.play(FadeOut(label))

        label = Tex(r"Let $AC = b,\, BC = a,\, AB = c$")
        self.play(Fancy_label(label))
        
        a_label = Tex('a').next_to(BC,DOWN)
        b_label = Tex('b').next_to(CA,LEFT)
        c_label = Tex('c').next_to((A.get_center()+B.get_center())/2,UR, buff=0.1)
        c_label.rotate(about_point=c_label.get_center(), angle=-np.arctan(4/5))
        
        self.play(FadeIn(VGroup(
            a_label, c_label, b_label,
        )))
        self.wait(0.3)

        self.play(FadeOut(label))

        label = Tex(r"Then $c^2=a^2+b^2$")
        self.play(Fancy_label(label))
        self.wait(0.3)
        self.play(FadeOut(label))

        label = Tex(r"Also, but in a different form $c = \sqrt{a^2+b^2}$")
        self.play(Fancy_label(label))

        self.play(Transform(c_label, Tex(r"$\sqrt{a^2+b^2}$").rotate(
            about_point=c_label.get_center(), angle=-np.arctan(4/5)).move_to(c_label.get_center()).shift(0.03*UR)))

        self.play(FadeOut(label))

        label = Tex("Let's prove it")
        self.play(Fancy_label(label))
        self.wait(0.2)
        self.play(FadeOut(label))
        self.play(FadeOut(c_label))
        self.wait()

class Prove_1(Scene):
    def construct(self):

        A = Dot(2*UP+2*LEFT).set_z_index(9)
        B = Dot(2*DOWN+3*RIGHT).set_z_index(9)
        C = Dot(2*DOWN+2*LEFT).set_z_index(9)

        A_label = Tex("A").next_to(A.get_center(),UL)
        B_label = Tex("B").next_to(B.get_center(),DR)
        C_label = Tex("C").next_to(C.get_center(),DL)

        AB = Line(A.get_center(), B.get_center(), color=BLUE)
        BC = Line(B.get_center(), C.get_center(), color=BLUE)
        CA = Line(C.get_center(), A.get_center(), color=BLUE)

        a_label = Tex('a').next_to(BC,DOWN)
        b_label = Tex('b').next_to(CA,LEFT)

        C_angle = Angle().from_three_points(
            A.get_center(), C.get_center(), B.get_center(), 
            elbow=True, radius=0.25, color=YELLOW).set_z_index(-1)
        

        self.add(A, B, C, 
                  A_label, B_label, C_label,
                  AB, BC, CA, C_angle,
                  a_label, b_label)
        
        altitude = Altitude(A.get_center(), C.get_center(), B.get_center(), color=RED)
        H = Dot(altitude.dot)
        H_label = Tex("H", font_size=40).next_to(H.get_center(), UR, buff=0.12)
        altitude_angles = altitude.angles(color=YELLOW, radius=0.3).set_z_index(-1)

        
        label = Tex("Let's draw the altitude from vertex C")
        self.play(Fancy_label(label))

        self.play(Create(altitude), GrowFromCenter(H))
        self.play(FadeIn(H_label))
        self.play(FadeIn(altitude_angles))
        self.play(FadeOut(label))

        label = Tex(r"Let $AH=x,\, BH=y$")
        self.play(Fancy_label(label))
        self.wait(0.6)

        x_label = Tex("x",font_size=38).next_to(
            Line(A.get_center(), H.get_center()).point_from_proportion(0.5), UR, buff=0.1)
        y_label = Tex("y",font_size=38).next_to(
            Line(B.get_center(), H.get_center()).point_from_proportion(0.5), UR, buff=0.1)
        
        self.play(FadeIn(VGroup(x_label, y_label)), run_time=0.7)
        self.play(FadeOut(label))
        self.play(x_label.animate.set_opacity(0.5), y_label.animate.set_opacity(0.5),
                  a_label.animate.set_opacity(0.5), b_label.animate.set_opacity(0.5))

        label = Tex(r"Let $\angle{A}=\alpha,\, \angle{B}=\beta$")

        A_angle = Angle().from_three_points(B.get_center(), A.get_center(), C.get_center(),radius=0.42, color=GREEN_B).set_z_index(-1)
        A_angle_label = Tex(r"$\alpha$", font_size=38).move_to(A_angle.get_center()+np.array([0.12,-0.22,0]))

        B_angle = Angle().from_three_points(A.get_center(), B.get_center(), C.get_center(),radius=0.45, color=GREEN_B).set_z_index(-1)
        B_angle_label = Tex(r"$\beta$", font_size=36).move_to(B_angle.get_center()+np.array([-0.3,0.13,0]))

        self.play(Fancy_label(label))

        self.play(FadeIn(A_angle), run_time=0.7)
        self.play(FadeIn(A_angle_label), run_time=0.7)

        self.play(FadeIn(B_angle), run_time=0.7)
        self.play(FadeIn(B_angle_label), run_time=0.7)

        self.wait(0.1)
        self.play(FadeOut(label))

        label = Tex(r"Then $\angle{HCB} = \alpha,\, \angle{HCA} = \beta$")
        self.play(Fancy_label(label))

        HCB_angle = Angle().from_three_points(H.get_center(), C.get_center(), B.get_center(), radius=0.46, color=GREEN_B).set_z_index(-1)
        HCB_angle_label = Tex(r"$\alpha$", font_size=36).move_to(HCB_angle.get_center()+np.array([0.2,0.1,0]))

        HCA_angle = Angle().from_three_points(H.get_center(), C.get_center(), A.get_center(), radius=0.40, color=GREEN_B).set_z_index(-1)
        HCA_angle_label = Tex(r"$\beta$", font_size=36).move_to(HCA_angle.get_center()+np.array([0.05,0.32,0]))

        self.play(C_angle.animate.set_stroke(opacity=0.4))
    

        self.play(FadeIn(HCB_angle), run_time=0.7)
        self.play(FadeIn(HCB_angle_label), run_time=0.7)

        self.play(FadeIn(HCA_angle), run_time=0.7)
        self.play(FadeIn(HCA_angle_label), run_time=0.7)

        self.play(FadeOut(label))

        label = Tex(r"Then triangles $ABC$ and $ACH$ are similar")
        self.play(Fancy_label(label))
        self.wait(2)
        self.play(
            A_angle.animate.set_stroke(opacity=0.3),
            A_angle_label.animate.set_opacity(0.3),
            B_angle.animate.set_stroke(opacity=0.3),
            B_angle_label.animate.set_opacity(0.3),    
            HCA_angle.animate.set_stroke(opacity=0.3),
            HCA_angle_label.animate.set_opacity(0.3),
            HCB_angle.animate.set_stroke(opacity=0.3),
            HCB_angle_label.animate.set_opacity(0.3),
            altitude_angles.animate.set_stroke(opacity=0.4)
        )
        self.play(
            a_label.animate.set_opacity(1),
            b_label.animate.set_opacity(1),
            x_label.animate.set_opacity(1),
            y_label.animate.set_opacity(1),
        )
        self.play(FadeOut(label))

        label = Tex(r"So $\dfrac{b}{x+y}=\dfrac{x}{b}$", font_size=44)
        self.play(Fancy_label(label))
        self.wait(2)
        self.play(FadeOut(label))

        label = Tex(r"Or the same $b^2=x(x+y)$")
        self.play(Fancy_label(label))
        self.wait(1)
        self.play(FadeOut(label))

        label = Tex(r"Similarly, triangles $ABC$ and $CBH$ are similar")
        self.play(Fancy_label(label))
        self.wait(3)
        self.play(FadeOut(label))

        label = Tex(r"So $a^2=y(y+x)$")
        self.play(Fancy_label(label, mode='low'))
        self.wait(1.5)
        self.play(FadeOut(label))

        label = Tex("Let's add these 2 equalities")
        self.play(Fancy_label(label))
        self.wait(0.1)
        self.play(FadeOut(label))

        label = Tex(r"$a^2+b^2=x(x+y)+y(x+y)$")
        self.play(Fancy_label(label,mode='vlow'))
        self.wait()
        new_label = Tex(r"$a^2+b^2=x^2+2xy+y^2$").to_edge(UP)
        self.play(Transform(label,new_label))
        self.wait()
        new_label = Tex(r"$a^2+b^2=(x+y)^2$").to_edge(UP)
        self.play(Transform(label,new_label))
        self.wait(0.2)

        c_label = Tex('c').next_to((A.get_center()+B.get_center())/2, UR, buff=0.1)
    
        self.play(LaggedStart(
            AnimationGroup(
                x_label.animate.move_to(c_label.get_center()),
                y_label.animate.move_to(c_label.get_center())
            ),
            AnimationGroup(
                Transform(x_label,c_label),
                Transform(y_label,c_label)
            ),
            lag_ratio=0.9, run_time=1.5
        ))
        self.wait(0.5)

        new_label = Tex(r"$a^2+b^2=c^2$").to_edge(UP)
        self.play(Transform(label,new_label))

        box = SurroundingRectangle(label, stroke_width=1)
        self.play(Create(box))
        self.wait(2.5)

        self.play(FadeOut(VGroup(label, box)))
        label = Tex("Let's prove the theorem in one more way")
        self.play(Fancy_label(label))
        self.wait(0.1)
        self.play(LaggedStart(
            FadeOut(VGroup(
                A_angle, B_angle,
                A_angle_label, B_angle_label,
                HCB_angle, HCA_angle,
                HCB_angle_label, HCA_angle_label,
                A, B, C, A_label, B_label, C_label,
                a_label, b_label, c_label, x_label, y_label
            )),
            FadeOut(H_label),
            FadeOut(H),
            FadeOut(altitude_angles),
            Uncreate(altitude),
            C_angle.animate.set_stroke(opacity=1), 
            lag_ratio=0.7, run_time=2.5
        ))
        self.play(FadeOut(label))

        self.wait(0.2)

class Prove_2(Scene):
    def construct(self):
        

        A = Dot(2*UP+2*LEFT).set_z_index(9).set_opacity(0)
        B = Dot(2*DOWN+3*RIGHT).set_z_index(9).set_opacity(0)
        C = Dot(2*DOWN+2*LEFT).set_z_index(9).set_opacity(0)

        A_label = Tex("A").next_to(A.get_center(),UL)
        B_label = Tex("B").next_to(B.get_center(),DR)
        C_label = Tex("C").next_to(C.get_center(),DL)

        AB = Line(A.get_center(), B.get_center(), color=BLUE)
        BC = Line(B.get_center(), C.get_center(), color=BLUE)
        CA = Line(C.get_center(), A.get_center(), color=BLUE)


        C_angle = Angle().from_three_points(
            A.get_center(), C.get_center(), B.get_center(), 
            elbow=True, radius=0.25, color=YELLOW).set_z_index(-1)
        

        self.add(AB, BC, CA, A, B, C, C_angle)
        label = Tex("Let's assemble a square of triangles")
        self.play(Fancy_label(label))
        
        triangle_1 = VGroup(AB, BC, CA, C, A, B, C_angle,)
        self.play(triangle_1.animate.scale(0.5).shift(1.5*DOWN).shift(1.5*LEFT))
        triangle_2 = triangle_1.copy()
        triangle_3 = triangle_1.copy()
        triangle_4 = triangle_1.copy()

        self.play(LaggedStart(
            triangle_2.animate.rotate(about_point=triangle_2.get_center(),angle=PI/2).shift(2.25*RIGHT+0.25*UP),
            triangle_3.animate.rotate(about_point=triangle_3.get_center(),angle=PI).shift(2.5*UP+2*RIGHT),
            triangle_4.animate.rotate(about_point=triangle_3.get_center(),angle=-PI/2).shift(2.25*UP+0.25*LEFT),
            lag_ratio=0.9, run_time=3
        ))

        a_1_label = Tex("a", font_size=30).next_to(triangle_1[1],DOWN)
        a_2_label = Tex("a", font_size=30).next_to(triangle_2[1],RIGHT)
        a_3_label = Tex("a", font_size=30).next_to(triangle_3[1],UP)
        a_4_label = Tex("a", font_size=30).next_to(triangle_4[1],LEFT)

        b_1_label = Tex("b", font_size=30).next_to(triangle_1[2],LEFT)
        b_2_label = Tex("b", font_size=30).next_to(triangle_2[2],DOWN)
        b_3_label = Tex("b", font_size=30).next_to(triangle_3[2],RIGHT)
        b_4_label = Tex("b", font_size=30).next_to(triangle_4[2],UP)

        c_1_label = Tex("c", font_size=30).next_to(triangle_1[0].get_center(),UR, buff=0.1)
        c_2_label = Tex("c", font_size=30).next_to(triangle_2[0].get_center(),UL, buff=0.1)
        c_3_label = Tex("c", font_size=30).next_to(triangle_3[0].get_center(),DL, buff=0.1)
        c_4_label = Tex("c", font_size=30).next_to(triangle_4[0].get_center(),DR, buff=0.1)

        self.play(LaggedStart(
            FadeIn(a_1_label),
            FadeIn(b_2_label),
            FadeIn(a_2_label),
            FadeIn(b_3_label),
            FadeIn(a_3_label),
            FadeIn(b_4_label),
            FadeIn(a_4_label),
            FadeIn(b_1_label),
            lag_ratio=0.4, run_time=3
        ))
        self.play(FadeIn(VGroup(c_1_label, c_2_label, c_3_label, c_4_label,)))

        square = Polygon(
            triangle_1[3].get_center(),
            triangle_2[3].get_center(),
            triangle_3[3].get_center(),
            triangle_4[3].get_center(),
        ).set_stroke(opacity=0).set_opacity(0.3)
        
        self.play(FadeOut(label))
        label = Tex(r"Then the area of the larger square is $(a+b)^2$")
        self.wait(0.15)
        self.play(Fancy_label(label))
        self.play(FadeIn(square))
        self.play(FadeOut(label))
        
        label = Tex(r"And the area of the smaller square is $c^2$")
        self.play(Fancy_label(label))

        square_new = Polygon(
            triangle_1[4].get_center(), triangle_1[5].get_center(), 
            triangle_3[4].get_center(), triangle_3[5].get_center(), 
        ).set_stroke(opacity=0).set_opacity(0.3)
        
        self.play(Transform(square, square_new))
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex(r"Let's express this area in terms of the area of a large square", font_size=44)
        self.play(Fancy_label(label))
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex(r"To do this, we subtract the areas of the triangles")

        triangle_1_extra = Polygon(
            triangle_1[3].get_center(), triangle_1[4].get_center(), triangle_1[5].get_center(),
            color=RED).set_opacity(0.3).set_stroke(opacity=0)
        
        triangle_2_extra = Polygon(
            triangle_2[3].get_center(), triangle_2[4].get_center(), triangle_2[5].get_center(),
            color=RED).set_opacity(0.3).set_stroke(opacity=0)
        
        triangle_3_extra = Polygon(
            triangle_3[3].get_center(), triangle_3[4].get_center(), triangle_3[5].get_center(),
            color=RED).set_opacity(0.3).set_stroke(opacity=0)
        
        triangle_4_extra = Polygon(
            triangle_4[3].get_center(), triangle_4[4].get_center(), triangle_4[5].get_center(),
            color=RED).set_opacity(0.3).set_stroke(opacity=0)

        self.play(Fancy_label(label))

        self.play(LaggedStart(
            FadeIn(triangle_1_extra),
            FadeIn(triangle_2_extra),
            FadeIn(triangle_3_extra),
            FadeIn(triangle_4_extra),
            lag_ratio=0.8, run_time=3
        ))

        self.wait(0.1)
        self.play(FadeOut(label))

        label = Tex(r"$c^2=(a+b)^2-4\dfrac{ab}{2}$")
        self.play(Fancy_label(label, mode='vlow'))
        self.wait(0.7)

        new_label = Tex(r"$c^2=(a+b)^2-2ab$").to_edge(UP)
        self.play(Transform(label, new_label))
        self.wait()

        new_label = Tex(r"$c^2=a^2+b^2+2ab-2ab$").to_edge(UP)
        self.play(Transform(label, new_label))
        self.wait()

        new_label = Tex(r"$c^2=a^2+b^2$").to_edge(UP)
        self.play(Transform(label, new_label))

        box = SurroundingRectangle(label, stroke_width=1)
        self.play(Create(box))
        self.wait()
        self.play(FadeOut(VGroup(
            triangle_1, triangle_2, triangle_3, triangle_4,
            triangle_1_extra, triangle_2_extra, triangle_3_extra, triangle_4_extra,
            a_1_label, a_2_label, a_3_label, a_4_label,
            b_1_label, b_2_label, b_3_label, b_4_label,
            c_1_label, c_2_label, c_3_label, c_4_label,
            square,label,box
        )))

class Triples(Scene):
    def construct(self):

        label = Tex(r"There are many right-angled triangles with integer side lengths", font_size=42)
        self.play(Fancy_label(label))
        
        A = Dot(2*DOWN+2*LEFT).set_opacity(0)
        B = Dot(1*UP+2*LEFT).set_opacity(0)
        C = Dot(2*DOWN+2*RIGHT).set_opacity(0)

        a = Line(B.get_center(), C.get_center(), color=BLUE)
        b = Line(C.get_center(), A.get_center(), color=BLUE)
        c = Line(A.get_center(), B.get_center(), color=BLUE)

        self.play(Create(a), run_time=0.5)
        self.play(Create(b), run_time=0.5)
        self.play(Create(c), run_time=0.5)

        a_label = Tex(r'$5$', font_size=52).next_to(a.get_center(),UR)
        b_label = Tex(r'$4$', font_size=52).next_to(b.get_center(),DOWN)
        c_label = Tex(r'$3$', font_size=52).next_to(c.get_center(),LEFT)

        self.play(FadeIn(VGroup(a_label, b_label, c_label)))

        info_1 = Tex(r'$(3,4,5)$', font_size=35).move_to(6*RIGHT+UP).set_opacity(0.4)
        self.play(FadeIn(info_1))

        v = VGroup(A, B, C, a, b, c, a_label, b_label, c_label)

        A_new = Dot(2*DOWN+3.5*LEFT).set_opacity(0)
        B_new = Dot(1*UP+3.5*LEFT).set_opacity(0)
        C_new = Dot(2*DOWN+3*RIGHT).set_opacity(0)

        a_new = Line(B_new.get_center(), C_new.get_center(), color=BLUE)
        b_new = Line(C_new.get_center(), A_new.get_center(), color=BLUE)
        c_new = Line(A_new.get_center(), B_new.get_center(), color=BLUE)

        a_label_new = Tex(r'$13$', font_size=52).next_to(a_new.get_center(),UR).set_z_index(-1)
        b_label_new = Tex(r'$12$', font_size=52).next_to(b_new.get_center(),DOWN).set_z_index(-1)
        c_label_new = Tex(r'$5$', font_size=52).next_to(c_new.get_center(),LEFT).set_z_index(-1)

        v_new = VGroup(A_new.set_z_index(1), B_new.set_z_index(1), C_new.set_z_index(1), 
                       a_new, b_new, c_new,
                       a_label_new, b_label_new, c_label_new)

        self.play(Transform(v, v_new))

        info_2 = Tex(r'$(5,12,13)$', font_size=35).move_to(6*RIGHT+0.6*UP).set_opacity(0.4)
        self.play(FadeIn(info_2))

        A_new = Dot(2*DOWN+3*LEFT).set_opacity(0)
        B_new = Dot(1.3*UP+3*LEFT).set_opacity(0)
        C_new = Dot(2*DOWN+3*RIGHT).set_opacity(0)

        a_new = Line(B_new.get_center(), C_new.get_center(), color=BLUE)
        b_new = Line(C_new.get_center(), A_new.get_center(), color=BLUE)
        c_new = Line(A_new.get_center(), B_new.get_center(), color=BLUE)

        a_label_new = Tex(r'$17$', font_size=52).next_to(a_new.get_center(),UR).set_z_index(-1)
        b_label_new = Tex(r'$15$', font_size=52).next_to(b_new.get_center(),DOWN).set_z_index(-1)
        c_label_new = Tex(r'$8$', font_size=52).next_to(c_new.get_center(),LEFT).set_z_index(-1)

        v_new = VGroup(A_new.set_z_index(1), B_new.set_z_index(1), C_new.set_z_index(1), 
                       a_new, b_new, c_new,
                       a_label_new, b_label_new, c_label_new)

        self.play(Transform(v, v_new))

        info_3 = Tex(r'$(8,15,17)$', font_size=35).move_to(6*RIGHT+0.2*UP).set_opacity(0.4)
        self.play(FadeIn(info_3))

        A_new = Dot(1.7*DOWN+3.5*LEFT).set_opacity(0)
        B_new = Dot(1*UP+3.5*LEFT).set_opacity(0)
        C_new = Dot(1.7*DOWN+4*RIGHT).set_opacity(0)

        a_new = Line(B_new.get_center(), C_new.get_center(), color=BLUE)
        b_new = Line(C_new.get_center(), A_new.get_center(), color=BLUE)
        c_new = Line(A_new.get_center(), B_new.get_center(), color=BLUE)

        a_label_new = Tex(r'$25$', font_size=52).next_to(a_new.get_center(),UR).set_z_index(-1)
        b_label_new = Tex(r'$24$', font_size=52).next_to(b_new.get_center(),DOWN).set_z_index(-1)
        c_label_new = Tex(r'$7$', font_size=52).next_to(c_new.get_center(),LEFT).set_z_index(-1)

        v_new = VGroup(A_new.set_z_index(1), B_new.set_z_index(1), C_new.set_z_index(1), 
                       a_new, b_new, c_new,
                       a_label_new, b_label_new, c_label_new)

        self.play(Transform(v, v_new))

        info_4 = Tex(r'$(7,24,25)$', font_size=35).move_to(6*RIGHT-0.2*UP).set_opacity(0.4)
        self.play(FadeIn(info_4))

        self.wait(0.2)
        self.play(FadeOut(v), FadeOut(label))
        info = VGroup(info_1, info_2, info_3, info_4)
        self.play(info.animate.scale(1.7).move_to(1.5*DOWN).set_opacity(0.65))

        label = Tex("The lengths of their sides are called Pythagorean triples")
        self.play(Fancy_label(label))

        info_0 = Tex(r"$3^2+4^2=5^2$", color=YELLOW).move_to(info_1.get_center()+1.5*UP)
        self.play(Write(info_0))
        self.wait(0.2)

        info_0_new = Tex(r"$5^2+12^2=13^2$", color=YELLOW).move_to(info_1.get_center()+1.5*UP)
        self.play(Transform(info_0, info_0_new))
        self.wait(0.2)

        info_0_new = Tex(r"$8^2+15^2=17^2$", color=YELLOW).move_to(info_1.get_center()+1.5*UP)
        self.play(Transform(info_0, info_0_new))
        self.wait(0.2)

        info_0_new = Tex(r"$7^2+24^2=25^2$", color=YELLOW).move_to(info_1.get_center()+1.5*UP)
        self.play(Transform(info_0, info_0_new))
        self.wait(0.2)

        self.play(FadeOut(label))
        self.play(FadeOut(info), FadeOut(info_0))

        label = Tex("You can get as many of these triples as you want")
        self.play(Fancy_label(label))
        self.wait(0.5)
        self.play(FadeOut(label))

        label = Tex("To obtain them, there is a formula")
        self.play(Fancy_label(label))
        
        label_1 = Tex(r"$\forall m,n \in \mathbb{Z}$", font_size=30).move_to(2.5*UP).set_opacity(0.5)
        self.play(FadeIn(label_1))

        label_2 = Tex(r"$a=2nm$", color=YELLOW).move_to(1.8*UP)
        label_3 = Tex(r"$b=n^2-m^2$", color=YELLOW).move_to(1.2*UP)
        label_4 = Tex(r"$c=n^2+m^2$", color=YELLOW).move_to(0.6*UP)

        self.play(LaggedStart(
            Write(label_2),
            Write(label_3),
            Write(label_4),
            lag_ratio=0.9, run_time=5
        ))

        label_5 = Tex(r"$(a,b,c)$ - Pythagorean triple", color=WHITE).move_to(0.6*DOWN)
        self.play(Write(label_5), run_time=3)

        box = SurroundingRectangle(VGroup(label_2, label_3, label_4), stroke_width=1, color=YELLOW)
        self.play(Create(box))
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex(r"It's easy to prove")
        self.play(Fancy_label(label))
        self.play(LaggedStart(
            FadeOut(label_1),
            FadeOut(label_5),
            VGroup(label_2,label_3,label_4, box).animate.shift(0.7*UP),
            lag_ratio=0.6, run_time=1.5
        ))

        label_x = Tex("$a^2+b^2=(2nm)^2 + (n^2 - m^2)^2 = 4n^2m^2 + n^4 - 2n^2m^2 + m^4 =" + '\n ' + " n^4 + 2n^2m^2 + m^4 = (n^2+m^2)^2 = c^2$", font_size=42)
        self.play(Write(label_x), run_time=15)
        label_new = Tex(r"$a^2+b^2=c^2$", font_size=52)
        self.wait(3)
        self.play(Transform(label_x, label_new))

        all = VGroup(label,label_x,label_2,label_3,label_4,box)
        self.wait(2)
        self.play(FadeOut(all))
        self.wait(8)
        
        
        



    
        

        

        
        

