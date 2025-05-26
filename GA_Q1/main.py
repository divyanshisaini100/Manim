from manim import *
import os
import shutil

media_path = './media/videos'
if os.path.exists(media_path):
    shutil.rmtree(media_path)

class ga_q1(Scene):
    def construct(self):

        #maths eq
        eq = MathTex(r"f_{XY} = \begin{cases}"
                     r"\frac{1}{36} (3x + y), & \text{if } x,y \in \{0,1,2\} \\"
                     r"0, & \text{otherwise}\\"
                     r"\end{cases}")
        eq.move_to(ORIGIN)
        self.play(Write(eq))
        self.wait(0.2)

        self.play(eq.animate.scale(1.5),run_time = 1)
        self.wait(1)

        self.play(eq.animate.scale(0.5).to_corner(UL),run_time=1)
        self.wait(0.5)

        box = SurroundingRectangle(eq,color=YELLOW,buff =0.2)
        self.play(Create(box)) 

        
        # Add example animation
          
        eg = MathTex(
            r"\text{Let's take, }",
            r"X = ",
            r"1",
            r"\text{ and } Y = ",
            r"2",
            font_size=34)

# Now eg has parts split as:
# 0: "Let's take, "
# 1: "X = "
# 2: "1"
# 3: " and Y = "
# 4: "2"

        eg[2].set_color(RED)
        eg[4].set_color(RED)
                
        self.add(eg)
        self.wait(0.2)

        self.play(eg.animate.shift(UP*1))
        self.wait(0.2)
        

        # Create the MathTex formula
        sol = MathTex(r"f_{XY}(0,0) = \frac{1}{36}(3 \cdot 1 + 2)",font_size=30)
        sol.next_to(eg, DOWN * 1.5, buff=0.2)
        self.add(sol)
        self.wait(0.1)

        # Calculate and display value
        val = (1/36) * (3 * 1 + 2)  # = 5/36
        val_text = MathTex(f"= {val:.2f}",font_size=30)
        val_text.next_to(sol,DOWN, buff=0.2)
        self.play(Create(val_text))
        self.wait(0.5)

        gr = VGroup(eg,sol,val_text)

        self.play(gr.animate.to_edge(LEFT,buff=0.5))
        self.wait(0.1)


        #create a 3x3 grid

        grid_size = 3
        square_size = 1
        
        squares = VGroup()
        texts= VGroup()

        for y in range(grid_size):
            for x in range(grid_size):
                sq = Square(side_length=square_size)
                sq.move_to(RIGHT*x  +  DOWN*y)
                sq.set_stroke(color=WHITE)
                squares.add(sq)

                value = (1/36)*((3*x) + y)
                square = squares[y*grid_size + x]
                label=Text(f'{value:.2f}',font_size = 24,color=BLUE).move_to(square)
                texts.add(label)

        #centre grid 
        squares.move_to(ORIGIN)
        
        self.play(LaggedStartMap(Create,squares), run_time = 3)   

        x_labels = VGroup()
        for i in range(grid_size):
            label = Text(str(i), font_size=24).next_to(squares[i],UP, buff=0.2)
            x_labels.add(label)

        y_labels = VGroup()
        for i in range(grid_size):
            label = Text(str(i),font_size=24).next_to(squares[i*grid_size],LEFT,buff=0.2)
            y_labels.add(label)

        self.play(Write(x_labels),Write(y_labels))   

        
        x_title = Text('X',font_size=24).next_to(x_labels,LEFT,buff=0.2)
        
        y_title = Text('Y',font_size=24).next_to(y_labels,UP,buff=0.2)

              

        self.play(Write(x_title),Write(y_title))

        corner = squares[0].get_corner(UL)
        diag_line = Line(start = corner+0.4*UL,
                         end = corner + 0.1*UL)
        diag_line.set_stroke(color=WHITE,width=2)
        self.play(Create(diag_line)) 
        #center texts
        texts.move_to(ORIGIN)
        for text in texts:
            self.play(Create(text), run_time=0.3)

        gro = VGroup(squares,x_labels,y_labels,x_title,y_title,texts,diag_line)  
        self.play(gro.animate.scale(1.5).shift(RIGHT*3)) 
        self.wait(5)
        