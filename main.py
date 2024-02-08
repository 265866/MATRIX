from manim import * 


class Test(Scene):
    def construct(self):
        m = Matrix(
            [["1", "2", "3", "4", "1"],
             ["0", "-1", "2", "4", "2"],
             ["0", "0", "4", "0", "0"],
             ["-3", "-6", "-9", "-12", "4"],
             ["0", "0", "1", "1", "1"]],
             h_buff=1,
             element_alignment_corner=ORIGIN,
        )
        self.add(m.get_brackets())
        rows = m.get_rows()
        self.play(Write(rows[0]))
        prev_row = rows[0]
        for row in rows[1:]:
            self.wait(0.1)
            self.play(
                ReplacementTransform(prev_row.copy(), row),
            )
            prev_row = row
        self.wait(1)
        self.play(m.animate.scale(0.7).shift(LEFT*2.65))
       
        #replace brackets with determinant signs around the matrix
        self.play(ReplacementTransform(m.get_brackets(), MathTex(r"\det").scale(2).shift(LEFT*5.5)))
        #add back parentheses around the matrix
        self.play(
            Write(MathTex("(").scale(2).shift(LEFT*4.5)),
            Write(MathTex(")").scale(2).shift(LEFT*0.7)),
            Write(MathTex("=").scale(2))
        )
        
        circle = Circle(radius=0.2, color=BLUE).shift(LEFT*3.9875).shift(UP*1.12)
        self.play(Create(circle))
        line1 = Line(start=LEFT*3.9875+UP*0.7, end=LEFT*3.9875+DOWN*1.2, color=RED)
        line2 = Line(start=LEFT*3.30+UP*1.12, end=LEFT*1.2+UP*1.12, color=RED)
        box = Rectangle(height=2.3, width=2.7, color=BLUE).shift(LEFT*2.28+DOWN*0.28)
        self.play(Create(line1), Create(line2))
        self.play(Create(box))
        self.wait(1)

        ##SECOND MATRIX
        m2 = Matrix(
            [["-1", "2", "4", "2"],
             ["0", "4", "0", "0"],
             ["-6", "-9", "-12", "4"],
             ["0", "1", "1", "1"]],
             h_buff=1,
             element_alignment_corner=RIGHT*4,
        )
        m2.shift(RIGHT*4).scale(0.7)
        self.add(m2.get_brackets())
        self.play(Write(m2.get_rows()[0]), Write(m2.get_rows()[1]), Write(m2.get_rows()[2]), Write(m2.get_rows()[3]), ReplacementTransform(box, m2.get_brackets()), run_time=2)
        self.wait(1)
        
        #replace brackets with determinant signs around the matrix
        self.play(ReplacementTransform(m2.get_brackets(), MathTex(r"\det").scale(2).shift(RIGHT*1.7)))
        #add back parentheses around the matrix
        self.play(
            Write(MathTex("(").scale(2).shift(RIGHT*2.6)),
            Write(MathTex(")").scale(2).shift(RIGHT*5.5)),
        )
        one = MathTex("1").scale(2).shift(RIGHT*0.8)
        self.play(ReplacementTransform(circle, one))