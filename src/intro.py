from manim import *

from manim_slides import Slide


class Bezier(ParametricFunction):
    def __init__(self, points, **kwargs):
        super().__init__(bezier(points),**kwargs)


class HongOuMendel(Slide):
    def construct(self):

        # Intro
        title = Text("L'effet Hong-Ou-Mendel")
        self.add(title)
        self.wait()
        self.next_slide()

        self.play(FadeOut(title))

        animations = []

        fermi = ImageMobject("figures/fermi.jpg")
        fermi.scale(0.4)
        fermi.to_edge(RIGHT, buff=1)
        fermi_name = Text("Enrico Fermi").next_to(fermi, DOWN)

        bose = ImageMobject("figures/bose.jpg")
        bose.scale(0.8)
        bose.to_edge(LEFT, buff=1)
        bose_name = Text("Satyendra Nath Bose").next_to(bose, DOWN)
        bose_name.scale(0.8)

        self.play(FadeIn(fermi, shift=UP), FadeIn(fermi_name))
        self.play(FadeIn(bose, shift=UP), FadeIn(bose_name))

        self.next_slide()
        # Dégénérescence d'échange

        title = Text("Dégénérescence d'échange")
        title.to_edge(LEFT, buff=1)
        title.to_edge(UP)
        title.scale(0.8)

        p1 = Circle(radius=0.2, fill_opacity=1)
        p1.to_edge(LEFT, buff=1)
        v1 = Vector([1,0])
        v1.next_to(p1, buff=-0.2)
        vitesse = Tex("$v$", color=BLUE)
        vitesse.next_to(v1, direction=DOWN)

        p2 = Circle(radius=0.2, fill_opacity=1)
        p2.to_edge(RIGHT, buff=1)
        v2 = Vector([-1,0])
        v2.next_to(p2, direction=LEFT, buff=-0.2)
        vitesse2 = Tex("$v$", color=BLUE)
        vitesse2.next_to(v2, direction=DOWN)

        self.play(FadeOut(bose), FadeOut(fermi), FadeOut(fermi_name))
        self.play(ReplacementTransform(bose_name, title))
        self.play(FadeIn(p1, shift=RIGHT), FadeIn(p2, shift=LEFT))
        self.play(FadeIn(v1, shift=RIGHT), FadeIn(v2, shift=LEFT))
        self.play(FadeIn(vitesse, shift=DOWN), FadeIn(vitesse2, shift=DOWN))

        self.next_slide()

        points1 = [
                4* RIGHT,
                3* RIGHT,
                2* RIGHT,
                1* RIGHT,
                np.array([0,0,0]),
                2*RIGHT + 2*UP,
                3*RIGHT + 3*UP
        ]
        curve1 = Bezier(points1)
        path1 = VMobject(stroke_color=RED)
        dot1 = Dot(4*RIGHT)
        path1.set_points_as_corners([dot1.get_center(), dot1.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot1.get_center()])
            path.become(previous_path)
        path1.add_updater(update_path)
        self.add(path1, dot1)

        points2 = [
                4* LEFT,
                3* LEFT,
                2* LEFT,
                1* LEFT,
                np.array([0,0,0]),
                2*LEFT + 2*DOWN,
                3*LEFT + 3*DOWN
        ]
        curve2 = Bezier(points2)
        path2 = VMobject(stroke_color=RED)
        dot2 = Dot(4*LEFT)
        path2.set_points_as_corners([dot2.get_center(), dot2.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot2.get_center()])
            path.become(previous_path)
        path2.add_updater(update_path)
        self.add(path2, dot2)

        points3 = [
                4* RIGHT,
                3* RIGHT,
                2* RIGHT,
                1* RIGHT,
                np.array([0,0,0]),
                2*LEFT + 2*DOWN,
                3*LEFT + 3*DOWN
        ]
        curve3 = Bezier(points3)
        path3 = VMobject(stroke_color=BLUE)
        dot3 = Dot(4*RIGHT)
        path3.set_points_as_corners([dot3.get_center(), dot3.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot3.get_center()])
            path.become(previous_path)
        path3.add_updater(update_path)
        self.add(path3, dot3)

        points4 = [
                4* LEFT,
                3* LEFT,
                2* LEFT,
                1* LEFT,
                np.array([0,0,0]),
                2*RIGHT + 2*UP,
                3*RIGHT + 3*UP
        ]
        curve4 = Bezier(points4)
        path4 = VMobject(stroke_color=BLUE)
        dot4 = Dot(4*LEFT)
        path4.set_points_as_corners([dot4.get_center(), dot4.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot4.get_center()])
            path.become(previous_path)
        path4.add_updater(update_path)
        self.add(path4, dot4)
        self.play(MoveAlongPath(dot1, curve1), MoveAlongPath(dot2, curve2), MoveAlongPath(dot3, curve3), MoveAlongPath(dot4, curve4))

        self.next_slide()
        self.remove(path1, path2, path3, path4, dot1, dot2, dot3, dot4)
        box = Square(side_length=3)
        box.set_fill(WHITE, opacity = 1)
        self.play(FadeIn(box))

        points1 = [
                4* RIGHT,
                3* RIGHT,
                2* RIGHT,
                1* RIGHT,
                0.5* RIGHT,
                np.array([0,0,0]),
                RIGHT + UP,
                2*RIGHT + 2*UP,
                3*RIGHT + 3*UP
        ]
        curve1 = Bezier(points1)
        path1 = VMobject()
        dot1 = Dot(4*RIGHT)
        path1.set_points_as_corners([dot1.get_center(), dot1.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot1.get_center()])
            path.become(previous_path)
        path1.add_updater(update_path)
        self.add(path1, dot1)

        points2 = [
                4* LEFT,
                3* LEFT,
                2* LEFT,
                1* LEFT,
                0.5* LEFT,
                np.array([0,0,0]),
                LEFT + DOWN,
                2*LEFT + 2*DOWN,
                3*LEFT + 3*DOWN
        ]
        curve2 = Bezier(points2)
        path2 = VMobject()
        dot2 = Dot(4*LEFT)
        path2.set_points_as_corners([dot2.get_center(), dot2.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot2.get_center()])
            path.become(previous_path)
        path2.add_updater(update_path)
        self.add(path2, dot2)

        points3 = [
                4* RIGHT,
                3* RIGHT,
                2* RIGHT,
                1* RIGHT,
                0.5* RIGHT,
                np.array([0,0,0]),
                LEFT + DOWN,
                2*LEFT + 2*DOWN,
                3*LEFT + 3*DOWN
        ]
        curve3 = Bezier(points3)
        path3 = VMobject()
        dot3 = Dot(4*RIGHT)
        path3.set_points_as_corners([dot3.get_center(), dot3.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot3.get_center()])
            path.become(previous_path)
        path3.add_updater(update_path)
        self.add(path3, dot3)

        points4 = [
                4* LEFT,
                3* LEFT,
                2* LEFT,
                1* LEFT,
                0.5* LEFT,
                np.array([0,0,0]),
                RIGHT + UP,
                2*RIGHT + 2*UP,
                3*RIGHT + 3*UP
        ]
        curve4 = Bezier(points4)
        path4 = VMobject()
        dot4 = Dot(4*LEFT)
        path4.set_points_as_corners([dot4.get_center(), dot4.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot4.get_center()])
            path.become(previous_path)
        path4.add_updater(update_path)
        self.add(path4, dot4)
        self.play(MoveAlongPath(dot1, curve1), MoveAlongPath(dot2, curve2), MoveAlongPath(dot3, curve3), MoveAlongPath(dot4, curve4))

        self.remove(path1, path2, path3, path4, dot1, dot2, dot3, dot4, vitesse, vitesse2)

        prob = Text("Fonction d'onde")
        prob.to_edge(LEFT, buff=1)
        prob.to_edge(UP)
        prob.scale(0.8)

        self.play(
                FadeOut(v1), FadeOut(v2),
                FadeOut(p1), FadeOut(p2),
                FadeOut(box),
        ReplacementTransform(title, prob)
        )

        fn1 = Tex(r"$P(x\in[a,b])=\int_a^b|\psi(x)|^2\text{d}x$")
        self.play(FadeIn(fn1, shift=UP))
        fn2 = Tex(r"$P(x_1\in[a,b],x_2\in[c,d])=\int_a^b\int_c^d|\psi(x_1,x_2)|^2\text{d}x_1\text{d}x_2$")
        self.next_slide()
        self.play(
        ReplacementTransform(fn1, fn2)
                )
        self.next_slide()
        pog = Tex(r"$\psi(x_1,x_2)=\pm\psi(x_2,x_1)$, Deux solutions!")
        pog.next_to(fn2, direction=DOWN)
        self.play(FadeIn(pog, shift=DOWN))
        self.next_slide()


        title = Text("Bosons")
        title.to_edge(LEFT, buff=1)
        title.to_edge(UP)
        title.scale(0.8)
        self.play(
                FadeOut(fn2),
                FadeOut(pog),
        ReplacementTransform(prob, title)
        )
        pog = Tex(r"$\psi(x_1,x_2)=\psi(x_2,x_1)$")
        adag = Tex(r"$|0\rangle\qquad\qquad a^\dagger|0\rangle\qquad\qquad a^\dagger a^\dagger|0\rangle$")
        adag.next_to(pog, direction=DOWN)

        self.play(
                FadeIn(pog),
                FadeIn(adag)
                )
        self.next_slide()
        adagn = Tex(r"$|0\rangle\qquad\qquad a_1^\dagger|0\rangle\qquad\qquad a_2^\dagger a_1^\dagger|0\rangle$")
        adagn.next_to(pog, direction=DOWN)
        self.play(
        ReplacementTransform(adag, adagn)
        )
        self.next_slide()
        prop1 = Tex(r"$a_1^\dagger a_2^\dagger=a_2^\dagger a_1^\dagger$")
        prop1.next_to(adagn, direction=DOWN)
        self.play(FadeIn(prop1))
        self.next_slide()
        self.remove(prop1)

        titlen = Text("Fermions")
        titlen.to_edge(LEFT, buff=1)
        titlen.to_edge(UP)
        titlen.scale(0.8)
        pogn = Tex(r"$\psi(x_1,x_2)=-\psi(x_2,x_1)$")
        adag = Tex(r"$|0\rangle\qquad\qquad c^\dagger|0\rangle\qquad\qquad c^\dagger c^\dagger|0\rangle$")
        adag.next_to(pog, direction=DOWN)

        self.play(
        ReplacementTransform(pog, pogn),
        ReplacementTransform(adagn, adag),
        ReplacementTransform(title, titlen)
        )
        self.next_slide()
        adagn = Tex(r"$|0\rangle\qquad\qquad c_1^\dagger|0\rangle\qquad\qquad c_2^\dagger c_1^\dagger|0\rangle$")
        adagn.next_to(pog, direction=DOWN)
        self.play(
        ReplacementTransform(adag, adagn)
        )
        self.next_slide()
        prop1 = Tex(r"$c_1^\dagger c_2^\dagger=-c_2^\dagger c_1^\dagger$")
        prop1.next_to(adagn, direction=DOWN)
        self.play(FadeIn(prop1))
        prop2 = Tex(r"$c_1^\dagger c_1^\dagger=0$")
        prop2.next_to(prop1, direction=DOWN)
        self.play(FadeIn(prop2))
        self.next_slide()
        self.remove(prop1)
        self.remove(prop2)

        self.wait()
