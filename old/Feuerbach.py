from ManimExtra import *
#ManimExtra v0.1

config.max_files_cached = 4096


class Title(Scene):
    def construct(self):
        black_rectangle = Rectangle(height=1.6,width=20).shift(3.5*UP).set_color(BLACK).set_opacity(1).set_z_index(101)
        self.add(black_rectangle)

        label = Tex("Feuerbach's theorem", font_size=70).to_edge(UP).shift(0.1*DOWN).set_z_index(9999)

        A = 2*LEFT + 2*DOWN 
        B = 1.4*LEFT + 1.5*UP
        C = 2*RIGHT + 2*DOWN 

        a = Line(B, C, color=BLUE)
        b = Line(A, C, color=BLUE)
        c = Line(A, B, color=BLUE)

        line_a = a.copy().set_length(20).set_opacity(0.5)
        line_b = b.copy().set_length(20).set_opacity(0.5)
        line_c = c.copy().set_length(20).set_opacity(0.5)
        

        self.add(label, a, b, c)

        euler_circle = EulerCircle(A, B, C, color=RED, stroke_width=3.2).set_z_index(99)
        incircle = InscribedCircle(A, B, C, color=GREEN, stroke_width=2.8)
        excircle_A = EscribedCircle(B, A, C, color=GREEN, stroke_width=2.8)
        excircle_B = EscribedCircle(A, B, C, color=GREEN, stroke_width=2.8)
        excircle_C = EscribedCircle(A, C, B, color=GREEN, stroke_width=2.8)

        self.add(euler_circle, incircle, excircle_A, excircle_B, excircle_C)
        self.add(line_a, line_b, line_c)




class Pre_start(Scene):
    def construct(self):
        title = Tex("Feuerbach's theorem", font_size=90).move_to(0.4*UP)
        sub = Tex("PDF version in the description").set_opacity(0.6).move_to(0.5*DOWN)
        self.play(Write(title), run_time=2.5)
        self.play(Write(sub), run_time=1.8)
        self.wait(0.5)
        self.play(FadeOut(title), FadeOut(sub))
        self.wait(0.5)


class Start(Scene):
    def construct(self):
        black_rectangle = Rectangle(height=1.2,width=20).shift(3.5*UP).set_color(BLACK).set_opacity(1).set_z_index(101)
        self.add(black_rectangle)

        label = Tex("An arbitrary triangle is given")
        self.play(Fancy_label(label))

        A = Dot(2.5*DOWN+4*LEFT, radius=0.1).set_z_index(1)
        B = Dot(2.6*UP+3.2*LEFT, radius=0.1).set_z_index(1)
        C = Dot(2.5*DOWN+3.4*RIGHT, radius=0.1).set_z_index(1)

        a = Line(B.get_center(), C.get_center(), color=BLUE).set_z_index(-1)
        b = Line(C.get_center(), A.get_center(), color=BLUE).set_z_index(-1)
        c = Line(A.get_center(), B.get_center(), color=BLUE).set_z_index(-1)

        self.play(FadeIn(VGroup(A, B, C)))
        self.play(Create(a), run_time=2/3)
        self.play(Create(b), run_time=2/3)
        self.play(Create(c), run_time=2/3)
        self.play(FadeOut(label), run_time=0.75)

        euler_circle = EulerCircle(A.get_center(), B.get_center(), C.get_center(), color=YELLOW)
        label = Tex("Let's construct the Euler's circle")
        self.play(Fancy_label(label))
        self.play(Create(euler_circle))
        self.wait(0.4)
        self.play(FadeOut(label))

        label = Tex("And now let's build an inscribed circle")
        inscribed_circle = InscribedCircle(A.get_center(), B.get_center(), C.get_center(), color=GREEN)

        self.play(Fancy_label(label))
        self.play(Create(inscribed_circle))
        self.wait(0.4)
        self.play(FadeOut(label))
        self.play(inscribed_circle.animate.set_stroke(opacity=0.45))

        label = Tex("Then we construct escribed circles").set_z_index(1)
        self.play(Fancy_label(label))
        self.play(VGroup(A, B, C, a, b, c, euler_circle, inscribed_circle).animate.scale(about_point=DOWN, scale_factor=0.5), run_time=1.5)
        escribed_circles = VGroup(
            EscribedCircle(A.get_center(), B.get_center(), C.get_center()).set_stroke(opacity=0.45),
            EscribedCircle(B.get_center(), A.get_center(), C.get_center()).set_stroke(opacity=0.45),
            EscribedCircle(A.get_center(), C.get_center(), B.get_center()).set_stroke(opacity=0.45)) 
        
        line_a = a.copy().set_length(30).set_opacity(0.3)
        line_b = b.copy().set_length(30).set_opacity(0.3)
        line_c = c.copy().set_length(30).set_opacity(0.3)

        self.play(FadeIn(VGroup(line_a, line_b, line_c)))
        
        for i in range(3):
            self.wait(0.25)
            self.play(Create(escribed_circles[i]))

        self.play(FadeOut(label))
        label = Tex("We get that 4 circles touch the Euler's circle")
        self.play(Fancy_label(label))

        F = Dot(intersection_circles(
            Circle(arc_center=euler_circle.get_center(), radius=euler_circle.radius/2), 
            Circle(arc_center=inscribed_circle.get_center(), radius=inscribed_circle.radius/2))[0],
            radius=0.05)
        F_1 = Dot(intersection_circles(
            Circle(arc_center=euler_circle.get_center(), radius=euler_circle.radius/2), 
            Circle(arc_center=escribed_circles[0].get_center(), radius=escribed_circles[0].radius))[0],
            radius=0.05)
        F_2 = Dot(intersection_circles(
            Circle(arc_center=euler_circle.get_center(), radius=euler_circle.radius/2), 
            Circle(arc_center=escribed_circles[1].get_center(), radius=escribed_circles[1].radius))[0],
            radius=0.05)
        F_3= Dot(intersection_circles(
            Circle(arc_center=euler_circle.get_center(), radius=euler_circle.radius/2), 
            Circle(arc_center=escribed_circles[2].get_center(), radius=escribed_circles[2].radius))[0],
            radius=0.05)


        self.play(FadeIn(VGroup(F, F_1, F_2, F_3)))

        self.wait(0.3)
        self.play(FadeOut(label))

        label = Tex("Now let's prove it!")
        self.wait(0.05)
        self.play(Fancy_label(label))
        self.wait(0.5)
        ALL = VGroup(A, B, C, a, b, c,
                     inscribed_circle, euler_circle, escribed_circles,
                     F, F_1, F_2, F_3, 
                     line_a, line_b, line_c, label)
        self.play(FadeOut(ALL))


        label = Tex("But we will need some auxiliary facts to prove it")
        self.play(Fancy_label(label))
        self.wait(0.3)
        self.play(FadeOut(label))

    
class Miquel(Scene):
    def construct(self):
        black_rectangle = Rectangle(height=1.2,width=20).shift(3.5*UP).set_color(BLACK).set_opacity(1).set_z_index(101)
        self.add(black_rectangle)

        circle = Circle(radius=2,color=BLUE_D).move_to(0.35*DOWN)
            
        A = Dot(circle.point_at_angle(0.25*PI)).set_z_index(1)
        B = Dot(circle.point_at_angle((4/6)*PI)).set_z_index(1)
        C = Dot(circle.point_at_angle(-(8/11)*PI)).set_z_index(1)
        D = Dot(circle.point_at_angle(-(1/3)*PI)).set_z_index(1)

        A_label = Tex('A',font_size=35).next_to(A.get_center(),UR,buff=0.17).set_z_index(99)
        B_label = Tex('B',font_size=35).next_to(B.get_center(),UL,buff=0.17).set_z_index(99)
        C_label = Tex('C',font_size=35).next_to(C.get_center(),DL,buff=0.17).set_z_index(99)
        D_label = Tex('D',font_size=35).next_to(D.get_center(),DR,buff=0.17).set_z_index(99)

        label = Tex("Given a circle and 4 points on it")
        self.play(Fancy_label(label))
        self.play(Create(circle))
        self.play(LaggedStart(
            FadeIn(VGroup(A, A_label)),
            FadeIn(VGroup(B, B_label)),
            FadeIn(VGroup(C, C_label)),
            FadeIn(VGroup(D, D_label)),
            run_time=1.7, lag_ratio=0.8
        ))
        self.wait(0.2)
        self.play(FadeOut(label))

        circle_AB = Circle().from_three_points(
            A.get_center(), B.get_center(), 2.3*UP+0.6*LEFT, color=YELLOW).set_stroke(opacity=0.35).set_z_index(-1)
        circle_BC = Circle().from_three_points(
            B.get_center(), C.get_center(), 3.8*LEFT+0.5*DOWN, color=YELLOW).set_stroke(opacity=0.35).set_z_index(-1)
        circle_CD = Circle().from_three_points(
            C.get_center(), D.get_center(), 3*DOWN+0.4*RIGHT, color=YELLOW).set_stroke(opacity=0.35).set_z_index(-1)
        circle_DA = Circle().from_three_points(
            D.get_center(), A.get_center(), 4*RIGHT+0.2*UP, color=YELLOW).set_stroke(opacity=0.35).set_z_index(-1)
        
        label = Tex("Let's construct 4 circles passing through these points")
        self.play(Fancy_label(label))

        self.play(Create(circle_AB))
        self.play(Create(circle_BC))
        self.play(Create(circle_CD))
        self.play(Create(circle_DA))

        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex("Let's denote their intersection points")
        self.play(Fancy_label(label))

        A_1 = Dot(intersection_circles(circle_AB, circle_DA)[1]).set_z_index(1)
        B_1 = Dot(intersection_circles(circle_BC, circle_AB)[1]).set_z_index(1)
        C_1 = Dot(intersection_circles(circle_CD, circle_BC)[1]).set_z_index(1)
        D_1 = Dot(intersection_circles(circle_DA, circle_CD)[1]).set_z_index(1)

        A_1_label = Tex(r"$\mathrm{A_1}$",font_size=28).next_to(A_1.get_center(),direction=UR,buff=0.13).set_z_index(9)
        B_1_label = Tex(r"$\mathrm{B_1}$",font_size=28).next_to(B_1.get_center(),direction=UL,buff=0.13).set_z_index(9)
        C_1_label = Tex(r"$\mathrm{C_1}$",font_size=28).next_to(C_1.get_center(),direction=(2*LEFT+0.7*DOWN),buff=0.08).set_z_index(9)
        D_1_label = Tex(r"$\mathrm{D_1}$",font_size=28).next_to(D_1.get_center(),direction=(2*RIGHT+0.7*DOWN),buff=0.08).set_z_index(9)

        self.play(LaggedStart(
            FadeIn(A_1, A_1_label),
            FadeIn(B_1, B_1_label),
            FadeIn(C_1, C_1_label),
            FadeIn(D_1, D_1_label),
            run_time=2.5, lag_ratio=0.7
        ))

        self.play(VGroup(A_label, B_label, C_label, D_label).animate.set_opacity(0.9))

        self.play(FadeOut(label))

        label = Tex("And these 4 points are on the same circle")
        self.play(Fancy_label(label))
        result_circle = Circle().from_three_points(A_1.get_center(), B_1.get_center(), C_1.get_center(), color=RED)
        self.play(VGroup(A_1_label, B_1_label, C_1_label, D_1_label).animate.set_opacity(0.9))
        self.play(Create(result_circle))
        self.play(FadeOut(label))

        label = Tex("This fact is called Miquel's theorem")
        self.play(Fancy_label(label))
        self.wait(0.1)
        self.play(FadeOut(label))

        label = Tex("This is easy to prove, you just need to consider the angles")
        self.play(Fancy_label(label))
        self.wait(0.3)
        self.play(FadeOut(label))
        label = Tex("Quadrilateral $D_1A_1AD$ inscribed")
        self.play(Fancy_label(label))
        self.play(Uncreate(result_circle), circle.animate.set_stroke(opacity=0.75))
        self.wait()
        self.play(FadeOut(label))

        label = Tex(r"If we denote  $\angle{D_1DA}$ as $\alpha$, then $\angle{D_1A_1A}=180^{\circ}-\alpha$")
        self.play(Fancy_label(label))

        DD_1 = Line(D.get_center(),D_1.get_center(),color=GREEN_C)
        DA = Line(D.get_center(),A.get_center(),color=GREEN_C)
        angle_D_1DA = Angle().from_three_points(D_1.get_center(), D.get_center(), A.get_center(), radius=0.2)
        angle_D_1DA_label = MathTex(r"\alpha",font_size=31).move_to(D.get_center()+np.array([-0.08,0.4,0]))

        self.play(LaggedStart(
            Create(DD_1),
            Create(DA),
            Create(angle_D_1DA),
            FadeIn(angle_D_1DA_label),
            lag_ratio=0.7,
            run_time=5
        ))
        self.wait(0.8)

        self.play(FadeOut(DD_1, DA, angle_D_1DA, angle_D_1DA_label), run_time=0.5)

        D_1A_1 = Line(D_1.get_center(),A_1.get_center(),color=GREEN_C)
        A_1A = Line(A_1.get_center(),A.get_center(),color=GREEN_C)
        angle_D_1A_1A = Angle().from_three_points(D_1.get_center(), A_1.get_center(), A.get_center(), radius=0.2)
        angle_D_1A_1A_label = Tex(r"$\mathrm{180^{\circ}-\alpha}$",font_size=25).move_to(A_1.get_center()+np.array([0.55,-0.3,0]))

        self.play(LaggedStart(
            Create(D_1A_1),
            Create(A_1A),
            Create(angle_D_1A_1A),
            FadeIn(angle_D_1A_1A_label),
            lag_ratio=0.7,
            run_time=5
        ))

        self.play(VGroup(D_1A_1, A_1A, angle_D_1A_1A_label).animate.set_opacity(0.5),
                  angle_D_1A_1A.animate.set_stroke(opacity=0.4), run_time=0.6)
        
        self.play(FadeOut(label))

        label = Tex(r"Similarly, if we denote $\angle{B_1BA}$ as $\beta$, then $\angle{B_1A_1A}=180^{\circ}-\beta$", font_size=44)
        self.play(Fancy_label(label))

        BA = Line(B.get_center(), A.get_center(), color=GREEN)
        BB_1 = Line(B.get_center(), B_1.get_center(), color=GREEN)
        angle_B_1BA = Angle().from_three_points(B_1.get_center(), B.get_center(), A.get_center(), radius=0.2)
        angle_B_1BA_label = Tex(r"$\mathrm{\beta}$",font_size=31).move_to(B.get_center()+np.array([0.4,-0.27,0]))

        self.play(LaggedStart(
            Create(BA), 
            Create(BB_1),
            Create(angle_B_1BA),
            FadeIn(angle_B_1BA_label),
            run_time=5, lag_ratio=0.8
        ))
        self.wait(0.4)

        self.play(FadeOut(BA, BB_1, angle_B_1BA_label, angle_B_1BA))

        B_1A_1 = Line(B_1.get_center(), A_1.get_center(), color=GREEN)
        angle_B_1A_1A = Angle().from_three_points(B_1.get_center(), A_1.get_center(), A.get_center(), radius=0.2)
        angle_B_1A_1A_label = Tex(r"$\mathrm{180^{\circ}-\beta}$",font_size=25).move_to(
            A_1.get_center()+np.array([-0.32,0.43,0])).set_z_index(-1)

        self.play(LaggedStart(
            Create(B_1A_1),
            A_1A.animate.set_opacity(1),
            Create(angle_B_1A_1A),
            run_time=2.2, lag_ratio=0.8
        ))
        self.wait(0.01)
        self.play(FadeIn(angle_B_1A_1A_label))
        self.wait(0.01)
        self.wait(0.3)
        self.play(angle_D_1A_1A_label.animate.set_opacity(1), 
                  angle_D_1A_1A.animate.set_stroke(opacity=1),
                  D_1A_1.animate.set_opacity(1))
        
        self.play(FadeOut(label))

        label = Tex(r"Therefore $\angle{B_1A_1D_1} = \alpha + \beta$")
        self.play(Fancy_label(label))

        angle_B_1A_1D_1 = Angle().from_three_points(
            B_1.get_center(), A_1.get_center(), D_1.get_center(), radius=0.2)
        angle_B_1A_1D_1_label = Tex(r"$\mathrm{\alpha + \beta}$",font_size=24).move_to(
            A_1.get_center()+np.array([-0.4,-0.3,0]))
        
        self.play(Create(angle_B_1A_1D_1), FadeIn(angle_B_1A_1D_1_label))
        self.play(FadeOut(VGroup(A_1A, angle_B_1A_1A, angle_B_1A_1A_label, angle_D_1A_1A, angle_D_1A_1A_label)))
        self.play(FadeOut(label))

        label = Tex("Let's do the same, but for another angles")
        self.play(Fancy_label(label))

        BC = Line(B.get_center(), C.get_center(), color=GREEN).set_opacity(0.8)
        BB_1 = Line(B.get_center(), B_1.get_center(), color=GREEN).set_opacity(0.8)
        angle_CBB_1 = Angle().from_three_points(C.get_center(), B.get_center(), B_1.get_center(), 
                                                radius=0.2).set_stroke(opacity=0.8)
        angle_CBB_1_label = Tex(r"$\mathrm{\gamma}$",font_size=31).move_to(
            B.get_center()+np.array([0.1,-0.41,0])).set_opacity(0.8)

        self.play(LaggedStart(
            Create(BC),
            Create(BB_1),
            Create(angle_CBB_1),
            FadeIn(angle_CBB_1_label),
            lag_ratio=0.7,
            run_time=5
        ))

        CD = Line(C.get_center(), D.get_center(), color=GREEN).set_opacity(0.8)
        DD_1 = Line(D.get_center(), D_1.get_center(), color=GREEN).set_opacity(0.8)
        angle_CDD_1 = Angle().from_three_points(C.get_center(), D.get_center(), D_1.get_center(), 
                                                radius=0.2).set_stroke(opacity=0.8)
        angle_CDD_1_label = Tex(r"$\mathrm{\delta}$",font_size=31).move_to(
            D.get_center()+np.array([-0.3,0.25,0])).set_opacity(0.8)

        self.play(LaggedStart(
            Create(CD),
            Create(DD_1),
            Create(angle_CDD_1),
            FadeIn(angle_CDD_1_label),
            lag_ratio=0.7,
            run_time=5
        ))

        C_1B_1 = Line(C_1.get_center(), B_1.get_center(), color=GREEN)
        C_1D_1 = Line(C_1.get_center(), D_1.get_center(), color=GREEN)

        angle_B_1C_1D_1 = Angle().from_three_points(B_1.get_center(), C_1.get_center(), D_1.get_center(), radius=0.2)
        angle_B_1C_1D_1_label = Tex(r"$\mathrm{\gamma+\delta}$",font_size=24).move_to(C_1.get_center()+np.array([0.4,0.3,0]))

        self.play(LaggedStart(
            Create(C_1B_1),
            Create(C_1D_1),
            Create(angle_B_1C_1D_1),
            FadeIn(angle_B_1C_1D_1_label),
            run_time=4, 
            lag_ratio=0.8
        ))

        self.play(FadeOut(VGroup(BB_1, DD_1, 
                                 angle_CDD_1, angle_CDD_1_label,
                                 angle_CBB_1, angle_CBB_1_label)),
                Create(VGroup(BA, DA)))

        
        angle_ADC = Angle().from_three_points(A.get_center(), D.get_center(), C.get_center(), radius=0.2)
        angle_ADC_label = Tex(r"$\mathrm{\alpha+\delta}$", font_size=28).next_to(
            D.get_center(), direction=np.array([-0.2,0.8,0]), buff=0.3)

        angle_CBA = Angle().from_three_points(C.get_center(), B.get_center(), A.get_center(), radius=0.2)
        angle_CBA_label = Tex(r"$\mathrm{\beta+\gamma}$", font_size=28).next_to(
            B.get_center(), direction=np.array([0.1,-0.7,0]), buff=0.3)

        self.play(Create(angle_ADC), FadeIn(angle_ADC_label))
        self.play(Create(angle_CBA), FadeIn(angle_CBA_label))

        self.play(FadeOut(label))

        label = Tex(r"So $\angle{CDA}+\angle{CBA}=\alpha+\beta+\gamma+\delta=\angle{B_1C_1D_1}+\angle{B_1A_1D_1}=180^{\circ}$", font_size=40)
        self.play(Fancy_label(label))    
        self.wait(2)
        self.play(FadeOut(label))

        label = Tex(r"Therefore, points $A_1, B_1, C_1, D_1$ are on the same circle") 
        self.play(Fancy_label(label))
        new_result_circle = Circle().from_three_points(
            A_1.get_center(), B_1.get_center(), C_1.get_center(), color=RED)
        self.play(FadeIn(new_result_circle))
        self.play(FadeOut(VGroup(
            BA, CD, DA, BC, 
            angle_ADC, angle_ADC_label, 
            angle_CBA, angle_CBA_label, 
            angle_B_1A_1D_1, angle_B_1A_1D_1_label, 
            angle_B_1C_1D_1, angle_B_1C_1D_1_label, 
            B_1A_1, C_1B_1, C_1D_1, D_1A_1,
        )))
        self.wait(0.5)


        ALL = VGroup(
            A, B, C, D,
            A_label, B_label, C_label, D_label,
            A_1, B_1, C_1, D_1,
            A_1_label, B_1_label, C_1_label, D_1_label,
            circle, result_circle,
            circle_AB, circle_BC, circle_CD, circle_DA, 
            label, new_result_circle
        )
        self.play(FadeOut(ALL))


        label = Tex("Now let's consider a few consequences of this theorem")
        self.play(Fancy_label(label))
        self.wait(0.5)
        self.play(FadeOut(label))
    

class Miquel_consequence_1(Scene):
    def construct(self):
        black_rectangle = Rectangle(height=1.2,width=20).shift(3.5*UP).set_color(BLACK).set_opacity(1).set_z_index(101)
        self.add(black_rectangle)

        circle = Circle(radius=2.6,color=BLUE_D).move_to(0.35*DOWN)

        A = Dot(circle.point_at_angle(0.15*PI)).set_z_index(9)
        B = Dot(circle.point_at_angle((4/5)*PI)).set_z_index(9)
        C = Dot(circle.point_at_angle(-(9/11)*PI)).set_z_index(9)
        D = Dot(circle.point_at_angle(-(1/4)*PI)).set_z_index(9)

        A_label = Tex('A',font_size=35).next_to(A.get_center(),UR,buff=0.17).set_z_index(99)
        B_label = Tex('B',font_size=35).next_to(B.get_center(),UL,buff=0.17).set_z_index(99)
        C_label = Tex('C',font_size=35).next_to(C.get_center(),DL,buff=0.17).set_z_index(99)
        D_label = Tex('D',font_size=35).next_to(D.get_center(),DR,buff=0.17).set_z_index(99)

        AB = Line(A.get_center(), B.get_center(), color=YELLOW).set_opacity(0.8)
        BC = Line(B.get_center(), C.get_center(), color=YELLOW).set_opacity(0.8)
        CD = Line(C.get_center(), D.get_center(), color=YELLOW).set_opacity(0.8)
        DA = Line(D.get_center(), A.get_center(), color=YELLOW).set_opacity(0.8)

        AC = Line(A.get_center(), C.get_center(), color=GREEN)
        BD = Line(B.get_center(), D.get_center(), color=GREEN)

        AH_a = Altitude(B.get_center(), A.get_center(), D.get_center(), color=RED)
        BH_b = Altitude(A.get_center(), B.get_center(), C.get_center(), color=RED)
        CH_c = Altitude(D.get_center(), C.get_center(), B.get_center(), color=RED)
        DH_d = Altitude(A.get_center(), D.get_center(), C.get_center(), color=RED)

        H_a = Dot(AH_a.dot).set_z_index(1)
        H_b = Dot(BH_b.dot).set_z_index(1)
        H_c = Dot(CH_c.dot).set_z_index(1)
        H_d = Dot(DH_d.dot).set_z_index(1)

        H_a_label = Tex(r"$\mathrm{H_a}$",font_size=28).next_to(H_a.get_center(),DL,buff=0.1).set_z_index(-0.5)
        H_b_label = Tex(r"$\mathrm{H_b}$",font_size=28).next_to(H_b.get_center(),2*DOWN+RIGHT,buff=0.08).set_z_index(-0.5)
        H_c_label = Tex(r"$\mathrm{H_c}$",font_size=28).next_to(H_c.get_center(),UR,buff=0.1).set_z_index(-0.5)
        H_d_label = Tex(r"$\mathrm{H_d}$",font_size=28).next_to(H_d.get_center(),2*UP+LEFT,buff=0.08).set_z_index(-0.5)

        H_a_angle = AH_a.angles(color=YELLOW, radius=0.2)[0].set_z_index(-1)
        H_b_angle = BH_b.angles(color=YELLOW, radius=0.2)[0].set_z_index(-1)
        H_c_angle = CH_c.angles(color=YELLOW, radius=0.2)[0].set_z_index(-1)
        H_d_angle = DH_d.angles(color=YELLOW, radius=0.2)[1].set_z_index(-1)

        result_circle = Circle().from_three_points(
            H_a.get_center(), H_b.get_center(), H_c.get_center(), color=RED)
        
        circle_AB = Circle().from_three_points(
            A.get_center(), B.get_center(), H_b.get_center(), color=GREEN)
        circle_BC = Circle().from_three_points(
            B.get_center(), C.get_center(), H_b.get_center(), color=GREEN)
        circle_CD = Circle().from_three_points(
            C.get_center(), D.get_center(), H_c.get_center(), color=GREEN)
        circle_DA = Circle().from_three_points(
            D.get_center(), A.get_center(), H_a.get_center(), color=GREEN)

        label = Tex("The inscribed quadrilateral $ABCD$ is given")

        self.play(Fancy_label(label))

        self.play(Create(circle))
        self.play(LaggedStart(
            FadeIn(VGroup(A, A_label)),
            FadeIn(VGroup(B, B_label)),
            FadeIn(VGroup(C, C_label)),
            FadeIn(VGroup(D, D_label)),
            run_time=3, lag_ratio=0.75
        ))
        self.play(LaggedStart(
            Create(AB),
            Create(BC),
            Create(CD),
            Create(DA),
            run_time=4, 
            lag_ratio=0.85
        ))

        self.play(FadeOut(label))
        label = Tex("Let's omit the perpendiculars on the diagonals from the vertices", font_size=46)
        self.play(Fancy_label(label))

        self.play(LaggedStart(
            Create(AC), 
            Create(BD), 
            run_time=1.5, lag_ratio=0.8
        ))

        self.wait(0.15)

        self.play(Create(AH_a), run_time=0.8)
        self.play(FadeIn(VGroup(H_a, H_a_label, H_a_angle)), run_time=0.5)
        self.wait(0.1)

        self.play(Create(BH_b), run_time=0.8)
        self.play(FadeIn(VGroup(H_b, H_b_label, H_b_angle)), run_time=0.5)
        self.wait(0.1)

        self.play(Create(CH_c), run_time=0.8)
        self.play(FadeIn(VGroup(H_c, H_c_label, H_c_angle)), run_time=0.5)
        self.wait(0.1)

        self.play(Create(DH_d), run_time=0.8)
        self.play(FadeIn(VGroup(H_d, H_d_label, H_d_angle)), run_time=0.5)
        self.wait(0.4)

        self.play(FadeOut(label))

        label = Tex("And then the bases of the perpendiculars are on the same circle", font_size=44)
        self.play(Fancy_label(label))

        self.play(VGroup(
            AB, BC, CD, DA,
            AC, BD,
            AH_a, BH_b, CH_c, DH_d,   
            H_a_label, H_b_label, H_c_label, H_d_label, 
            ).animate.set_opacity(0.3),
            VGroup(H_a_angle, H_b_angle, H_c_angle, H_d_angle).animate.set_stroke(opacity=0.5),
            VGroup(H_a, H_b, H_c, H_d).animate.set_opacity(0.65),
            circle.animate.set_stroke(opacity=0.3))
        
        self.wait(0.2)

        self.play(Create(result_circle))
        self.wait(2)
        self.play(Uncreate(result_circle))
        self.play(FadeOut(label))

        label = Tex(r"$\angle{BH_cC}=\angle{BH_bC}=90^{\circ}$, so $BCH_bH_c$ is inscribed")
        self.play(Fancy_label(label))
        self.play(Create(circle_BC))
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex("Similarly for other quadrilaterals")
        self.play(Fancy_label(label))
        self.play(Create(circle_CD))
        self.play(Create(circle_DA))
        self.play(Create(circle_AB))

        self.play(FadeOut(VGroup(
            AB, BC, CD, DA, AC, BD, 
            AH_a, BH_b, CH_c, DH_d, 
            H_a_angle, H_b_angle, H_c_angle, H_d_angle, 
            )), 
            VGroup(
            H_a, H_b, H_c, H_c, 
            ).animate.set_opacity(1))
    
        self.wait(0.15)
        self.play(FadeOut(label))

        label = Tex("So $H_a, H_b, H_c, H_d$ are on the same circle")
        self.play(Fancy_label(label))
        self.play(circle.animate.set_stroke(opacity=1))
        self.play(VGroup(
            circle_AB, circle_BC, circle_CD, circle_DA,
            ).animate.set_stroke(opacity=0.5))
        new_result_circle = Circle().from_three_points(
            H_a.get_center(), H_b.get_center(), H_c.get_center(), color=RED)
        
        self.play(Create(new_result_circle))
        self.wait()
        ALL = VGroup(
            A, B, C, D,
            A_label, B_label, C_label, D_label,
            H_a, H_b, H_c, H_d,
            H_a_label, H_b_label, H_c_label, H_d_label,
            circle_AB, circle_BC, circle_CD, circle_DA, 
            new_result_circle, circle, label
        )
        self.play(FadeOut(ALL))


class Miquel_consequence_2(Scene):
    def construct(self):
        black_rectangle = Rectangle(height=1.2,width=20).shift(3.5*UP).set_color(BLACK).set_opacity(1).set_z_index(101)
        self.add(black_rectangle)

        A = Dot(1.4*DOWN+3*LEFT).set_z_index(2)
        B = Dot(2.15*UP+1.8*LEFT).set_z_index(2)
        C = Dot(1.4*DOWN+2*RIGHT).set_z_index(2)

        A_label = Tex('A',font_size=35).next_to(A.get_center(),DL,buff=0.17).set_z_index(99)
        B_label = Tex('B',font_size=35).next_to(B.get_center(),UP,buff=0.17).set_z_index(99)
        C_label = Tex('C',font_size=35).next_to(C.get_center(),DR,buff=0.17).set_z_index(99)

        AB = Line(A.get_center(),B.get_center(), color=BLUE)
        BC = Line(B.get_center(),C.get_center(), color=BLUE)
        CA = Line(C.get_center(),A.get_center(), color=BLUE)

        B_bisector = Bisector(A.get_center(), B.get_center(), C.get_center(), 
                              color=GREEN).set_length_about_point(B.get_center(), 7)
    
        
        AH_a = Altitude(B.get_center(), A.get_center(), B_bisector.get_end(), color=YELLOW)
        BH_b = Altitude(A.get_center(), B.get_center(), C.get_center(), color=RED)
        CH_c = Altitude(B.get_center(), C.get_center(), B_bisector.get_end(), color=YELLOW)

        H_a = Dot(AH_a.dot).set_z_index(1)
        H_c = Dot(CH_c.dot).set_z_index(1)
        H_b = Dot(BH_b.dot).set_z_index(1)

        H_a_label = Tex(r'$\mathrm{H_a}$', font_size=28).next_to(H_a.get_center(), RIGHT, buff=0.13).set_z_index(9)
        H_b_label = Tex(r'$\mathrm{H_b}$', font_size=28).next_to(H_b.get_center(), DOWN, buff=0.13).set_z_index(9)
        H_c_label = Tex(r'$\mathrm{H_c}$', font_size=28).next_to(H_c.get_center(), LEFT, buff=0.13).set_z_index(9)

        H_a_angle = AH_a.angles(color=YELLOW_D, radius=0.16)[0].set_stroke(opacity=0.75)
        H_b_angle = BH_b.angles(color=YELLOW_D, radius=0.16)[1].set_stroke(opacity=0.75)
        H_c_angle = CH_c.angles(color=YELLOW_D, radius=0.16)[0].set_stroke(opacity=0.75)

        M_b = Dot(CA.point_from_proportion(0.5)).set_z_index(2)
        M_b_label = Tex(r'$\mathrm{M_b}$', font_size=26).next_to(M_b.get_center(), DR, buff=0.1).set_z_index(9).set_z_index(22)
        M_b_equals = VGroup(
            Line(A.get_center(), M_b.get_center()).equal(),
            Line(C.get_center(), M_b.get_center()).equal()
        )

        circumcircle = Circle().from_three_points(A.get_center(), B.get_center(), C.get_center(), color=YELLOW)

        L = Dot(intersection_line_and_circle(B_bisector, circumcircle)[0]).set_z_index(2)
        L_label = Tex(r"$\mathrm{L}$", font_size=30).next_to(L.get_center(), DR, buff=0.13).set_z_index(22)

        AL = Line(A.get_center(), L.get_center(), color=GREEN)
        CL = Line(C.get_center(), L.get_center(), color=GREEN)

        LM_b = Altitude(A.get_center(), L.get_center(), C.get_center(), color=RED_D)
        M_b_angle = LM_b.angles(color=YELLOW_D, radius=0.16)[0]

        L_equals = VGroup(AL.equal(2), CL.equal(2))

        BL = Line(B.get_center(), L.get_center(), color=GREEN).set_opacity(0.6)


        label = Tex("Now let's discuss the second consequence")
        self.play(Fancy_label(label))
        
        self.play(LaggedStart(
            FadeIn(VGroup(A, A_label)),
            FadeIn(VGroup(B, B_label)),
            FadeIn(VGroup(C, C_label)),
            run_time=1.5, lag_ratio=0.7
        ))

        self.play(LaggedStart(
            Create(AB), 
            Create(BC), 
            Create(CA),
            run_time=2, lag_ratio=0.85
        ))

        self.play(FadeOut(label))

        label = Tex(r"Let's draw the bisector of the angle $\angle{B}$")
        self.play(Fancy_label(label))
        self.play(Create(B_bisector))
        self.wait(0.1)
        self.play(FadeOut(label))

        label = Tex(r"Now draw the perpendiculars $AH_a$ and $CH_c$ to the bisector")
        self.play(Fancy_label(label))

        self.play(LaggedStart(
            Create(AH_a),
            FadeIn(H_a), 
            FadeIn(H_a_label),
            run_time=1.6, lag_ratio=0.6
        ))
        self.play(FadeIn(H_a_angle), run_time=0.6)

        self.play(LaggedStart(
            Create(CH_c),
            FadeIn(H_c), 
            FadeIn(H_c_label),
            run_time=1.6, lag_ratio=0.6
        ))
        self.play(FadeIn(H_c_angle), run_time=0.6)

        self.play(FadeOut(label))

        label = Tex(r"Now let's draw the altitude $BH_b$ of the triangle $ABC$")       
        self.play(Fancy_label(label))

        self.play(LaggedStart(
            Create(BH_b),
            FadeIn(H_b), 
            FadeIn(H_b_label),
            run_time=1.6, lag_ratio=0.6
        ))
        self.play(FadeIn(H_b_angle), run_time=0.6)

        self.play(FadeOut(label))

        label = Tex("And now we denote the middle of AC")
        self.play(Fancy_label(label))

        self.play(FadeIn(VGroup(M_b, M_b_label)))
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex(r"Then the points $H_a, H_b, H_c, M_b$ are on the same circle")
        self.play(Fancy_label(label))

        self.play(
            VGroup(BH_b, B_bisector, AH_a, CH_c).animate.set_opacity(0.4),
            VGroup(H_a, H_b, H_c, M_b).animate.set_opacity(0.9),
            VGroup(H_a_label, H_b_label, H_c_label, M_b_label).animate.set_opacity(0.5),
            VGroup(H_a_angle, H_b_angle, H_c_angle).animate.set_stroke(opacity=0.5)
        )

        result_circle = CircumscribedCircle(H_a.get_center(), H_b.get_center(), H_c.get_center(), color=RED)

        self.play(Create(result_circle))
        self.wait(2)
        self.play(Uncreate(result_circle))
        self.play(FadeOut(label))

        label = Tex("To prove it, we draw a circumscribed circle")
        self.play(Fancy_label(label))
        self.play(Create(circumcircle))
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex("$L$ is the intersection of the bisectors and the circumcircle")
        self.play(Fancy_label(label))
        self.play(FadeIn(L, L_label))
        self.wait(0.3)
        self.play(FadeOut(label))

        label = Tex("But then $AL=CL$")
        self.play(Fancy_label(label))
        self.play(LaggedStart(
            Create(AL),
            Create(CL),
            run_time=1.5, lag_ratio=0.85
        ))
        self.play(FadeIn(L_equals))
        self.play(FadeOut(label))

        label = Tex(r"So $ALC$ is isosceles, and the median $LM_b$ is also the altitude", font_size=44)
        self.play(Fancy_label(label))

        self.play(Create(LM_b))
        self.play(FadeIn(M_b_angle))
        self.wait(0.7)
        self.play(FadeOut(label))

        label = Tex("Now the proof of this fact comes down to the previous one")
        self.play(Fancy_label(label))

        self.play(
            FadeOut(L_equals),
            AL.animate.set_color(BLUE),
            CL.animate.set_color(BLUE),
            CA.animate.set_color(GREEN).set_opacity(0.7),
            FadeIn(BL),
            BH_b.animate.set_opacity(0.7),
            LM_b.animate.set_opacity(0.7),
            AH_a.animate.set_color(RED).set_opacity(0.7),
            CH_c.animate.set_color(RED).set_opacity(0.7),
            H_b_angle.animate.set_stroke(opacity=0.7),
            H_a_angle.animate.set_stroke(opacity=0.7),
            H_c_angle.animate.set_stroke(opacity=0.7),
            M_b_angle.animate.set_stroke(opacity=0.7)
        )

        result_circle = CircumscribedCircle(H_a.get_center(), H_b.get_center(), H_c.get_center(), color=YELLOW)
        O = Dot(result_circle.get_center()).set_z_index(1)
        O_label = Tex(r"$\mathrm{O}$", font_size=27).next_to(O.get_center(), DOWN, buff=0.12).set_z_index(1)
        euler_circle = EulerCircle(A.get_center(), B.get_center(), C.get_center())


        self.play(Create(result_circle))
        self.wait(1.5)
        self.play(FadeOut(label))

        label = Tex("Okay, where is the center of this circle?")
        self.play(Fancy_label(label))
        self.wait()
        self.play(FadeOut(label))

        label = Tex("The center of this circle is on the Euler's circle of triangle $ABC$", font_size=44)
        self.play(Fancy_label(label))
    
        self.play(
            BH_b.animate.set_opacity(0.3),
            LM_b.animate.set_opacity(0.3),
            AH_a.animate.set_opacity(0.3),
            CH_c.animate.set_opacity(0.3),
            FadeOut(BL),
            CA.animate.set_opacity(0.3),
            circumcircle.animate.set_stroke(opacity=0.4),
            VGroup(H_a_angle, H_b_angle, H_c_angle, M_b_angle).animate.set_stroke(opacity=0.3)
        )
        self.play(FadeIn(VGroup(O, O_label)))
        self.play(Create(euler_circle))

        self.play(FadeOut(label))

        label = Tex("Now let's prove this too")
        self.play(Fancy_label(label))
        self.wait(0.7)
        self.play(FadeOut(label))

        label = Tex("Let $O$ be the center of the arc $H_bM_b$ of the Euler's circle", font_size=46)
        self.play(Fancy_label(label))
        self.play(FadeOut(result_circle),
                  VGroup(H_a, H_c, M_b, H_b).animate.set_opacity(0.7),
                  VGroup(H_a_label, H_c_label, H_b_label, M_b_label).animate.set_opacity(0.7),
                  VGroup(AB, BC, AL, CL).animate.set_opacity(0.75))
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex("We prove that $O$ is on the perpendicular bisectors to $H_bM_b$ and $H_aH_c$", font_size=42)
        self.play(Fancy_label(label))
        self.wait()
        self.play(FadeOut(label))

        label = Tex("From the definition of $O$, it lies on perpendicular bisector $H_bM_b$", font_size=44)
        self.play(Fancy_label(label))
        self.wait()
        self.play(FadeOut(label))

        label = Tex("$O_1$ is a point diametrically opposite to $O$ on the Euler's circle", font_size=44)
        self.play(Fancy_label(label))

        tmp = Line(O.get_center(), euler_circle.get_center())
        O_1 = Dot(tmp.set_length_about_point(O.get_center(), 2*tmp.get_length()).get_end()).set_z_index(9)
        O_1_label = Tex("$\mathrm{O_1}$", font_size=30).next_to(O_1.get_center(), np.array([-0.05,0.8,0]), buff=0.13).set_z_index(9)

        self.play(FadeIn(VGroup(O_1, O_1_label)))
        self.wait(0.25)
        self.play(FadeOut(label))

        label = Tex("Let's denote the midpoints of sides $AB$ and $BC$ as $M_c$ and $M_a$", font_size=44)
        self.play(Fancy_label(label))

        M_a = Dot(BC.get_center()).set_z_index(9)
        M_c = Dot(AB.get_center()).set_z_index(9)   

        M_a_label = Tex(r"$\mathrm{M_a}$", font_size=28).next_to(M_a.get_center(), UR, buff=0.11).set_z_index(9)
        M_c_label = Tex(r"$\mathrm{M_c}$", font_size=28).next_to(M_c.get_center(), UL, buff=0.11).set_z_index(9)

        self.play(LaggedStart(
            FadeIn(VGroup(M_a, M_a_label)),
            FadeIn(VGroup(M_c, M_c_label)),
            run_time=1.2, lag_ratio=0.8
        ))
        self.play(FadeOut(label))

        label = Tex(r"Obviously, $H_bM_c=\frac{AB}{2}$ as the median of a right triangle", font_size=44)
        self.play(Fancy_label(label))
        self.wait()
        self.play(FadeOut(label))

        label = Tex(r"And $M_bM_c=\frac{AB}{2}$ as the middle line, so $M_bM_c=H_bM_c$", font_size=44)
        self.play(Fancy_label(label))

        M_cH_b = Line(M_c.get_center(), H_b.get_center(), color=YELLOW)
        M_aM_b = Line(M_a.get_center(), M_b.get_center(), color=YELLOW)
        tmp_equals = VGroup(M_cH_b.equal(), M_aM_b.equal())

        self.play(LaggedStart(
            Create(M_cH_b),
            Create(M_aM_b),
            run_time=1.5, lag_ratio=0.85
        ))
        self.play(FadeIn(tmp_equals))
        self.wait(0.5)
        self.play(FadeOut(label))

        label = Tex("So $O_1$ is the middle of the $M_cM_a$ arc")
        self.play(Fancy_label(label))
        self.play(FadeOut(VGroup(M_cH_b, M_aM_b, tmp_equals)))

        M_cO_1 = Line(M_c.get_center(), O_1.get_center(), color=YELLOW)
        O_1M_a = Line(O_1.get_center(), M_a.get_center(), color=YELLOW)

        tmp_equals = VGroup(M_cO_1.equal(2), O_1M_a.equal(2))

        self.play(LaggedStart(
            Create(M_cO_1),
            Create(O_1M_a),
            run_time=1.5, lag_ratio=0.75
        ))
        self.play(FadeIn(tmp_equals))

        self.play(FadeOut(label))

        label = Tex(r"Therefore, $M_bO_1$ is the bisector of the angle $\angle{M_cM_bM_a}$")
        self.play(Fancy_label(label))

        M_bO_1 = Line(M_b.get_center(), O_1.get_center(), color=GREEN).set_opacity(0.5)

        M_cM_b = Line(M_c.get_center(), M_b.get_center(), color=BLUE)
        M_aM_b.set_color(BLUE)

        BM_c = Line(B.get_center(), M_c.get_center(), color=BLUE)
        BM_a = Line(B.get_center(), M_a.get_center(), color=BLUE)

        self.play(FadeOut(VGroup(M_cO_1, O_1M_a, tmp_equals)), FadeOut(VGroup(H_a_label, H_a)))

        self.play(FadeIn(VGroup(BM_c, BM_a)))

        self.play(LaggedStart(
            Create(M_cM_b),
            Create(M_aM_b),
            Create(M_bO_1),
            run_time=2.4, lag_ratio=0.75
        ))

        self.play(FadeOut(label))

        label = Tex("$BM_aM_bM_c$ is a parallelogram, so $BL$ is parallel to $M_bO_1$")
        self.play(Fancy_label(label))

        for_paral_line = Line(B.get_center(), BL.point_from_proportion(0.7))
        paral_1 = VGroup(for_paral_line.paral(), M_bO_1.paral(rotate=True))

        VGroup(H_a, H_a_label).set_opacity(0)
        self.add(VGroup(H_a, H_a_label))

        self.play(FadeIn(paral_1))
        self.play(FadeOut(VGroup(
            M_aM_b, M_cM_b, BM_c, BM_a
        )), VGroup(H_a, H_a_label).animate.set_opacity(0.5))
        self.play(FadeOut(label))

        label = Tex(r"$OO_1$ is the diameter, so the angle $\angle{OM_bO_1}$ is $90^{\circ}$")
        self.play(Fancy_label(label))
        
        OM_b = Line(O.get_center(), M_b.get_center(), color=BLUE)
        angle_OM_bO_1 = Angle().from_three_points(
            O.get_center(), M_b.get_center(), O_1.get_center(), color=YELLOW, radius=0.13, elbow=True
        )

        self.play(euler_circle.animate.set_stroke(opacity=0.6), run_time=0.5)
        self.play(Create(OM_b))
        self.play(FadeIn(angle_OM_bO_1))

        self.play(FadeOut(label))

        label = Tex(r"But $BL$ and $M_bO_1$ are parallel, so $OM_b$ and $BL$ are perpendicular too", font_size=40)
        self.play(Fancy_label(label))
        tmp = Dot(intersection_lines(BL, OM_b), radius=0.035).set_z_index(1)
        self.play(Transform(angle_OM_bO_1, 
            Angle().from_three_points(
                O.get_center(), tmp.get_center(), B.get_center(), color=YELLOW, radius=0.1, elbow=True
        )))
        self.play(FadeOut(label))

        label = Tex("So $O$ is on the perpendicular bisector to $H_aH_c$")
        self.play(Fancy_label(label))
        tmp_equals = VGroup(
            Line(H_a.get_center(), tmp.get_center()).equal().scale(0.6).set_opacity(0.8),
            Line(H_c.get_center(), tmp.get_center()).equal().scale(0.6).set_opacity(0.8),
            )
        self.play(FadeIn(VGroup(tmp, tmp_equals)))
        self.wait(1.5)
        self.play(FadeOut(label), FadeOut(VGroup(
            tmp, tmp_equals, OM_b, angle_OM_bO_1, paral_1, M_bO_1
            )))

        label = Tex("It means that $O$ is the center of the circle $H_aH_bH_cM_b$", font_size=46)
        self.play(Fancy_label(label))
        self.play(Create(result_circle))
        self.wait(2.5)

        ALL = VGroup(
            A, B, C, AB, BC, CA, 
            AL, CL, L, L_label,
            A_label, B_label, C_label, 
            H_a_label, H_b_label, H_c_label, 
            M_b, M_b_label, 
            result_circle, euler_circle, circumcircle,
            B_bisector, O, O_1, O_label, O_1_label,
            M_a, M_c, M_a_label, M_c_label,  
            AH_a, BH_b, CH_c, LM_b, H_a, H_b, H_c,
            H_a_angle, H_b_angle, H_c_angle, M_b_angle, 
        )

        self.play(FadeOut(ALL), FadeOut(label))
        self.wait()


class Miquel_consequence_3(Scene):
    def construct(self):
        black_rectangle = Rectangle(height=1.2,width=20).shift(3.5*UP).set_color(BLACK).set_opacity(1).set_z_index(101)
        self.add(black_rectangle)

        A = Dot(1.2*DOWN+2*LEFT).set_z_index(2)
        B = Dot(2.15*UP+1.8*LEFT).set_z_index(2)
        C = Dot(1.2*DOWN+1.7*RIGHT).set_z_index(2)

        A_label = Tex('A',font_size=35).next_to(A.get_center(),LEFT,buff=0.17).set_z_index(99)
        B_label = Tex('B',font_size=35).next_to(B.get_center(),UP,buff=0.17).set_z_index(99)
        C_label = Tex('C',font_size=35).next_to(C.get_center(),RIGHT,buff=0.17).set_z_index(99)

        AB = Line(A.get_center(),B.get_center(), color=BLUE)
        BC = Line(B.get_center(),C.get_center(), color=BLUE)
        CA = Line(C.get_center(),A.get_center(), color=BLUE)

        B_bisector = Bisector(A.get_center(), B.get_center(), C.get_center(), 
                              color=GREEN).set_length_about_point(B.get_center(), 7)
        
        AH_a = Altitude(B.get_center(), A.get_center(), B_bisector.get_end(), color=RED)
        CH_c = Altitude(B.get_center(), C.get_center(), B_bisector.get_end(), color=RED)

        H_a = Dot(AH_a.dot).set_z_index(1)
        H_c = Dot(CH_c.dot).set_z_index(1)

        H_a_label = Tex(r'$\mathrm{H_a}$', font_size=28).next_to(H_a.get_center(), np.array([0.9,-0.1,0]), buff=0.13).set_z_index(9)
        H_c_label = Tex(r'$\mathrm{H_c}$', font_size=28).next_to(H_c.get_center(), np.array([-0.9,-0.1,0]), buff=0.13).set_z_index(9)

        H_a_angle = AH_a.angles(color=YELLOW, radius=0.16)[0].set_stroke(opacity=0.75)
        H_c_angle = CH_c.angles(color=YELLOW, radius=0.16)[0].set_stroke(opacity=0.75)
        
        inscribed_circle = InscribedCircle(A.get_center(), B.get_center(), C.get_center(), color=YELLOW)
        escribed_circle = EscribedCircle(A.get_center(), B.get_center(), C.get_center(), color=YELLOW)


        X = Dot(intersection_line_and_circle(CA, inscribed_circle)[0]).set_z_index(9)
        Y = Dot(intersection_line_and_circle(CA, escribed_circle)[0]).set_z_index(9)

        X_label = Tex("X", font_size=30).next_to(X.get_center(), DL, buff=0.12).set_z_index(9)
        Y_label = Tex("Y", font_size=30).next_to(Y.get_center(), UR, buff=0.12).set_z_index(9)

        
        label = Tex("And the last consequence of Miquel's theorem")
        self.play(Fancy_label(label))   
        self.wait(0.5)
        self.play(FadeOut(label))

        self.play(LaggedStart(
            FadeIn(VGroup(A, A_label)),
            FadeIn(VGroup(B, B_label)),
            FadeIn(VGroup(C, C_label)),
            run_time=1.5, lag_ratio=0.7
        ))

        self.play(LaggedStart(
            Create(AB),
            Create(BC),
            Create(CA),
            run_time=2.2, lag_ratio=0.7
        ))

        label = Tex(r"We will lower the perpendiculars to the bisector of the angle $\angle{B}$", font_size=42)     
        self.play(Fancy_label(label))

        self.play(Create(B_bisector))

        self.play(Create(AH_a))
        self.play(FadeIn(VGroup(H_a, H_a_label, H_a_angle)))

        self.wait(0.3)

        self.play(Create(CH_c))
        self.play(FadeIn(VGroup(H_c, H_c_label, H_c_angle)))
        
        self.play(FadeOut(label))

        label = Tex("Now let's build an inscribed circle")
        self.play(Fancy_label(label))
        self.play(VGroup(AH_a, CH_c).animate.set_opacity(0.4), 
                  VGroup(H_a_angle, H_c_angle).animate.set_stroke(opacity=0.5))
        self.play(Create(inscribed_circle))
        self.play(FadeOut(label))

        label = Tex("Let $X$ be the tangent point of the inscribed circle with $AC$")
        self.play(Fancy_label(label))
        self.play(FadeIn(VGroup(X, X_label)))
        self.play(FadeOut(label))
        self.play(FadeOut(inscribed_circle), VGroup(X, X_label).animate.set_opacity(0.5))

        label = Tex("Now let's build an escribed circle")
        tmp_1 = Line(B.get_center(), A.get_center(), color=BLUE).set_length_about_point(B.get_center(), 8).set_opacity(0.3)
        tmp_2 = Line(B.get_center(), C.get_center(), color=BLUE).set_length_about_point(B.get_center(), 8).set_opacity(0.3)
        self.play(Fancy_label(label))
        self.play(FadeIn(VGroup(tmp_1, tmp_2)), run_time=0.6)
        self.play(Create(escribed_circle))
        self.play(FadeOut(label))

        label = Tex("Let $Y$ be the tangent point of an escribed circle with $AC$", font_size=46)
        self.play(Fancy_label(label))
        self.play(FadeIn(VGroup(Y, Y_label)))
        self.play(FadeOut(label))
        self.play(FadeOut(escribed_circle), FadeOut(tmp_1, tmp_2))

        self.play(VGroup(X, X_label).animate.set_opacity(1))

        label = Tex("It turns out that the points $H_a, H_c, X, Y$ are on the same circle", font_size=46)
        circle = Circle().from_three_points(H_a.get_center(), H_c.get_center(), X.get_center(), color=YELLOW)
        self.play(Fancy_label(label))
        self.play(Create(circle))
        self.wait()
        self.play(FadeOut(label))

        label = Tex("Prove this fact yourself, it's not difficult")
        self.play(Fancy_label(label))
        self.wait(1.5)
        self.play(FadeOut(label))

        label = Tex("Also prove that the center of this circle is the middle of AC")
        self.play(Fancy_label(label))
        M_b = Dot(CA.get_center())
        M_b_label = Tex(r"$\mathrm{M_b}$", font_size=30).next_to(M_b.get_center(), DOWN, buff=0.12)
        self.play(FadeIn(VGroup(M_b, M_b_label)))
        self.wait(2)

        ALL = VGroup(
            A, B, C, 
            A_label, B_label, C_label, 
            AB, BC, CA, B_bisector,
            X, X_label, Y, Y_label, 
            H_a, H_a_label, H_c, H_c_label, circle,
            H_a_angle, H_c_angle, AH_a, CH_c,
            M_b, M_b_label,
            label
        )
        self.play(FadeOut(ALL))

        self.wait()


class Archimedes_lemma(Scene):  
    def construct(self):
        black_rectangle = Rectangle(height=1.2,width=20).shift(3.5*UP).set_color(BLACK).set_opacity(1).set_z_index(101)
        self.add(black_rectangle)

        Omega = Circle(color=BLUE, radius=2.5, arc_center=0.5*DOWN)
        Omega_label = Tex(r"$\mathrm{\Omega}$",font_size=35).move_to(1.7*RIGHT+1*UP)
        
        M = Dot(Omega.point_at_angle(0.9*PI)).set_z_index(9)
        N = Dot(Omega.point_at_angle(0.1*PI)).set_z_index(9)

        M_label = Tex("M", font_size=32).next_to(M.get_center(), np.array([-0.8,-0.6,0]), buff=0.12).set_z_index(9)
        N_label = Tex("N", font_size=32).next_to(N.get_center(), np.array([0.8,-0.6,0]), buff=0.12).set_z_index(9)

        MN = Line(M.get_center(), N.get_center(), color=GREEN)

        A = Dot(Omega.point_at_angle(0.65*PI)).set_z_index(9)
        B = Dot(intersection_lines(Bisector(M.get_center(), A.get_center(), N.get_center()), MN)).set_z_index(9)

        AB = Line(A.get_center(), B.get_center(), color=RED)
        MA = Line(M.get_center(), A.get_center(), color=BLUE).set_opacity(0.6)
        AN = Line(A.get_center(), N.get_center(), color=BLUE).set_opacity(0.6)

        A_label = Tex("A", font_size=30).next_to(A.get_center(), UL, buff=0.1).set_z_index(9)
        B_label = Tex("B", font_size=30).next_to(B.get_center(), DOWN, buff=0.1).set_z_index(9)

        perpendicular_bisector_AB = PerpendicularBisector(A.get_center(), B.get_center())
        perpendicular_B = Perpendicular(Line(M.get_center(), N.get_center()), B.get_center())
        X = intersection_lines(perpendicular_bisector_AB, perpendicular_B)

        omega = Circle(radius=Line(X, B.get_center()).get_length(), arc_center=X)
        omega_label = Tex(r"$\mathrm{\omega}$",font_size=35).move_to(np.array([-0.35,1.45,0])).set_z_index(9)

        tangent = Tangent(omega, A.get_center(), color=YELLOW)

        K = Dot(intersection_lines(MN, tangent))
        K_label = Tex("K", font_size=30).next_to(K, LEFT, buff=0.1)

        MK = Line(M.get_center(), K.get_center(), color=GREEN)
        tangent.set_length(2*Line(K.get_center(), A.get_center()).get_length())

        angle_MAB = Angle().from_three_points(M.get_center(), A.get_center(), B.get_center(), radius=0.3).set_z_index(-1)
        angle_BAN = Angle().from_three_points(B.get_center(), A.get_center(), N.get_center(), radius=0.26).set_z_index(-1)
        angle_KAM = Angle().from_three_points(K.get_center(), A.get_center(), M.get_center(), radius=0.26).set_z_index(-1)




        label = Tex("Now let's discuss the following theorem - Archimedes' lemma", font_size=44)
        self.play(Fancy_label(label))
        self.play(Create(Omega))
        self.play(FadeIn(Omega_label), run_time=0.6)
        self.play(FadeOut(label))

        label = Tex("Let's draw the chord $MN$ of the circle $\Omega$")
        self.play(Fancy_label(label))
        self.play(LaggedStart(
            FadeIn(VGroup(M, M_label)),
            FadeIn(VGroup(N, N_label)),
            Create(MN),
            run_time=2, lag_ratio=0.75
        ))
        self.play(FadeOut(label))

        label = Tex("Let's construct a circle $\omega$ that touches both $MN$ and $\Omega$")
        self.play(Fancy_label(label))
        self.play(Create(omega))
        self.play(FadeIn(omega_label), run_time=0.6)
        self.wait(0.5)
        self.play(FadeOut(label))

        label = Tex(r"$A$ and $B$ are the points of tangency of $\omega$ with $\Omega$ and $MN$", font_size=44)
        self.play(Fancy_label(label))
        self.play(LaggedStart(
            FadeIn(VGroup(A, A_label)),
            FadeIn(VGroup(B, B_label)),
            run_time=1.2, lag_ratio=0.75
        ))
        self.wait()
        self.play(FadeOut(label))

        label = Tex(r"Then $AB$ is the bisector of the angle $\angle{MAN}$")
        self.play(Fancy_label(label))
        self.play(FadeOut(VGroup(omega, omega_label)))
        self.play(LaggedStart(
            Create(MA),
            Create(AN),
            run_time=1.5, lag_ratio=0.85
        ))
        self.play(Create(AB))
        self.play(FadeIn(angle_MAB), run_time=0.75)
        self.play(FadeIn(angle_BAN), run_time=0.75)
        self.wait()
        self.play(FadeOut(VGroup(angle_MAB, angle_BAN, label)))

        label = Tex(r"Let's draw a tangent to the circles through $A$")
        self.play(Fancy_label(label))
        self.play(Create(tangent))
        self.play(FadeOut(label))

        label = Tex("$K$ is the intersection point of this tangent with the line $MN$", font_size=44)
        self.play(Fancy_label(label))
        self.play(Create(MK))
        self.play(FadeIn(VGroup(K, K_label)))
        self.play(FadeOut(label))

        label = Tex(r"Let $\angle{KAM}=\alpha$ and $\angle{MAB}=\beta$")
        angle_KAM_label = Tex(r"$\alpha$", font_size=28).next_to(A.get_center(), np.array([-0.7,-0.6,0]), buff=0.37)
        angle_MAB_label = Tex(r"$\beta$", font_size=28).next_to(A.get_center(), np.array([-0.1, -0.9, 0]), buff=0.38)

        self.play(Fancy_label(label))

        self.play(LaggedStart(
            FadeIn(VGroup(angle_KAM, angle_KAM_label)),
            FadeIn(VGroup(angle_MAB, angle_MAB_label)),
            run_time=2, lag_ratio=0.8
        ))
        self.wait(0.3)
        self.play(FadeOut(label))

        label = Tex(r"But $KA=KB$ as tangents to $\omega$, so $\angle{KBA}=\alpha+\beta$")
        self.play(Fancy_label(label, mode='low'))

        angle_KBA = Angle().from_three_points(K.get_center(), B.get_center(), A.get_center(), radius=0.17)
        angle_KBA_label = Tex(r"$\alpha+\beta$", font_size=28).next_to(B.get_center(), np.array([-0.8,0.5,0]), buff=0.17)

        self.play(FadeIn(VGroup(angle_KBA, angle_KBA_label)))

        self.wait(0.35)
        self.play(FadeOut(label))

        label = Tex("The angle between the chord and the tangent is equal to half of the arc", font_size=42)
        self.play(Fancy_label(label))
        self.wait(1.5)
        self.play(FadeOut(label))

        label = Tex(r"So $\angle{KAM}=\angle{ANM}=\alpha$")
        self.play(Fancy_label(label, mode='low'))
        self.wait(0.2)

        angle_ANM = Angle().from_three_points(A.get_center(), N.get_center(), M.get_center(), radius=0.44).set_z_index(-1)
        angle_ANM_label = Tex(r"$\alpha$", font_size=28).next_to(N.get_center(), np.array([-0.9, 0.1, 0]), buff=0.6)

        self.play(FadeIn(VGroup(angle_ANM_label, angle_ANM)))
        self.wait()
        self.play(FadeOut(label))

        label = Tex(r"But then $\angle{BAN}=\angle{MBA}-\angle{MNA}=\beta$")
        self.play(Fancy_label(label, mode='low'))
        
        angle_BAN_label = Tex(r"$\beta$", font_size=28).next_to(A.get_center(), np.array([0.5,-0.8,0]), buff=0.27)

        self.play(FadeIn(VGroup(angle_BAN, angle_BAN_label)))
        self.wait(2.5)
        self.play(FadeOut(VGroup(
            angle_KBA, angle_KBA_label, angle_KAM, angle_KAM_label, angle_ANM, angle_ANM_label, label)))
        
        label = Tex("So $AB$ is a bisector")
        self.play(Fancy_label(label))
        self.wait(1.5)
        self.play(FadeOut(label))

        label = Tex("Prove the case when the tangent is parallel to the chord yourself", font_size=42)
        self.play(Fancy_label(label))
        self.wait()
        self.play(FadeOut(VGroup(
            M, N, M_label, N_label, 
            A, B, A_label, B_label, 
            Omega, Omega_label, 
            tangent, MN, MK, K, K_label,
            angle_MAB, angle_MAB_label, angle_BAN, angle_BAN_label, 
            MA, AN, AB,
            label
        )))


class External_archimedes_lemma(Scene):
    def construct(self):
        black_rectangle = Rectangle(height=1.2,width=20).shift(3.5*UP).set_color(BLACK).set_opacity(1).set_z_index(101)
        self.add(black_rectangle)

        Omega = Circle(color=BLUE, arc_center=1.5*DOWN+2*RIGHT, radius=2)
        Omega_label = Tex(r"$\mathrm{\Omega}$", font_size=34).move_to(3.38*RIGHT+0.5*DOWN)

        O_1 = Dot(Omega.get_center()).set_z_index(1)
        O_1_label = Tex(r"$\mathrm{O_1}$", font_size=30).next_to(O_1.get_center(), DOWN, buff=0.12)

        M = Dot(Omega.point_at_angle(0.95*PI)).set_z_index(9)
        N = Dot(Omega.point_at_angle(0.05*PI)).set_z_index(9)

        M_label = Tex("M", font_size=32).next_to(M.get_center(), np.array([-0.8,-0.6,0]), buff=0.12).set_z_index(9)
        N_label = Tex("N", font_size=32).next_to(N.get_center(), np.array([0.8,-0.6,0]), buff=0.12).set_z_index(9)

        MN = Line(M.get_center(), N.get_center(), color=GREEN).set_length(20)

        C = Dot(intersection_line_and_circle(
            PerpendicularBisector(M.get_center(), N.get_center()), Omega)[0]).set_z_index(3)
        C_label = Tex("C", font_size=30).next_to(C.get_center(), UP, buff=0.13).set_z_index(3)

        A = Dot(Omega.point_at_angle(0.83*PI)).set_z_index(9)
        A_label = Tex("A", font_size=30).next_to(A.get_center(), np.array([0.2,-0.9,0]), buff=0.13).set_z_index(3)

        B = Dot(intersection_lines(Line(C.get_center(), A.get_center()), MN)).set_z_index(3)
        B_label = Tex("B", font_size=30).next_to(B.get_center(), DOWN, buff=0.13).set_z_index(3)

        O_2 = Dot(intersection_lines(
            Perpendicular(Line(M.get_center(), N.get_center()), B.get_center()),
            PerpendicularBisector(B.get_center(), A.get_center())
        )).set_z_index(1)
        O_2_label = Tex(r"$\mathrm{O_2}$", font_size=32).next_to(O_2.get_center(), UP, buff=0.13)

        omega = Circle(radius=Line(O_2.get_center(), B.get_center()).get_length(), arc_center=O_2.get_center(), color=YELLOW)
        omega_label = Tex("$\mathrm{\omega}$", font_size=36).move_to(
            omega.get_center()+omega.radius*LEFT*0.65 + omega.radius*UP*0.45)

        BC = Line(B.get_center(), C.get_center(), color=RED)

        O_1C = Line(O_1.get_center(), C.get_center(), color=RED)
        O_1A = Line(O_1.get_center(), A.get_center(), color=RED)
        
        O_2A = Line(O_2.get_center(), A.get_center(), color=RED)
        O_2B = Line(O_2.get_center(), B.get_center(), color=RED)

        O_1_equals = VGroup(O_1C.equal(), O_1A.equal())
        O_2_equals = VGroup(O_2B.equal(2), O_2A.equal(2))

        paral = VGroup(O_1C.paral(), O_2B.paral(rotate=True))

        O_2B_angle = Angle().from_three_points(
            O_2.get_center(), B.get_center(), MN.get_start(), 
            elbow=True, radius=0.25, color=YELLOW)
        O_2B_angle_copy = O_2B_angle.copy()


        label = Tex("Consider a similar statement, but for an external touch")
        self.play(Fancy_label(label))
        self.play(Create(Omega))
        self.play(FadeIn(Omega_label), run_time=0.6)
        self.play(LaggedStart(
            FadeIn(VGroup(M, M_label)),
            FadeIn(VGroup(N, N_label)),
            run_time=1.2, lag_ratio=0.7
        ))
        self.play(Create(MN))
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex("Let's construct a circle that touches $MN$ and $\Omega$")
        self.play(Fancy_label(label))
        self.play(Create(omega))
        self.play(FadeIn(omega_label), run_time=0.6)
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex(r"$B$ and $A$ - points of contact of $\omega$ with $MN$ and $\Omega$, respectively", font_size=44)
        self.play(Fancy_label(label))
        self.play(LaggedStart(
            FadeIn(VGroup(B, B_label)),
            FadeIn(VGroup(A, A_label)),
            run_time=1.2, lag_ratio=0.8
        ))
        self.wait(0.3)
        self.play(FadeOut(label))

        label = Tex("$C$ is the intersection point of the line $AB$ with circle $\Omega$")
        self.play(Fancy_label(label))
        self.play(FadeIn(VGroup(C, C_label)))
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex("Then the line $BC$ divides the arc $MN$ in half")
        self.play(Fancy_label(label))
        self.play(Create(BC))
        self.wait(1.5)
        self.play(FadeOut(label))
        
        label = Tex("$O_1C = O_1A$ as the radii of the circle")
        self.play(Fancy_label(label))
        self.play(FadeIn(VGroup(O_1, O_1_label)))
        self.play(LaggedStart(
            Create(O_1C),
            Create(O_1A),
            run_time=1.8, lag_ratio=0.8
        ))
        self.play(FadeIn(O_1_equals), run_time=0.75)
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex("Similarly, $O_2A=O_2B$")
        self.play(Fancy_label(label))
        self.play(FadeIn(VGroup(O_2, O_2_label)))
        self.play(LaggedStart(
            Create(O_2A),
            Create(O_2B),
            run_time=1.8, lag_ratio=0.8
        ))
        self.play(FadeIn(O_2_equals))
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex(r"Obviously, $O_1, A, O_2$ are on the same line, then $\angle{O_2AB}=\angle{CAO_1}$", font_size=44)
        self.play(Fancy_label(label))

        tmp_angle_1 = Angle().from_three_points(
            O_2.get_center(), A.get_center(), B.get_center(), radius=0.2).set_z_index(-1)
        tmp_angle_2 = Angle().from_three_points(
            O_1.get_center(), A.get_center(), C.get_center(), radius=0.2).set_z_index(-1)
        
        self.play(FadeIn(tmp_angle_1), run_time=0.75)
        self.play(FadeIn(tmp_angle_2), run_time=0.75)
        self.play(Wiggle(tmp_angle_1), run_time=0.75)
        self.play(Wiggle(tmp_angle_2), run_time=0.75)
        self.wait(0.3)
        self.play(FadeOut(label))

        label = Tex("Therefore, the triangles $BAO_2$ and $CAO_1$ are similar")
        self.play(Fancy_label(label))
        self.wait(1)
        self.play(FadeOut(VGroup(tmp_angle_1, tmp_angle_2)), run_time=0.75)
        self.play(FadeOut(label))

        label = Tex("This means that $O_1C$ and $O_2B$ are parallel")   
        self.play(Fancy_label(label))    
        self.play(FadeOut(O_1_equals), FadeOut(O_2_equals), run_time=0.65)
        self.play(FadeIn(paral), run_time=0.65)
        self.wait(0.3)
        self.play(FadeOut(label))

        label = Tex("$MN$ is tangent to $\omega$, so $O_2B$ and $MN$ are perpendicular", font_size=42)
        self.play(Fancy_label(label))
        self.play(FadeIn(O_2B_angle))
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex("So $MN$ and $O_1C$ are perpendicular too")
        self.play(Fancy_label(label))
        self.add(O_2B_angle_copy)
        tmp = intersection_lines(MN, O_1C)
        self.play(O_2B_angle_copy.animate.shift(RIGHT*(tmp[0]-B.get_center()[0])))
        self.wait(0.2)
        self.play(FadeOut(label))
        label = Tex("Therefore, $O_1C$ is the perpendicular bisector to $MN$")
        self.play(Fancy_label(label))
        self.wait(1.5)
        self.play(FadeOut(label))

        label = Tex("This means that $C$ is the middle of the $MN$ arc")
        self.play(Fancy_label(label))
        self.wait(2)
        ALL = VGroup(
            M, N, M_label, N_label, 
            A, B, C, A_label, B_label, C_label,
            Omega, omega, Omega_label, omega_label,
            BC, O_1C, O_1A, O_2A, O_2A, MN,
            O_2B, O_1C, paral, 
            O_1, O_2, O_1_label, O_2_label, 
            O_2B_angle, O_2B_angle_copy, 
            label
        )
        self.play(FadeOut(ALL))
        

class Exercise_1(Scene):
    def construct(self):
        black_rectangle = Rectangle(height=1.2,width=20).shift(3.5*UP).set_color(BLACK).set_opacity(1).set_z_index(101)
        self.add(black_rectangle)

        Omega = Circle(color=BLUE, radius=2.5, arc_center=0.5*DOWN)
        Omega_label = Tex(r"$\mathrm{\Omega}$",font_size=35).move_to(1.7*RIGHT+1*UP)
        
        M = Dot(Omega.point_at_angle(0.9*PI)).set_z_index(9)
        N = Dot(Omega.point_at_angle(0.1*PI)).set_z_index(9)

        M_label = Tex("M", font_size=32).next_to(M.get_center(), np.array([-0.8,-0.6,0]), buff=0.12).set_z_index(9)
        N_label = Tex("N", font_size=32).next_to(N.get_center(), np.array([0.8,-0.6,0]), buff=0.12).set_z_index(9)

        MN = Line(M.get_center(), N.get_center(), color=GREEN)

        A = Dot(Omega.point_at_angle(0.65*PI)).set_z_index(9)
        B = Dot(intersection_lines(Bisector(M.get_center(), A.get_center(), N.get_center()), MN)).set_z_index(9)

        B_label = Tex("B", font_size=30).next_to(B.get_center(), DOWN, buff=0.1).set_z_index(9)

        perpendicular_bisector_AB = PerpendicularBisector(A.get_center(), B.get_center())
        perpendicular_B = Perpendicular(Line(M.get_center(), N.get_center()), B.get_center())
        X = intersection_lines(perpendicular_bisector_AB, perpendicular_B)

        omega = Circle(radius=Line(X, B.get_center()).get_length(), arc_center=X)
        omega_label = Tex(r"$\mathrm{\omega}$",font_size=35).move_to(np.array([-0.35,1.45,0])).set_z_index(9)

        label = Tex("Now a few exercises for you")
        self.play(Fancy_label(label))
        self.wait()
        self.play(FadeOut(label))

        label = Tex("Given a circle $\Omega$ and a chord $MN$")
        self.play(Fancy_label(label))
        self.play(Create(Omega))
        self.play(FadeIn(Omega_label))
        self.play(LaggedStart(
            FadeIn(VGroup(M, M_label)),
            FadeIn(VGroup(N, N_label)),
            run_time=1.4, lag_ratio=0.8
        ))
        self.play(Create(MN))
        self.play(FadeOut(label))

        label = Tex("Point $B$ is on $MN$")
        self.play(Fancy_label(label))
        self.play(FadeIn(VGroup(B, B_label)))
        self.play(FadeOut(label))

        label = Tex("How to construct a circle that touches $MN$ at point $B$ and the $\Omega$?", font_size=42)
        self.play(Fancy_label(label))
        self.play(FadeIn(VGroup(omega, omega_label)))
        self.wait(1.5)
        
        ALL = VGroup(
            M, N, M_label, N_label, 
            B, B_label, Omega, omega,
            Omega_label, omega_label, MN, label
        )
        self.play(FadeOut(ALL))
        self.wait(0.7)


class Exercise_2(Scene):
    def construct(self):
        black_rectangle = Rectangle(height=1.2,width=20).shift(3.5*UP).set_color(BLACK).set_opacity(1).set_z_index(101)
        self.add(black_rectangle)

        Omega = Circle(color=BLUE, radius=2.5, arc_center=0.5*DOWN)
        Omega_label = Tex(r"$\mathrm{\Omega}$",font_size=35).move_to(1.7*RIGHT+1*UP)
        
        M = Dot(Omega.point_at_angle(0.9*PI)).set_z_index(9)
        N = Dot(Omega.point_at_angle(0.1*PI)).set_z_index(9)

        M_label = Tex("M", font_size=32).next_to(M.get_center(), np.array([-0.8,-0.6,0]), buff=0.12).set_z_index(9)
        N_label = Tex("N", font_size=32).next_to(N.get_center(), np.array([0.8,-0.6,0]), buff=0.12).set_z_index(9)

        MN = Line(M.get_center(), N.get_center(), color=GREEN)

        A = Dot(Omega.point_at_angle(0.65*PI)).set_z_index(9)
        B = Dot(intersection_lines(Bisector(M.get_center(), A.get_center(), N.get_center()), MN)).set_z_index(9)

        A_label = Tex("A", font_size=30).next_to(A.get_center(), UL, buff=0.1).set_z_index(9)
        B_label = Tex("B", font_size=30).next_to(B.get_center(), np.array([-0.1,-0.9,0]), buff=0.1).set_z_index(9)

        perpendicular_bisector_AB = PerpendicularBisector(A.get_center(), B.get_center())
        perpendicular_B = Perpendicular(Line(M.get_center(), N.get_center()), B.get_center())
        X = intersection_lines(perpendicular_bisector_AB, perpendicular_B)

        omega = Circle(radius=Line(X, B.get_center()).get_length(), arc_center=X, color=YELLOW)
        omega_label = Tex(r"$\mathrm{\omega}$",font_size=35).move_to(np.array([-0.35,1.45,0])).set_z_index(9)

        AB = Line(A.get_center(), B.get_center())

        L = Dot(intersection_line_and_circle(AB, Omega)[0]).set_z_index(1)
        L_label = Tex("L", font_size=30).next_to(L.get_center(), DOWN, buff=0.12)

        AL = Line(A.get_center(), L.get_center(), color=RED)
        LM = Line(L.get_center(), M.get_center(), color=YELLOW)
        LN = Line(L.get_center(), N.get_center(), color=YELLOW)

        label = Tex("Let's build a similar construction")
        self.play(Fancy_label(label))

        self.play(Create(Omega))
        self.play(FadeIn(Omega_label))
        self.play(LaggedStart(
            FadeIn(VGroup(M, M_label)),
            FadeIn(VGroup(N, N_label)),
            run_time=1, lag_ratio=0.8
        ))
        self.play(Create(MN))
        self.play(Create(omega))
        self.play(FadeIn(omega_label))
        self.play(LaggedStart(
            FadeIn(VGroup(A, A_label)),
            FadeIn(VGroup(B, B_label)),
            run_time=1, lag_ratio=0.8
        ))
        self.play(FadeOut(label))

        label = Tex("Let $L$ be the intersection point of $\Omega$ with $AB$")
        self.play(Fancy_label(label))
        self.play(FadeIn(VGroup(L, L_label)))
        self.play(FadeOut(label))

        label = Tex("Prove that $LM^2=LN^2=LB \cdot LA$")
        self.play(Fancy_label(label, mode='low'))
        self.play(omega.animate.set_stroke(opacity=0.4), omega_label.animate.set_opacity(0.4))
        self.play(LaggedStart(
            Create(AL),
            Create(LM),
            Create(LN),
            run_time=2.5, lag_ratio=0.85
        ))
        self.wait(2)
        
        ALL = VGroup(
            M, N, M_label, N_label, 
            A, B, A_label, B_label, 
            L, L_label, 
            Omega, omega, Omega_label, omega_label,
            AL, LM, LN, MN, label
        )
        self.play(FadeOut(ALL))
        self.wait(0.5)


class Definition(Scene):
    def construct(self):
        circle_1 = Circle(radius=1.8, arc_center=1.5*LEFT+DOWN, color=BLUE).set_z_index(-0.7)
        circle_2 = Circle(radius=2.2, arc_center=1.6*RIGHT+DOWN, color=BLUE).set_z_index(-0.7)

        A = Dot(intersection_circles(circle_1, circle_2)[0]).set_z_index(1)

        tangent_1 = Tangent(circle_1, A.get_center(), length=3, color=YELLOW)
        tangent_2 = Tangent(circle_2, A.get_center(), length=3, color=YELLOW)

        angle = Angle().from_three_points(
            tangent_1.get_start(), A.get_center(), tangent_2.get_end(), color=RED, radius=0.27)
        
        label = Tex("Let's define the angle between the circles")
        self.play(Fancy_label(label))
        self.play(Create(circle_1))
        self.play(Create(circle_2))
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex("Let's draw tangents to the intersection point of the circles", font_size=44)
        self.play(Fancy_label(label))
        self.play(FadeIn(A))
        self.play(LaggedStart(
            Create(tangent_1),
            Create(tangent_2),
            run_time=1.4, lag_ratio=0.85
        ))
        self.play(FadeOut(label))

        label = Tex("Then the angle between the circles is the angle between the tangents", font_size=42)
        self.play(Fancy_label(label))
        self.play(FadeIn(angle))
        self.play(FadeOut(label))

        label = Tex(r"Circles are perpendicular if the angle between them is $90^{\circ}$", font_size=44)
        self.play(Fancy_label(label))
        self.wait(1.5)
        self.play(FadeOut(VGroup(
            circle_1, circle_2, tangent_1, tangent_2, A, angle, label
        )))


class Lemma_1(Scene):
    def construct(self):
        black_rectangle = Rectangle(height=1.2,width=20).shift(3.5*UP).set_color(BLACK).set_opacity(1).set_z_index(101)
        self.add(black_rectangle)

        Omega = Circle(color=BLUE, radius=2.5, arc_center=0.5*DOWN)
        Omega_label = Tex(r"$\mathrm{\Omega}$",font_size=35).move_to(1.7*RIGHT+1*UP)
        
        M = Dot(Omega.point_at_angle(0.9*PI)).set_z_index(9)
        N = Dot(Omega.point_at_angle(0.1*PI)).set_z_index(9)

        M_label = Tex("M", font_size=32).next_to(M.get_center(), np.array([-0.8,0.2,0]), buff=0.12).set_z_index(9)
        N_label = Tex("N", font_size=32).next_to(N.get_center(), np.array([0.8,0.2,0]), buff=0.12).set_z_index(9)

        MN = Line(M.get_center(), N.get_center(), color=GREEN)

        A = Dot(Omega.point_at_angle(0.65*PI)).set_z_index(9)
        B = Dot(intersection_lines(Bisector(M.get_center(), A.get_center(), N.get_center()), MN)).set_z_index(9)

        A_label = Tex("A", font_size=30).next_to(A.get_center(), UL, buff=0.1).set_z_index(9)
        B_label = Tex("B", font_size=30).next_to(B.get_center(), np.array([-0.1,-0.9,0]), buff=0.1).set_z_index(9)

        perpendicular_bisector_AB = PerpendicularBisector(A.get_center(), B.get_center())
        perpendicular_B = Perpendicular(Line(M.get_center(), N.get_center()), B.get_center())
        X = intersection_lines(perpendicular_bisector_AB, perpendicular_B)

        omega = Circle(radius=Line(X, B.get_center()).get_length(), arc_center=X, color=YELLOW)
        omega_label = Tex(r"$\mathrm{\omega}$",font_size=35).move_to(np.array([-0.35,1.45,0])).set_z_index(9)

        AB = Line(A.get_center(), B.get_center())

        L = Dot(intersection_line_and_circle(AB, Omega)[0]).set_z_index(1)
        L_label = Tex("L", font_size=30).next_to(L.get_center(), DOWN, buff=0.12)

        omega_1 = Circle(radius=Line(L.get_center(), M.get_center()).get_length(), arc_center=L.get_center())
        omega_1_label = Tex(r"$\mathrm{\omega_1}$", font_size=34).move_to(3*RIGHT+0.7*DOWN)

        K = Dot(intersection_circles(omega, omega_1)[1]).set_z_index(1)
        K_label = Tex("K", font_size=30).next_to(K.get_center(), UL, buff=0.15)

        LK = Line(L.get_center(), K.get_center(), color=RED)
        omega_rad = Line(K.get_center(), omega.get_center(), color=RED)
        omega_rad_angle = Angle().from_three_points(
            omega.get_center(), K.get_center(), L.get_center(), elbow=True, color=YELLOW, radius=0.25)
        omega_center = Dot(omega.get_center())


        label = Tex(r"Let's restore the construction from the recent exercise", font_size=46)
        self.play(Fancy_label(label))

        self.play(FadeIn(VGroup(
            A, B, A_label, B_label, 
            M, N, M_label, N_label, 
            Omega, omega, Omega_label, omega_label, 
            L, L_label, MN
        )))
        self.play(FadeOut(label))

        label = Tex("Let's construct a circle $\omega_1$ with center in $L$ and radius $LM$", font_size=46)
        self.play(Fancy_label(label))
        self.wait(0.1)
        self.play(Create(omega_1))
        self.play(FadeIn(omega_1_label))
        self.play(FadeOut(label))

        label = Tex("We need to prove that then the circles $\omega$ and $\omega_1$ are perpendicular", font_size=44)
        self.play(Fancy_label(label))
        self.wait()
        self.play(FadeOut(label))

        label = Tex("Let $K$ be the intersection point of $\omega$ and $\omega_1$")
        self.play(Fancy_label(label))
        self.play(FadeIn(VGroup(K, K_label)))
        self.wait(0.3)
        self.play(FadeOut(label))

        label = Tex("$LM = LK = LB \cdot LA$ as the radii of the circle")
        self.play(Fancy_label(label))
        self.wait()
        self.play(FadeOut(label))

        label = Tex("So by the tangent and secant theorem - $LK$ is a tangent")
        self.play(Fancy_label(label))
        self.play(VGroup(omega_1, omega).animate.set_stroke(opacity=0.3), run_time=0.6)
        self.play(Create(LK))
        self.play(Create(omega_rad), FadeIn(omega_rad_angle), FadeIn(omega_center))
        self.play(FadeOut(label))

        label = Tex("So $\omega$ and $\omega_1$ are perpendicular")
        self.play(Fancy_label(label))
        self.wait(2)

        ALL = VGroup(
            M, N, M_label, N_label, 
            A, B, A_label, B_label, 
            L, L_label, 
            Omega, omega, Omega_label, omega_label,
            omega_1, omega_1_label, LK,
            omega_rad, omega_rad_angle, omega_center,
            K, K_label, MN, label
        )
        self.play(FadeOut(ALL))
        self.wait(0.3)



    

  
        
        
        self.wait(3)

        
class Lemma_2(Scene):
    def construct(self):
        black_rectangle = Rectangle(height=1.2,width=20).shift(3.5*UP).set_color(BLACK).set_opacity(1).set_z_index(101)
        self.add(black_rectangle)

        omega_1 = Circle(radius=1.35, color=BLUE, arc_center=1.2*LEFT+0.5*UP)
        omega_2 = Circle(radius=1.75, color=BLUE, arc_center=1.35*RIGHT+0.5*UP)

        omega_1_label = Tex(r"$\mathrm{\omega_1}$", font_size=32).move_to(2.05*LEFT+1.2*UP).set_z_index(1)
        omega_2_label = Tex(r"$\mathrm{\omega_2}$", font_size=32).move_to(2.7*RIGHT+UP).set_z_index(1)

        O_1 = Dot(omega_1.get_center()).set_z_index(1)
        O_2 = Dot(omega_2.get_center()).set_z_index(1)

        O_1_label = Tex(r"$\mathrm{O_1}$", font_size=30).next_to(O_1.get_center(), LEFT, buff=0.15).set_z_index(1)
        O_2_label = Tex(r"$\mathrm{O_2}$", font_size=30).next_to(O_2.get_center(), RIGHT, buff=0.15).set_z_index(1)
        
        A = Dot(intersection_circles(omega_1, omega_2)[0]).set_z_index(1)
        B = Dot(intersection_circles(omega_1, omega_2)[1]).set_z_index(1)
        C = Dot(omega_1.point_at_angle(-0.7*PI)).set_z_index(1)
        
        A_label = Tex("A", font_size=30).next_to(A.get_center(), np.array([0.95, 0.05, 0]), buff=0.15).set_z_index(1)
        B_label = Tex("B", font_size=30).next_to(B.get_center(), np.array([-0.9, 0.3, 0]), buff=0.15).set_z_index(1)
        C_label = Tex("C", font_size=30).next_to(C.get_center(), LEFT, buff=0.17).set_z_index(1)
        
        AB = Line(A.get_center(), B.get_center(), color=GREEN).set_length(10).set_opacity(0.6)

        tangent_1 = Tangent(omega_1, C.get_center())

        O_3 = Dot(intersection_lines(tangent_1, AB)).set_z_index(1)
        O_3_label = Tex(r"$\mathrm{O_3}$", font_size=30).next_to(O_3.get_center(), np.array([0.9, -0.3, 0]), buff=0.15).set_z_index(1)

        omega_3 = Circle(radius=Line(O_3.get_center(), C.get_center()).get_length(), arc_center=O_3.get_center())
        omega_3_label = Tex("$\mathrm{\omega_3}$", font_size=30).move_to(1.7*DOWN+1.75*RIGHT).set_z_index(1)

        D = Dot(intersection_circles(omega_2, omega_3)[0]).set_z_index(1)
        D_label = Tex("D", font_size=30).next_to(D.get_center(), np.array([0.8, -0.3, 0]), buff=0.15).set_z_index(1)

        CO_3 = Line(O_3.get_center(), C.get_center(), color=YELLOW)
        DO_3 = Line(O_3.get_center(), D.get_center(), color=YELLOW)

        O_1C = Line(O_1.get_center(), C.get_center(), color=YELLOW)
        O_2D = Line(O_2.get_center(), D.get_center(), color=YELLOW)

        omega_1_angle = Angle().from_three_points(
            O_1.get_center(), C.get_center(), O_3.get_center(), elbow=True, color=YELLOW, radius=0.2
        )
        omega_2_angle = Angle().from_three_points(
            O_2.get_center(), D.get_center(), O_3.get_center(), elbow=True, color=YELLOW, radius=0.2
        )

        self.play(Create(omega_1))
        self.play(FadeIn(VGroup(omega_1_label, O_1, O_1_label)), run_time=0.75)
        self.play(Create(omega_2))
        self.play(FadeIn(VGroup(omega_2_label, O_2, O_2_label)), run_time=0.75)

        label = Tex("$A$ and $B$ are the intersection points of the circles $\omega_1$ and $\omega_2$")
        self.play(Fancy_label(label))
        self.play(LaggedStart(
            FadeIn(VGroup(A, A_label)),
            FadeIn(VGroup(B, B_label)),
            run_time=1, lag_ratio=0.75
        ))
        self.play(FadeOut(label))

        label = Tex("Let's construct a circle $\omega_3$ centered on a line $AB$")
        self.play(Fancy_label(label))
        self.play(Create(AB))
        self.play(Create(omega_3))
        self.play(FadeIn(VGroup(omega_3_label, O_3, O_3_label)), run_time=0.75)
        self.play(FadeOut(label))

        label = Tex("If $\omega_3$ is perpendicular to $\omega_1$, then $\omega_3$ is perpendicular to $\omega_2$", font_size=44)
        self.play(Fancy_label(label))
        self.play(LaggedStart(
             Create(O_1C),
             Create(CO_3),
             FadeIn(VGroup(C, C_label)),
             run_time=1.5, lag_ratio=0.9
        ))
        self.play(FadeIn(omega_1_angle))
        self.play(LaggedStart(
             Create(O_2D),
             Create(DO_3),
             FadeIn(VGroup(D, D_label)),
             run_time=1.5, lag_ratio=0.9
        ))
        self.play(FadeIn(omega_2_angle))
        self.play(FadeOut(label), FadeOut(omega_2_angle))
        omega_2_angle.set_stroke(opacity=0)
        self.add(omega_2_angle)
        
        ALL = VGroup(
            omega_1, omega_2, omega_3, 
            omega_1_label, omega_2_label, omega_3_label,
            A, B, C, D,  
            A_label, B_label, C_label, D_label,  
            O_1C, CO_3, O_2D, DO_3, 
            omega_1_angle, omega_2_angle, AB,
            O_1, O_2, O_1_label, O_2_label, 
            O_3, O_3_label,
        )
        self.play(ALL.animate.shift(2.25*LEFT))

        label = Tex("By the Pythagorean theorem $O_1O_3^2 - O_1C^2 = O_3C^2$")
        self.play(Fancy_label(label, mode='low'))
        info_1 = Tex("$\mathrm{O_1O_3^2 - O_1C^2 = O_3C^2}$", 
                     font_size=40).move_to(0.5*UP+4.2*RIGHT).set_opacity(0.75)
        self.play(FadeIn(info_1))
        self.wait(2)
        self.play(FadeOut(label))


        label = Tex("$AB$ is the radical axis of the circles $\omega_1$ and $\omega_2$")
        self.play(Fancy_label(label))
        self.wait(1.5)
        self.play(FadeOut(label))

        label = Tex("So $O_1O_3^2 - O_1C^2 = O_2O_3^2 - O_2D^2$")
        self.play(Fancy_label(label, mode='low'))
        info_2 = Tex("$\mathrm{O_1O_3^2 - O_1C^2 = O_2O_3^2 - O_2D^2}$", 
                     font_size=40).move_to(4.2*RIGHT).set_opacity(0.75)
        self.play(FadeIn(info_2))
        self.wait(2.5)
        self.play(FadeOut(label))

        label = Tex("Substitute this in the previous expression")
        self.play(Fancy_label(label))
        info_3 = VGroup(info_1, info_2)
        self.wait()
        self.play(Transform(info_3, 
            Tex("$\mathrm{O_3C^2 = O_2O_3^2 - O_2D^2}$", 
                font_size=40).move_to(0.25*UP+4.2*RIGHT).set_opacity(0.75)))
        self.wait()
        self.play(FadeOut(label))

        label = Tex("But also $O_3C=O_3D$ as radii")
        self.play(Fancy_label(label))
        info_4 = Tex("$O_3C=O_3D$", 
                     font_size=40).move_to(0.25*DOWN+4.2*RIGHT).set_opacity(0.75)
        self.play(FadeIn(info_4))
        self.wait(2)
        info_5 = VGroup(info_3, info_4)
        self.play(Transform(info_5,
                Tex("$\mathrm{O_3D^2 = O_2O_3^2 - O_2D^2}$", 
                    font_size=40).move_to(4.2*RIGHT).set_opacity(0.75) ))
        self.play(FadeOut(label))

        label = Tex(r"So by the inverse Pythagorean theorem $\angle{O_3DO_2} = 90^{\circ}$")
        self.play(Fancy_label(label))
        self.play(omega_2_angle.animate.set_stroke(opacity=1))
        self.wait(1.5)
        self.play(FadeOut(label))

        label = Tex("The converse statement is also true")
        self.play(Fancy_label(label))
        self.wait()
        ALL = VGroup(ALL, info_5, label)
        self.play(FadeOut(ALL))




        self.wait(3)

        
class Archimedes_criteria(Scene):
    def construct(self):
        black_rectangle = Rectangle(height=1.2,width=20).shift(3.5*UP).set_color(BLACK).set_opacity(1).set_z_index(101)
        self.add(black_rectangle)

        Omega = Circle(radius=2, arc_center=0.1*UP, color=BLUE)
        Omega_label = Tex(r"$\mathrm{\Omega}$", font_size=34).move_to(1.35*UP+1.3*RIGHT)
        
        M = Dot(Omega.point_at_angle(0.9*PI)).set_z_index(1)
        N = Dot(Omega.point_at_angle(0.1*PI)).set_z_index(1)
        L = Dot(Omega.point_at_angle(-0.5*PI)).set_z_index(1)

        M_label = Tex("M", font_size=32).next_to(M.get_center(), np.array([-0.9, 0.1, 0]), buff=0.13).set_z_index(1)
        N_label = Tex("N", font_size=32).next_to(N.get_center(), np.array([0.9, 0.1, 0]), buff=0.13).set_z_index(1)
        L_label = Tex("L", font_size=32).next_to(L.get_center(), DOWN, buff=0.13).set_z_index(1)

        MN = Line(M.get_center(), N.get_center(), color=GREEN)

        A = Dot(Omega.point_at_angle(0.7*PI)).set_z_index(1)
        B = Dot(intersection_lines(
            Bisector(M.get_center(), A.get_center(), N.get_center()),
            MN)).set_z_index(1)
        
        A_label = Tex("A", font_size=32).next_to(A.get_center(), UL, buff=0.11).set_z_index(1)
        B_label = Tex("B", font_size=32).next_to(B.get_center(), DOWN, buff=0.13).set_z_index(1)

        perpendicular_bisector_AB = PerpendicularBisector(A.get_center(), B.get_center())
        perpendicular_B = Perpendicular(Line(M.get_center(), N.get_center()), B.get_center())
        X = intersection_lines(perpendicular_bisector_AB, perpendicular_B)

        omega = Circle(radius=Line(X, B.get_center()).get_length(), arc_center=X)
        omega_fake = omega.copy().scale(0.9).shift(0.1*omega.radius*DOWN+0.15*RIGHT)
        omega_label = Tex(r"$\mathrm{\omega}$",font_size=34).move_to(np.array([-0.55,1.5,0])).set_z_index(9)

        omega_1 = Circle(radius=Line(L.get_center(), M.get_center()).get_length(), 
                         arc_center=L.get_center(), color=GREEN).set_stroke(opacity=0.7)
        omega_1_label = Tex(r"$\mathrm{\omega_1}$",font_size=34).move_to(2.9*RIGHT+DOWN)

        omega_extra = omega.copy().set_stroke(color=YELLOW)
        omega_extra_label = Tex(r"$\mathrm{\omega'}$",font_size=30).move_to(np.array([-1.16,1.55,0])).set_z_index(9)

        C = Dot(intersection_circles(omega_extra, omega_fake)[0])
        C_label = Tex("C", font_size=28).next_to(C.get_center(), np.array([0.7, 0.4, 0]), buff=0.09)

        label = Tex("Let's discuss the criteria of touching two circles - Archimedes criteria", font_size=42)
        self.play(Fancy_label(label))
        self.wait(0.15)

        self.play(Create(Omega))
        self.play(FadeIn(Omega_label), run_time=0.75)
        self.wait(0.1)
        self.play(LaggedStart(
            FadeIn(VGroup(M, M_label)),
            FadeIn(VGroup(N, N_label)),
            run_time=1.2, lag_ratio=0.75
        ))
        self.play(Create(MN))
        self.play(FadeOut(label))

        label = Tex(r"Circle $\omega$ touches $MN$ at point $B$")
        self.play(Fancy_label(label))
        omega_label.shift(0.1*omega.radius*DOWN+0.1*RIGHT)
        omega_now = omega_fake.copy()
        self.play(Create(omega_now))
        self.play(FadeIn(omega_label), run_time=0.75)
        self.play(FadeIn(VGroup(B, B_label)), run_time=0.75)
        self.wait(0.1)
        self.play(FadeOut(label))

        label = Tex("Point $L$ is the middle of the $MN$ arc")
        self.play(Fancy_label(label))
        self.play(FadeIn(VGroup(L, L_label)))
        self.wait(0.15)
        self.play(FadeOut(label))

        label = Tex("Let's construct a circle $\omega_1$ with center in $L$ and radius $LM$", font_size=44)
        self.play(Fancy_label(label))
        self.play(Create(omega_1))
        self.play(FadeIn(omega_1_label), run_time=0.75)
        self.play(FadeOut(label))

        label = Tex("If $\omega$ and $\omega_1$ are perpendicular, then $\omega$ and $\Omega$ touch")
        self.play(Fancy_label(label))
        self.play(Transform(omega_now, omega), omega_label.animate.shift(0.25*omega.radius*UP+0.15*LEFT))
        self.wait()
        self.play(FadeOut(label))

        label = Tex("To prove it, let them not touch")
        self.play(Fancy_label(label))
        self.play(Transform(omega_now, omega_fake.copy()), 
                  omega_label.animate.shift(0.13*omega.radius*DOWN+0.1*RIGHT))
        self.wait(0.4)
        self.play(FadeOut(label))

        label = Tex("Then let's build a circle $\omega'$")
        self.play(Fancy_label(label))
        self.play(omega_now.animate.set_stroke(opacity=0.4), omega_label.animate.set_opacity(0.4), run_time=0.75)
        self.play(Create(omega_extra))
        self.play(FadeIn(omega_extra_label), run_time=0.75)
        self.play(FadeOut(label))

        label = Tex("$\omega'$ touches the line MN at point $B$, and the circle $\Omega$ at $A$", font_size=44)
        self.play(Fancy_label(label))
        self.play(FadeIn(VGroup(A, A_label)))     
        self.wait()
        self.play(FadeOut(label))

        label = Tex("Recently we have already proved that $\omega_1$ and $\omega'$ are perpendicular", font_size=42)  
        self.play(Fancy_label(label))
        self.wait(1.5)
        self.play(FadeOut(label))

        label = Tex("It turns out that $\omega_1$ is perpendicular to both $\omega$ and $\omega'$", font_size=40)  
        self.play(Fancy_label(label))
        self.wait(1.5)
        self.play(FadeOut(label))

        label = Tex("Let $\omega'$ and $\omega$ intersect at point $C$")
        self.play(Fancy_label(label))
        self.play(FadeIn(VGroup(C, C_label)))
        self.wait(0.5)
        self.play(FadeOut(label))

        label = Tex("So $C, B, L$ must be on the same line")
        self.play(Fancy_label(label))
        self.wait(1.5)
        self.play(FadeOut(label))

        label = Tex("But according to Archimedes' lemma, $A, B, L$ are on the same line", font_size=42)
        self.play(Fancy_label(label))
        self.wait(1.5)
        self.play(FadeOut(label))

        label = Tex("This means that the points $C$ and $A$ coincide")
        self.play(Fancy_label(label))
        self.play(Transform(omega_now, omega_extra.copy().set_stroke(color=RED)), 
                  omega_label.animate.shift(0.15*LEFT+0.05*UP), FadeOut(omega_extra_label),
                  FadeOut(VGroup(C, C_label)), FadeOut(omega_extra), omega_label.animate.set_opacity(1).shift(0.05*LEFT))
        self.wait(0.3)
        self.play(FadeOut(label))

        label = Tex("So the circle $\omega$ touches the circle $\Omega$")
        self.play(Fancy_label(label))
        self.wait(2)
        ALL = VGroup(
            Omega, omega_now, omega_1, Omega_label, omega_1_label,
            A, B, M, N, A_label, B_label, M_label, N_label, 
            label, MN, omega_label, L, L_label
        )
        self.play(FadeOut(ALL))
        self.wait()


class External_archimedes_criteria(Scene):
    def construct(self):
        A = Dot(LEFT)
        B = Dot(5*UP+3*LEFT)
        C = Dot(1.7*RIGHT)

        Omega = EulerCircle(A.get_center(), B.get_center(), C.get_center(), color=BLUE)
        omega = EscribedCircle(A.get_center(), B.get_center(), C.get_center(), color=RED)
    
        H_b = Dot(Altitude(A.get_center(), B.get_center(), C.get_center()).get_base()).set_z_index(1)
        M_b = Dot(Median(A.get_center(), B.get_center(), C.get_center()).get_base()).set_z_index(1)

        L = Dot(Omega.point_at_angle(-0.5*PI)).set_z_index(1)
        L_label = Tex("L", font_size=30).next_to(L.get_center(), DOWN, buff=0.12).set_z_index(1)

        omega_1 = Circle(
            arc_center=Omega.point_at_angle(-0.5*PI),
            radius = Line(Omega.point_at_angle(-0.5*PI),
                          Line(A.get_center(), C.get_center()).get_center()).get_length(), 
            color=YELLOW
        )
        line = Line(H_b.get_center(), M_b.get_center(), color=GREEN).set_opacity(0.6).set_length(30)

        H_b_label = Tex("N", font_size=30).next_to(H_b.get_center(), np.array([-0.9, 0.4, 0]), buff=0.15).set_z_index(1)
        M_b_label = Tex("M", font_size=30).next_to(M_b.get_center(), np.array([0.9, 0.4, 0]), buff=0.15).set_z_index(1)

        Omega_label = Tex("$\mathrm{\Omega}$", font_size=30).move_to(2.85*LEFT+1.5*UP)
        omega_label = Tex("$\mathrm{\omega}$", font_size=30).move_to(1.9*RIGHT+0.5*DOWN)
        omega_1_label = Tex("$\mathrm{\omega_1}$", font_size=30).move_to(3.05*LEFT+1*DOWN)

        label = Tex("Prove the criteria for external touch yourself")
        self.play(Fancy_label(label))


        self.play(Create(Omega), FadeIn(Omega_label))
        self.play(LaggedStart(
            FadeIn(VGroup(H_b, H_b_label)),
            FadeIn(VGroup(M_b, M_b_label)),
            run_time=1, lag_ratio=0.7
        ))
        
        self.play(FadeIn(line))
        self.play(FadeIn(VGroup(L, L_label)))
        self.play(Create(omega_1), FadeIn(omega_1_label))
        self.play(Create(omega), FadeIn(omega_label))

        self.wait(2.5)

        ALL = VGroup(
            Omega, omega, omega_1, Omega_label, omega_label, omega_1_label,
            M_b, H_b, L, M_b_label, H_b_label, L_label, 
            line, label
        )
        self.play(FadeOut(ALL))


class Feuerbach(Scene):
    def construct(self):
        black_rectangle = Rectangle(height=1.15,width=20).shift(3.5*UP).set_color(BLACK).set_opacity(1).set_z_index(101)
        self.add(black_rectangle)

        A = Dot(2.2*LEFT+0.5*DOWN).set_z_index(1)
        B = Dot(2.8*LEFT+2.5*UP).set_z_index(1)
        C = Dot(2.2*RIGHT+0.5*DOWN).set_z_index(1)

        A_label = Tex("A", font_size=32).next_to(A.get_center(), np.array([-0.2, -0.9, 0]), buff=0.14).set_z_index(1)
        B_label = Tex("B", font_size=32).next_to(B.get_center(), UP, buff=0.12).set_z_index(1)
        C_label = Tex("C", font_size=32).next_to(C.get_center(), DOWN, buff=0.14).set_z_index(1)

        a = Line(B.get_center(), C.get_center(), color=BLUE)
        b = Line(C.get_center(), A.get_center(), color=BLUE)
        c = Line(A.get_center(), B.get_center(), color=BLUE)

        AC_line = Line(A.get_center(), C.get_center(), color=BLUE).set_opacity(0.4).set_length(20)
        BC_line = Line(B.get_center(), C.get_center(), color=BLUE).set_opacity(0.4).set_length(20)
        BA_line = Line(A.get_center(), B.get_center(), color=BLUE).set_opacity(0.4).set_length(20)

        B_bisector = Bisector(A.get_center(), B.get_center(), C.get_center(), color=GREEN).set_length_about_point(
            B.get_center(), length=15
        )

        BH_b = Perpendicular(b, B.get_center(), color=GREEN)
        H_b = Dot(AC_line.get_projection(B.get_center())).set_z_index(1)
        H_b_label = Tex(r"$\mathrm{H_b}$", font_size=28).next_to(H_b.get_center(), DOWN, buff=0.12).set_z_index(1)
        H_b_angle = BH_b.angles(color=YELLOW, radius=0.18)[0]

        M_b = Dot(b.get_center()).set_z_index(1)
        M_b_label = Tex(r"$\mathrm{M_b}$", font_size=28).next_to(M_b.get_center(), DOWN, buff=0.12).set_z_index(1)

        I = Dot(InscribedCircle(A.get_center(), B.get_center(), C.get_center()).get_center()).set_z_index(1)
        I_label = Tex("I", font_size=28).next_to(I.get_center(), np.array([0.4, 0.9, 0]), buff=0.12).set_z_index(1)

        I_b = Dot(EscribedCircle(A.get_center(), B.get_center(), C.get_center()).get_center()).set_z_index(1)
        I_b_label = Tex(r"$\mathrm{I_b}$", font_size=28).next_to(I_b.get_center(), UR, buff=0.12).set_z_index(1)

        AH_a = Perpendicular(B_bisector, A.get_center(), color=RED)
        CH_c = Perpendicular(B_bisector, C.get_center(), color=RED)
        
        H_a = Dot(AH_a.get_base()).set_z_index(1)
        H_c = Dot(CH_c.get_base()).set_z_index(1)

        H_a_label = Tex(r"$\mathrm{H_a}$", font_size=28).next_to(H_a.get_center(), UR, buff=0.09).set_z_index(1)
        H_c_label = Tex(r"$\mathrm{H_c}$", font_size=28).next_to(H_c.get_center(), DL, buff=0.09).set_z_index(1)

        H_a_angle = AH_a.angles(radius=0.18, color=YELLOW)[0]
        H_c_angle = CH_c.angles(radius=0.18, color=YELLOW)[0]

        incircle = InscribedCircle(A.get_center(), B.get_center(), C.get_center(), color=YELLOW)
        excircle_B = EscribedCircle(A.get_center(), B.get_center(), C.get_center(), color=YELLOW)
        euler_circle = EulerCircle(A.get_center(), B.get_center(), C.get_center(), color=RED)

        incircle_label = Tex(r"$\mathrm{\omega}$", font_size=30).move_to(I.get_center()+0.8*RIGHT+0.3*UP)
        excircle_B_label = Tex(r"$\mathrm{\omega_b}$", font_size=30).move_to(I_b.get_center()+1.8*RIGHT+2*UP)
        euler_circle_label = Tex(r"$\mathrm{\Omega}$", font_size=30).move_to(
            euler_circle.get_center()+1.25*LEFT+0.5*UP)

        excircle_A = EscribedCircle(B.get_center(), A.get_center(), C.get_center(), color=YELLOW)
        excircle_C = EscribedCircle(A.get_center(), C.get_center(), B.get_center(), color=YELLOW)

        arc_A = Arc(
            radius=excircle_A.radius,
            arc_center=excircle_A.get_center(),
            start_angle=-0.3*PI, 
            angle=-PI, 
            color=YELLOW
        )

        X = Dot(intersection_line_and_circle(b, incircle)[0]).set_z_index(1)
        Y = Dot(intersection_line_and_circle(b, excircle_B)[0]).set_z_index(1)

        X_label = Tex("X", font_size=28).next_to(X.get_center(), DOWN, buff=0.12).set_z_index(1)
        Y_label = Tex("Y", font_size=28).next_to(Y.get_center(), UP, buff=0.12).set_z_index(1)

        feuerbach_point = Dot(intersection_circles(euler_circle, incircle)[0])
        feuerbach_point_A = Dot(intersection_circles(euler_circle, excircle_A)[0])
        feuerbach_point_B = Dot(intersection_circles(euler_circle, excircle_B)[0])
        feuerbach_point_C = Dot(intersection_circles(euler_circle, excircle_C)[0])
        
        L = Dot(intersection_line_and_circle(
            PerpendicularBisector(H_b.get_center(), M_b.get_center()), euler_circle)[1])
        L_label = Tex("L", font_size=30).next_to(L.get_center(), DOWN, buff=0.12)

        omega_1 = Circle(arc_center=L.get_center(), 
                    radius=Line(L.get_center(), M_b.get_center()).get_length(), color=GREEN_D).set_stroke(opacity=0.9)
        omega_1_label = Tex(r"$\mathrm{\omega_1}$", font_size=30).move_to(1.4*DOWN+2.85*LEFT)

        omega_2 = Circle(arc_center=M_b.get_center(), 
                    radius=Line(M_b.get_center(), X.get_center()).get_length(), color=GREEN_D).set_stroke(opacity=0.95)
        omega_2_label = Tex(r"$\mathrm{\omega_2}$", font_size=30).move_to(0.75*RIGHT+0.45*UP)

        ALL = VGroup(
            A, B, C, A_label, B_label, C_label, 
            a, b, c, 
            BH_b, H_b, H_b_label, 
            M_b, M_b_label,
            AH_a, CH_c, H_a, H_c, H_a_label, H_c_label, 
            I, I_b, I_label, I_b_label,
            X, Y, X_label, Y_label, incircle, excircle_B, euler_circle, 
            AC_line, B_bisector, excircle_B, BA_line, BC_line,
            omega_1, omega_2, omega_1_label, omega_2_label,
            H_b_angle, H_a_angle, H_c_angle, L, L_label, 
            euler_circle_label, incircle_label, excircle_B_label
        )

        label = Tex("And now the culmination is Feuerbach's theorem")
        self.play(Fancy_label(label))
        self.wait()
        self.play(FadeOut(label))

        label = Tex("Let me remind you of the condition of the theorem")
        self.play(Fancy_label(label))
        self.play(LaggedStart(
            Create(a),
            Create(b),
            Create(c),
            run_time=2.5, lag_ratio=0.85
        ))
        self.play(Create(incircle))
        self.play(FadeIn(VGroup(AC_line, BA_line, BC_line)))
        self.play(Create(arc_A), run_time=1.5)
        self.play(Create(excircle_B), run_time=1)
        self.play(Create(excircle_C), run_time=1)
        self.play(Create(euler_circle))
        self.play(FadeOut(label))

        label = Tex("Euler's circle touches inscribed and all escribed circles", font_size=46)
        self.play(Fancy_label(label))
        self.play(LaggedStart(
            FadeIn(feuerbach_point),
            FadeIn(feuerbach_point_A),
            FadeIn(feuerbach_point_B),
            FadeIn(feuerbach_point_C),
            run_time=1.5, lag_ratio=0.6
        ))
        self.wait(1.5)
        self.play(FadeOut(label), FadeOut(VGroup(
            feuerbach_point,
            feuerbach_point_A,
            feuerbach_point_B,
            feuerbach_point_C,
        )))

        label = Tex("During the proof, we will consider only one escribed circles", font_size=44)
        self.play(Fancy_label(label))
        self.play(FadeOut(VGroup(arc_A, excircle_C)))
        self.wait(0.5)
        self.play(FadeOut(label))

        label = Tex("Let's denote the inscribed and escribed circle as $\omega$ and $\omega_b$", font_size=44)
        self.play(Fancy_label(label))
        self.play(FadeIn(incircle_label))
        self.play(FadeIn(excircle_B_label))
        self.play(FadeOut(label))

        label = Tex("And the Euler's circle is denoted as $\Omega$")
        self.play(Fancy_label(label))
        self.play(FadeIn(euler_circle_label))
        self.play(FadeOut(label))

        self.play(VGroup(euler_circle, incircle, excircle_B).animate.set_stroke(opacity=0.35))
        self.play(LaggedStart(
            FadeIn(VGroup(A, A_label)),
            FadeIn(VGroup(B, B_label)),
            FadeIn(VGroup(C, C_label)),
            run_time=1.5, lag_ratio=0.75
        ))

        label = Tex("Let's draw the altitude $BH_b$")
        self.play(Fancy_label(label))
        self.play(Create(BH_b))
        self.play(FadeIn(VGroup(H_b, H_b_label, H_b_angle)))
        self.wait(0.2)
        self.play(BH_b.animate.set_opacity(0.4),
                  H_b_angle.animate.set_stroke(opacity=0.4))
        self.play(FadeOut(label))

        label = Tex("Note the middle of $AC$")
        self.play(Fancy_label(label))
        self.play(FadeIn(VGroup(M_b, M_b_label)))
        M_b_equals = VGroup(
            Line(A.get_center(), M_b.get_center()).equal(),
            Line(C.get_center(), M_b.get_center()).equal(),
        )
        self.play(FadeIn(M_b_equals))
        self.wait(0.75)
        self.play(FadeOut(M_b_equals))
        self.play(FadeOut(label))

        label = Tex(r"Let's draw the bisector of the angle $\angle{B}$")
        self.play(Fancy_label(label))
        self.play(Create(B_bisector))
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex("Now we lower the perpendiculars $AH_a$ and $CH_c$ onto this bisector", font_size=44)
        self.play(Fancy_label(label))
        self.play(Create(AH_a))
        self.play(FadeIn(VGroup(H_a, H_a_label, H_a_angle)))
        self.play(Create(CH_c))
        self.play(FadeIn(VGroup(H_c, H_c_label, H_c_angle)))
        self.wait(0.3)
        self.play(
            VGroup(AH_a, CH_c).animate.set_opacity(0.4),
            VGroup(H_a_angle, H_c_angle).animate.set_stroke(opacity=0.5)
        )
        self.play(FadeOut(label))
    
        label = Tex("Note the centers of the inscribed and escribed circles")
        self.play(Fancy_label(label))
        self.play(FadeIn(VGroup(I, I_label)), run_time=0.75)
        self.play(FadeIn(VGroup(I_b, I_b_label)), run_time=0.75)
        self.play(FadeOut(label))

        label = Tex("$X$ and $Y$ are tangent points of the inscribed and escribed circles with $AC$", font_size=40)
        self.play(Fancy_label(label))
        self.play(FadeIn(VGroup(X, X_label)))
        self.play(FadeIn(VGroup(Y, Y_label)))
        self.play(FadeOut(label))

        label = Tex("Let $L$ be the center of the arc $H_bM_b$ of the Euler's circle")
        self.play(Fancy_label(label))
        self.play(FadeIn(VGroup(L, L_label)))
        self.wait()
        self.play(FadeOut(label))

        label = Tex("Let's construct a circle $\omega_1$ with center in $L$ and radius $LM_b$")
        self.play(Fancy_label(label))
        self.play(VGroup(
            euler_circle_label, incircle_label,
            X_label, Y_label, 
            I_label, I_b_label, 
            excircle_B_label,
            X, Y, 
            I, I_b, 
            ).animate.set_opacity(0.5),
            B_bisector.animate.set_opacity(0.4))
        self.play(Create(omega_1))
        self.play(FadeIn(omega_1_label))
        self.play(FadeOut(label))

        label = Tex("Then on this circle there are also $H_b, M_b, H_a, H_c$", font_size=44)
        self.play(Fancy_label(label))
        self.wait(1.5)
        self.play(FadeOut(label))

        label = Tex("Construct a circle $\omega_2$ with the center $M_b$ and the radius $M_bX$", font_size=42)
        self.play(Fancy_label(label))
        self.play(
            omega_1.animate.set_stroke(opacity=0.3),
            omega_1_label.animate.set_opacity(0.5),
            VGroup(H_b, M_b, H_b_label, M_b_label, L, L_label).animate.set_opacity(0.5),
            VGroup(X, Y, X_label, Y_label).animate.set_opacity(1)
        )
        self.play(Create(omega_2))
        self.play(FadeIn(omega_2_label))
        self.play(FadeOut(label))

        label = Tex("On this circle are $X, Y, H_a, H_c$")
        self.play(Fancy_label(label))
        self.wait()
        self.play(VGroup(
            X, Y, X_label, Y_label, M_b, M_b_label, H_a, H_c, H_a_label, H_c_label).animate.set_opacity(0.5),
            omega_2.animate.set_stroke(opacity=0.4),
            omega_2_label.animate.set_opacity(0.5))
        self.play(FadeOut(label))

        label = Tex(r"$\angle{IXA}=90^{\circ}$, which means the circles $\omega$ and $\omega_2$ are perpendicular", font_size=44)
        self.play(Fancy_label(label))
        IX = Line(I.get_center(), X.get_center(), color=RED).set_z_index(-1)
        angle_IXA = Angle().from_three_points(
            I.get_center(), X.get_center(), A.get_center(), elbow=True, radius=0.2, color=YELLOW).set_z_index(0.1)
        self.play(VGroup(X, I).animate.set_opacity(1))
        self.play(Create(IX))
        self.play(FadeIn(angle_IXA))
        self.play(VGroup(incircle, omega_2).animate.set_stroke(opacity=1), 
                  VGroup(incircle_label, omega_2_label).animate.set_opacity(1))
        self.play(FadeOut(label))

        label = Tex("$I$ is on the line $H_aH_c$, so $\omega$ and $\omega_1$ are also perpendicular", font_size=46)
        self.play(Fancy_label(label))
        self.play(omega_2.animate.set_stroke(opacity=0.4), 
                  omega_1.animate.set_stroke(opacity=1),
                  omega_2_label.animate.set_opacity(0.4),
                  omega_1_label.animate.set_opacity(1),
                  VGroup(X, I).animate.set_opacity(0.4))
        self.play(FadeOut(VGroup(IX, angle_IXA)))
        self.play(FadeOut(label))

        label = Tex("And then, according to Archimedes' criteria, $\omega$ and $\Omega$ touch", font_size=46)
        self.play(Fancy_label(label))
        self.play(omega_1.animate.set_stroke(opacity=0.4),
                  omega_1_label.animate.set_opacity(0.5),
                  euler_circle.animate.set_stroke(opacity=1),
                  euler_circle_label.animate.set_opacity(1))
        self.play(FadeIn(feuerbach_point))
        self.wait(1.5)
        self.play(FadeOut(label))
        self.play(
            VGroup(euler_circle, incircle).animate.set_stroke(opacity=0.4),
            VGroup(euler_circle_label, incircle_label).animate.set_opacity(0.5),
            FadeOut(feuerbach_point))
        
        label = Tex(r"$\angle{I_bYA} = 90^{\circ}$ so $\omega_b$ and $\omega_2$ are perpendicular", font_size=46)
        self.play(Fancy_label(label))
        I_bY = Line(I_b.get_center(), Y.get_center(), color=RED)
        angle_I_bYA = Angle().from_three_points(I_b.get_center(), Y.get_center(), A.get_center(),
                                                elbow=True, color=YELLOW, radius=0.2)
        self.play(VGroup(Y, I_b, Y_label, I_b_label).animate.set_opacity(1))
        self.play(Create(I_bY))
        self.play(FadeIn(angle_I_bYA))
        self.play(
            VGroup(excircle_B, omega_2).animate.set_stroke(opacity=1),
            VGroup(excircle_B_label, omega_2_label).animate.set_opacity(1))
        self.wait(0.2)
        self.play(FadeOut(label))

        label = Tex("But then $\omega_b$ and $\omega_1$ are perpendicular")
        self.play(Fancy_label(label))
        self.play(FadeOut(VGroup(I_bY, angle_I_bYA)), VGroup(Y, I_b, Y_label, I_b_label).animate.set_opacity(0.4))
        self.play(
            omega_1.animate.set_stroke(opacity=1),
            omega_1_label.animate.set_opacity(1),
            omega_2.animate.set_stroke(opacity=0.4),
            omega_2_label.animate.set_opacity(0.4),
        )
        self.play(FadeOut(label))

        label = Tex("Then by the external criteria of Archimedes, $\Omega$ and $\omega_b$ touch")
        self.play(Fancy_label(label))
        self.play(
            omega_1.animate.set_stroke(opacity=0.4),
            omega_1_label.animate.set_opacity(0.4),
            euler_circle.animate.set_stroke(opacity=1),
            euler_circle_label.animate.set_opacity(1),
        )
        self.play(FadeIn(feuerbach_point_B))
        self.wait(3.5)
        self.play(FadeOut(VGroup(ALL, label, feuerbach_point_B)))

        self.wait(3)


class Circles_16(Scene):
    def construct(self):
        black_rectangle = Rectangle(height=1.2,width=20).shift(3.5*UP).set_color(BLACK).set_opacity(1).set_z_index(101)
        self.add(black_rectangle)

        A = Dot(2*LEFT+2*DOWN).set_z_index(1)
        B = Dot(1.2*LEFT+1.4*UP).set_z_index(1)
        C = Dot(2*RIGHT+2*DOWN).set_z_index(1)

        a = Line(B.get_center(), C.get_center(), color=BLUE)
        b = Line(A.get_center(), C.get_center(), color=BLUE)
        c = Line(A.get_center(), B.get_center(), color=BLUE)

        euler_circle = EulerCircle(A.get_center(), B.get_center(), C.get_center(), color=RED).set_z_index(1)

        incircle = InscribedCircle(A.get_center(), B.get_center(), C.get_center(), color=GREEN, stroke_width=2)
        excircle_A = EscribedCircle(B.get_center(), A.get_center(), C.get_center(), color=GREEN, stroke_width=2)
        excircle_B = EscribedCircle(A.get_center(), B.get_center(), C.get_center(), color=GREEN, stroke_width=2)
        excircle_C = EscribedCircle(B.get_center(), C.get_center(), A.get_center(), color=GREEN, stroke_width=2)

        AH_a = Altitude(B.get_center(), A.get_center(), C.get_center(), color=YELLOW)
        BH_b = Altitude(A.get_center(), B.get_center(), C.get_center(), color=YELLOW)
        CH_c = Altitude(B.get_center(), C.get_center(), A.get_center(), color=YELLOW)

        H_a = Dot(AH_a.dot).set_z_index(2)
        H_b = Dot(BH_b.dot).set_z_index(2)
        H_c = Dot(CH_c.dot).set_z_index(2)

        H_a_angle = AH_a.angles(color=YELLOW, radius=0.2)[0]
        H_b_angle = BH_b.angles(color=YELLOW, radius=0.2)[0]
        H_c_angle = CH_c.angles(color=YELLOW, radius=0.2)[0]

        H = Dot(intersection_lines(AH_a, BH_b)).set_z_index(1)




        label = Tex("Finally, another beautiful construction")
        self.play(Fancy_label(label))
        self.play(LaggedStart(
            FadeIn(A),
            FadeIn(B),
            FadeIn(C),
            run_time=1.4, lag_ratio=0.75
        ))
        self.play(LaggedStart(
            Create(a),
            Create(b),
            Create(c),
            run_time=3, lag_ratio=0.9
        ))
        self.play(FadeOut(label))

        label = Tex("Now let's construct the Euler's circle")
        self.play(Fancy_label(label))
        self.play(Create(euler_circle))
        self.wait(0.4)
        self.play(FadeOut(label))

        label = Tex("Find the orthocenter")
        self.play(Fancy_label(label))
        
        self.play(Create(AH_a))
        self.play(FadeIn(VGroup(H_a, H_a_angle)), run_time=0.7)
        
        self.play(Create(BH_b))
        self.play(FadeIn(VGroup(H_b, H_b_angle)), run_time=0.7)

        self.play(Create(CH_c))
        self.play(FadeIn(VGroup(H_c, H_c_angle)), run_time=0.7)

        self.play(VGroup(AH_a, BH_b, CH_c, H_a, H_b, H_c).animate.set_opacity(0.5), 
                  VGroup(H_a_angle, H_b_angle, H_c_angle).animate.set_stroke(opacity=0.5))
        self.play(FadeIn(H))
        self.play(FadeOut(label))

        label = Tex("And now let's build 16 circles that touch the Euler's circle")
        self.play(Fancy_label(label))
        self.play(FadeOut(VGroup(AH_a, BH_b, CH_c, H_a, H_b, H_c, H_a_angle, H_b_angle, H_c_angle)))

        self.play(Create(incircle))

        line_AB = Line(A.get_center(), B.get_center(), color=BLUE).set_length(20).set_z_index(-1).set_opacity(0.35)
        line_BC = Line(B.get_center(), C.get_center(), color=BLUE).set_length(20).set_z_index(-1).set_opacity(0.35)
        line_CA = Line(C.get_center(), A.get_center(), color=BLUE).set_length(20).set_z_index(-1).set_opacity(0.35)
        self.play(FadeIn(VGroup(line_AB, line_BC, line_CA)))

        self.play(Create(excircle_A))
        self.play(Create(excircle_B))
        self.play(Create(excircle_C))

        self.play(FadeOut(VGroup(line_CA, line_BC)))

        line_AH = Line(A.get_center(), H.get_center(), color=BLUE).set_length(20).set_z_index(-1).set_opacity(0.35)
        line_BH = Line(B.get_center(), H.get_center(), color=BLUE).set_length(20).set_z_index(-1).set_opacity(0.35)

        self.play(FadeIn(VGroup(line_AH, line_BH)))

        incircle_1 = InscribedCircle(A.get_center(), B.get_center(), H.get_center(), color=GREEN, stroke_width=2)

        excircle_1 = EscribedCircle(A.get_center(), B.get_center(), H.get_center(), color=GREEN, stroke_width=2)
        excircle_2 = EscribedCircle(B.get_center(), A.get_center(), H.get_center(), color=GREEN, stroke_width=2)
        excircle_3 = EscribedCircle(A.get_center(), H.get_center(), B.get_center(), color=GREEN, stroke_width=2)

        self.play(Create(incircle_1))
        self.play(Create(excircle_1))
        self.play(Create(excircle_2))
        self.play(Create(excircle_3))

        self.play(FadeOut(VGroup(line_AH, line_AB)))

        line_CH = Line(C.get_center(), H.get_center(), color=BLUE).set_length(20).set_z_index(-1).set_opacity(0.35)
        
        self.play(FadeIn(VGroup(line_CH, line_BC)))

        incircle_2 = InscribedCircle(C.get_center(), B.get_center(), H.get_center(), color=GREEN, stroke_width=2)

        excircle_4 = EscribedCircle(C.get_center(), B.get_center(), H.get_center(), color=GREEN, stroke_width=2)
        excircle_5 = EscribedCircle(B.get_center(), C.get_center(), H.get_center(), color=GREEN, stroke_width=2)
        excircle_6 = EscribedCircle(C.get_center(), H.get_center(), B.get_center(), color=GREEN, stroke_width=2)

        self.play(Create(incircle_2))
        self.play(Create(excircle_4))
        self.play(Create(excircle_5))
        self.play(Create(excircle_6))

        self.play(FadeOut(VGroup(line_BC, line_BH)))
        
        self.play(FadeIn(VGroup(line_AH, line_CA)))

        incircle_3 = InscribedCircle(C.get_center(), A.get_center(), H.get_center(), color=GREEN, stroke_width=2)

        excircle_7 = EscribedCircle(C.get_center(), A.get_center(), H.get_center(), color=GREEN, stroke_width=2)
        excircle_8 = EscribedCircle(A.get_center(), C.get_center(), H.get_center(), color=GREEN, stroke_width=2)
        excircle_9 = EscribedCircle(C.get_center(), H.get_center(), A.get_center(), color=GREEN, stroke_width=2)

        self.play(Create(incircle_3))
        self.play(Create(excircle_7))
        self.play(Create(excircle_8))
        self.play(Create(excircle_9))

        self.play(FadeOut(VGroup(line_CA, line_CH, line_AH, H)))
        self.play(FadeOut(label))

        label = Tex("Prove this using Feuerbach's theorem")
        self.play(Fancy_label(label))
        self.wait(2)

        ALL = VGroup(
            A, B, C, a, b, c, 
            incircle, excircle_A, excircle_B, excircle_C,
            incircle_1, excircle_1, excircle_2, excircle_3,
            incircle_2, excircle_4, excircle_5, excircle_6,
            incircle_3, excircle_7, excircle_8, excircle_9,
            label, euler_circle
        )
        self.play(FadeOut(ALL))

        self.wait(3)


        

  


    

