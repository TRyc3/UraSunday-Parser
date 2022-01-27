import PySimpleGUI as sg
import urllib.request
import string
import os.path

layout = [
        [sg.Text("Paste Text"), 
        sg.InputText(key = "Text")],

        [sg.Text("Folder"),
        sg.InputText(key = "Folder"),
        sg.FolderBrowse()],

        [sg.Button("Parse"),
         sg.Button("Done")]
    ]
    
window = sg.Window("Parser", layout)
while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == "Done":
        break

    if event == "Parse":
        try:
            request_url = urllib.request.urlopen(values["Text"])
            SrcCode = request_url.read()
            SrcCode = SrcCode.decode('utf8')
            Target = "https://urasunday.com/secure/"
            lines = SrcCode.split()
            urlList = []

            for x in lines:
                if Target in x:
                    bound = "'"
                    if x.find(bound) != x.rfind(bound):
                        urlList.append(x[x.find(bound) + 1: x.rfind(bound)])

            count = 1
            for x in urlList:
                folder = values["Folder"]
                try:
                    SaveAs = os.path.join(folder, str(count) + ".webp")
                    urllib.request.urlretrieve(x, SaveAs)
                    count += 1
                except Exception as e :
                    sg.popup(str(e))
                    pass

            sg.popup("Done")

        except Exception as e :
            sg.popup(str(e))

window.close()