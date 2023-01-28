import PySimpleGUI as sg


GradesDictionary = {}
subjects = ["English", "Math", 'Science', "Chinese", "gezegence"]
studentNames =['Albedo', 'Barbara', 'Chongyun']

layout_subjects = [
    [sg.Text(subject), sg.Push(), sg.InputText(do_not_clear=False, key=subject)]
        for subject in subjects
]
Layout = [
    [sg.Text('Select student name'),
     sg.Combo(studentNames, enable_events=True, key='current_student')],
    [sg.Column(layout_subjects)],
    [sg.B("Submit"), sg.Cancel()],  # standard button to submit score and leave window
]
resultsWindow = sg.Window("Register Results", Layout, finalize=True)

while True:
    event, values = resultsWindow.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
    elif event == "Submit":
        name = values['current_student']
        if name in studentNames:
            GradesDictionary[name] = {subject:values[subject] for subject in subjects}
            print(GradesDictionary)

resultsWindow.close()