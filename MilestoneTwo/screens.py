"""
Help docstring encapsulates the entire purpose of this file.

This module is to create three data explerer screens.

with a chat system
"""

# Importing necessary modules to run the GUI and charts.
# Number Py, matpilotlib, Tkinter functions in Pysimplegui etc

import PySimpleGUI as sg
import matplotlib.pyplot
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')

# Variables for filling the graph with mock data.

fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

def draw_figure(canvas, figure):
    """
    Uses the canvas and figure arguments to draw the graph on a canvas with multiple variables and a Tkinter widget.
    """
    figure_canvas_graph = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_graph.draw()
    figure_canvas_graph.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_graph


class desScreen(object):
    def makeColumns(self):
        sz=(50,20)
        # self.col1=[[sg.Text(size=sz)]]
        # self.col2=[[sg.Text(size=(175, 0))]]
        # self.col3=[[sg.Text(size=(90 , 0))]]
        # self.col4=[[sg.Text(size=(175, 0))]]
        # self.col5=[[sg.Text(size=(175, 0))]]
        # self.col6=[[sg.Text(size=(177, 0))]]
        # self.col7=[[sg.Text(size=(70 , 0))]]

        # self.col8=[[sg.Text(size=sz)]]
        # self.col9=[[sg.Text(size=(175, 0))]]
        # self.col10=[[sg.Text(size=(90 , 0))]]
        # self.col11=[[sg.Text(size=(175, 0))]]
        # self.col12=[[sg.Text(size=(175, 0))]]
        # self.col13=[[sg.Text(size=(177, 0))]]
        # self.col14=[[sg.Text(size=(70 , 0))]]

        self.col15=[[sg.Text(size=sz)]]
        self.col16=[[sg.Text(size=(175, 0))]]
        self.col17=[[sg.Text(size=(90 , 0))]]
        self.col18=[[sg.Text(size=(175, 0))]]
        self.col19=[[sg.Text(size=(175, 0))]]
        self.col20=[[sg.Text(size=(175, 0))]]
        self.col21=[[sg.Text(size=(70 , 0))]]
        
    def display(self):
        """
        Refer to docstring of DESone.
        """
        global DESone
        global DEStwo
        global DESthree
        
        sg.theme('DarkBlack1') 
        
        self.makeColumns()
        
        layout = [  [sg.Column(self.col15), sg.Canvas(key='-CANVAS-')],
                    [sg.Column(self.col17), sg.Button('Pan'), sg.Button('Zoom In'), sg.Button('Zoom Out')],
                    [sg.Column(self.col16), sg.Output(size=(10, 5))],           
                    [sg.Column(self.col18), sg.Output(size=(10, 5))],
                    [sg.Column(self.col19), sg.Multiline(size=(10, 5), enter_submits=True)], 
                    [sg.Column(self.col20), sg.Button('Chat')],
                    [sg.Button('Use Data'), sg.Button('Upload Data')],
                    [sg.Column(self.col21), sg.Button('DES One'), sg.Button('DES Two'), sg.Button('DES Three'), sg.Button('Logout')] ]
        
        
        window = sg.Window('DES App', layout, resizable=True, size=(1200,700)).Finalize()
        window.Maximize()
        
        fig_canvas_graph = draw_figure(window['-CANVAS-'].TKCanvas, fig)
        
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Logout':
                break
            if event == 'Chat':
                print(values[0])
            if event == 'DES Two':
                window.close()
                DEStwo.display()
            if event == 'DES Three':
                window.close()
                DESthree.display()
            if event == 'DES One':
                window.close()
                DESone.display()

DESone = desScreen()
DEStwo = desScreen()
DESthree = desScreen()

def main():
    """
    The main function runs DESone() to start the windows running but as DEES functions call each other it is unnecessary to call again.
    """
    # DESone()
    global DESone

    DESone.display()

# The if name string is required to run functions through the interpreter. 

if __name__ == "__main__":
    main()