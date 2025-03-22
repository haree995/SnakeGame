from tkinter import  *

width = 800
height = 600
segment_size = 20
in_game = True

class Segment(object):
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x,
                                           y,
                                           x + segment_size,
                                           y + segment_size,fill = "white")



class Snake(object):
    def __init__(self, segments):
        self.segments = segments

        self.mapping = {
            "Down" : (0, 1),
            "Up" : (0, -1),
            "Left" : (1, -1),
            "Right" : (1, 0)
        }

        self.vector = self.mapping["Right"]

    def move(self):
        for i in range(len(self.segments)-1):
            segment = self.segments[i].instance

            x1, y2, x2, y2 = c.coords(self.segments[i+1].instance)
            c.coords(segment, x1, y1, x2, y2)

            x1, y1, x2, y2 = c.coords(self.segments[-2].instance)

            c.coords(self.segments[-1].instance,
                     x1 + self.vector[0] * segment_size,
                     y1 + self.vector[1] * segment_size,
                     x2 + self.vector[0] * segment_size,
                     y2 + self.vector[1] * segment_size)

    def change_derection(self, event):
        if event.keysum in self.mapping:
            self.vector = self.mapping[event.keysum]
    def add_segment(self):
        last_segment = c.coords(self.segments[0].instance)
        x = last_segment[2] - segment_size
        y = last_segment[3] - segment_size
        self.segments.insert(0, Segment(x, y))



root = Tk()

c = Canvas(root, width = width, height=height, bg = "#FFD700")
c.place(x=0, y=0)

segments = {
    Segment(segment_size, segment_size),
    Segment(segment_size*2, segment_size),
    Segment(segment_size*3, segment_size)
}

s = Snake(segments)

c.focus_set()
root.mainloop()