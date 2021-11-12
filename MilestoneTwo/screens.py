"""
Help docstring encapsulates the entire purpose of this file.

This module is to create three data explerer screens.

with a chat system
"""

# Importing necessary modules to run the GUI and charts.
# matpilotlib, Tkinter functions in Pysimplegui etc

import PySimpleGUI as sg
import matplotlib.pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
matplotlib.use('TkAgg')
import read as rd
import canvas as can

# Variables for filling the graph with data.

fig = matplotlib.figure.Figure(figsize=(10, 4), dpi=100)
timber = rd.returnValues()
fig.add_subplot().plot(timber.Year, timber["Export Quantity"])
# fig_canvas_graph = can.draw_figure_w_toolbar()
class desScreen(object):
    def makeColumns(self):
        
        sz=(20,20)
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
                    # [sg.Column(self.col17), sg.Button('Pan'), sg.Button('Zoom In'), sg.Button('Zoom Out')],
                    [sg.Column(self.col16), sg.Output(size=(10, 5))],           
                    [sg.Column(self.col18), sg.Output(size=(10, 5))],
                    [sg.Column(self.col19), sg.Multiline(size=(10, 5), enter_submits=True)], 
                    [sg.Column(self.col20), sg.Button('Chat')],
                    [sg.Button('Use Data'), sg.Button('Upload Data')],
                    [sg.Column(self.col21), sg.Button('DES One'), sg.Button('DES Two'), sg.Button('DES Three'), sg.Button('Logout')] ]
        
        
        window = sg.Window('DES App', layout, resizable=True, size=(1200,700)).Finalize()
        window.Maximize()
        
        can.draw_figure_w_toolbar(window['-CANVAS-'].TKCanvas, fig, window['-CANVAS-'].TKCanvas)
        
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
    The main function runs global variable DESone to start the windows running but as DEES functions call each other it is unnecessary to call again.
    """
    global DESone

    DESone.display()

# The if name string is required to run functions through the interpreter. 

if __name__ == "__main__":
    main()
    
