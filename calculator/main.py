import PySimpleGUI as sg

col_1 = [
    [sg.B("7", size=(4, 2)), sg.B("8", size=(4, 2)), sg.B("9", size=(4, 2))],
    [sg.B("4", size=(4, 2)), sg.B("5", size=(4, 2)), sg.B("6", size=(4, 2))],
    [sg.B("1", size=(4, 2)), sg.B("2", size=(4, 2)), sg.B("3", size=(4, 2))],
    [
        sg.B("+/-", size=(4, 2), key="SIGNCHG"),
        sg.B("0", size=(4, 2)),
        sg.B(".", size=(4, 2), key="."),
    ],
]
col_2 = [
    [sg.B("+", size=(4, 2), key="+")],
    [sg.B("-", size=(4, 2), key="-")],
    [sg.B("%", size=(4, 2), key="%")],
    [sg.B("=", size=(4, 2), key="equal",button_color="red")],
]
col_3 = [
    [sg.B("*", size=(4, 2), key="*")],
    [sg.B("/", size=(4, 2), key="/")],
    [sg.B("C", size=(4, 2), key="clear")],
    [sg.B("CE", size=(4, 2), key="cevery")],
]
layout = [
    [sg.I(size=(14, 1), font=("Arial", 30, "bold"), key="INPUT")],
    [sg.Col(col_1), sg.VerticalSeparator(), sg.Col(col_2), sg.Col(col_3)],
]
root = sg.Window("Calculator", layout)
num = [str(i) for i in range(10)]
num.extend(["."])
history = str()
operator = ["+", "-", "*", "/"]
while True:
    event, values = root.read()
    if event in ["Cancel", sg.WINDOW_CLOSED]:
        root.close()
        break
    elif event in num and len(history) < 12:
        history += str(event)
    elif event in operator:
        op = event
        num1 = history
        history = ""
    elif event == "equal":
        try:
            num2 = history
            expression = str(num1) + op + str(num2)
            result = eval(expression)
        except ZeroDivisionError:
            sg.popup_timed("Number can be divided by zero", auto_close_duration=1)
        except SyntaxError:
            sg.popup_timed("Use signs properly", auto_close_duration=1)
        except NameError:
            pass
        else:
            history = str(result)
    elif event == "clear" and len(history):
        history = history[:-1]
    elif event == "cevery":
        history, op = ("", "")
        num1, num2 = 0, 0
    elif event == "SIGNCHG":
        history = int(history) * -1
    root["INPUT"].update(str(history))
