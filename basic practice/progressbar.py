import PySimpleGUI as sg

# ----LAYOUT PYSIMPLEGUI---------------#
# layout=[[sg.ProgressBar(max_value=1000,orientation="h",key="P_BAR",bar_color="red",border_width=1,size=(30,15)),]]

# root = sg.Window("ProgressBar App", layout, size=(600, 600))
# for i in range(1000):
#     event, value = root.read(timeout=1)
#     root["P_BAR"].UpdateBar(i+1)


lang_list = ["Python", "C++", "Java"]
# --------------Tab Layout-------------------#
# tab1 = [
#     [sg.T("Type your Name:")],
#     [sg.CB("Python", key="CB1")],
#     [sg.CB("C++", key="CB2")],
# ]
# tab2 = [
#     [sg.T("Type your Address:")],
#     [sg.CB("Java", key="CB3")],
#     [sg.CB("JS", key="CB4")],
# ]
# layout = [[sg.TabGroup(
#     [
#         [sg.Tab("Tab1", tab1), sg.Tab("Tab2", tab2)]
#         ],[sg.VerticalSeparator()]
#     )
#     ]]


layout = [
    [sg.StatusBar("Welcome to my app")],
    [sg.T("Gender")],
    [sg.Radio("Male", group_id=1, key="gender")],
    [sg.Rad("Female", group_id=1, key="gender")],
    [sg.Rad("Non-Binary", group_id=1, key="gender",default=True)],
    [sg.T("Age")],
    [sg.Slider(range=(0, 100), key="age", orientation="h",default_value=25)],
    [sg.Spin(values=list(range(-101,101)),size=(10,8),initial_value=15,key="spinner"),],
    [sg.Ok(), sg.Cancel()],
]


root = sg.Window(
    "Tabs",
    layout,
)
event, value = root.read()
print(event, value)
