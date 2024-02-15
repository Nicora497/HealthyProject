import tkinter as tk

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.ticker import MaxNLocator

import datetime

from Calendar import Calendar

#main
class HEALTH(tk.Frame):
    def __init__(self, master=None,cnf={},**kw):
        tk.Frame.__init__(self,master,cnf,**kw)
        
        self.master.title("App")
        self.master.geometry("400x800")
        self.propagate(False)
        self.pack()
    
        ketu = KETU(root)
        ketu.pack()
        
        mycal = Calendar(root)
        mycal.pack()
        

#血圧
class KETU(tk.Frame):
    def __init__(self,master=None,cnf={},**kw):
        super().__init__(master,cnf,**kw)

        frame_top = tk.Frame(self.master, width=400, height=300, bg = 'black', relief='solid')
        frame_top.pack()
        
        fig = Figure(dpi=100,figsize=(4, 3))
        ax = fig.add_subplot(1, 1, 1)
        
        fig_canvas = FigureCanvasTkAgg(fig, frame_top)
        fig_canvas.get_tk_widget().pack(fill=tk.Y, expand=False)
        
        date = datetime.datetime.now()
        date_num = date.day
        x = [date_num-4, date_num-3, date_num-2, date_num-1, date_num]
        y = [10,20,30,40,50]
        
        ax.plot(x, y, marker='.')
        
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        #ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        
        # 表示
        fig_canvas.draw()


        frame_top.propagate(False)
        


class TMP(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        B = tk.Button()
        B.pack()
        
        self.pack()
        
        
root = tk.Tk()
app = HEALTH(master=root)
app.mainloop()
