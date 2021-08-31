# Importing necessary modules to run the GUI and charts.
# Number Py, matpilotlib, Tkinter functions in Pysimplegui etc 

import PySimpleGUI as sg
import matplotlib.pyplot
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')


#TODO 1) Research and implement Canvas Graph placeholder. Done.
#TODO 2) Layout of Frames or Columns of elements. Done.

# Variables declared for spacer columns to move elements around.
# Just as an indicator of placement not finalised.

sz=(50,20)
col1=[[sg.Text(size=sz)]]
col2=[[sg.Text(size=(175, 0))]]
col3=[[sg.Text(size=(90 , 0))]]
col4=[[sg.Text(size=(175, 0))]]
col5=[[sg.Text(size=(175, 0))]]
col6=[[sg.Text(size=(177, 0))]]
col7=[[sg.Text(size=(70 , 0))]]

col8=[[sg.Text(size=sz)]]
col9=[[sg.Text(size=(175, 0))]]
col10=[[sg.Text(size=(90 , 0))]]
col11=[[sg.Text(size=(175, 0))]]
col12=[[sg.Text(size=(175, 0))]]
col13=[[sg.Text(size=(177, 0))]]
col14=[[sg.Text(size=(70 , 0))]]

col15=[[sg.Text(size=sz)]]
col16=[[sg.Text(size=(175, 0))]]
col17=[[sg.Text(size=(90 , 0))]]
col18=[[sg.Text(size=(175, 0))]]
col19=[[sg.Text(size=(175, 0))]]
col20=[[sg.Text(size=(177, 0))]]
col21=[[sg.Text(size=(70 , 0))]]

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

    
def DESone():
    """
    All of the DES screens / functions are the same the graph will be changed in later versions.
    All buttons except for chat, DES screens and Logout are non functional in this prototype.
    
    The first line of the function sets the theme of the GUI to dark mode.
    
    Layouts populate the window with buttons, chat windows or even canvas elements with columns pushing elements into place.
    
    Chat window is functional can output text input, the first output is intended to grab login information i.e., 
    member names to know who is online and is non functional.
    
    Window creates a window with a title from the layout, a resizeable window and size of the it defaults to which we finalise.
    
    Window maximise starts the window maximised to the screen. 
    
    Figure canvas graph variable creates a window we load into the main window.
    
    While loop that while true reads all events and values i.e., registering button clicks etc
    
    If the window closed or logout button (logout will go to login eventually) is clicked it will close otherwise it will run.
    
    The rest of the if statements switch between DES screens. 
    
    NOTE 
    
    Currently you can only navigate in a line i.e., DES One -> DES Two -> DES Three as columns throw an error if you try to
    load the same screen you are on or try to move back to a screen previously visited in the session but you can navigate
    between all screens once. Later version will fix this.
    
    """
    sg.theme('DarkBlack1') 
    
    layout = [  [sg.Column(col1), sg.Canvas(key='-CANVAS-')],
                [sg.Column(col3), sg.Button('Pan'), sg.Button('Zoom In'), sg.Button('Zoom Out')],
                [sg.Column(col4), sg.Output(size=(5, 5))],           
                [sg.Column(col2), sg.Output(size=(5, 5))],
                [sg.Column(col5), sg.Multiline(size=(5, 5), enter_submits=True)], 
                [sg.Column(col6), sg.Button('Chat')],
                [sg.Button('Use Data'), sg.Button('Upload Data')],
                [sg.Column(col7), sg.Button('DES One'), sg.Button('DES Two'), sg.Button('DES Three'), sg.Button('Logout')] ]
    
    
    window = sg.Window('DES App - Screen One', layout, resizable=True, size=(1200,700)).Finalize()
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
            DEStwo()
        if event == 'DES Three':
            window.close()
            DESthree()
        if event == 'DES One':
            window.close()
            DESone()
        

def DEStwo():
    """
    Refer to docstring of DESone.
    """
    sg.theme('DarkBlack1') 
    
    layout = [  [sg.Column(col8), sg.Canvas(key='-CANVAS-')],
                [sg.Column(col10), sg.Button('Pan'), sg.Button('Zoom In'), sg.Button('Zoom Out')],
                [sg.Column(col9), sg.Output(size=(5, 5))],           
                [sg.Column(col11), sg.Output(size=(5, 5))],
                [sg.Column(col12), sg.Multiline(size=(5, 5), enter_submits=True)], 
                [sg.Column(col13), sg.Button('Chat')],
                [sg.Button('Use Data'), sg.Button('Upload Data')],
                [sg.Column(col14), sg.Button('DES One'), sg.Button('DES Two'), sg.Button('DES Three'), sg.Button('Logout')] ]
    
    
    window = sg.Window('DES App - Screen Two', layout, resizable=True, size=(1200,700)).Finalize()
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
            DEStwo()
        if event == 'DES Three':
            window.close()
            DESthree()
        if event == 'DES One':
            window.close()
            DESone()
            
def DESthree():
    """
    Refer to docstring of DESone.
    """
    sg.theme('DarkBlack1') 
    
    layout = [  [sg.Column(col15), sg.Canvas(key='-CANVAS-')],
                [sg.Column(col17), sg.Button('Pan'), sg.Button('Zoom In'), sg.Button('Zoom Out')],
                [sg.Column(col16), sg.Output(size=(5, 5))],           
                [sg.Column(col18), sg.Output(size=(5, 5))],
                [sg.Column(col19), sg.Multiline(size=(5, 5), enter_submits=True)], 
                [sg.Column(col20), sg.Button('Chat')],
                [sg.Button('Use Data'), sg.Button('Upload Data')],
                [sg.Column(col21), sg.Button('DES One'), sg.Button('DES Two'), sg.Button('DES Three'), sg.Button('Logout')] ]
    
    
    window = sg.Window('DES App - Screen Three', layout, resizable=True, size=(1200,700)).Finalize()
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
            DEStwo()
        if event == 'DES Three':
            window.close()
            DESthree()
        if event == 'DES One':
            window.close()
            DESone()
            

def main():
    """
    The main function runs DESone() to start the windows running but as DEES functions call each other it is unnecessary to call again.
    """
    DESone()

# The if name string is required to run functions through the interpreter. 

if __name__ == "__main__":
    main()
