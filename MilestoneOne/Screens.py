import PySimpleGUI as sg

def main():
    DESone()

def DESone():
    
    sg.theme('DarkBlack1') 
    
    layout = [  [sg.Output(size=(50, 20))],
                [sg.Multiline(size=(50, 20), enter_submits=True)], 
                [sg.Button('Chat')],
                [sg.Button('Pan'), sg.Button('Zoom In'), sg.Button('Zoom Out')],
                [sg.Button('Use Data'), sg.Button('Upload Data')],
                [sg.Button('DES One'), sg.Button('DES Two'), sg.Button('DES Three'), sg.Button('Logout')] ]
    
    
    window = sg.Window('DES App - Screen One', layout, resizable=True, size=(1200,700), element_padding=(10,10)).Finalize()
    window.Maximize()
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Chat':
            print(values[0]) 

if __name__ == "__main__":
    main()
