from time import sleep
from pywinauto import backend

desktop = backend.registry.backends['uia'].element_info_class()
def DetectZoomMeeting():
    for app in desktop.children():
        if app.name[-12:] == "Zoom Meeting":
            return app
    return -1

order = ["ContentLeftPanel", "Meeting Tools", ""]
def CheckStatus(app, depth):
    if depth == 3:
        return "muted" if app.children()[1].name.split(',')[0] == 'Unmute' else "unmuted"
    for i in app.children():
        if i.name == order[depth]:
            return CheckStatus(i, depth+1)

while True:
    app = DetectZoomMeeting()
    if app != -1:
        print(CheckStatus(app, 0))
    sleep(0.5)