from win32com.client import Dispatch

msg = "独断万古荒天帝, 唯负罪州火桑女"
speaker = Dispatch('SAPI.SpVoice')  # set up SAPI
speaker.Speak(msg)  # speak the message
del speaker  # delete the speaker object
