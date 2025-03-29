from tkinter import *
import random as r


WIDTH = 800
HEIGHT = 600
SEGMENT_SIZE = 20
IN_GAME = True
SCORES = 0
# Igrovie Funksii
def create_apple():
    global Apple

    posx = SEGMENT_SIZE * r.randint(1, int((WIDTH -SEGMENT_SIZE) / SEGMENT_SIZE))
    posy = SEGMENT_SIZE * r.randint(1, int((HEIGHT -SEGMENT_SIZE) / SEGMENT_SIZE))

    Apple = c.create_oval(posx, posy,
                          posx + SEGMENT_SIZE, posy + SEGMENT_SIZE,
                          fill = "red")

def main():
    global IN_GAME, SCORES
    if IN_GAME == True:
        s.move()
        head_coods = c.coords(s.segments[-1].instance)
        x1, y1, x2, y2 = head_coods
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            IN_GAME = False
        elif head_coods == c.coords(Apple):
            SCORES += 1
            scores_label["text"] = SCORES
            if SCORES > 0 and SCORES < 10:
                scores_label["bg"] = "#FF0000"
            if SCORES > 10 and SCORES < 20:
                scores_label["bg"] = "FF00FF"
            s.add_segment()
            c.delete(Apple)
            create_apple()
        else:
            for i in range (len(s.segments) - 1):
                if head_coods == c.coords(s.segments[i].instance):
                    IN_GAME = False
        root.after(100, main)
    else:
        c.create_text(WIDTH/2, HEIGHT/2,
                      text = "Igra okonchena",
                      font = ("Arial", 25),
                      fill = "red")

class Segment(object):
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x,
                                           y,
                                           x + SEGMENT_SIZE,
                                           y + SEGMENT_SIZE,
                                           fill="white")


class Snake(object):
    def __init__(self, segments):
        self.segments = segments

        self.mapping = {
            "Down": (0, 1),
            "Up": (0, -1),
            "Right": (1, 0),
            "Left": (-1, 0)
        }

        self.vector = self.mapping['Right']

    def move(self):
        for i in range(len(self.segments) - 1):
            segment = self.segments[i].instance

            x1, y1, x2, y2 = c.coords(self.segments[i + 1].instance)
            c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)

        c.coords(self.segments[-1].instance,
                 x1 + self.vector[0] * SEGMENT_SIZE,
                 y1 + self.vector[1] * SEGMENT_SIZE,
                 x2 + self.vector[0] * SEGMENT_SIZE,
                 y2 + self.vector[1] * SEGMENT_SIZE)
    def change_direction(self, event):
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]
    def add_segment(self):
        last_segment = c.coords(self.segments[0].instance)
        x = last_segment[2] - SEGMENT_SIZE
        y = last_segment[3] - SEGMENT_SIZE
        self.segments.insert(0, Segment(x, y))

root = Tk()

c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#003300")
c.grid()

scores_label = Label(root, text="0")
scores_label.grid()

segments = [
    Segment(SEGMENT_SIZE, SEGMENT_SIZE),
    Segment(SEGMENT_SIZE*2, SEGMENT_SIZE),
    Segment(SEGMENT_SIZE*3, SEGMENT_SIZE)
]

s = Snake(segments)

c.bind("<KeyPress>", s.change_direction)
create_apple()
main()
c.focus_set()

root.mainloop()