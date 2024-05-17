import PySimpleGUI as sg

label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")
window = sg.Window("File Compressor",
                   layout=[[label],
                           [sg.Radio("Amphibians", group_id="question1")],
                           [sg.Radio("Fish", group_id="question1")],
                           [sg.Radio("Mammals", group_id="question1")],
                           [sg.Radio("Birds", group_id="question1")],
                           [[sg.Image(sg.EMOJI_BASE64_READING)]]
                           ])


window.read()
window.close()