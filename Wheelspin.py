import pyautogui
import keyboard
import time
import threading

def FindImage(file_name, confidence, interval=0, limit=0, scroll=0):
    for _ in iter(int, 1) if limit == 0 else range(limit):
        if (interval > 0):
            time.sleep(interval)
        try:
            location = pyautogui.locateOnScreen(f"./Images/{file_name}", grayscale=True, confidence=confidence) # using the confidence parameter will force to use _locateAll_opencv() instead of _locateAll_pillow()
            return location
        except pyautogui.ImageNotFoundException:
            if scroll > 0:
                pyautogui.press("down", presses=scroll, interval=0.05)
            elif scroll < 0:
                pyautogui.press("up", presses=-scroll, interval=0.05)
            continue
    
    return None

def UnlockPerk():
    pyautogui.press("enter") # unlock perk
    time.sleep(0.25)
    pyautogui.press("enter") # confirm unlock
    found = FindImage("NoSkillPoint.png", 0.9, interval=0.5, limit=1)
    return True if found == None else False

# buy in Car Collection
def Macro(interrupt_event, loop=39): # 999sp / 25sp per car = 39.96 cars
    is_first = True
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
                break

        # open View All menu
        time.sleep(0.1)
        if is_first:
            pyautogui.press("left", presses=3, interval=0.05)
            pyautogui.press("up", presses=3, interval=0.05)
            pyautogui.press("right")
        pyautogui.press("enter")

        # wait for the Buy Car menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        # open search window
        time.sleep(0.1)
        pyautogui.moveTo(1, 1) # move the cursor to the top left corner to prevent interference
        pyautogui.press("backspace")
        time.sleep(0.25)
        """ # select "Toyota"
        location = FindImage("Toyota.png", 0.9, interval=0.1, scroll=-1)
        pyautogui.moveTo(location)
        pyautogui.mouseDown()
        pyautogui.mouseUp() """
        pyautogui.press("up", presses=2, interval=0.05)
        pyautogui.press("right", presses=2, interval=0.05)
        pyautogui.press("enter")

        time.sleep(0.25)
        pyautogui.press("down", presses=2, interval=0.05)
        pyautogui.press("enter") # select Toyota Supra RZ
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        time.sleep(0.1)
        pyautogui.press('y') # enter the color menu
        time.sleep(0.5)
        pyautogui.press("enter") # select default color
        time.sleep(0.25)
        pyautogui.press("enter") # confirm color
        time.sleep(0.25)
        pyautogui.press("enter") # confirm purchase

        # wait for the Forza Vista to load
        time.sleep(5)
        FindImage("Esc.png", 0.9, interval=0.1)

        # exit Forza Vista
        time.sleep(0.25) # forza vista is very slow and laggy compared to the other menus, so it needs more delay
        pyautogui.press("esc") # back to the Garage menu

        # wait for the Autoshow menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        # move to the Garage tab
        time.sleep(0.1)
        pyautogui.press("pagedown")

        # enter the Upgrade & Tuning menu
        time.sleep(0.1)
        pyautogui.press("right")
        pyautogui.press("enter")

        # wait for the Upgrade & Tuning menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        # enter Car Mastery menu
        time.sleep(0.1)
        pyautogui.press("down")
        pyautogui.press("enter")

        # unlock perks
        time.sleep(0.5)
        is_unlocked = UnlockPerk() # unlock first perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        time.sleep(3)
        pyautogui.press("right")
        is_unlocked = UnlockPerk() # unlock second perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        time.sleep(3)
        pyautogui.press("left")
        pyautogui.press("up")
        is_unlocked = UnlockPerk() # unlock third perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        time.sleep(3)
        pyautogui.press("up")
        is_unlocked = UnlockPerk() # unlock fourth perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        time.sleep(3)
        pyautogui.press("right")
        is_unlocked = UnlockPerk() # unlock last perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        time.sleep(3)
        pyautogui.press("left")
        pyautogui.press("up")
        is_unlocked = UnlockPerk() # unlock last perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        # back to Upgrades & Tuning menu
        time.sleep(3)
        pyautogui.press("esc")

        # wait for the Upgrade & Tuning menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        # back to Garage menu
        time.sleep(0.1)
        pyautogui.press("esc")

        # wait for the Garage menu to load
        time.sleep(0.25)
        FindImage("Esc.png", 0.9, interval=0.1)

        # move to the Autoshow tab
        time.sleep(0.1)
        pyautogui.press("pageup")

        if is_first == True:
            is_first = False

    interrupt_event.set()

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