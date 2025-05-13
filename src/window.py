from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root_widget = Tk()
        self.__root_widget.title = "Maze Solver"
        self.__canvas = Canvas(self.__root_widget, bg="gray", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__active = True
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.Close)

    def Draw_item(self, item, fill_color):
        item.Draw(self.__canvas, fill_color)

    def Draw_item_over_time(self, item, fill_color):
        return item.Draw_over_time(self.__canvas, fill_color)

    def Redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def Wait_for_close(self):
        while self.__active:
            self.Redraw()

    def Is_active(self):
        return self.__active

    def Close(self):
        self.__active = False