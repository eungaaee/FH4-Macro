import pyautogui
import keyboard
import time
import threading

def FindImage(file_name, confidence, interval=0):
    while True:
        if (interval > 0):
            time.sleep(interval)
        try:
            location = pyautogui.locateOnScreen(f"./Images/{file_name}", grayscale=True, confidence=confidence)
            return location
        except pyautogui.ImageNotFoundException:
            continue

def Macro(interrupt_event, loop=100, air_wait=78, landing_wait=14, rewind=7): # 10sp * 100 = 1000sp
    current_loop = 0
    while interrupt_event.is_set() == False:
        if (loop == 0): # set loop 0 to run infinitely
            current_loop += 1
            print(f"{current_loop} / INF")
        else:
            if (current_loop < loop):
                current_loop += 1
                print(f"{current_loop} / {loop}")
            else:
                print("Completed.")
                interrupt_event.set()
                break

        # stack the barrel roll points for air_wait seconds
        time.sleep(air_wait)

        # stop hovering
        pyautogui.press("backspace") # open Blueprint Builder
        time.sleep(1.5)
        pyautogui.press("esc") # exit Blueprint Builder
        time.sleep(0.25)
        pyautogui.press("enter") # confirm exit

        # discard alert
        time.sleep(1.5)
        pyautogui.press("enter")

        # landing and wait for the points to be added
        time.sleep(0.25)
        pyautogui.keyDown('s') # brake
        time.sleep(landing_wait)
        pyautogui.keyUp('s')

        # rewind to the barrel roll point
        for _ in range(rewind):
            pyautogui.press('r') # rewind
            FindImage("Esc.png", 0.75, interval=0.1) # wait for the rewind to be available
            time.sleep(0.1)
        pyautogui.press("enter") # resume

        # discard alert
        time.sleep(1.5)
        pyautogui.press("enter")

def Stopper(interrupt_event):
    while interrupt_event.is_set() == False:
        if keyboard.is_pressed("F2"):
            interrupt_event.set()
            print("Script will be stopped after the current loop.")
            break
        time.sleep(0.1)

def main():
    # wait for F1 key to start
    print("Press F1 to start the script.")
    keyboard.wait("F1")
    print("Script started.")

    interrupt_event = threading.Event()

    macro_thread = threading.Thread(target=Macro, args=(interrupt_event, ))
    stopper_thread = threading.Thread(target=Stopper, args=(interrupt_event, ))

    macro_thread.start()
    stopper_thread.start()

    macro_thread.join()
    stopper_thread.join()

    print("Exiting the script.")

if __name__ == "__main__":
    main()