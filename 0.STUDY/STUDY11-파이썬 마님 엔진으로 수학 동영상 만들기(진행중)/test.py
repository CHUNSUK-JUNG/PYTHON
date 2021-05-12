from manimlib.imports import *

class CoordinateEx1(Scene):
    def construct(self):
        #1. create objects
        title = self.get_title()
        body = self.get_body()
        subtitle = self.get_subtitle()

        #2. locate objects
        title.move_to(ORIGIN).to_edge(UP, buff=1)
        body.next_to(title, DOWN, buff=1)
        subtitle.to_edge(DOWN, buff=0.5)

        #3. animate objects
        self.play(FadeIn(title), run_time=2)
        self.play(FadeIn(body), run_time=2)
        self.play(FadeIn(subtitle), run_time=2)
        self.wait(2)

    def get_text(self, str, color=WHITE, size=0.4):
        return Text(str, font='굴림', stroke_width=1, color=color, size=size)

    def get_title(self):
        t1 = self.get_text("IMF 국제통화기금", color=BLUE, size=0.4 )
        t2 = self.get_text("2020 세계 경제 전망", color=WHITE, size=0.6)

        t2.next_to(t1, RIGHT, buff=0.3)
        text = VGroup(t1, t2)