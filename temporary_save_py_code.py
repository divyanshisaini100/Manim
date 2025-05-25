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