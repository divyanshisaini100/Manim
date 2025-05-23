from manim import *
class NameOfAnimation(Scene):
  def construct(self):
    Gri = NumberPlane(x_range =[-5,5,1] , y_range = [-5,5,1] , background_line_style={"stroke_color":BLUE, "stroke_width": 1, "stroke_opacity":0.4},
    x_axis_config ={'numbers_to_include':list(range(-5,5)) ,'font_size':24, 'color': WHITE} ,
      y_axis_config={'numbers_to_include':list(range(-5,5)),'font_size':24,'color':WHITE},
      axis_config={'include_tip':True, 'tip_shape':StealthTip,'stroke_color':WHITE,'stroke_width':3})
    x_axis = Line(LEFT*5,RIGHT*5,stroke_color=WHITE, stroke_width = 3)
    y_axis = Line(LEFT*5,RIGHT*5,stroke_color=WHITE, stroke_width = 3)
    
   
    self.add(Gri,x_axis,y_axis)

                       
    box = Rectangle(stroke_color = GREEN_C, stroke_opacity=0.7,fill_color = RED_B, fill_opacity = 0.5,height=1,width=1)
    self.add(box)
    self.play(box.animate.shift(RIGHT*2),run_time=2)
    self.play(box.animate.shift(UP*3),run_time=2)
    self.play(box.animate.shift(DOWN*5+LEFT*5), run_time=2)
    self.play(box.animate.shift(UP*1.5+RIGHT*1), run_time=2)
    
