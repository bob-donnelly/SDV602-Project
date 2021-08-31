# Importing necessary modules to run the GUI and charts.
# Number Py, matpilotlib, Tkinter functions in Pysimplegui etc 

import PySimpleGUI as sg
import matplotlib.pyplot
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')


#TODO 1) Research and implement Canvas Graph placeholder. Done.
#TODO 2) Layout of Frames or Columns of elements.

fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

def main():
    DESone()
    
def DESone():
    
    sg.theme('DarkBlack1') 
    
    layout = [  [sg.Canvas(key='-CANVAS-')],
                [sg.Output(size=(5, 5))],           
                [sg.Output(size=(5, 5))],
                [sg.Multiline(size=(5, 5), enter_submits=True)], 
                [sg.Button('Chat')],
                [sg.Button('Pan'), sg.Button('Zoom In'), sg.Button('Zoom Out')],
                [sg.Button('Use Data'), sg.Button('Upload Data')],
                [sg.Button('DES One'), sg.Button('DES Two'), sg.Button('DES Three'), sg.Button('Logout')] ]
    
    
    window = sg.Window('DES App - Screen One', layout, resizable=True, size=(1200,700)).Finalize()
    window.Maximize()
    
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
    
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
    
    sg.theme('DarkBlack1') 
    
    layout = [  [sg.Canvas(key='-CANVAS-')],
                [sg.Output(size=(5, 5))],           
                [sg.Output(size=(5, 5))],
                [sg.Multiline(size=(5, 5), enter_submits=True)], 
                [sg.Button('Chat')],
                [sg.Button('Pan'), sg.Button('Zoom In'), sg.Button('Zoom Out')],
                [sg.Button('Use Data'), sg.Button('Upload Data')],
                [sg.Button('DES One'), sg.Button('DES Two'), sg.Button('DES Three'), sg.Button('Logout')] ]
    
    
    window = sg.Window('DES App - Screen One', layout, resizable=True, size=(1200,700)).Finalize()
    window.Maximize()
    
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
    
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
    
    sg.theme('DarkBlack1') 
    
    layout = [  [sg.Canvas(key='-CANVAS-')],
                [sg.Output(size=(5, 5))],           
                [sg.Output(size=(5, 5))],
                [sg.Multiline(size=(5, 5), enter_submits=True)], 
                [sg.Button('Chat')],
                [sg.Button('Pan'), sg.Button('Zoom In'), sg.Button('Zoom Out')],
                [sg.Button('Use Data'), sg.Button('Upload Data')],
                [sg.Button('DES One'), sg.Button('DES Two'), sg.Button('DES Three'), sg.Button('Logout')] ]
    
    
    window = sg.Window('DES App - Screen One', layout, resizable=True, size=(1200,700)).Finalize()
    window.Maximize()
    
    fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
    
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
            
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

if __name__ == "__main__":
    main()
