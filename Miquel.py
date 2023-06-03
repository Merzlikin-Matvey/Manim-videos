from manim import *
import numpy as np

class Lable(MovingCameraScene):
    def construct(self):
       general = Tex("Miquel's Theorem",font_size=120)
       self.add(general)

class Miquel(MovingCameraScene):
    def construct(self):
        
        def circle_intersection(Circle1: Circle, Circle2: Circle, Dot11: Dot, Dot12: Dot, Dot13: Dot, Dot21: Dot, Dot22: Dot, Dot23: Dot,):

            angle_for_radius1 = Angle(Line(Dot11.get_center(),Dot13.get_center()),
                                     Line(Dot11.get_center(),Dot12.get_center())).get_value()

            R1 = Line(Dot12.get_center(),Dot13.get_center()).get_length() / np.sin(angle_for_radius1) * 1/2

            angle_for_radius2 = Angle(Line(Dot21.get_center(),Dot23.get_center()),
                                     Line(Dot21.get_center(),Dot22.get_center())).get_value()

            R2 = Line(Dot22.get_center(),Dot23.get_center()).get_length() / np.sin(angle_for_radius2) * 1/2
            
            O1 = Circle1.get_center()
            O2 = Circle2.get_center()

            L = np.sqrt((O1[0]-O2[0])**2+(O1[1]-O2[1])**2)



            result_angle_1 = Angle(Line(Dot(RIGHT+O1),Dot(O1)),Line(Dot(O2),Dot(O1)),radius=0.1).get_value() + np.arccos(
                min((R2**2-R1**2-L**2)/(-2*R1*L),1)
            )
                            

            result = Dot(O1+np.array([R1,0,0])).rotate(about_point=O1,angle=result_angle_1).get_center()

            return result

        def change_opacity_50(mob):
            mob.set_stroke(opacity=0.5)
            return mob

        general = Tex("Miquel's Theorem",font_size=120)

        self.play(Write(general),run_time=2)
        self.wait(0.7)
        self.play(FadeOut(general))

        circle = Circle(radius=2,color=BLUE_D).move_to(0.35*DOWN)


        label_1 = Tex('Draw a circle').to_edge(UP)
        self.play(LaggedStart(
            Write(label_1),
            Create(circle),
            lag_ratio=0.5,
            run_time=1.5
        ))

        self.wait(0.3)
        self.play(FadeOut(label_1))
        self.wait(0.3)
        

        A = Dot(circle.point_at_angle(0.25*PI))
        B = Dot(circle.point_at_angle((4/6)*PI))
        C = Dot(circle.point_at_angle(-(8/11)*PI))
        D = Dot(circle.point_at_angle(-(1/3)*PI))

        A_label = always_redraw(lambda: Tex('A',font_size=35).next_to(A.get_center(),UR,buff=0.17).set_z_index(99))
        B_label = always_redraw(lambda: Tex('B',font_size=35).next_to(B.get_center(),UL,buff=0.17).set_z_index(99))
        C_label = always_redraw(lambda: Tex('C',font_size=35).next_to(C.get_center(),DL,buff=0.17).set_z_index(99))
        D_label = always_redraw(lambda: Tex('D',font_size=35).next_to(D.get_center(),DR,buff=0.17).set_z_index(99))


        label_2 = Tex("Let's take 4 points on it").to_edge(UP)

        general_dots_anims = AnimationGroup(
            GrowFromCenter(A),
            GrowFromCenter(B),
            GrowFromCenter(C),
            GrowFromCenter(D),
            Write(A_label),
            Write(B_label),
            Write(C_label),
            Write(D_label)
            )
    

        self.play(LaggedStart(
            Write(label_2),
            general_dots_anims,
            lag_ratio=0.8,
            run_time=2
        ))

        self.wait(0.3)

        self.play(FadeOut(label_2))

        Dot_for_AB = Dot(2.3*UP+0.6*LEFT).set_opacity(0.).set_z_index(0)
        Dot_for_BC = Dot(3.8*LEFT+0.5*DOWN).set_opacity(0.).set_z_index(0)
        Dot_for_CD = Dot(3*DOWN+0.4*RIGHT).set_opacity(0.).set_z_index(0)
        Dot_for_DA = Dot(4*RIGHT+0.2*UP).set_opacity(0.).set_z_index(0)

        self.add(
            Dot_for_AB,
            Dot_for_BC,
            Dot_for_CD,
            Dot_for_DA
        )

        label_3 = Tex("Now let's build 4 circles passing through these points").to_edge(UP)        

        Circle_AB = Circle.from_three_points(
                                    A.get_center(),
                                    B.get_center(),
                                    Dot_for_AB.get_center(),
                                    color=YELLOW_C
                                ).set_z_index(-4)
                                      
        Circle_BC = Circle.from_three_points(
                                    B.get_center(),
                                    C.get_center(),
                                    Dot_for_BC.get_center(),
                                    color=YELLOW_C
                                ).set_z_index(-4)
        
        Circle_CD =  Circle.from_three_points(
                                    C.get_center(),
                                    D.get_center(),
                                    Dot_for_CD.get_center(),
                                    color=YELLOW_C
                                ).set_z_index(-4)
        
        Circle_DA = Circle.from_three_points(
                                    D.get_center(),
                                    A.get_center(),
                                    Dot_for_DA.get_center(),
                                    color=YELLOW_C
                                ).set_z_index(-4)
        
        self.play(Write(label_3))
        self.wait(0.3)
        self.play(Create(Circle_AB),run_time=2)
        self.play(Create(Circle_BC),run_time=2)
        self.play(Create(Circle_CD),run_time=2)
        self.play(Create(Circle_DA),run_time=2)


        self.wait(0.3)

        self.play(FadeOut(label_3))

        label_4 = Tex("Denote their intersection points").to_edge(UP)

        A1_view = always_redraw(lambda: Dot(circle_intersection(Circle_DA,Circle_AB,D,A,Dot_for_DA,A,B,Dot_for_AB)).set_z_index(1))
        B1_view = always_redraw(lambda: Dot(circle_intersection(Circle_AB,Circle_BC,A,B,Dot_for_AB,B,C,Dot_for_BC)).set_z_index(1))
        C1_view = always_redraw(lambda: Dot(circle_intersection(Circle_BC,Circle_CD,B,C,Dot_for_BC,C,D,Dot_for_CD)).set_z_index(1))
        D1_view = always_redraw(lambda: Dot(circle_intersection(Circle_CD,Circle_DA,C,D,Dot_for_CD,D,A,Dot_for_DA)).set_z_index(1))

        A1 = always_redraw(lambda: Dot(circle_intersection(Circle_DA,Circle_AB,D,A,Dot_for_DA,A,B,Dot_for_AB)).set_z_index(0).set_opacity(0))
        B1 = always_redraw(lambda: Dot(circle_intersection(Circle_AB,Circle_BC,A,B,Dot_for_AB,B,C,Dot_for_BC)).set_z_index(0).set_opacity(0))
        C1 = always_redraw(lambda: Dot(circle_intersection(Circle_BC,Circle_CD,B,C,Dot_for_BC,C,D,Dot_for_CD)).set_z_index(0).set_opacity(0))
        D1 = always_redraw(lambda: Dot(circle_intersection(Circle_CD,Circle_DA,C,D,Dot_for_CD,D,A,Dot_for_DA)).set_z_index(0).set_opacity(0))

        A1_label = always_redraw(lambda: MathTex(r"\mathrm{A_1}",font_size=28).next_to(A1.get_center(),UR,buff=0.13))
        B1_label = always_redraw(lambda: MathTex(r"\mathrm{B_1}",font_size=28).next_to(B1.get_center(),UL,buff=0.13))
        C1_label = always_redraw(lambda: MathTex(r"\mathrm{C_1}",font_size=28).next_to(C1.get_center(),DL,buff=0.13))
        D1_label = always_redraw(lambda: MathTex(r"\mathrm{D_1}",font_size=28).next_to(D1.get_center(),DR,buff=0.13))

        self.add(A1,B1,C1,D1)

        Intersection_points = AnimationGroup(
            GrowFromCenter(A1_view),
            GrowFromCenter(B1_view),
            GrowFromCenter(C1_view),
            GrowFromCenter(D1_view),
            Write(A1_label),
            Write(B1_label),
            Write(C1_label),
            Write(D1_label),
        )

        tmp = AnimationGroup(
            ApplyFunction(change_opacity_50, Circle_AB),
            ApplyFunction(change_opacity_50, Circle_BC),
            ApplyFunction(change_opacity_50, Circle_CD),
            ApplyFunction(change_opacity_50, Circle_DA),
        )

        self.play(LaggedStart(
            Write(label_4),
            Intersection_points,
            tmp,
            lag_ratio=0.6,
            run_time=3
        ))

        self.wait(0.5)
        self.play(FadeOut(label_4))
        self.wait(0.7)

        Circle_AB.set_stroke(opacity=0.5)
        Circle_BC.set_stroke(opacity=0.5)
        Circle_CD.set_stroke(opacity=0.5)
        Circle_DA.set_stroke(opacity=0.5)

        label_5 = Tex("These points will always lie on the circle").to_edge(UP)

        Circle_result = always_redraw(lambda:
                                      Circle.from_three_points(
                                            A1.get_center(),
                                            B1.get_center(),
                                            C1.get_center(),
                                            color=RED_C
                                      ))

        self.play(LaggedStart(
            Write(label_5),
            Create(Circle_result),
            lag_ratio=0.8,
            run_time=2.5
        ))

        self.wait(0.2)
        self.play(FadeOut(label_5))
        self.wait(0.4)

        self.remove(Circle_AB,Circle_BC,Circle_CD,Circle_DA)

        Circle_AB = always_redraw(lambda: Circle.from_three_points(
                                    A.get_center(),
                                    B.get_center(),
                                    Dot_for_AB.get_center(),
                                    color=YELLOW_C
                                ).set_stroke(opacity=0.5))
                                    
        Circle_BC = always_redraw(lambda: Circle.from_three_points(
                                    B.get_center(),
                                    C.get_center(),
                                    Dot_for_BC.get_center(),
                                    color=YELLOW_C
                                ).set_stroke(opacity=0.5))
        
        Circle_CD = always_redraw(lambda: Circle.from_three_points(
                                    C.get_center(),
                                    D.get_center(),
                                    Dot_for_CD.get_center(),
                                    color=YELLOW_C
                                ).set_stroke(opacity=0.5))
        
        Circle_DA = always_redraw(lambda: Circle.from_three_points(
                                    D.get_center(),
                                    A.get_center(),
                                    Dot_for_DA.get_center(),
                                    color=YELLOW_C
                                ).set_stroke(opacity=0.5))

        self.add(Circle_AB,Circle_BC,Circle_CD,Circle_DA)

        
        self.play(LaggedStart(
            Dot_for_AB.animate.shift(UP+0.3*RIGHT),
            Dot_for_BC.animate.shift(1.2*UP+0.3*LEFT),
            Dot_for_CD.animate.shift(0.5*DOWN+0.1*RIGHT),
            Dot_for_DA.animate.shift(0.5*RIGHT+0.2*UP),

            lag_ratio=0.4,
            run_time=6
        ))
        self.play(LaggedStart(
            Dot_for_AB.animate.shift(DOWN+0.3*LEFT),
            Dot_for_BC.animate.shift(1.2*DOWN+0.3*RIGHT),
            Dot_for_CD.animate.shift(0.5*UP+0.1*LEFT),
            Dot_for_DA.animate.shift(0.5*LEFT+0.2*DOWN),

            lag_ratio=0.4,
            run_time=6
        ))


        self.wait()


class Miquel_proove(MovingCameraScene):
    def construct(self):

        def circle_intersection(Circle1: Circle, Circle2: Circle, Dot11: Dot, Dot12: Dot, Dot13: Dot, Dot21: Dot, Dot22: Dot, Dot23: Dot,):

            angle_for_radius1 = Angle(Line(Dot11.get_center(),Dot13.get_center()),
                                     Line(Dot11.get_center(),Dot12.get_center())).get_value()

            R1 = Line(Dot12.get_center(),Dot13.get_center()).get_length() / np.sin(angle_for_radius1) * 1/2

            angle_for_radius2 = Angle(Line(Dot21.get_center(),Dot23.get_center()),
                                     Line(Dot21.get_center(),Dot22.get_center())).get_value()

            R2 = Line(Dot22.get_center(),Dot23.get_center()).get_length() / np.sin(angle_for_radius2) * 1/2
            
            O1 = Circle1.get_center()
            O2 = Circle2.get_center()

            L = np.sqrt((O1[0]-O2[0])**2+(O1[1]-O2[1])**2)



            result_angle_1 = Angle(Line(Dot(RIGHT+O1),Dot(O1)),Line(Dot(O2),Dot(O1)),radius=0.1).get_value() + np.arccos(
                min((R2**2-R1**2-L**2)/(-2*R1*L),1)
            )
                            

            result = Dot(O1+np.array([R1,0,0])).rotate(about_point=O1,angle=result_angle_1).get_center()

            return result

        def change_opacity_0(mob):
            mob.set_stroke(opacity=0)
            return mob
        
        def change_opacity_10(mob):
            mob.set_stroke(opacity=0.1)
            return mob
        
        def change_opacity_30(mob):
            mob.set_stroke(opacity=0.3)
            return mob

        def change_opacity_50(mob):
            mob.set_stroke(opacity=0.5)
            return mob
        
        def change_opacity_70(mob):
            mob.set_stroke(opacity=0.7)
            return mob
        


        circle = Circle(radius=2,color=BLUE_D).move_to(0.35*DOWN)

        A = Dot(circle.point_at_angle(0.25*PI)).set_z_index(1)
        B = Dot(circle.point_at_angle((4/6)*PI)).set_z_index(1)
        C = Dot(circle.point_at_angle(-(8/11)*PI)).set_z_index(1)
        D = Dot(circle.point_at_angle(-(1/3)*PI)).set_z_index(1)

        A_label = Tex('A',font_size=35).next_to(A.get_center(),UR,buff=0.17).set_z_index(99)
        B_label = Tex('B',font_size=35).next_to(B.get_center(),UL,buff=0.17).set_z_index(99)
        C_label = Tex('C',font_size=35).next_to(C.get_center(),DL,buff=0.17).set_z_index(99)
        D_label = Tex('D',font_size=35).next_to(D.get_center(),DR,buff=0.17).set_z_index(99)

        Dot_for_AB = Dot(2.3*UP+0.6*LEFT).set_opacity(0).set_z_index(0)
        Dot_for_BC = Dot(3.8*LEFT+0.5*DOWN).set_opacity(0).set_z_index(0)
        Dot_for_CD = Dot(3*DOWN+0.4*RIGHT).set_opacity(0).set_z_index(0)
        Dot_for_DA = Dot(4*RIGHT+0.2*UP).set_opacity(0).set_z_index(0)

        Circle_AB = Circle.from_three_points(
                                    A.get_center(),
                                    B.get_center(),
                                    Dot_for_AB.get_center(),
                                    color=YELLOW_C
                                ).set_z_index(-4).set_stroke(opacity=0.5)                                     
        Circle_BC = Circle.from_three_points(
                                    B.get_center(),
                                    C.get_center(),
                                    Dot_for_BC.get_center(),
                                    color=YELLOW_C
                                ).set_z_index(-4).set_stroke(opacity=0.5)    
        Circle_CD =  Circle.from_three_points(
                                    C.get_center(),
                                    D.get_center(),
                                    Dot_for_CD.get_center(),
                                    color=YELLOW_C
                                ).set_z_index(-4).set_stroke(opacity=0.5)        
        Circle_DA = Circle.from_three_points(
                                    D.get_center(),
                                    A.get_center(),
                                    Dot_for_DA.get_center(),
                                    color=YELLOW_C
                                ).set_z_index(-4).set_stroke(opacity=0.5)
        
        A1 = Dot(circle_intersection(Circle_DA,Circle_AB,D,A,Dot_for_DA,A,B,Dot_for_AB)).set_z_index(1)
        B1 = Dot(circle_intersection(Circle_AB,Circle_BC,A,B,Dot_for_AB,B,C,Dot_for_BC)).set_z_index(1)
        C1 = Dot(circle_intersection(Circle_BC,Circle_CD,B,C,Dot_for_BC,C,D,Dot_for_CD)).set_z_index(1)
        D1 = Dot(circle_intersection(Circle_CD,Circle_DA,C,D,Dot_for_CD,D,A,Dot_for_DA)).set_z_index(1)

        A1_label = MathTex(r"\mathrm{A_1}",font_size=28).next_to(A1.get_center(),UR,buff=0.13).set_z_index(999)
        B1_label = MathTex(r"\mathrm{B_1}",font_size=28).next_to(B1.get_center(),UL,buff=0.13).set_z_index(999)
        C1_label = MathTex(r"\mathrm{C_1}",font_size=28).next_to(C1.get_center(),DL,buff=0.13).set_z_index(999)
        D1_label = MathTex(r"\mathrm{D_1}",font_size=28).next_to(D1.get_center(),DR,buff=0.13).set_z_index(999)

        Circle_result = Circle.from_three_points(
            A1.get_center(),
            B1.get_center(),
            C1.get_center(),
            color=RED_C
        ).set_z_index(-9)

        ALL = VGroup(
            circle,
            A,B,C,D,
            A_label,B_label,C_label,D_label,
            Dot_for_AB,Dot_for_BC,Dot_for_CD,Dot_for_DA,
            Circle_AB,Circle_BC,Circle_CD,Circle_DA,
            A1,B1,C1,D1,
            A1_label,B1_label,C1_label,D1_label,
            Circle_result
        )

        self.add(ALL)

        label_1 = Tex("Now let's prove it").to_edge(UP)

        self.play(Write(label_1))
        self.wait(0.8)
        self.play(FadeOut(label_1))
        self.wait(0.2)

        self.play(FadeOut(Circle_result))

        self.play(
            AnimationGroup(
                ApplyFunction(change_opacity_30,Circle_AB),
                ApplyFunction(change_opacity_30,Circle_BC),
                ApplyFunction(change_opacity_30,Circle_CD),
                ApplyFunction(change_opacity_30,Circle_DA),
            ),run_time=0.7
        )
        
        self.play(
            AnimationGroup(
                A.animate.scale(0.7),
                B.animate.scale(0.7),
                C.animate.scale(0.7),
                D.animate.scale(0.7),
                A1.animate.scale(0.7),
                B1.animate.scale(0.7),
                C1.animate.scale(0.7),
                D1.animate.scale(0.7),
                A1_label.animate.set_opacity(0.6),
                B1_label.animate.set_opacity(0.6),
                C1_label.animate.set_opacity(0.6),
                D1_label.animate.set_opacity(0.6),
            )
        )


        label_2 = MathTex(r"\mathrm{Let}\,\,\angle{D_1DA} = \alpha\,\,\mathrm{and}\,\,\angle{B_1BA} = \beta",font_size=40).to_edge(UP)

        self.play(Write(label_2),run_time=1.5)

        DD1 = Line(D.get_center(),D1.get_center(),color=GREEN_C)
        DA = Line(D.get_center(),A.get_center(),color=GREEN_C)
        Angle_D1DA = Angle(DA,DD1,radius=0.2,color=GREEN_C)
        Angle_D1DA_label = MathTex(r"\alpha",font_size=31).move_to(D.get_center()+np.array([-0.08,0.4,0]))

        self.play(LaggedStart(
            Create(DD1),
            Create(DA),
            Create(Angle_D1DA),
            Write(Angle_D1DA_label),
            lag_ratio=0.5,
            run_time=4
        ))
        
        BB1 = Line(B.get_center(),B1.get_center(),color=GREEN_C)
        BA = Line(B.get_center(),A.get_center(),color=GREEN_C)
        Angle_B1BA = Angle(BB1,BA,radius=0.2,color=GREEN_C)
        Angle_B1BA_label = MathTex(r"\beta",font_size=31).move_to(B.get_center()+np.array([0.4,-0.27,0]))

        self.wait(0.5)

        

        self.play(LaggedStart(
            Create(BB1),
            Create(BA),
            lag_ratio=0.5,
            run_time=1
        ))

        self.play(Create(Angle_B1BA),
            Write(Angle_B1BA_label))

        self.wait(0.1)
        self.play(FadeOut(label_2))
        self.wait(0.2)

        label_3 = MathTex(r"\mathrm{The quadrilaterals}\,\,DD_1A_1A\,\,\mathrm{and}\,\,AA_1B_1B\,\,\mathrm{are\,\,inscribed}",font_size=40).to_edge(UP)

        self.play(Write(label_3),run_time=2)
        self.wait(0.7)
        self.play(FadeOut(label_3))
        self.wait(0.3)
    

        label_4 = MathTex(r"\mathrm{So}\,\,\angle{D_1A_1A} = 180^{\circ} - \alpha\,\,\mathrm{and}\,\,\angle{B_1A_1A} = 180^{\circ} -\beta",font_size=40).to_edge(UP)

        self.play(Write(label_4),run_time=2)


        A1B1 = Line(A1.get_center(),B1.get_center(),color=GREEN_C)
        A1D1 = Line(A1.get_center(),D1.get_center(),color=GREEN_C)
        A1A = Line(A1.get_center(),A.get_center(),color=GREEN_C)

        Angle_B1A1A = Angle(A1A,A1B1,radius=0.2,color=GREEN_C)
        Angle_B1A1A_label = MathTex(r"180^{\circ}-\beta",font_size=25).move_to(A1.get_center()+np.array([-0.32,0.43,0]))

        Angle_D1A1A = Angle(A1D1,A1A,radius=0.2,color=GREEN_C)
        Angle_D1A1A_label = MathTex(r"180^{\circ}-\alpha",font_size=25).move_to(A1.get_center()+np.array([0.55,-0.3,0]))

        self.play(LaggedStart(
            AnimationGroup(
                FadeOut(BB1),
                FadeOut(BA),
                FadeOut(Angle_D1DA_label),
                FadeOut(Angle_D1DA),
                FadeOut(Angle_B1BA_label),
                FadeOut(Angle_B1BA),
                FadeOut(DD1),
                FadeOut(DA),
            ),
            Create(A1B1),
            Create(A1D1),
            Create(A1A),
            lag_ratio=0.7,
            run_time=3
        ))

        self.play(Create(Angle_B1A1A),Write(Angle_B1A1A_label))
        self.play(Create(Angle_D1A1A),Write(Angle_D1A1A_label))

        self.wait(0.2)
        self.play(FadeOut(label_4))
        self.wait(0.3)

        label_5 = MathTex(r"\mathrm{Then}\,\,\angle{B_1A_1D_1} = \alpha+\beta",font_size=40).to_edge(UP)

        self.play(Write(label_5),run_time=2)

        Angle_B1A1D1 = Angle(A1B1,A1D1,radius=0.2,color=GREEN_C).set_z_index(99)
        Angle_B1A1D1_label = MathTex(r"\alpha+\beta",font_size=24).move_to(A1.get_center()+np.array([-0.4,-0.3,0]))

        self.play(LaggedStart(
            Create(Angle_B1A1D1),
            Write(Angle_B1A1D1_label),
            FadeOut(Angle_B1A1A),
            FadeOut(Angle_B1A1A_label),
            FadeOut(Angle_D1A1A),
            FadeOut(Angle_D1A1A_label),
            FadeOut(A1A),
            FadeOut(label_5),
            lag_ratio=0.3,
            run_time=5
        ))

        self.wait(0.2)

        label_6 = MathTex(r"\mathrm{Let}\,\,\angle{B_1BC} = \gamma\,\,\mathrm{and}\,\,\angle{D_1DC}=\delta",font_size=40).to_edge(UP)

        self.play(Write(label_6))
        

        BC = Line(B.get_center(),C.get_center(),color=GREEN_C)
        DC = Line(D.get_center(),C.get_center(),color=GREEN_C)

        Angle_B1BC = Angle(BC,BB1,radius=0.2,color=GREEN_C)
        Angle_B1BC_label = MathTex(r"\gamma",font_size=31).move_to(B.get_center()+np.array([0.1,-0.41,0]))

        Angle_D1DC = Angle(DD1,DC,radius=0.2,color=GREEN_C)
        Angle_D1DC_label = MathTex(r"\delta",font_size=31).move_to(D.get_center()+np.array([-0.35,0.3,0]))

        self.play(LaggedStart(
            Create(BB1),
            Create(BC),
            Create(Angle_B1BC),
            Write(Angle_B1BC_label),
            lag_ratio=0.3,
            run_time=3
        ))

        self.wait(0.2)

        self.play(LaggedStart(
            Create(DD1),
            Create(DC),
            Create(Angle_D1DC),
            Write(Angle_D1DC_label),
            FadeOut(label_6),
            lag_ratio=0.3,
            run_time=4
        ))
    

        C1B1 = Line(C1.get_center(),B1.get_center(),color=GREEN_C)
        C1D1 = Line(C1.get_center(),D1.get_center(),color=GREEN_C)

        label_7 = MathTex(r"\mathrm{Similarly,}\,\,\angle{B_1C_1D_1}=\gamma+\delta",font_size=40).to_edge(UP)

        Angle_B1C1D1 = Angle(C1D1,C1B1,radius=0.2,color=GREEN_C)
        Angle_B1C1D1_label = MathTex(r"\gamma+\delta",font_size=24).move_to(C1.get_center()+np.array([0.4,0.3,0]))

        self.wait(0.2)
        self.play(Write(label_7))
        self.play(LaggedStart(
            Create(C1B1),
            Create(C1D1),
            Create(Angle_B1C1D1),
            Write(Angle_B1C1D1_label),
            lag_ratio=0.4,
            run_time=4
        ))
        self.wait(0.3)
        self.play(LaggedStart(
            FadeOut(label_7),
            AnimationGroup(
                FadeOut(Angle_B1BC_label),
                FadeOut(Angle_B1BC),
                FadeOut(Angle_D1DC_label),
                FadeOut(Angle_D1DC) 
            ),  
            AnimationGroup( 
                FadeOut(BC),
                FadeOut(DC),
                FadeOut(BB1),
                FadeOut(DD1)
            ),
            lag_ratio=0.7,
            run_time=2.5
        ))

        self.wait(0.3)

        label_8 = MathTex(r"ABCD\,\,\mathrm{ is\,\, an\,\, inscribed\,\, quadrilateral}",font_size=40).to_edge(UP)

        self.play(Write(label_8),run_time=2)
        self.wait(0.3)
        self.play(FadeOut(label_8))

        label_9 = MathTex(r"\mathrm{So}\,\,\alpha+\beta+\gamma+\delta=180^{\circ}\,\,\mathrm{and}\,\,A_1,B_1,C_1\,\,,D_1\,\,\mathrm{lie\,\, on\,\, a\,\, common\,\, circle}",font_size=40).to_edge(UP)

        Circle_result1 = Circle.from_three_points(
            A1.get_center(),
            B1.get_center(),
            C1.get_center(),
            color=RED_C
        ).set_z_index(-9)

        self.play(LaggedStart(
            Write(label_9),
            AnimationGroup(
                FadeOut(Angle_B1C1D1_label),
                FadeOut(Angle_B1A1D1_label),
                FadeOut(Angle_B1C1D1),
                FadeOut(Angle_B1A1D1),
            ),
            AnimationGroup(
                FadeOut(A1B1),
                FadeOut(A1D1),
                FadeOut(C1B1),
                FadeOut(C1D1),
            ),
            lag_ratio=0.5,
            run_time=4
        ))
        self.play(Create(Circle_result1))
        self.wait(1)
        self.play(FadeOut(label_9))
        self.wait(0.2)
        label_10 = MathTex(r"\mathrm{Now\,\, let's\,\, discuss\,\, the\,\, consequences\,\, of\,\, the\,\, theorem}",font_size=40).to_edge(UP)
        self.play(LaggedStart(
            Write(label_10),
            AnimationGroup(
                FadeOut(ALL),
                FadeOut(Circle_result1)
            ),
            lag_ratio=0.6,
            run_time=1.5
        ))
        self.wait(0.3)
        self.play(FadeOut(label_10))
        self.wait(2)


class Miquel_consequence_1(MovingCameraScene):
    def construct(self):
        label_1 = MathTex(r"\mathrm{The\,\, first\,\, consequence}",font_size=40).to_edge(UP)
        
        self.play(Write(label_1))
        self.wait(0.4)
        self.play(FadeOut(label_1),run_time=0.8)
        self.wait(0.2)


        circle = Circle(radius=2.6,color=BLUE_D).move_to(0.35*DOWN)

        A = Dot(circle.point_at_angle(0.15*PI)).set_z_index(9)
        B = Dot(circle.point_at_angle((4/5)*PI)).set_z_index(9)
        C = Dot(circle.point_at_angle(-(9/11)*PI)).set_z_index(9)
        D = Dot(circle.point_at_angle(-(1/4)*PI)).set_z_index(9)

        A_label = Tex('A',font_size=35).next_to(A.get_center(),UR,buff=0.17).set_z_index(99)
        B_label = Tex('B',font_size=35).next_to(B.get_center(),UL,buff=0.17).set_z_index(99)
        C_label = Tex('C',font_size=35).next_to(C.get_center(),DL,buff=0.17).set_z_index(99)
        D_label = Tex('D',font_size=35).next_to(D.get_center(),DR,buff=0.17).set_z_index(99)


        label_2 = MathTex(r"\mathrm{A\,\, quadrilateral\,\, is\,\, inscribed\,\, in\,\, the\,\, circle}",font_size=40).to_edge(UP)

        polygon = Polygon(
            A.get_center(),
            B.get_center(),
            C.get_center(),
            D.get_center(),
            color=YELLOW_C
        )

        self.play(LaggedStart(
            Write(label_2),
            Create(circle),
            AnimationGroup(
                Create(A),
                Create(B),
                Create(C),
                Create(D),
                Write(A_label),
                Write(B_label),
                Write(C_label),
                Write(D_label),
            ),
            Create(polygon),
            lag_ratio=0.5,
            run_time=5
        ))
        self.wait(0.3)
        self.play(FadeOut(label_2),run_time=0.8)
        self.wait(0.3)

        label_3 = MathTex(r"\mathrm{Draw\,\, diagonals}",font_size=40).to_edge(UP)

        AC = Line(A.get_center(),C.get_center(),color=GREEN_C).set_z_index(0)
        BD = Line(B.get_center(),D.get_center(),color=GREEN_C).set_z_index(0)

        self.play(LaggedStart(
            Write(label_3),
            Create(AC),
            Create(BD),
            lag_ratio=0.6,
            run_time=3
        ))
        self.wait(0.4)
        self.play(FadeOut(label_3))
        self.wait(0.2)

        HA = Dot(BD.get_projection(A.get_center()))
        HB = Dot(AC.get_projection(B.get_center()))
        HC = Dot(BD.get_projection(C.get_center()))
        HD = Dot(AC.get_projection(D.get_center()))

        HA_label = MathTex(r"H_a",font_size=30).next_to(HA.get_center(),DL,buff=0.12).set_z_index(-0.5)
        HB_label = MathTex(r"H_b",font_size=30).next_to(HB.get_center(),DR,buff=0.12).set_z_index(-0.5)
        HC_label = MathTex(r"H_c",font_size=30).next_to(HC.get_center(),UR,buff=0.12).set_z_index(-0.5)
        HD_label = MathTex(r"H_d",font_size=30).next_to(HD.get_center(),UL,buff=0.12).set_z_index(-0.5)

        Line_HA = Line(A.get_center(),HA.get_center(),color=RED)
        Line_HB = Line(B.get_center(),HB.get_center(),color=RED)
        Line_HC = Line(C.get_center(),HC.get_center(),color=RED)
        Line_HD = Line(D.get_center(),HD.get_center(),color=RED)

        Angle_HA = RightAngle(Line_HA,BD,length=0.15,color=YELLOW,quadrant=(-1,-1)).set_z_index(-1)
        Angle_HB = RightAngle(Line_HB,AC,length=0.15,color=YELLOW,quadrant=(-1,-1)).set_z_index(-1)
        Angle_HC = RightAngle(Line_HC,BD,length=0.15,color=YELLOW,quadrant=(-1,1)).set_z_index(-1)
        Angle_HD = RightAngle(Line_HD,AC,length=0.15,color=YELLOW,quadrant=(-1,1)).set_z_index(-1)


        label_4 = MathTex(r"\mathrm{Let's\,\, omit\,\, the\,\, perpendiculars\,\, on\,\, the\,\, diagonals}",font_size=40).to_edge(UP)

        self.play(LaggedStart(
            Write(label_4),
            AnimationGroup(
                Create(Line_HA),
                Create(Line_HB),
                Create(Line_HC),
                Create(Line_HD),
            ),
            AnimationGroup(
                GrowFromCenter(HA),
                GrowFromCenter(HB),
                GrowFromCenter(HC),
                GrowFromCenter(HD),
            ),
            lag_ratio=0.7,
            run_time=7
        ))
        self.play(
                Write(HA_label),
                Write(HB_label),
                Write(HC_label),
                Write(HD_label)
        )
        self.play(
            FadeIn(Angle_HA),
            FadeIn(Angle_HB),
            FadeIn(Angle_HC),
            FadeIn(Angle_HD),
            run_time=0.6
        )

        self.play(FadeOut(label_4))

        self.wait(0.2)

        label_5 = MathTex(r"\mathrm{Then\,\, the\,\, bases\,\, of\,\, the\,\, perpendiculars\,\, lie\,\, on\,\, the\,\, circle}",font_size=40).to_edge(UP)

        self.play(Write(label_5),run_time=1.5)
        self.play(
            FadeOut(Angle_HA),
            FadeOut(Angle_HB),
            FadeOut(Angle_HC),
            FadeOut(Angle_HD),
            run_time=0.4
        )
        self.play(
            AC.animate.set_opacity(0.3),
            BD.animate.set_opacity(0.3),
            Line_HA.animate.set_opacity(0.3),
            Line_HB.animate.set_opacity(0.3),
            Line_HC.animate.set_opacity(0.3),
            Line_HD.animate.set_opacity(0.3),
            HA_label.animate.set_opacity(0.4),
            HB_label.animate.set_opacity(0.4),
            HC_label.animate.set_opacity(0.4),
            HD_label.animate.set_opacity(0.4),
            run_time=1.5
        )
        Circle_result = Circle.from_three_points(
            HA.get_center(),
            HB.get_center(),
            HC.get_center(),
            color=RED_C
        ).set_z_index(-0.01)
        self.play(Create(Circle_result),run_time=1.3)
        
        self.wait(0.5)
        self.play(FadeOut(label_5))
        self.wait(0.1)

        self.play(
            FadeOut(A),
            FadeOut(B),
            FadeOut(C),
            FadeOut(D),
            FadeOut(A_label),
            FadeOut(B_label),
            FadeOut(C_label),
            FadeOut(D_label),
            FadeOut(polygon),
            FadeOut(AC),
            FadeOut(BD),
            FadeOut(HA),
            FadeOut(HB),
            FadeOut(HC),
            FadeOut(HD),
            FadeOut(HA_label),
            FadeOut(HB_label),
            FadeOut(HC_label),
            FadeOut(HD_label),
            FadeOut(Line_HA),
            FadeOut(Line_HB),
            FadeOut(Line_HC),
            FadeOut(Line_HD),
            FadeOut(circle),
            FadeOut(Circle_result),
            run_time=1.5
        )


        self.wait(2)

class Miquel_consequence_2(MovingCameraScene):
    def construct(self):
        def change_opacity_50(mob):
            mob.set_stroke(opacity=0.5)
            return mob

        label_1 = MathTex(r"\mathrm{The\,\, second\,\, consequence}",font_size=40).to_edge(UP)

        self.play(Write(label_1))
        self.wait(0.2)
        self.play(FadeOut(label_1))
        self.wait(0.5)

        A = Dot(2*DOWN+3*LEFT).set_z_index(2)
        B = Dot(2*UP+1.5*LEFT).set_z_index(2)
        C = Dot(2*DOWN+2*RIGHT).set_z_index(2)

        A_label = Tex('A',font_size=35).next_to(A.get_center(),DL,buff=0.17).set_z_index(99)
        B_label = Tex('B',font_size=35).next_to(B.get_center(),UP,buff=0.17).set_z_index(99)
        C_label = Tex('C',font_size=35).next_to(C.get_center(),DR,buff=0.17).set_z_index(99)

        AC = Line(A.get_center(),C.get_center()).set_opacity(0).set_z_index(0)
        AB = Line(A.get_center(),B.get_center()).set_opacity(0).set_z_index(0)
        BC = Line(B.get_center(),C.get_center()).set_opacity(0).set_z_index(0)

        ABC = Polygon(
            A.get_center(),
            B.get_center(),
            C.get_center(),
            color = BLUE_C
        ).set_z_index(0.95)

        label_2 = MathTex(r"\mathrm{Let's\,\, build\,\, a\,\, triangle\,\, ABC}",font_size=40).to_edge(UP)
        self.play(LaggedStart(
            Write(label_2),
            AnimationGroup(
                GrowFromCenter(A),
                GrowFromCenter(B),
                GrowFromCenter(C),
                Write(A_label),
                Write(B_label),
                Write(C_label),
            ),
            Create(ABC),
            lag_ratio=0.6,
            run_time=2.5
        ))
        self.add(AC,AB,BC)
        self.wait(0.2)
        self.play(FadeOut(label_2))


        label_3 = MathTex(r"\mathrm{The\,\, height\,\, and\,\, bisector\,\, are\,\, drawn\,\, from\,\, point\,\, B}",font_size=40).to_edge(UP)

        HB = Dot(AC.get_projection(B.get_center())).set_oapcity(1).set_z_index(1)
        HB_label = MathTex(r'\mathrm{H_b}',font_size=28).next_to(HB.get_center(),DOWN,buff=0.15).set_z_index(9)
        Line_HB = Line(B.get_center(),HB.get_center(),color=GREEN)
        Angle_HB = RightAngle(Line_HB,AC,length=0.15,quadrant=(-1,1),color=YELLOW).set_z_index(-0.01)

        Angle_B = Angle(Line(B.get_center(),A.get_center()),Line(B.get_center(),C.get_center())).get_value()

        Biss_len = (2*AB.get_length()*BC.get_length()*np.cos(Angle_B/2))/(AB.get_length()+AC.get_length())*0.97

        L = Dot(B.get_center()+np.array([Biss_len*1.5,0,0])).rotate(
            angle=-1*(Angle_B/2+Angle(Line(B.get_center(),C.get_center()),
                            Line(B.get_center(),(B.get_center()+RIGHT))).get_value()),
            about_point=B.get_center()               
        ).set_z_index(2).set_opacity(0)

        Biss = Line(B.get_center(),L.get_center(),color=YELLOW).set_z_index(0.55)
                 
        self.play(LaggedStart(
            Write(label_3),
            Create(Line_HB),
            AnimationGroup(
                GrowFromCenter(HB),
                Write(HB_label),
            ),
            AnimationGroup(
                Create(Biss),
                GrowFromCenter(L)
            ),
            lag_ratio=0.8,
            run_time=5
        ))

        Angle_B1 = Angle(Line(B.get_center(),A.get_center()),
                Line(B.get_center(),L.get_center()),radius=0.4,color=RED_B).set_z_index(0.01)
        Angle_B2 = Angle(Line(B.get_center(),L.get_center()),
                Line(B.get_center(),C.get_center()),radius=0.45,color=RED_B).set_z_index(0.01)
        
        self.play(
            Create(Angle_B1),
            Create(Angle_B2),
            FadeIn(Angle_HB)
        )

        self.play(FadeOut(label_3))
        self.wait(0.5)

        label_4 = MathTex(r"\mathrm{From\,\, points\,\, A\,\, and\,\, C\,\,, the\,\, perpendiculars\,\, were\,\, lowered\,\, onto\,\, the\,\, bisector}",font_size=40).to_edge(UP)

        HA = Dot(Biss.get_projection(A.get_center())).set_z_index(2)
        HA_label = MathTex(r'\mathrm{H_a}',font_size=28).next_to(HA.get_center(),RIGHT,buff=0.15).set_z_index(9)
        Line_HA = Line(A.get_center(),HA.get_center(),color=GREEN)
        Angle_HA = RightAngle(Line_HA,Biss,length=0.15,quadrant=(-1,1),color=YELLOW).set_z_index(-0.01)

        HC = Dot(Biss.get_projection(C.get_center())).set_z_index(2)
        HC_label = MathTex(r'\mathrm{H_c}',font_size=28).next_to(HC.get_center(),LEFT,buff=0.15).set_z_index(9)
        Line_HC = Line(C.get_center(),HC.get_center(),color=GREEN)
        Angle_HC = RightAngle(Line_HC,Biss,length=0.15,quadrant=(-1,1),color=YELLOW).set_z_index(-0.01)

        self.play(LaggedStart(
            Write(label_4),
            AnimationGroup(
                GrowFromCenter(HA),
                Write(HA_label),
                Create(Line_HA)
            ),
            AnimationGroup(
                GrowFromCenter(HC),
                Write(HC_label),
                FadeIn(Angle_HC),
                Create(Line_HC)
            ),
            lag_ratio=0.7,
            run_time=4
        ))
        self.play(FadeIn(Angle_HA),FadeIn(Angle_HC))

        self.wait(0.2)
        self.play(FadeOut(label_4))
        self.wait(0.2)

        label_5 =  MathTex(r"\mathrm{Denote\,\, the\,\, middle\,\, of\,\, the\,\, side\,\, AC}",font_size=40).to_edge(UP)

        M = Dot((A.get_center()+C.get_center())/2).set_z_index(3)
        M_label = MathTex(r'\mathrm{M}',font_size=28).next_to(M.get_center(),DR,buff=0.14).set_z_index(9)

        self.play(LaggedStart(
            Write(label_5),
            AnimationGroup(
                GrowFromCenter(M),
                Write(M_label)
            ),
            lag_ratio=0.7,
            run_time=2.5
        ))

        self.wait(0.5)
        self.play(FadeOut(label_5))
        self.wait(0.2)

        label_6 =  MathTex(r"\mathrm{Then\,\, H_a,H_b,H_c\,\, and\,\, M\,\, lie\,\, on\,\, the\,\, same\,\, circle}",font_size=40).to_edge(UP)

        self.play(LaggedStart(
            Write(label_6),
            AnimationGroup(
                Biss.animate.set_opacity(0.5),
                Line_HA.animate.set_opacity(0.5),
                Line_HC.animate.set_opacity(0.5),
                Line_HB.animate.set_opacity(0.5),
                HC.animate.set_opacity(0.7),
                HA.animate.set_opacity(0.7),
                HB.animate.set_opacity(0.7),
                HC_label.animate.set_opacity(0.7),
                HA_label.animate.set_opacity(0.7),
                HB_label.animate.set_opacity(0.7),
                M.animate.set_opacity(0.7),
                M_label.animate.set_opacity(0.7),
            ),
            lag_ratio = 0.8,
            run_time=2.5
        ))

        self.play(
            ApplyFunction(change_opacity_50,Angle_HB),
            ApplyFunction(change_opacity_50,Angle_HA),
            ApplyFunction(change_opacity_50,Angle_HC),
            run_time=0.6
        )

        circle = Circle.from_three_points(
            HA.get_center(),
            HB.get_center(),
            HC.get_center(),
        )

        self.play(Create(circle),run_time=1.5)

        ALL = VGroup(
            A,B,C,
            A_label,B_label,C_label,
            ABC,
            AB,AC,BC,
            Angle_B1,Angle_B2,
            HA,HB,HC,
            HA_label,HB_label,HC_label,
            Line_HA,Line_HB,Line_HC,
            Angle_HA,Angle_HB,Angle_HC,
            M,M_label,circle,Biss
        )

        self.wait(0.5)
        self.play(FadeOut(label_6))
        self.wait(0.5)
        self.play(FadeOut(ALL))
        self.wait()

