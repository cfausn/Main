"""
CONFIDENTIALITY NOTE:  This code is intended only for the instructors of
CS1, as well as graders and mentors of this course who have previously
received permission to use said material in assisting students.  Under no
circumstances should this program be reviewed, retransmitted, disseminated
or in any other way shared with anyone other than the intended recipients
mentioned above.  If you received this program and are not its intended
audience, please contact the author immediately and destroy all copies
(electronic or hardcopy).
"""

"""
Project: Unigrams
Task: Word Frequencies and Average Word Length (Part Two/Three)

This is a plotting utility the students will use in parts two and
three of the project to plot the data the calculate.  This plotter
uses the Python defacto standard GUI, tkInter.

Author: Amar Saric
Language: Python 3
"""

import tkinter 
from tkinter import font as tkfont
import math
from string import ascii_lowercase as _LETTERS

###########################################################
# IMPLEMENTATION                                 
###########################################################


class plot2D(tkinter.Tk):
    
    class _plot2D_canvas(tkinter.Canvas):
    
        def __init__(self, root, labels):
            super().__init__(root, width=800, height=600)
            self.boundary = 25
            self.space_label = 40 if labels != ('','') else 0
            self.left_boundary = 100 + self.space_label
            self.bottom_boundary = 75 + self.space_label
            self.hlabel, self.vlabel = labels
            self.pack(fill="both", expand=True)
            self.configure(background='white')
            self.bind("<Configure>", self.resize)
            self.font = tkfont.Font(family='Courier', size=12, weight='normal')
            self.data =[]

        def resize(self, event):
            self.plot()     
                
        def add_point(self, x, y):
            self.data.append((x, y))
            
    
        def plot(self):
            if len(self.data) < 1:
                return
            
            width, height= self.winfo_width(),  self.winfo_height()
            self.create_rectangle(0, 0, width, height, fill="white")
            width -= self.boundary + self.left_boundary
            height -= self.boundary + self.bottom_boundary
            
            if width < 2*self.boundary or height < 2*self.boundary: # too small to display anything
                return
            
            def range_x(data):
                return min (a for (a,_) in data), max (a for (a,_) in data)
        
            def range_y(data):
                return min (b for (_,b) in data), max (b for (_,b) in data)
            
            x_min, x_max= range_x(self.data)
            y_min, y_max= range_y(self.data)
            
            len_x, len_y= x_max - x_min, y_max - y_min
            if len_x <= 0 or len_y <= 0:
                return
               
            scaled = [  ((x-x_min)*width/len_x + self.left_boundary, -(y-y_min)*height/len_y+  self.boundary + height) 
                        for (x,y) in self.data  ] 
            
            first = True                 
            for x, y in scaled:
                if first:         
                    first = False
                else:
                    self.create_line( prev_x, prev_y, x, y, fill="black") #@UndefinedVariable
                prev_x, prev_y = x, y  #@UnusedVariable
            
            #grid...
            def log_magnitude (x):
                return math.floor(math.log(math.fabs(x))/math.log(10)) - 1 
            
            def format_label(val,inc):
                if (math.fabs(int (inc) - inc) < 0.00001):
                    label = str(int(val))
                else:
                    label = "{0:4.2f}".format(val)
                if len(label) > 7:
                    label = '{:.1e}'.format(val)
                return label
            
            x_min_bound, x_max_bound = range_x (scaled)
            y_min_bound, y_max_bound = range_y (scaled)
            width, height=  x_max_bound - x_min_bound, y_max_bound - y_min_bound 
            
            inc_x, inc_y = 10**log_magnitude(len_x), 10**log_magnitude(len_y)
            delta_x, delta_y = inc_x, inc_y
            step_x, step_y = 0, 0
            
            for i in [1, 5, 10, 50, 100]:
                if step_x >= 50 and step_y >= 50:
                    break
                if step_x < 50:
                    inc_x = i*delta_x
                    step_x = inc_x * width/len_x
                if step_y < 50:
                    inc_y = i*delta_y
                    step_y = inc_y * height/len_y  
                                 
            start_x, start_y = x_min//inc_x*inc_x,  y_min//inc_y*inc_y
            offset_x, offset_y = (start_x - x_min)* width/len_x, (start_y - y_min)* height/len_y            
            num_x_lines, num_y_lines= math.floor(width/step_x), math.floor( height/step_y) 
             
            for i in range ( num_x_lines + 1):
                x = self.left_boundary + offset_x + i*step_x
                if not (x_min_bound < x < x_max_bound):
                    continue
                self.create_line(x, self.boundary, x, self.boundary + height, dash = (2, 4)) 
                label = format_label(start_x + i*inc_x, inc_x)
                self.create_text(x, y_max_bound + (self.bottom_boundary-self.space_label)/2, 
                                 font = self.font, text=label) 
            for i in range (num_y_lines + 1):
                y = self.boundary + height - offset_y - i*step_y
                if not (y_min_bound < y < y_max_bound):
                    continue
                self.create_line(self.left_boundary, y, self.left_boundary + width, y, dash=(2, 4)) 
                label = format_label(start_y + i*inc_y, inc_y)
                self.create_text((self.left_boundary-self.space_label)/2 +self.space_label, y, font=self.font, text=label)  
    
            #labels...  
            vlablel_offset = (y_min_bound + y_max_bound)/2 - 25 * len(self.vlabel)//2
            for i in range (len(self.vlabel)):
                self.create_text(self.space_label /2,vlablel_offset + 25*i,
                                  font = self.font,  text= self.vlabel[i])
            self.create_text( (x_min_bound + x_max_bound)/2, 
                              y_max_bound + self.bottom_boundary - self.space_label, 
                              font = self.font,  text= self.hlabel)
            
            #box ...    
            self.create_line( x_min_bound, y_min_bound, x_max_bound, y_min_bound, fill="black")
            self.create_line( x_min_bound, y_max_bound, x_max_bound, y_max_bound, fill="black")
            self.create_line( x_min_bound, y_min_bound, x_min_bound, y_max_bound, fill="black")
            self.create_line( x_max_bound, y_min_bound, x_max_bound, y_max_bound, fill="black")
        
    def  __init__ (self, title, labels = ('','')):
        super().__init__()
        self.title(title)
        self.canvas = self._plot2D_canvas(self,labels)
    
    def addPoint(self,p):
        self.canvas.add_point(p[0],p[1])
        
    def display(self):
        self.canvas.update()
        self.mainloop()    

###########################################################
# EXAMPLES                                  
########################################################### 
       
if __name__ == '__main__':
    labels = 'X values', 'Y values'
    plot = plot2D('XY plot demo', labels)
    for i in range(3000):
        x = i/100 - 10
        point = x, 1099.122*(math.sin(x)+math.log(11+x)) + 123.22
        plot.addPoint(point)
    plot.display()
    labels = 'Log x values', 'Log y values'
    plot = plot2D('XY loglog plot demo', labels)
    for i in range(1,3000):
        x = i/100 
        point = math.log(x,10), math.log(x**(-5)*10**2,10)
        plot.addPoint(point)
    plot.display()



###########################################################
# INTERFACE
########################################################### 

def wordFreqPlot(freqList):
    """
    Plot the frequency counts of words on a log-log plot to show Zipf's Law.
    Assumes that all values are positive.
    :param freqList (list): A list of WordCount objects
    :return: None
    :rtype: NoneType
    """
    labels = 'Log of word rank', 'Log of frequency'
    plot = plot2D("Zipf's Law (log-log plot)", labels)
    
    for i, wordCount in enumerate(freqList):
        point = math.log(1+i)/math.log(10), math.log(1 + wordCount.count)/math.log(10)
        plot.addPoint(point)
    
    plot.display()
        
def averageWordLengthPlot(startYear, endYear, lengthsList):
    """
    This routine plots the average word lengths over a range of years.
    :param startYear (int): The start year
    :param endYear (int): The end year
    :param lengthsList (list): List of average lengths (floats)
    :return: None
    :rtype: NoneType
    """       
    labels = 'Year', 'Length of word'
    plot = plot2D("Average word length:", labels)
    
    for i, year in enumerate(range(startYear, endYear +1)):
        point = year, lengthsList[i]
        plot.addPoint(point)
        
    plot.display()
    
        
