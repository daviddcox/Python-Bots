import PySimpleGUI as Sg

while True:
    Sg.Window(title="Hello World", layout=[[Sg.Text('hi')]], margins=(100, 100)).read()
