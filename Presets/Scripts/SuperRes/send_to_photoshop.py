# This script copyrights belong to 3deep.org and the used solutions authors as mentioned.
# And it's available for academic and non-commercial use only.

from win32com.client import GetActiveObject, Dispatch

def send_to_ps(filename):
    try:
        app = GetActiveObject("Photoshop.Application")

    except Exception as e:
        print ("couldn't find an opened photoshop. Will try to open a new session.")

    app = Dispatch("Photoshop.Application")
    doc = app.Open(filename)