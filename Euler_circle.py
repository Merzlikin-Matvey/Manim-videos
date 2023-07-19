from ManimExtra import *



class theorem_scene(Scene):
    def construct(self):
        A = Dot(2.5*DOWN + 3*LEFT).set_z_index(1)
        B = Dot(2.5*UP + 1.4*LEFT).set_z_index(1)
        C = Dot(2.5*DOWN + 4*RIGHT).set_z_index(1)

        A_label = Tex(r"A", font_size=42).next_to(A.get_center(), DL).set_z_index(3)
        B_label = Tex(r"B", font_size=42).next_to(B.get_center(), UP, buff=0.2).set_z_index(3)
        C_label = Tex(r"C", font_size=42).next_to(C.get_center(), DR).set_z_index(3)

        a = Line(B.get_center(), C.get_center(), color=BLUE)
        b = Line(C.get_center(), A.get_center(), color=BLUE)
        c = Line(A.get_center(), B.get_center(), color=BLUE)

        self.play(FadeIn(VGroup(A, B, C)))
        self.play(LaggedStart(
            Create(a),
            Create(b),
            Create(c),
            lag_ratio=0.9, run_time=2
        ))
        self.play(FadeIn(VGroup(A_label, B_label, C_label)))

        AM_a = Median(B.get_center(), A.get_center(), C.get_center(), color=RED)
        BM_b = Median(A.get_center(), B.get_center(), C.get_center(), color=RED)
        CM_c = Median(B.get_center(), C.get_center(), A.get_center(), color=RED)

        M_a = Dot(AM_a.dot).set_z_index(1)
        M_b = Dot(BM_b.dot).set_z_index(1)
        M_c = Dot(CM_c.dot).set_z_index(1)
        
        M_a_label = Tex(r"$\mathrm{M_a}$", font_size=32).next_to(M_a.get_center(), RIGHT, buff=0.17).set_z_index(3)
        M_b_label = Tex(r"$\mathrm{M_b}$", font_size=32).next_to(M_b.get_center(), DOWN, buff=0.17).set_z_index(3)
        M_c_label = Tex(r"$\mathrm{M_c}$", font_size=32).next_to(M_c.get_center(), LEFT).set_z_index(3)

        A_equals = VGroup(
            Line(B.get_center(), M_a.get_center()).equal(),
            Line(C.get_center(), M_a.get_center()).equal())

        B_equals = VGroup(
            Line(A.get_center(), M_b.get_center()).equal(2),
            Line(C.get_center(), M_b.get_center()).equal(2))
        
        C_equals = VGroup(
            Line(A.get_center(), M_c.get_center()).equal(3),
            Line(B.get_center(), M_c.get_center()).equal(3))

        self.play(Create(AM_a), FadeIn(M_a), FadeIn(M_a_label), FadeIn(A_equals))
        self.play(Create(BM_b), FadeIn(M_b), FadeIn(M_b_label), FadeIn(B_equals))
        self.play(Create(CM_c), FadeIn(M_c), FadeIn(M_c_label), FadeIn(C_equals))

        self.wait(0.3)

        self.play(
            AM_a.animate.set_opacity(0.1),
            BM_b.animate.set_opacity(0.1),
            CM_c.animate.set_opacity(0.1),
            M_a.animate.set_opacity(0.3),
            M_b.animate.set_opacity(0.3),
            M_c.animate.set_opacity(0.3),
            M_a_label.animate.set_opacity(0.3),
            M_b_label.animate.set_opacity(0.3),
            M_c_label.animate.set_opacity(0.3),
            A_equals.animate.set_opacity(0.1),
            B_equals.animate.set_opacity(0.1),
            C_equals.animate.set_opacity(0.1),
        )

        AH_a = Altitude(B.get_center(), A.get_center(), C.get_center(), color=GREEN)
        BH_b = Altitude(A.get_center(), B.get_center(), C.get_center(), color=GREEN)
        CH_c = Altitude(B.get_center(), C.get_center(), A.get_center(), color=GREEN)

        H_a = Dot(AH_a.dot).set_z_index(1)
        H_b = Dot(BH_b.dot).set_z_index(1)
        H_c = Dot(CH_c.dot).set_z_index(1)

        H_a_label = Tex(r"$\mathrm{H_a}$", font_size=32).next_to(H_a.get_center(), UR, buff=0.18).set_z_index(3)
        H_b_label = Tex(r"$\mathrm{H_b}$", font_size=32).next_to(H_b.get_center(), DOWN, buff=0.18).set_z_index(3)
        H_c_label = Tex(r"$\mathrm{H_c}$", font_size=32).next_to(H_c.get_center(), LEFT).set_z_index(3)

        H_a_angle = AH_a.angles(color=YELLOW, radius=0.2)[0]
        H_b_angle = BH_b.angles(color=YELLOW, radius=0.2)[1]
        H_c_angle = CH_c.angles(color=YELLOW, radius=0.2)[0]

        self.play(Create(AH_a), FadeIn(H_a), FadeIn(H_a_label))
        self.play(FadeIn(H_a_angle), run_time=0.7)

        self.play(Create(BH_b), FadeIn(H_b), FadeIn(H_b_label))
        self.play(FadeIn(H_b_angle), run_time=0.7)

        self.play(Create(CH_c), FadeIn(H_c), FadeIn(H_c_label))
        self.play(FadeIn(H_c_angle), run_time=0.7)


        self.play(
            AH_a.animate.set_opacity(0.7),
            BH_b.animate.set_opacity(0.7),
            CH_c.animate.set_opacity(0.7),
            H_a.animate.set_opacity(0.3),
            H_b.animate.set_opacity(0.3),
            H_c.animate.set_opacity(0.3),
            H_a_label.animate.set_opacity(0.3),
            H_b_label.animate.set_opacity(0.3),
            H_c_label.animate.set_opacity(0.3),
            H_a_angle.animate.set_stroke(opacity=0.1),
            H_b_angle.animate.set_stroke(opacity=0.1),
            H_c_angle.animate.set_stroke(opacity=0.1),
        )

        H = Dot(intersection_lines(AH_a, BH_b)).set_z_index(1)
        H_label = Tex(r"H", font_size=30).next_to(H.get_center(), np.array([0.8,-1,0]), buff=0.14)

        self.play(FadeIn(VGroup(H, H_label)))

        self.play(
            AH_a.animate.set_opacity(0.1),
            BH_b.animate.set_opacity(0.1),
            CH_c.animate.set_opacity(0.1),
            A_equals.animate.set_opacity(0),
            B_equals.animate.set_opacity(0),
            C_equals.animate.set_opacity(0))
        
        self.remove(A_equals, B_equals, C_equals)

        AH = Line(A.get_center(), H.get_center(), color=GREEN).set_opacity(0)
        BH = Line(B.get_center(), H.get_center(), color=GREEN).set_opacity(0)
        CH = Line(C.get_center(), H.get_center(), color=GREEN).set_opacity(0)

        E_a = Dot(AH.point_from_proportion(0.5)).set_z_index(1)
        E_b = Dot(BH.point_from_proportion(0.5)).set_z_index(1)
        E_c = Dot(CH.point_from_proportion(0.5)).set_z_index(1)

        E_a_label = Tex(r'$E_a$', font_size=32).next_to(E_a.get_center(), RIGHT).set_z_index(3)
        E_b_label = Tex(r'$E_b$', font_size=32).next_to(E_b.get_center(), RIGHT + 0.2*DOWN, buff=0.1).set_z_index(3)
        E_c_label = Tex(r'$E_c$', font_size=32).next_to(E_c.get_center(), DOWN + 0.7*RIGHT, buff=0.1).set_z_index(3)
        
        A_equals = VGroup(
            Line(A.get_center(), E_a.get_center()).equal(),
            Line(E_a.get_center(), H.get_center()).equal())

        B_equals = VGroup(
            Line(B.get_center(), E_b.get_center()).equal(2),
            Line(E_b.get_center(), H.get_center()).equal(2))
        
        C_equals = VGroup(
            Line(C.get_center(), E_c.get_center()).equal(3),
            Line(E_c.get_center(), H.get_center()).equal(3))

        self.play(AH.animate.set_opacity(1))
        self.play(FadeIn(VGroup(E_a, E_a_label)), FadeIn(A_equals))
        self.play(VGroup(E_a, E_a_label, AH).animate.set_opacity(0.2), FadeOut(A_equals))

        self.play(BH.animate.set_opacity(1))
        self.play(FadeIn(VGroup(E_b, E_b_label)), FadeIn(B_equals))
        self.play(VGroup(E_b, E_b_label, BH).animate.set_opacity(0.2), FadeOut(B_equals))

        self.play(CH.animate.set_opacity(1))
        self.play(FadeIn(VGroup(E_c, E_c_label)), FadeIn(C_equals))
        self.play(VGroup(E_c, E_c_label, CH).animate.set_opacity(0.2), FadeOut(C_equals))

        self.play(VGroup(H, H_label).animate.set_opacity(0.2))

        circle = Circle().from_three_points(
            M_a.get_center(), M_b.get_center(), M_c.get_center(), 
            color=YELLOW, stroke_width=3.5
        ).set_z_index(0.5).set_stroke(opacity=0.8)

        self.play(
            M_a.animate.set_opacity(1),
            M_b.animate.set_opacity(1),
            M_c.animate.set_opacity(1),
            E_a.animate.set_opacity(1),
            E_b.animate.set_opacity(1),
            E_c.animate.set_opacity(1),
            H_a.animate.set_opacity(1),
            H_b.animate.set_opacity(1),
            H_c.animate.set_opacity(1),
            FadeOut(H),
            FadeOut(H_label),
        )

        self.play(Create(circle))
        self.wait(3)


class proof_scene(Scene):
    def construct(self):
        A = Dot(2.5*DOWN + 3*LEFT).set_z_index(1)
        B = Dot(2.5*UP + 1.35*LEFT).set_z_index(1)
        C = Dot(2.5*DOWN + 4*RIGHT).set_z_index(1)

        A_label = Tex(r"A", font_size=42).next_to(A.get_center(), DL).set_z_index(3)
        B_label = Tex(r"B", font_size=42).next_to(B.get_center(), UP, buff=0.2).set_z_index(3)
        C_label = Tex(r"C", font_size=42).next_to(C.get_center(), DR).set_z_index(3)

        a = Line(B.get_center(), C.get_center(), color=BLUE)
        b = Line(C.get_center(), A.get_center(), color=BLUE)
        c = Line(A.get_center(), B.get_center(), color=BLUE)

        AM_a = Median(B.get_center(), A.get_center(), C.get_center(), color=RED).set_opacity(0.1)
        BM_b = Median(A.get_center(), B.get_center(), C.get_center(), color=RED).set_opacity(0.1)
        CM_c = Median(B.get_center(), C.get_center(), A.get_center(), color=RED).set_opacity(0.1)

        M_a = Dot(AM_a.dot).set_z_index(1)
        M_b = Dot(BM_b.dot).set_z_index(1)
        M_c = Dot(CM_c.dot).set_z_index(1)
        
        M_a_label = Tex(r"$\mathrm{M_a}$", font_size=32).next_to(M_a.get_center(), RIGHT, buff=0.17).set_z_index(3)
        M_b_label = Tex(r"$\mathrm{M_b}$", font_size=32).next_to(M_b.get_center(), DOWN, buff=0.17).set_z_index(3)
        M_c_label = Tex(r"$\mathrm{M_c}$", font_size=32).next_to(M_c.get_center(), LEFT).set_z_index(3)

        A_equals = VGroup(
            Line(B.get_center(), M_a.get_center()).equal(),
            Line(C.get_center(), M_a.get_center()).equal())

        B_equals = VGroup(
            Line(A.get_center(), M_b.get_center()).equal(2),
            Line(C.get_center(), M_b.get_center()).equal(2))
        
        C_equals = VGroup(
            Line(A.get_center(), M_c.get_center()).equal(3),
            Line(B.get_center(), M_c.get_center()).equal(3))

        AH_a = Altitude(B.get_center(), A.get_center(), C.get_center(), color=GREEN).set_opacity(0.1)
        BH_b = Altitude(A.get_center(), B.get_center(), C.get_center(), color=GREEN).set_opacity(0.1)
        CH_c = Altitude(B.get_center(), C.get_center(), A.get_center(), color=GREEN).set_opacity(0.1)

        H_a = Dot(AH_a.dot).set_z_index(1)
        H_b = Dot(BH_b.dot).set_z_index(1)
        H_c = Dot(CH_c.dot).set_z_index(1)

        H_a_label = Tex(r"$\mathrm{H_a}$", font_size=32).next_to(H_a.get_center(), UR, buff=0.12).set_z_index(3)
        H_b_label = Tex(r"$\mathrm{H_b}$", font_size=32).next_to(H_b.get_center(), DOWN, buff=0.18).set_z_index(3)
        H_c_label = Tex(r"$\mathrm{H_c}$", font_size=32).next_to(H_c.get_center(), LEFT).set_z_index(3)

        H_a_angle = AH_a.angles(color=YELLOW, radius=0.2)[0]
        H_b_angle = BH_b.angles(color=YELLOW, radius=0.2)[1]
        H_c_angle = CH_c.angles(color=YELLOW, radius=0.2)[0]

        H = Dot(intersection_lines(AH_a, BH_b)).set_z_index(1)
        H_label = Tex(r"H", font_size=30).next_to(H.get_center(), np.array([0.2,-1,0]), buff=0.14)


        AH = Line(A.get_center(), H.get_center(), color=GREEN).set_opacity(0)
        BH = Line(B.get_center(), H.get_center(), color=GREEN).set_opacity(0)
        CH = Line(C.get_center(), H.get_center(), color=GREEN).set_opacity(0)

        E_a = Dot(AH.point_from_proportion(0.5)).set_z_index(1)
        E_b = Dot(BH.point_from_proportion(0.5)).set_z_index(1)
        E_c = Dot(CH.point_from_proportion(0.5)).set_z_index(1)

        E_a_label = Tex(r'$E_a$', font_size=31).next_to(E_a.get_center(), LEFT).set_z_index(3)
        E_b_label = Tex(r'$E_b$', font_size=31).next_to(E_b.get_center(), LEFT + 0.2*UP, buff=0.1).set_z_index(3)
        E_c_label = Tex(r'$E_c$', font_size=31).next_to(E_c.get_center(), DOWN + 0.7*RIGHT, buff=0.1).set_z_index(3)

        circle = Circle().from_three_points(
            M_a.get_center(), M_b.get_center(), M_c.get_center(), 
            color=YELLOW, stroke_width=3.5
        ).set_z_index(0.5).set_stroke(opacity=0.8)

        self.add(VGroup(
            A, B, C, a, b, c, 
            M_a, M_b, M_c, AM_a, BM_b, CM_c, 
            H_a, H_b, H_c, AH_a, BH_b, CH_c, 
            E_a, E_b, E_c, 
            A_label, B_label, C_label, 
            M_a_label, M_b_label, M_c_label, 
            H_a_label, H_b_label, H_c_label, 
            E_a_label, E_b_label, E_c_label, 
            circle
        ))

        self.play(Uncreate(circle))
        self.play(FadeOut(VGroup(
            E_a, E_b, E_c, 
            E_a_label, E_b_label, E_c_label, 
            H_a, H_c, 
            H_a_label, H_c_label
        )))

        self.play(VGroup(a, b, c).animate.set_opacity(0.45), run_time=0.7)

        M_cH_b = Line(M_c.get_center(), H_b.get_center(), color=RED_D)
        H_bM_b = Line(H_b.get_center(), M_b.get_center(), color=RED_D)
        M_bM_a = Line(M_b.get_center(), M_a.get_center(), color=RED_D)
        M_aM_c = Line(M_a.get_center(), M_c.get_center(), color=RED_D)

        self.play(LaggedStart(
            Create(M_cH_b), 
            Create(H_bM_b), 
            Create(M_bM_a), 
            Create(M_aM_c), 
            lag_ratio=0.95, run_time=4
        ))
        
        self.play(M_cH_b.animate.set_opacity(0.2), 
                  M_bM_a.animate.set_opacity(0.2))

        parals_1 = VGroup(M_aM_c.paral(rotate=True),
                        Line(H_b.get_center(), M_b.get_center()).paral())
        
        self.play(FadeIn(parals_1))
        self.wait(0.5)
        self.play(FadeOut(parals_1))
        self.play(M_cH_b.animate.set_opacity(1), 
                  M_bM_a.animate.set_opacity(1))
        
        self.play(
        VGroup(M_aM_c, M_cH_b).animate.set_opacity(0.2),
        FadeOut(M_c, M_c_label, H_b, H_b_label, H_bM_b)
        )


        parals_1 = VGroup(c.paral(), M_bM_a.paral())
        self.play(c.animate.set_opacity(1), run_time=0.5)
        self.play(FadeIn(parals_1))
        self.wait()
        self.play(FadeOut(parals_1))

        label_1 = Tex(r"$2x$", font_size=44).next_to(c.get_center(), LEFT)
        label_2 = Tex(r"$x$", font_size=44).next_to(M_bM_a.get_center(), RIGHT)

        self.play(FadeIn(VGroup(label_1, label_2)))

        H_b_angle.set_z_index(-1)
        AH_b = Line(A.get_center(), H_b.get_center(), color=BLUE)

        self.play(
            FadeIn(H_b_angle, AH_b, H_b, H_b_label),
            BH_b.animate.set_opacity(1),
        )
        

        label_3 = Tex(r"$x$", font_size=44).next_to(
            Line(A.get_center(), M_c.get_center()).get_center(), LEFT, buff=0.23)
        label_4 = Tex(r"$x$", font_size=44).next_to(
            Line(B.get_center(), M_c.get_center()).get_center(), LEFT, buff=0.23)

        self.play(FadeIn(M_c), FadeIn(C_equals))
        self.play(Transform(label_1, VGroup(label_3, label_4)))
        self.play(M_cH_b.animate.set_opacity(1))

        label_5 = Tex(r"$x$", font_size=44).next_to(
            M_cH_b.point_from_proportion(0.6), LEFT, buff=0.16)
        self.play(FadeIn(label_5))

        self.play(FadeOut(VGroup(C_equals, label_1)), c.animate.set_opacity(0.45))
        self.play(
            BH_b.animate.set_opacity(0.2),
            FadeOut(AH_b),
            FadeOut(H_b_angle))

        self.play(VGroup(H_bM_b, M_aM_c).animate.set_opacity(1),
                  FadeIn(M_c_label))
        
        self.wait(0.5)
        self.play(FadeOut(VGroup(label_5, label_2)))
        circle = Circle().from_three_points(M_a.get_center(), M_b.get_center(), M_c.get_center(), color=YELLOW)
        self.play(Create(circle))

        new_group_1 = VGroup(
            Line(M_c.get_center(), H_c.get_center(), color=RED),
            Line(H_c.get_center(), M_b.get_center(), color=RED),
            Line(M_b.get_center(), M_a.get_center(), color=RED),
            Line(M_a.get_center(), M_c.get_center(), color=RED),
        )

        tmp = VGroup(M_cH_b, H_bM_b, M_bM_a, M_aM_c)

        self.play(FadeIn(VGroup(H_c, H_c_label)), 
                  Transform(tmp, new_group_1))

        new_group_2 = VGroup(
            Line(M_c.get_center(), H_a.get_center(), color=RED),
            Line(H_a.get_center(), M_a.get_center(), color=RED),
            Line(M_a.get_center(), M_b.get_center(), color=RED),
            Line(M_b.get_center(), M_c.get_center(), color=RED),
        )

        self.play(FadeIn(VGroup(H_a, H_a_label)), 
                  Transform(tmp, new_group_2))
        
        self.play(FadeOut(tmp))

        self.play(FadeIn(VGroup(
            E_a, E_a_label, E_b, E_b_label, E_c, E_c_label
        )))
    
        self.wait(0.5)

        X = Dot(AH.point_from_proportion(0.5)).set_z_index(3)
        X_label = Tex(r'$X$', font_size=32).next_to(X.get_center(), LEFT).set_z_index(3)

        self.play(
            E_a.animate.shift(AH.point_from_proportion(0.27)-E_a.get_center()),
            E_a_label.animate.shift(AH.point_from_proportion(0.27)-E_a.get_center()),
        )
        self.play(FadeOut(VGroup(E_a, E_a_label)))
        self.play(FadeIn(VGroup(X, X_label)))

        Y = Dot(BH.point_from_proportion(0.5)).set_z_index(3)
        Y_label = Tex(r'$Y$', font_size=32).next_to(Y.get_center(), LEFT + 0.2*UP, buff=0.1).set_z_index(3)

        self.play(
            E_b.animate.shift(BH.point_from_proportion(0.35)-E_b.get_center()),
            E_b_label.animate.shift(BH.point_from_proportion(0.35)-E_b.get_center()),
        )
        self.play(FadeOut(VGroup(E_b, E_b_label)))
        self.play(FadeIn(VGroup(Y, Y_label)))

        Z = Dot(CH.point_from_proportion(0.5)).set_z_index(3)
        Z_label = Tex(r'$Z$', font_size=32).next_to(Z.get_center(), RIGHT + 0.7*DOWN, buff=0.1).set_z_index(3)

        self.play(
            E_c.animate.shift(CH.point_from_proportion(0.35)-E_c.get_center()),
            E_c_label.animate.shift(CH.point_from_proportion(0.35)-E_c.get_center()),
        )
        self.play(FadeOut(VGroup(E_c, E_c_label)))
        self.play(FadeIn(VGroup(Z, Z_label)))

        rectangle = Polygon(
            Y.get_center(), Z.get_center(), M_b.get_center(), M_c.get_center(), color=BLUE
        ).set_opacity(0.2).set_stroke(opacity=0.5)

        self.play(FadeIn(rectangle), run_time=2/3)
        self.wait(0.3)
        self.play(FadeOut(rectangle))

        self.play(FadeIn(H_b_angle))
        self.play(Wiggle(H_b_angle, scale_value=1.5))
        

        diam_1 = Line(Y.get_center(), M_b.get_center(), color=RED)

        self.play(Create(diam_1))
        self.play(FadeOut(H_b_angle))
        self.wait(0.3)
        self.play(diam_1.animate.set_opacity(0.4))

        self.play(FadeIn(H_c_angle))
        self.play(Wiggle(H_c_angle, scale_value=1.5))
        self.wait(0.2)

        diam_2 = Line(Z.get_center(), M_c.get_center(), color=RED)

        self.play(Create(diam_2))
        self.play(FadeOut(H_c_angle))
        self.wait(0.3)
        self.play(FadeOut(H_b_angle))
        self.play(diam_1.animate.set_opacity(1))

        O = Dot(intersection_lines(diam_1, diam_2)).set_z_index(3)
        O_label = Tex(r'$O$', font_size=30).next_to(O.get_center(), buff=0.1, direction=UR)

        self.play(FadeIn(VGroup(O, O_label)))

        diam_equals = VGroup(
            Line(Y.get_center(), O.get_center()).equal(),
            Line(Z.get_center(), O.get_center()).equal(),
            Line(M_b.get_center(), O.get_center()).equal(),
            Line(M_c.get_center(), O.get_center()).equal(),
        )

        self.play(FadeIn(diam_equals))

        rectangle.set_opacity(0).set_stroke(opacity=0.85)
        self.play(Create(rectangle))
        self.wait(0.2)

        self.play(FadeOut(VGroup(diam_equals, diam_1, diam_2, O, O_label)))
        self.play(FadeOut(VGroup(X, X_label, H_c, H_c_label, H_b, H_b_label, H_a, H_a_label, M_a, M_a_label)))
        self.play(FadeOut(circle))
        self.play(a.animate.set_opacity(1))

        a_label = Tex(r'$2x$', font_size=40).next_to(
            a.get_center(), buff=0.1, direction=UR)
        
        M_cM_b_label = Tex(r'$x$', font_size=40).next_to(
            Line(M_c.get_center(), M_b.get_center()).get_center(), buff=0.1, direction=DL)
        
        YZ_label = Tex(r'$x$', font_size=40).next_to(
            Line(Y.get_center(), Z.get_center()).get_center(), buff=0.1, direction=UR)

        self.play(FadeIn(a_label))
        self.play(FadeIn(M_cM_b_label))
        self.play(FadeIn(YZ_label))

        a_par = a.paral()
        M_cM_b_par = Line(M_c.get_center(), M_b.get_center()).paral()
        YZ_par = Line(Y.get_center(), Z.get_center()).paral()

        self.play(FadeIn(a_par))
        self.play(FadeIn(M_cM_b_par))
        self.play(FadeIn(YZ_par))

        YZ = Line(Y.get_center(), Z.get_center(), color=BLUE)
        self.add(YZ)
        self.play(Uncreate(rectangle), FadeOut(VGroup(
            M_b, M_b_label, M_c, M_c_label, M_cM_b_label, M_cM_b_par
        )))
        
        self.play(FadeIn(VGroup(H, H_label)), BH.animate.set_opacity(0.8), CH.animate.set_opacity(0.8))

        BH_equals = VGroup(Line(B.get_center(), Y.get_center()).equal(1),
                           Line(H.get_center(), Y.get_center()).equal(1))

        CH_equals = VGroup(Line(C.get_center(), Z.get_center()).equal(2),
                           Line(H.get_center(), Z.get_center()).equal(2))
        
        self.play(LaggedStart(
            FadeIn(BH_equals), FadeIn(CH_equals), lag_ratio=0.75, run_time=1.5
        ))

        self.play(Transform(Y_label, Tex(r'$E_b$', font_size=32).next_to(
            Y.get_center(), LEFT + 0.2*UP, buff=0.1).set_z_index(3)))
        self.play(Transform(Z_label, Tex(r'$E_c$', font_size=32).next_to(
            Z.get_center(), DOWN + 0.7*RIGHT, buff=0.1).set_z_index(3)))
        self.wait(0.3)

        X_label = Tex(r'$E_a$', font_size=32).next_to(X.get_center(), LEFT).set_z_index(3)
        AH_equals = VGroup(Line(A.get_center(), X.get_center()).equal(3),
                           Line(H.get_center(), X.get_center()).equal(3))
        self.play(FadeIn(VGroup(X, X_label)), AH.animate.set_opacity(0.8), FadeIn(AH_equals))

        self.play(FadeOut(VGroup(YZ, YZ_par, a_par, YZ_label, a_label)))

        self.play(VGroup(AH, BH, CH).animate.set_opacity(0), 
                  FadeOut(VGroup(AH_equals, BH_equals, CH_equals, H, H_label)))
        
        self.play(FadeIn(VGroup(M_a, M_b, M_c, M_a_label, M_b_label, M_c_label,
                                H_a, H_b, H_c, H_a_label, H_b_label, H_c_label)))
        
        self.wait(0.2)
        self.play(Create(circle))
















        



        self.wait(3)

