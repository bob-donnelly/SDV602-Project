import PySimpleGUI as sg

#TODO 1) Research and implement Canvas Graph placeholder. 2) Layout of Frames or Columns of elements.
# , element_padding=(10,10)

def main():
    DESone()
    
def DESone():
    
    sg.theme('DarkBlack1') 
    
    layout = [  [sg.Output(size=(20, 10))],           
                [sg.Output(size=(20, 20))],
                [sg.Multiline(size=(20, 5), enter_submits=True)], 
                [sg.Button('Chat')],
                [sg.Button('Pan'), sg.Button('Zoom In'), sg.Button('Zoom Out')],
                [sg.Button('Use Data'), sg.Button('Upload Data')],
                [sg.Button('DES One'), sg.Button('DES Two'), sg.Button('DES Three'), sg.Button('Logout')] ]
    
    
    window = sg.Window('DES App - Screen One', layout, resizable=True, size=(1200,700)).Finalize()
    window.Maximize()
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Logout':
            break
        if event == 'Chat':
            print(values[0])
#         if event == 'DES Two':
#             window.close()
#             DEStwo()
#         if event == 'DES Three':
#             window.close()
#             DESthree()
#         if event == 'DES One':
#             window.close()
#             DESone()

# def DEStwo():
    
#     sg.theme('DarkBlack1') 
    
#     layout = [  [sg.Output(size=(50, 10))],
#                 [sg.Multiline(size=(50, 10), enter_submits=True)], 
#                 [sg.Button('Chat')],
#                 [sg.Button('Pan'), sg.Button('Zoom In'), sg.Button('Zoom Out')],
#                 [sg.Button('Use Data'), sg.Button('Upload Data')],
#                 [sg.Button('DES One'), sg.Button('DES Two'), sg.Button('DES Three'), sg.Button('Logout')] ]
    
    
#     window = sg.Window('DES App - Screen Two', layout, resizable=True, size=(1200,700), element_padding=(10,10)).Finalize()
#     window.Maximize()
    
#     while True:
#         event, values = window.read()
#         if event == sg.WIN_CLOSED or event == 'Logout':
#             break
#         if event == 'Chat':
#             print(values[0]) 
#         if event == 'DES Two':
#             window.close()
#             DEStwo()
#         if event == 'DES Three':
#             window.close()
#             DESthree()
#         if event == 'DES One':
#             window.close()
#             DESone()
            
# def DESthree():
    
#     sg.theme('DarkBlack1') 
    
#     layout = [  [sg.Output(size=(50, 10))],
#                 [sg.Multiline(size=(50, 10), enter_submits=True)], 
#                 [sg.Button('Chat')],
#                 [sg.Button('Pan'), sg.Button('Zoom In'), sg.Button('Zoom Out')],
#                 [sg.Button('Use Data'), sg.Button('Upload Data')],
#                 [sg.Button('DES One'), sg.Button('DES Two'), sg.Button('DES Three'), sg.Button('Logout')] ]
    
    
#     window = sg.Window('DES App - Screen Three', layout, resizable=True, size=(1200,700), element_padding=(10,10)).Finalize()
#     window.Maximize()
    
#     while True:
#         event, values = window.read()
#         if event == sg.WIN_CLOSED or event == 'Logout':
#             break
#         if event == 'Chat':
#             print(values[0]) 
#         if event == 'DES Two':
#             window.close()
#             DEStwo()
#         if event == 'DES Three':
#             window.close()
#             DESthree()
#         if event == 'DES One':
#             window.close()
#             DESone()

if __name__ == "__main__":
    main()
