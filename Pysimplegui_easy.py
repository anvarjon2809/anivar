import PySimpleGUI as sg

layout = [[sg.Graph((800, 400), (-400, -200), (400, 200), background_color='white', key='-GRAPH-')]]

# Window
window = sg.Window(title='Graph Element', layout=layout)
# Allows you to modify the graph before a window.read() call
window.finalize()

# Add text to the graph
window['-GRAPH-'].draw_text('PySimpleGUI is easy!', (-200, 100), font=14)