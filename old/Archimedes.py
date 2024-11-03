from manim import * 
import numpy as np

class Title_lemma(Scene):
    def construct(self):
        title = Tex("Archimedes' lemma",font_size=120)
        self.add(title)

class Title_Criteria(Scene):
    def construct(self):
        title = Tex("Archimedes' criteria",font_size=120)
        self.add(title)
        
class Lemma(Scene):
    def construct(self):
        def change_opacity_50(mob):
            mob.set_stroke(opacity=0.5)
            return mob
        
        title = Tex("Archimedes' lemma",font_size=100)

        self.play(Write(title),run_time=1.5)
        self.wait(0.5)
        self.play(FadeOut(title))
        self.wait(0.3)

        rad = 2.5

        label_1 = MathTex(r"\mathrm{Let's\,\, build\,\, a\,\, circle}").to_edge(UP)

        Circle_1 = Circle(radius=rad,color=BLUE_C).move_to(0.7*DOWN)

        self.play(LaggedStart(
            Write(label_1),
            Create(Circle_1),
            lag_ratio=0.7,
            run_time=3
        ))
        self.wait(0.5)
        self.play(FadeOut(label_1))
        self.wait(0.5)

        M = Dot(Circle_1.point_at_angle(0.1*PI)).set_z_index(9)
        N = Dot(Circle_1.point_at_angle(0.9*PI)).set_z_index(9)

        M_label = MathTex(r"\mathrm{M}",font_size=35).next_to(M.get_center(),UR,buff=0.12)
        N_label = MathTex(r"\mathrm{N}",font_size=35).next_to(N.get_center(),UL,buff=0.12)

        label_2 = MathTex(r"\mathrm{Let's\,\, draw\,\, a\,\, chord\,\, MN}").to_edge(UP)

        MN = Line(M.get_center(),N.get_center(),color=GREEN)

        self.play(LaggedStart(
            Write(label_2),
            AnimationGroup(
                GrowFromCenter(M),
                GrowFromCenter(N)
            ),
            AnimationGroup(
                Write(M_label),
                Write(N_label)
            ),
            Create(MN),
            lag_ratio=0.7,
            run_time=5
        ))
        self.wait(0.5)
        self.play(FadeOut(label_2))
        self.wait(0.5)

        MN_half = Dot((M.get_center()+N.get_center())/2).set_opacity(0)
        Sector_dot = Dot(Circle_1.point_at_angle(0.4*PI)).set_opacity(0)
        Sector_line = Line(MN_half.get_center(),Sector_dot.get_center()).set_opacity(0)

        Angle_for_tangent = Angle(
            Line(MN_half.get_center(),M.get_center()),
            Line(MN_half.get_center(),Sector_dot.get_center())
        ).get_value() + Angle(
            Line(MN_half.get_center(),Sector_dot.get_center()),
            Line(MN_half.get_center(),N.get_center())
        ).get_value()/2

        Tangent = Dot(Circle_1.get_center()+np.array([rad,0,0])).rotate(
            about_point=Circle_1.get_center(),
            angle = Angle_for_tangent
        ).set_opacity(0)

        Tangent_Line = TangentLine(Circle_1,alpha=Angle_for_tangent/TAU,length=6).set_opacity(0)
        Tangent_intersection_1 = Dot(
            line_intersection(
                np.array([M.get_center(),N.get_center()]),
                np.array([Tangent.get_center(),
                          Dot(Circle_1.get_center()).rotate(
                                about_point = Tangent.get_center(),
                                angle = -PI/2
                          ).get_center()])
            )
        ).set_opacity(0).set_z_index(1)

        Tangent_intersection_2 = Dot(
            line_intersection(
                np.array([MN_half.get_center(),Sector_dot.get_center()]),
                np.array([Tangent.get_center(),
                          Dot(Circle_1.get_center()).rotate(
                                about_point = Tangent.get_center(),
                                angle = -PI/2
                          ).get_center()])
            )
        ).set_opacity(0)

        Biss_1 = Line(MN_half.get_center(),Tangent.get_center()).set_opacity(0)
        Biss_2 = Line(Tangent_intersection_1.get_center(),
                      Dot(Tangent_intersection_2.get_center()).rotate(
                        about_point = Tangent_intersection_1.get_center(),
                        angle = -Angle(
                            Line(Tangent_intersection_1.get_center(),
                                 M.get_center()),
                            Line(Tangent_intersection_1.get_center(),
                                 Tangent_intersection_2.get_center()),
                        ).get_value()/2
                      ).get_center()).set_opacity(0)
        
        I = Dot(
            line_intersection(
                np.array([
                    MN_half.get_center(),Tangent.get_center()
                ]),
                np.array([
                    Tangent_intersection_1.get_center(),
                    Dot(Tangent_intersection_2.get_center()).rotate(
                        about_point = Tangent_intersection_1.get_center(),
                        angle = -Angle(
                            Line(Tangent_intersection_1.get_center(),
                                 M.get_center()),
                            Line(Tangent_intersection_1.get_center(),
                                 Tangent_intersection_2.get_center()),
                        ).get_value()/2
                      ).get_center()
                ])
            )+np.array([-0.135,-0.04,0])
        ).set_opacity(0)   

        Circle_inner = Circle(radius=Line(
            I.get_center(),MN.get_projection(I.get_center())
        ).get_length()*0.965).move_to(I.get_center()).set_z_index(-99)  


        self.add(MN_half,Sector_dot,Sector_line,Tangent,Tangent_Line)
        self.add(Tangent_intersection_1,Tangent_intersection_2)
        self.add(Biss_1,Biss_2,I)

        A = Dot(Tangent.get_center()).set_z_index(7)

        AN = Line(A.get_center(),N.get_center(),color=YELLOW)
        AM = Line(A.get_center(),M.get_center(),color=YELLOW)

        Angle_NAM = Angle(AN,AM).set_opacity(0)
        self.add(Angle_NAM)

        For_B = Dot(N.get_center()).rotate(
            about_point = A.get_center(),
            angle = Angle_NAM.get_value()/2+0.03)
        
        B = Dot(line_intersection(
            np.array([A.get_center(),For_B.get_center()]),
            np.array([M.get_center(),N.get_center()])
        ))
        
        A_label = MathTex(r"\mathrm{A}",font_size=35).next_to(A.get_center(),UP,buff=0.2)
        B_label = MathTex(r"\mathrm{B}",font_size=35).next_to(B.get_center(),DR,buff=0.2)

        self.wait(0.4)
        
        label_3 = MathTex(r"\mathrm{Let's\,\, draw\,\, a\,\, circle\,\, that\,\, touches\,\, the\,\, chord\,\, and\,\, another\,\, circle\,\,}").to_edge(UP)

        self.play(Write(label_3))
        self.play(Create(Circle_inner))
        self.play(FadeIn(A),FadeIn(B))
        self.play(Write(A_label),Write(B_label))
        self.wait(0.3)
        self.play(FadeOut(label_3))

        label_4 = MathTex(r"\mathrm{A\,\, and\,\, B\,\, are\,\, the\,\, points\,\, of\,\, tangency}").to_edge(UP)
        
        self.wait(0.2)
        self.play(Write(label_4))
        self.wait(0.5)
        self.play(FadeOut(label_4))

        AB = Line(A.get_center(),B.get_center(),color=RED_D).set_z_index(-1)

        Angle_NAB = Angle(
            Line(A.get_center(),N.get_center()),
            Line(A.get_center(),B.get_center()),
            color=GREEN_C, radius=0.3
        ).set_z_index(-9)

        Angle_BAM = Angle(
            Line(A.get_center(),B.get_center()),
            Line(A.get_center(),M.get_center()),
            color=GREEN_C, radius=0.34
        ).set_z_index(-9)

        label_5 = MathTex(r"\mathrm{Then\,\, AB\,\, is\,\, the\,\, bisector\,\, of\,\,}\,\,\angle{NAM}").to_edge(UP)
        
        self.play(LaggedStart(
            Write(label_5),
            ApplyFunction(change_opacity_50,Circle_inner),
            lag_ratio=0.4,
            run_time=1.5
        ))
        self.play(Create(AB))
        self.play(Create(AN), Create(AM))
        self.play(FadeIn(Angle_NAB),FadeIn(Angle_BAM))
        self.wait(0.5)
        self.play(FadeOut(label_5))
        self.wait(0.3)

        label_6 = MathTex(r"\mathrm{Let's\,\, prove\,\, it}").to_edge(UP)

        self.play(Write(label_6))
        self.wait(0.3)
        self.play(FadeOut(label_6),
                  A_label.animate.set_opacity(0.7),
                  B_label.animate.set_opacity(0.7),
                  N_label.animate.set_opacity(0.7),
                  M_label.animate.set_opacity(0.7))
        self.wait(0.4)

        label_7 = MathTex(r"\mathrm{Let's\,\, draw\,\, a\,\, tangent\,\, to\,\, the\,\, point\,\, of\,\, tangency\,\, of\,\, the\,\, circles\,\, }").to_edge(UP)

        self.play(Write(label_7))
        Tangent_show = Tangent_Line.copy().set_opacity(1).set_color(GREEN).set_length(5.2)
        self.play(Create(Tangent_show))
        self.wait(0.3)
        self.play(FadeOut(label_7))
        self.wait(0.4)

        K = Tangent_intersection_1.copy().set_opacity(1)
        K_label = MathTex(r"\mathrm{K}",font_size=35).next_to(K.get_center(),LEFT,buff=0.12).set_opacity(0.7)


        label_8 = MathTex(r"\mathrm{Extend\,\, MN\,\, to\,\, the\,\, intersection\,\, with\,\, the\,\, tangent\,\, at\,\, point\,\, K}").to_edge(UP)
        self.play(Write(label_8))
        NM_extend = Line(N.get_center(),Tangent_intersection_1.get_center(),color=GREEN).set_z_index(-1)
        self.play(Create(NM_extend),
                 FadeIn(K),Write(K_label))
        self.wait(0.3)
        self.play(FadeOut(label_8))
        self.wait(0.3)

        label_9 = MathTex(r"\mathrm{Let}\,\,\angle{KAN}=\alpha\,\,\mathrm{and}\,\,\angle{NAB}=\beta").to_edge(UP)

        Angle_KAN = Angle(
            Line(A.get_center(),K.get_center()),
            Line(A.get_center(),N.get_center()),
            color = GREEN,radius=0.4
        )

        Angle_KAN_label = MathTex(r"\alpha",font_size=33).move_to(A.get_center()+np.array([-0.52,-0.47,0]))
        Angle_NAB_label = MathTex(r"\beta",font_size=33).move_to(A.get_center()+np.array([-0.1,-0.55,0]))


        self.play(Write(label_9))
        self.play(
            AN.animate.set_opacity(0.6),
            AM.animate.set_opacity(0.6),
            ApplyFunction(change_opacity_50, Circle_1)
        )
        self.play(FadeIn(Angle_KAN))
        self.play(Write(Angle_KAN_label),Write(Angle_NAB_label))
        self.wait(0.3)
        self.play(FadeOut(label_9))
        self.wait(0.3)

        label_10 = MathTex(r"\mathrm{KA\,\, and\,\, KB\,\, are\,\, tangent\,\, segments,\,\, so\,\, they\,\, are\,\, equal\,\,}").to_edge(UP)
        self.play(Write(label_10),run_time=2.4)
        self.wait()
        self.play(FadeOut(label_10))
        self.wait(0.3)

        label_11 = MathTex(r"\mathrm{Therefore}\,\, \angle{KAB}=\angle{KBA}").to_edge(UP)
        Angle_KBA = Angle(
            Line(B.get_center(),A.get_center()),
            Line(B.get_center(),K.get_center()),
            radius=0.35, color=GREEN
        )
        Angle_KBA_label = MathTex(r"\alpha+\beta",font_size=30).move_to(B.get_center()+np.array([-0.65,0.33,0]))
        self.play(Write(label_11))
        self.play(FadeIn(Angle_KBA),Write(Angle_KBA_label))
        self.wait(0.4)
        self.play(FadeOut(label_11))
        self.wait(0.3)

        label_12 = MathTex(r"\mathrm{Note\,\, that\,\, the\,\, angles}\,\,\angle{KAN}\,\,\mathrm{and}\,\,\angle{AMB}\,\,\mathrm{are\,\, equal}").to_edge(UP)
        Angle_BMA = Angle(
            Line(M.get_center(),A.get_center()),
            Line(M.get_center(),B.get_center()),
            radius=0.51,color=GREEN
        )
        Angle_BMA_label = MathTex(r"\alpha",font_size=30).move_to(M.get_center()+np.array([-0.75,0.15,0]))

        self.play(Write(label_12),run_time=2)
        self.play(FadeIn(Angle_BMA),Write(Angle_BMA_label))
        self.wait()
        self.play(FadeOut(label_12))
        self.wait(0.4)

        label_12 = MathTex(r"\mathrm{As\,\, a\,\, result,}\,\,\angle{BAM}=\beta").to_edge(UP)
        Angle_BAM_label = MathTex(r"\beta",font_size=33).move_to(A.get_center()+np.array([0.38,-0.43,0]))

        self.play(Write(label_12))
        self.play(Write(Angle_BAM_label))
        self.wait(0.4)

        self.play(
            FadeOut(Angle_KAN_label),
            FadeOut(Angle_BMA_label),
            FadeOut(Angle_KBA_label),
            FadeOut(Angle_KAN),
            FadeOut(Angle_BMA),
            FadeOut(Angle_KBA),
        )
        self.play(FadeOut(label_12))
        self.wait(0.3)

        label_13 = MathTex(r"\mathrm{So\,\, AB\,\ is\,\ a\,\ bisector}").to_edge(UP)
        self.play(Write(label_13),run_time=1.3)
        self.wait(2)
        self.play(FadeOut(label_13))

        ALL = VGroup(
            A,B,Circle_1,K,N,M,AN,AM,Tangent_show,MN,NM_extend,Angle_NAB,Angle_BAM,
            Angle_NAB_label,Angle_BAM_label,Circle_inner,A_label,B_label,M_label,N_label,K_label,AB
        )

        self.play(FadeOut(ALL))
        self.wait(6)

class Criteria_1(Scene):
    def construct(self):
        title = MathTex(r"\mathrm{Archimedes'\,\, criteria}",font_size=100)
        self.play(Write(title),run_time=1.5)
        self.wait()
        self.play(FadeOut(title))
        self.wait()

        label_1 = MathTex(r"\mathrm{Let's\,\, construct\,\, a\,\, circle\,\, \Omega\,\, and\,\, a\,\, chord\,\, MN}").to_edge(UP)

        rad = 2

        Circle_Omega = Circle(radius=rad,color=BLUE)
        Omega_label = MathTex(r"\mathrm{\Omega}}",font_size=35).move_to(np.array([2.2,-0.4,0]))

        M = Dot(Circle_Omega.point_at_angle(0.1*PI)).set_z_index(9)
        N = Dot(Circle_Omega.point_at_angle(0.9*PI)).set_z_index(9)

        M_label = MathTex(r"\mathrm{M}",font_size=35).next_to(M.get_center(),UR,buff=0.12)
        N_label = MathTex(r"\mathrm{N}",font_size=35).next_to(N.get_center(),UL,buff=0.12)

        MN = Line(M.get_center(),N.get_center(),color=RED)

        self.play(Write(label_1))
        self.play(LaggedStart(
            Create(Circle_Omega),
            FadeIn(Omega_label),
            AnimationGroup(
                GrowFromCenter(M),
                GrowFromCenter(N),
            ),
            AnimationGroup(
                GrowFromCenter(M_label),
                GrowFromCenter(N_label),
            ),
            Create(MN),
            lag_ratio=0.7,
            run_time=4
        ))
        self.wait(0.2)
        self.play(FadeOut(label_1))
        self.wait(0.6)

        MN_half = Dot((M.get_center()+N.get_center())/2).set_opacity(0)
        Sector_dot = Dot(Circle_Omega.point_at_angle(0.4*PI)).set_opacity(0)
        Sector_line = Line(MN_half.get_center(),Sector_dot.get_center()).set_opacity(0)

        Angle_for_tangent = Angle(
            Line(MN_half.get_center(),M.get_center()),
            Line(MN_half.get_center(),Sector_dot.get_center())
        ).get_value() + Angle(
            Line(MN_half.get_center(),Sector_dot.get_center()),
            Line(MN_half.get_center(),N.get_center())
        ).get_value()/2

        Tangent = Dot(Circle_Omega.get_center()+np.array([rad,0,0])).rotate(
            about_point=Circle_Omega.get_center(),
            angle = Angle_for_tangent
        ).set_opacity(0)

        Tangent_Line = TangentLine(Circle_Omega,alpha=Angle_for_tangent/TAU,length=6).set_opacity(0)
        Tangent_intersection_1 = Dot(
            line_intersection(
                np.array([M.get_center(),N.get_center()]),
                np.array([Tangent.get_center(),
                          Dot(Circle_Omega.get_center()).rotate(
                                about_point = Tangent.get_center(),
                                angle = -PI/2
                          ).get_center()])
            )
        ).set_opacity(0).set_z_index(1)

        Tangent_intersection_2 = Dot(
            line_intersection(
                np.array([MN_half.get_center(),Sector_dot.get_center()]),
                np.array([Tangent.get_center(),
                          Dot(Circle_Omega.get_center()).rotate(
                                about_point = Tangent.get_center(),
                                angle = -PI/2
                          ).get_center()])
            )
        ).set_opacity(0)

        Biss_1 = Line(MN_half.get_center(),Tangent.get_center()).set_opacity(0)
        Biss_2 = Line(Tangent_intersection_1.get_center(),
                      Dot(Tangent_intersection_2.get_center()).rotate(
                        about_point = Tangent_intersection_1.get_center(),
                        angle = -Angle(
                            Line(Tangent_intersection_1.get_center(),
                                 M.get_center()),
                            Line(Tangent_intersection_1.get_center(),
                                 Tangent_intersection_2.get_center()),
                        ).get_value()/2
                      ).get_center()).set_opacity(0)
        
        I = Dot(
            line_intersection(
                np.array([
                    MN_half.get_center(),Tangent.get_center()
                ]),
                np.array([
                    Tangent_intersection_1.get_center(),
                    Dot(Tangent_intersection_2.get_center()).rotate(
                        about_point = Tangent_intersection_1.get_center(),
                        angle = -Angle(
                            Line(Tangent_intersection_1.get_center(),
                                 M.get_center()),
                            Line(Tangent_intersection_1.get_center(),
                                 Tangent_intersection_2.get_center()),
                        ).get_value()/2
                      ).get_center()
                ])
            )+np.array([-0.135,-0.04,0])
        ).set_opacity(0)   

        Circle_omega = Circle(radius=Line(
            I.get_center(),MN.get_projection(I.get_center())
        ).get_length()*0.965,color=YELLOW).move_to(I.get_center()).set_z_index(-99)  
        self.add(MN_half,Sector_dot,Sector_line,Tangent_intersection_1,Tangent_intersection_2,
                 Tangent_Line,Tangent,Biss_1,Biss_2,I)
        
        Circle_omega_label = MathTex(r"\mathrm{\omega}",font_size=35).move_to(np.array([-0.1,1.6,0]))

        A = Dot(Tangent.get_center()).set_z_index(7)

        AN = Line(A.get_center(),N.get_center(),color=YELLOW)
        AM = Line(A.get_center(),M.get_center(),color=YELLOW)

        Angle_NAM = Angle(AN,AM).set_opacity(0)

        For_B = Dot(N.get_center()).rotate(
            about_point = A.get_center(),
            angle = Angle_NAM.get_value()/2+0.03)

        B = Dot(line_intersection(
            np.array([A.get_center(),For_B.get_center()]),
            np.array([M.get_center(),N.get_center()])
        ))

        A_label = MathTex(r"\mathrm{A}",font_size=35).next_to(A.get_center(),UP,buff=0.2)
        B_label = MathTex(r"\mathrm{B}",font_size=35).next_to(B.get_center(),DR,buff=0.15)

        label_2 = MathTex(r"\mathrm{The\,\, circle\,\, \omega\,\, touches\,\, the\,\, MN\,\, chord\,\, at\,\, point\,\, B}").to_edge(UP)
        self.play(Write(label_2),run_time=1.5)
        self.play(Create(Circle_omega),FadeIn(Circle_omega_label))
        self.wait(0.3)
        self.play(LaggedStart(
            FadeIn(B),
            FadeIn(B_label),
            FadeOut(label_2),
            lag_ratio=0.8,
            run_time=2.5
        ))
        self.wait(0.8)

        L = Dot(Circle_Omega.point_at_angle(3*PI/2))
        L_label = MathTex(r"\mathrm{L}",font_size=35).next_to(L.get_center(),DR,buff=0.15)
        Circle_omega_star = Circle(radius=Line(
            L.get_center(),M.get_center()).get_length()
        ,color=GREEN).move_to(L.get_center()).set_stroke(opacity=0.5)

        Circle_omega_star_label = MathTex(r"\mathrm{\omega^*}",font_size=35).move_to(np.array([3.55,-2,0]))

        label_3 = MathTex(r"\mathrm{L\,\, is\,\, the\,\, center\,\, of\,\, the\,\, arc\,\, MN}").to_edge(UP)

        self.play(LaggedStart(
            Write(label_3),
            FadeIn(L),
            FadeIn(L_label),
            lag_ratio = 0.8,
            run_time=3
        ))
        self.wait(0.3)
        self.play(FadeOut(label_3))
        self.wait(0.6)


        label_4 = MathTex(r"\mathrm{A\,\, circle\,\, \omega^*\,\, with\,\, center\,\, L\,\, and\,\, radius\,\, LM\,\, is\,\, constructed}").to_edge(UP)
        self.play(Write(label_4),run_time=1.5)
        self.play(LaggedStart(
            Create(Circle_omega_star),
            FadeIn(Circle_omega_star_label),
            lag_ratio=0.6,
            run_time=1.5
        ))
        self.wait(0.7)
        self.play(FadeOut(label_4))

        label_5 = MathTex(r"\mathrm{Note\,\, that\,\, circles\,\, \omega\,\, and\,\, \omega^*\,\, are\,\, perpendicular}").to_edge(UP)
   
        self.play(Write(label_5))
        self.wait()
        self.play(FadeOut(label_5))
        self.wait(0.3)

        label_6 = MathTex(r"\mathrm{Then\,\, the\,\, circle\,\, \omega\,\, touches\,\, the\,\, circle\,\, \Omega}").to_edge(UP)
        self.play(LaggedStart(
            Write(label_6),
            FadeIn(A),
            FadeIn(A_label),
            lag_ratio=0.7,
            run_time=4
        ))
        self.wait()
        self.play(FadeOut(label_6))
        label_7 = MathTex(r"\mathrm{To\,\, prove\,\ it,\,\, we\,\ first\,\ formulate\,\ an\,\ auxiliary\,\ statement}").to_edge(UP)
        self.play(Write(label_7),run_time=1.5)
        self.wait(1.6)
        ALL = VGroup(
            A,M,N,B,Circle_Omega,Circle_omega,Circle_omega_star,
            A_label,M_label,N_label,B_label,Omega_label,Circle_omega_label,Circle_omega_star_label,
            L,L_label,MN
        )
        self.play(FadeOut(label_7))
        self.play(FadeOut(ALL))
        self.wait(1.4)

class Auxiliary_Statement(Scene):
    def construct(self):
        def circle_intersections(Circle_1,Circle_2,Radius_1,Radius_2):
            O1 = Circle_1.get_center()
            O2 = Circle_2.get_center()
            L = Line(O1,O2).get_length()
            try:
                Angle_1 = -Angle(
                    Line(O1,O2),
                    Line(O1,O1+RIGHT)).get_value()
            except:
                Angle_1 = 0
            
            X = Dot(np.array(O1+[Radius_1,0,0])).rotate(
                about_point = O1,
                angle = Angle_1+np.arccos((Radius_2**2-Radius_1**2-L**2)/(-2*Radius_1*L)))
            Y = Dot(np.array(O1+[Radius_1,0,0])).rotate(
                about_point = O1,
                angle = Angle_1-np.arccos((Radius_2**2-Radius_1**2-L**2)/(-2*Radius_1*L)))
            return X,Y
        
        def change_opacity_50(mob):
            mob.set_stroke(opacity=0.5)
            return mob
        
        def change_opacity_70(mob):
            mob.set_stroke(opacity=0.7)
            return mob
        
        def change_opacity_100(mob):
            mob.set_stroke(opacity=1)
            return mob
        
        Radius_1 = 1
        Radius_2 = 1.5

        Circle_1 = Circle(radius=Radius_1,color=BLUE).move_to(LEFT+UP)
        Circle_2 = Circle(radius=Radius_2,color=BLUE).move_to(RIGHT+UP)

        Circle_1_label = MathTex(r"\mathrm{\omega_1}",font_size=35).move_to(np.array([-2.27,1,0]))
        Circle_2_label = MathTex(r"\mathrm{\omega_2}",font_size=35).move_to(np.array([2.85,0.8,0]))

        A,B = circle_intersections(Circle_1,Circle_2,Radius_1,Radius_2)

        A.set_z_index(7)
        B.set_z_index(7)

        A_label = MathTex(r"\mathrm{A}",font_size=35).next_to(A.get_center(),UP,buff=0.2)
        B_label = MathTex(r"\mathrm{B}",font_size=35).next_to(B.get_center(),DOWN,buff=0.2)

        O1 = Dot(Circle_1.get_center()).set_z_index(9)
        O2 = Dot(Circle_2.get_center()).set_z_index(9)

        O1_label = MathTex(r"\mathrm{O_1}",font_size=30).next_to(O1.get_center(),UL,buff=0.15)
        O2_label = MathTex(r"\mathrm{O_2}",font_size=30).next_to(O2.get_center(),UR,buff=0.15)


        label_1 = MathTex(r"\mathrm{Circles\,\, \omega_1\,\, and\,\, \omega_2\,\, intersect\,\, at\,\, points\,\, A\,\, and\,\, B}").to_edge(UP)

        self.play(LaggedStart(
            Write(label_1),
            Create(Circle_1),
            Create(Circle_2),
            AnimationGroup(
                FadeIn(Circle_1_label),
                FadeIn(Circle_2_label),
            ),
            AnimationGroup(
                FadeIn(O1),
                FadeIn(O2),
                FadeIn(O1_label),
                FadeIn(O2_label),
            ),
            AnimationGroup(
                FadeIn(A),
                FadeIn(B),
            ),
            AnimationGroup(
                FadeIn(A_label),
                FadeIn(B_label),
            ),
            lag_ratio=0.7,
            run_time=7
        ))
        self.wait(0.3)
        self.play(FadeOut(label_1))

        label_2 = MathTex(r"\mathrm{Let's\,\, construct\,\, a\,\, circle\,\, \omega_3\,\, centered\,\, on\,\, AB}").to_edge(UP)

        AB = Line(A.get_center(),B.get_center(),color=YELLOW).set_opacity(0.4).set_length(10)

        Radius_3 = 2
        Circle_3 = Circle(radius = Radius_3,color=GREEN).move_to(A.get_center()+3*DOWN)
        Circle_3_label =  MathTex(r"\mathrm{\omega_3}",font_size=35).move_to(np.array(
            [A.get_center()+2.9*DOWN+2.3*RIGHT]))

        O3 = Dot(Circle_3.get_center()).set_z_index(9)
        O3_label =  MathTex(r"\mathrm{O_3}",font_size=30).next_to(O3.get_center(),LEFT,buff=0.15)

        self.play(Write(label_2),run_time=1.5)
        self.play(LaggedStart(
            Create(AB),
            Create(Circle_3),
            FadeIn(Circle_3_label),
            lag_ratio=0.7,
            run_time=2
        ))
        self.play(FadeIn(O3),
                FadeIn(O3_label))
        self.play(FadeOut(AB),FadeOut(label_2))
        
        
        _,C = circle_intersections(Circle_1,Circle_3,Radius_1,Radius_3)
        C_label = MathTex(r"\mathrm{C}",font_size=35).next_to(C.get_center(),LEFT,buff=0.2).set_z_index(100)
        C.set_z_index(99)
        
        CO1 = Line(C.get_center(),O1.get_center(),color=YELLOW)
        CO3 = Line(C.get_center(),O3.get_center(),color=YELLOW)

        Angle_O1CO3 = RightAngle(
            CO3,
            CO1,
            color=RED,
            length=0.25
        ).set_z_index(-1)

        label_3 = MathTex(r"\mathrm{The\,\, circles\,\, \omega_1\,\, and\,\, \omega_3\,\, are\,\, perpendicular}").to_edge(UP)
        
        self.play(Write(label_3),run_time=1.5)
        self.play(LaggedStart(
            FadeIn(C),
            FadeIn(C_label),
            Create(CO1),
            Create(CO3),
            AnimationGroup(
                ApplyFunction(change_opacity_50,Circle_1),
                ApplyFunction(change_opacity_50,Circle_2),
                ApplyFunction(change_opacity_50,Circle_3),
            ),
            lag_ratio=0.6,
            run_time=3.5
        ))
        
        self.play(FadeIn(Angle_O1CO3))
        self.play(LaggedStart(
            AnimationGroup(
                ApplyFunction(change_opacity_100,Circle_1),
                ApplyFunction(change_opacity_100,Circle_2),
                ApplyFunction(change_opacity_100,Circle_3),
            ),
            ApplyFunction(change_opacity_50,Angle_O1CO3),
            AnimationGroup(
                ApplyFunction(change_opacity_50,CO1),
                ApplyFunction(change_opacity_50,CO3),
            ),
            FadeOut(label_3),
            lag_ratio=0.7,
            run_time=3.5
        ))

        label_3 = MathTex(r"\mathrm{Then\,\, the\,\, circles\,\, \omega_2\,\, and\,\, \omega_3\,\, are\,\, perpendicular}").to_edge(UP)

        D,_ = circle_intersections(Circle_2,Circle_3,Radius_2,Radius_3)
        D.set_z_index(80)
        D_label = MathTex(r"\mathrm{D}",font_size=35).next_to(D.get_center(),RIGHT+0.01*DOWN,buff=0.2).set_z_index(100)
        
        DO2 = Line(D.get_center(),O2.get_center(),color=YELLOW)
        DO3 = Line(D.get_center(),O3.get_center(),color=YELLOW)

        Angle_O2DO3 = RightAngle(
            DO2,DO3,
            length=0.25,color=RED
        ).set_z_index(-1)

        self.play(Write(label_3),run_time=1.5)
        self.play(LaggedStart(
            FadeIn(D),
            FadeIn(D_label),
            Create(DO2),
            Create(DO3),
            lag_ratio=0.6,
            run_time=2.5
        ))
        self.play(FadeIn(Angle_O2DO3))
        self.wait(0.2)
        self.play(FadeOut(label_3))
        self.wait()

        label_4 = MathTex(r"\mathrm{Let's\,\, prove\,\, it}").to_edge(UP)
        self.play(Write(label_4))
        self.play(FadeOut(DO2),
                  FadeOut(DO3),
                  FadeOut(Angle_O2DO3))
        self.wait(0.5)
        self.play(FadeOut(label_4))

        O1O3 = Line(O1.get_center(),O3.get_center(),color=YELLOW)


        label_6 = MathTex(r"\mathrm{By\,\, the\,\, Pythagorean\,\, theorem\,\, O_1O_3^2 - O_1C^2 = O_3C^2}").to_edge(UP)
        self.play(Write(label_6),run_time=1.5)
        self.wait(0.2)
        self.play(LaggedStart(
            AnimationGroup(
                ApplyFunction(change_opacity_50,Circle_1),
                ApplyFunction(change_opacity_50,Circle_2),
                ApplyFunction(change_opacity_50,Circle_3),
            ),
            ApplyFunction(change_opacity_100,CO3),
            ApplyFunction(change_opacity_100,CO1),
            ApplyFunction(change_opacity_100,Angle_O1CO3),
            Create(O1O3),
            lag_ratio=0.8,
            run_time=3
        ))
        self.wait(2)
        self.play(LaggedStart(
            AnimationGroup(
                ApplyFunction(change_opacity_100,Circle_1),
                ApplyFunction(change_opacity_100,Circle_2),
                ApplyFunction(change_opacity_100,Circle_3),
            ),
            ApplyFunction(change_opacity_50,CO3),
            ApplyFunction(change_opacity_50,CO1),
            ApplyFunction(change_opacity_50,Angle_O1CO3),
            FadeOut(O1O3),
            lag_ratio=0.8,
            run_time=3
        ))
        self.wait(0.5)
        self.play(FadeOut(label_6))
        self.wait(0.5)

        label_7 = MathTex(r"\mathrm{Also\,\, O_3C = O_3D\,\, as\,\, radiuses}").to_edge(UP)
        self.play(Write(label_7))
        self.play(ApplyFunction(change_opacity_100,CO3))
        self.play(FadeIn(DO3))
        self.wait(0.6)
        self.play(FadeOut(label_7))
        self.wait()
    
        label_8 = MathTex(r"\mathrm{AB\,\, is\,\, the\,\, radical\,\, axis\,\, of\,\, \omega_1\,\, and\,\, \omega_2}").to_edge(UP)
        self.play(Write(label_8),run_time=1.3)
        self.play(Create(AB))
        self.wait(0.3)
        self.play(FadeOut(label_8))

        O2O3 = Line(O2.get_center(),O3.get_center(),color=YELLOW)

        label_9 = MathTex(r"\mathrm{Therefore\,\, O_3D^2 = O_3O_2^2 - O_2D^2}").to_edge(UP)
        self.play(Write(label_9),run_time=1.5)
        self.play(LaggedStart(
            Create(DO2),
            Create(O2O3),
            lag_ratio=0.7,
            run_time=2.4
        ))
        self.play(FadeOut(AB))
        self.wait()
        self.play(FadeOut(label_9))
        self.wait()

        label_10 = MathTex(r"\mathrm{So\,\, the\,\, circles\,\, \omega_2\,\, and\,\, \omega_3\,\, are\,\, perpendicular}").to_edge(UP)
        Angle_O3DO2 = RightAngle(
            Line(O3.get_center(),D.get_center()),
            Line(D.get_center(),O2.get_center()),
            length=0.25, color=RED, quadrant=(-1,1)
        ).set_z_index(-1)
        self.play(Write(label_10),run_time=1.3)
        self.play(
            ApplyFunction(change_opacity_70,Circle_1),
            ApplyFunction(change_opacity_70,Circle_2),
            ApplyFunction(change_opacity_70,Circle_3),
        )
        self.play(FadeOut(O2O3))
        self.play(ApplyFunction(change_opacity_100,CO1))
        self.play(ApplyFunction(change_opacity_100,Angle_O1CO3))
        self.play(FadeIn(Angle_O3DO2))
        self.wait(1.5)
        self.play(FadeOut(label_10))
        self.wait()

        ALL = VGroup(
            Circle_1,Circle_2,Circle_3,
            Circle_1_label,Circle_2_label,Circle_3_label,
            A,B,C,D,A_label,B_label,C_label,D_label,
            Angle_O1CO3,Angle_O2DO3,Angle_O3DO2,
            O1,O2,O3,O1_label,O2_label,O3_label,
            DO3,CO3,CO1,DO2
        )

        self.play(FadeOut(ALL))
        
class Criteria_proove(Scene):
    def construct(self):   
        def circle_intersections(Circle_1,Circle_2,Radius_1,Radius_2):
            O1 = Circle_1.get_center()
            O2 = Circle_2.get_center()
            L = Line(O1,O2).get_length()
            try:
                Angle_1 = -Angle(
                    Line(O1,O2),
                    Line(O1,O1+RIGHT)).get_value()
            except:
                Angle_1 = 0
            
            X = Dot(np.array(O1+[Radius_1,0,0])).rotate(
                about_point = O1,
                angle = Angle_1+np.arccos((Radius_2**2-Radius_1**2-L**2)/(-2*Radius_1*L)))
            Y = Dot(np.array(O1+[Radius_1,0,0])).rotate(
                about_point = O1,
                angle = Angle_1-np.arccos((Radius_2**2-Radius_1**2-L**2)/(-2*Radius_1*L)))
            return X,Y

        def change_opacity_30(mob):
            mob.set_stroke(opacity=0.3)
            return mob

        def change_opacity_50(mob):
            mob.set_stroke(opacity=0.5)
            return mob
        
        def change_opacity_100(mob):
            mob.set_stroke(opacity=1)
            return mob

        rad = 2

        Circle_Omega = Circle(radius=rad,color=BLUE)
        Omega_label = MathTex(r"\mathrm{\Omega}}",font_size=35).move_to(np.array([2.2,-0.4,0]))

        M = Dot(Circle_Omega.point_at_angle(0.1*PI)).set_z_index(9)
        N = Dot(Circle_Omega.point_at_angle(0.9*PI)).set_z_index(9)

        M_label = MathTex(r"\mathrm{M}",font_size=35).next_to(M.get_center(),UR,buff=0.12)
        N_label = MathTex(r"\mathrm{N}",font_size=35).next_to(N.get_center(),UL,buff=0.12)

        MN = Line(M.get_center(),N.get_center(),color=RED)

        MN_half = Dot((M.get_center()+N.get_center())/2).set_opacity(0)
        Sector_dot = Dot(Circle_Omega.point_at_angle(0.4*PI)).set_opacity(0)
        Sector_line = Line(MN_half.get_center(),Sector_dot.get_center()).set_opacity(0)

        Angle_for_tangent = Angle(
            Line(MN_half.get_center(),M.get_center()),
            Line(MN_half.get_center(),Sector_dot.get_center())
        ).get_value() + Angle(
            Line(MN_half.get_center(),Sector_dot.get_center()),
            Line(MN_half.get_center(),N.get_center())
        ).get_value()/2

        Tangent = Dot(Circle_Omega.get_center()+np.array([rad,0,0])).rotate(
            about_point=Circle_Omega.get_center(),
            angle = Angle_for_tangent
        ).set_opacity(0)

        Tangent_Line = TangentLine(Circle_Omega,alpha=Angle_for_tangent/TAU,length=6).set_opacity(0)
        Tangent_intersection_1 = Dot(
            line_intersection(
                np.array([M.get_center(),N.get_center()]),
                np.array([Tangent.get_center(),
                          Dot(Circle_Omega.get_center()).rotate(
                                about_point = Tangent.get_center(),
                                angle = -PI/2
                          ).get_center()])
            )
        ).set_opacity(0).set_z_index(1)

        Tangent_intersection_2 = Dot(
            line_intersection(
                np.array([MN_half.get_center(),Sector_dot.get_center()]),
                np.array([Tangent.get_center(),
                          Dot(Circle_Omega.get_center()).rotate(
                                about_point = Tangent.get_center(),
                                angle = -PI/2
                          ).get_center()])
            )
        ).set_opacity(0)

        Biss_1 = Line(MN_half.get_center(),Tangent.get_center()).set_opacity(0)
        Biss_2 = Line(Tangent_intersection_1.get_center(),
                      Dot(Tangent_intersection_2.get_center()).rotate(
                        about_point = Tangent_intersection_1.get_center(),
                        angle = -Angle(
                            Line(Tangent_intersection_1.get_center(),
                                 M.get_center()),
                            Line(Tangent_intersection_1.get_center(),
                                 Tangent_intersection_2.get_center()),
                        ).get_value()/2
                      ).get_center()).set_opacity(0)
        
        I = Dot(
            line_intersection(
                np.array([
                    MN_half.get_center(),Tangent.get_center()
                ]),
                np.array([
                    Tangent_intersection_1.get_center(),
                    Dot(Tangent_intersection_2.get_center()).rotate(
                        about_point = Tangent_intersection_1.get_center(),
                        angle = -Angle(
                            Line(Tangent_intersection_1.get_center(),
                                 M.get_center()),
                            Line(Tangent_intersection_1.get_center(),
                                 Tangent_intersection_2.get_center()),
                        ).get_value()/2
                      ).get_center()
                ])
            )+np.array([-0.135,-0.04,0])
        ).set_opacity(0)   

        Circle_omega = Circle(radius=Line(
            I.get_center(),MN.get_projection(I.get_center())
        ).get_length()*0.965,color=YELLOW).move_to(I.get_center()).set_z_index(-99)  

        self.add(MN_half,Sector_dot,Sector_line,Tangent_intersection_1,Tangent_intersection_2,
                 Tangent_Line,Tangent,Biss_1,Biss_2,I)
        
        Circle_omega_label = MathTex(r"\mathrm{\omega}",font_size=35).move_to(np.array([-0.1,1.6,0]))

        A = Dot(Tangent.get_center()).set_z_index(7)

        AN = Line(A.get_center(),N.get_center(),color=YELLOW).set_opacity(0)
        AM = Line(A.get_center(),M.get_center(),color=YELLOW).set_opacity(0)

        Angle_NAM = Angle(AN,AM).set_opacity(0)

        For_B = Dot(N.get_center()).rotate(
            about_point = A.get_center(),
            angle = Angle_NAM.get_value()/2+0.03)

        B = Dot(line_intersection(
            np.array([A.get_center(),For_B.get_center()]),
            np.array([M.get_center(),N.get_center()])
        ))

        A_label = MathTex(r"\mathrm{A}",font_size=35).next_to(A.get_center(),UP,buff=0.2)
        B_label = MathTex(r"\mathrm{B}",font_size=35).next_to(B.get_center(),DR,buff=0.15)

        L = Dot(Circle_Omega.point_at_angle(3*PI/2+0.04))
        L_label = MathTex(r"\mathrm{L}",font_size=35).next_to(L.get_center(),DR,buff=0.15)
        Circle_omega_star = Circle(radius=Line(
            Dot(Circle_Omega.point_at_angle(3*PI/2)).get_center(),
            M.get_center()).get_length()
        ,color=GREEN).move_to(Dot(Circle_Omega.point_at_angle(3*PI/2)).get_center()).set_stroke(opacity=0.5)

        Circle_omega_star_label = MathTex(r"\mathrm{\omega^*}",font_size=35).move_to(np.array([3.55,-2,0]))

        ALL = VGroup(
             Circle_Omega,Omega_label,M,N,M_label,N_label,
             MN,MN_half,Sector_dot,Sector_line,
             Tangent,Tangent_Line,Tangent_intersection_1,Tangent_intersection_2,
             Circle_omega,Circle_omega_label,A,AN,AM,Angle_NAM,A_label,B_label,
             L_label,L,Circle_omega_star,Circle_omega_star_label,B
        )
        self.wait(0.3)

        label_1 = MathTex(r"\mathrm{Let's\,\, get\,\, back\,\, to\,\, the\,\, main\,\, task}").to_edge(UP)
        self.play(Write(label_1))
        self.play(FadeIn(ALL))
        self.wait(0.4)
        self.play(FadeOut(label_1))
        self.wait(0.3)

        label_2 = MathTex(r"\mathrm{Let\,\, the\,\, circles\,\, \omega\,\, and\,\, \Omega\,\, not\,\, touch}").to_edge(UP)
        self.play(Write(label_2),run_time=1.3)
        self.play(FadeOut(A),
                FadeOut(A_label))
        self.play(Circle_omega.animate.shift(0.15*RIGHT),
        Circle_omega_label.animate.set_opacity(0.3).shift(0.2*RIGHT+0.6*DOWN),run_time=1.3)
        
        self.play(ApplyFunction(change_opacity_30,Circle_omega))
        self.play(FadeOut(label_2))

        label_3 = MathTex(r"\mathrm{\omega_1\,\, is\,\, the\,\, circle\,\, that\,\, touches\,\, \Omega\,\,and\,\,MN\,\,}").to_edge(UP)
        
        Circle_omega_1 = Circle(radius=Line(
            I.get_center(),MN.get_projection(I.get_center())
        ).get_length()*0.965,color=GREEN_D).move_to(I.get_center()).set_z_index(-99)  

        Circle_omega_1_label = MathTex(r"\mathrm{\omega_1}",font_size=35).move_to(np.array([0,1.45,0]))

        self.play(Write(label_3))
        self.play(Create(Circle_omega_1),FadeIn(Circle_omega_1_label))
        self.wait()
        self.play(FadeOut(label_3))

        F,G = circle_intersections(Circle_omega,Circle_omega_1,
                                   Line(I.get_center(),MN.get_projection(I.get_center())).get_length()*0.965,
                                   Line(I.get_center(),MN.get_projection(I.get_center())).get_length()*0.965)
        
        label_4 = MathTex(r"\mathrm{But\,\, also\,\, the\,\, circles\,\, \omega_1\,\, and\,\, \omega^*\,\, are\,\, perpendicular}").to_edge(UP)
        self.play(Write(label_4),run_time=1.5)
        self.wait()
        self.play(FadeOut(label_4))
        self.wait(0.7)

        label_5 = MathTex(r"\mathrm{Let\,\, A_1\,\, be\,\, the\,\, tangent\,\, point\,\, of\,\, \omega_1\,\, and\,\, \Omega}").to_edge(UP)
        self.play(Write(label_5),run_time=1.5)
        A_1 = Dot(A.get_center())
        A_1_label = MathTex(r"\mathrm{A_1}",font_size=35).next_to(A_1.get_center(),UP,buff=0.2)
        self.play(FadeIn(A_1),FadeIn(A_1_label))
        self.wait()
        self.play(FadeOut(label_5))
        self.wait(0.7)

        label_6 = MathTex(r"\mathrm{Point\,\, F\,\, is\,\, the\,\, intersection\,\, of\,\, \omega\,\, and\,\, \omega_1}").to_edge(UP)
        self.play(Write(label_6),run_time=2)
        F_label = MathTex(r"\mathrm{F}",font_size=35).next_to(F.get_center(),RIGHT,buff=0.2)
        self.play(FadeIn(F),FadeIn(F_label))
        self.wait()
        self.play(FadeOut(label_6))
        self.wait(0.7)

        label_7 = MathTex(r"\mathrm{Circles\,\, \omega\,\, and\,\, \omega^*\,\, are\,\, perpendicular}").to_edge(UP)
        self.play(Write(label_7),run_time=2)
        self.wait()
        self.play(FadeOut(label_7))
        self.wait(0.7)

        label_8 = MathTex(r"\mathrm{But\,\, \omega_1\,\, and\,\, \omega^*\,\, are\,\, perpendicular\,\, too}").to_edge(UP)
        self.play(Write(label_8),run_time=2)
        self.wait()
        self.play(FadeOut(label_8))
        self.wait(0.7)

        label_9 = MathTex(r"\mathrm{Then\,\, by\,\, lemma\,\, the\,\, center\,\, of\,\, the\,\, \omega^*\,\, lies\,\, on\,\, the\,\, line\,\, FB}").to_edge(UP)
        self.play(Write(label_9),run_time=2.2)
        self.wait(1.5)
        self.play(FadeOut(label_9))
        self.wait(0.7)

        label_10 = MathTex(r"\mathrm{L\,\, is\,\ the\,\ center\,\ of\,\ \omega^*}").to_edge(UP)
        self.play(Write(label_10),run_time=2)
        self.wait(1.2)
        self.play(FadeOut(label_10))
        self.wait(0.6)

        label_11 = MathTex(r"\mathrm{But\,\, also\,\, L\,\, is\,\, the\,\, middle\,\, of\,\, the\,\, arc\,\, MN}").to_edge(UP)
        self.play(Write(label_11),run_time=2)
        self.wait(1.2)
        self.play(FadeOut(label_11))
        self.wait(0.6)

        label_12 = MathTex(r"\mathrm{Then\,\, by\,\, Archimedes'\,\, lemma\,\, L\,\, lies\,\, on\,\, A_1B}").to_edge(UP)
        AL = Line(A_1.get_center(),L.get_center(),color=RED).set_opacity(0.6).set_z_index(-99999)
        self.play(Write(label_12),run_time=2)
        self.play(Create(AL))
        self.wait(1.3)
        self.play(FadeOut(label_12))
        self.wait(0.6)

        label_13 = MathTex(r"\mathrm{But\,\, L\,\, also\,\, lies\,\, on\,\, FB}").to_edge(UP)
        self.play(Write(label_13),run_time=2)
        self.wait(1.3)
        self.play(FadeOut(label_13))
        self.wait(0.6)

        label_14 = MathTex(r"\mathrm{So\,\, FB\,\, and\,\, A_1B\,\, are\,\, the\,\, same}").to_edge(UP)
        self.play(Write(label_14),run_time=2)
        self.wait()
        self.play(FadeOut(label_14))
        self.wait(0.6)

        label_15 = MathTex(r"\mathrm{That\,\, is,\,\, F\,\, coincides\,\, with\,\, A_1}").to_edge(UP)
        self.play(Write(label_15),run_time=2)
        self.play(
            FadeOut(A_1),
            FadeOut(A_1_label),
            FadeOut(F),
            FadeOut(F_label),
        ),
        self.play(
            FadeOut(Circle_omega_1),
            FadeOut(Circle_omega_1_label)
        )
        self.play(ApplyFunction(change_opacity_100,Circle_omega))
        self.play(Circle_omega.animate.shift(-0.15*RIGHT),
        Circle_omega_label.animate.set_opacity(1).shift(-(0.2*RIGHT+0.6*DOWN)))
        self.play(FadeIn(A),FadeIn(A_label))
        self.wait()
        self.play(FadeOut(AL))
        self.play(FadeOut(label_15))
        self.wait(0.6)

        label_16 = MathTex(r"\mathrm{So\,\, circle\,\, \omega\,\, touches\,\, circle\,\, \Omega}").to_edge(UP)
        self.play(Write(label_16),run_time=2)
        self.wait()
        self.play(FadeOut(label_16))
        self.wait(1.5)

        self.play(FadeOut(ALL),run_time=1.5)

        self.wait(1)

class Criteria_2(Scene):
    def construct(self):
        def change_opacity_50(mob):
            mob.set_stroke(opacity=0.5)
            return mob
        
        def circle_intersections(Circle_1,Circle_2,Radius_1,Radius_2):
            O1 = Circle_1.get_center()
            O2 = Circle_2.get_center()
            L = Line(O1,O2).get_length()
            try:
                Angle_1 = -Angle(
                    Line(O1,O2),
                    Line(O1,O1+RIGHT)).get_value()
            except:
                Angle_1 = 0
            
            X = Dot(np.array(O1+[Radius_1,0,0])).rotate(
                about_point = O1,
                angle = Angle_1+np.arccos((Radius_2**2-Radius_1**2-L**2)/(-2*Radius_1*L)))
            Y = Dot(np.array(O1+[Radius_1,0,0])).rotate(
                about_point = O1,
                angle = Angle_1-np.arccos((Radius_2**2-Radius_1**2-L**2)/(-2*Radius_1*L)))
            return X,Y
        
        Circle_1 = Circle(radius=1.5,color=BLUE)
        M = Dot(Circle_1.point_at_angle(0.1*PI)).set_z_index(9)
        N = Dot(Circle_1.point_at_angle(0.9*PI)).set_z_index(9)
        MN = Line(M.get_center(),N.get_center(),color=YELLOW).set_length(20).set_opacity(0.5)
        L = Dot(Circle_1.point_at_angle(3/2*PI)).set_z_index(9)
        Circle_2 = Circle(radius=Line(
            L.get_center(),M.get_center()).get_length(),
            color=GREEN).move_to(L.get_center())
        Circle_3 = Circle(radius=1.5).move_to(M.get_center()+np.array(
            [2.472,-1.5,0]
        ))
        A,_ =  circle_intersections(Circle_2,Circle_3,
                                    Line(L.get_center(),M.get_center()).get_length(),1.5)
        
        B = Dot(M.get_center()+np.array([2.472,0,0]))

        M_label = MathTex(r"\mathrm{M}",font_size=35).next_to(M.get_center(),UR,buff=0.12)
        N_label = MathTex(r"\mathrm{N}",font_size=35).next_to(N.get_center(),UL,buff=0.12)
        L_label = MathTex(r"\mathrm{L}",font_size=35).next_to(L.get_center(),DR,buff=0.15)
        A_label = MathTex(r"\mathrm{A}",font_size=35).next_to(A.get_center(),LEFT,buff=0.15)
        B_label = MathTex(r"\mathrm{B}",font_size=35).next_to(B.get_center(),UP,buff=0.15)
        

        ALL = VGroup(Circle_1,Circle_2,Circle_3,M,N,L,MN,A,
                 M_label,N_label,L_label,A_label,B_label,B)

        label_1 = MathTex(r"\mathrm{There\,\, is\,\, a\,\, similar\,\, statement\,\, for\,\, external\,\, touch}").to_edge(UP)
        self.play(LaggedStart(
            Write(label_1),
            AnimationGroup(
                Create(Circle_1),
                Create(Circle_2),
            ),
            AnimationGroup(
                FadeIn(M),
                FadeIn(N),
                FadeIn(M_label),
                FadeIn(N_label),
            ),
            AnimationGroup(
                FadeIn(L),
                FadeIn(L_label),
            ),
            Create(MN),
            lag_ratio=0.8,
            run_time=6.5
        ))
        self.wait(0.2)
        self.play(LaggedStart(
            FadeOut(label_1),
            Create(Circle_3),
            AnimationGroup(
                FadeIn(A),
                FadeIn(A_label),
            ),
            AnimationGroup(
                FadeIn(B),
                FadeIn(B_label),
            ),
            lag_ratio=0.7,
            run_time=4.3
        )),

        label_2 = MathTex(r"\mathrm{You\,\, can\,\, prove\,\, it\,\, yourself}").to_edge(UP)
        self.play(Write(label_2),run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(label_2))
        self.wait(0.5)
        self.play(FadeOut(ALL))
        self.wait(3)

