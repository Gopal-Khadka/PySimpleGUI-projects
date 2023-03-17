import PySimpleGUI as sg

conversion = ["Km to m", "m to Km", "sec to min", "min to sec", "min to hour","hour to min"]
layout = [
    [sg.I(key="-INPUT-"), sg.Sp(conversion,key="-UNITS-"), sg.B("Convert",key="-CONVERT-")],
    [sg.T("Output:",key="-OUTPUT-")],
]
root = sg.Window("Converter", layout)
while True:
    event, values = root.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event=="-CONVERT-":
        input_value=values["-INPUT-"]
        if not input_value.isnumeric():
            sg.popup_auto_close("Please Enter Number Only.",title="ValueError")
            root["-INPUT-"].update("")
        match values["-UNITS-"]:
            case "Km to m":
                output=round(float(input_value)*1000,2)
                output_string=f"{input_value} km equals to {output} meters."
            case "m to Km":
                output=round(float(input_value)/1000,2)
                output_string=f"{input_value} meters equals to {output} km."
            case "sec to min":
                output=round(float(input_value)/60,2)
                output_string=f"{input_value} seconds equals to {output} minutes."
            case "min to sec":
                output=round(float(input_value)*60,2)
                output_string=f"{input_value} min equals to {output} seconds."
            case "min to hour":
                output=round(float(input_value)/60,2)
                output_string=f"{input_value} minutes equals to {output} hours."
            case "hour to min":
                output=round(float(input_value)*60,2)
                output_string=f"{input_value} hours equals to {output} minutes."

        root["-OUTPUT-"].update(f"Output:{output_string}")
root.close()
