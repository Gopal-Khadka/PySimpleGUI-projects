import PySimpleGUI as sg

# layout = [
#     [sg.I(key="PATH")],
# [
#     sg.FileBrowse(
#         target="PATH", file_types=(("ALL FILES", "*"), ("PNG FILES", ".png"))
#     )
# ],
# [
#     sg.FilesBrowse(
#         target="PATH", file_types=(("ALL FILES", "*"), ("PNG FILES", ".png"))
#     )
# ],
# [sg.FolderBrowse(target="PATH")],
# [sg.CalendarButton("Calendar",key="calendar")],
# [sg.FileSaveAs()],
# [sg.Ok(), sg.Cancel()],
# ]
header = ["name", "Age", "gender"]
rows = [
    ["Harry", 26, "Male"],
    ["Henry", 28, "Male"],
    ["Henry", 28, "Male"],
    ["Henry", 28, "Male"],
    ["Henry", 28, "Male"],
    ["Henry", 28, "Male"],
]
layout = [[sg.Table(headings=header, values=rows, key="TABLE")], [sg.Ok(), sg.Cancel()]]

root = sg.Window("Buttons App", layout)
event, value = root.read()
print(event, value)
