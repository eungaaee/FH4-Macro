import pyautogui
import keyboard
import asyncio

async def FindImage(file_name, confidence, interval=0, limit=0, scroll=0):
    for _ in iter(int, 1) if limit == 0 else range(limit):
        if (interval > 0):
            await asyncio.sleep(interval)

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

async def UnlockPerk():
    pyautogui.press("enter") # unlock perk
    await asyncio.sleep(0.25)
    pyautogui.press("enter") # confirm unlock
    found = await FindImage("NoSkillPoint.png", 0.9, interval=0.5, limit=1)
    return True if found == None else False

# buy in Car Collection
async def Macro(interrupt_event, loop=39): # 999sp / 25sp per car = 39.96 cars
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
        await asyncio.sleep(0.1)
        if is_first:
            pyautogui.press("left", presses=3, interval=0.05)
            pyautogui.press("up", presses=3, interval=0.05)
            pyautogui.press("right")
        pyautogui.press("enter")

        # wait for the Buy Car menu to load
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)

        # open search window
        await asyncio.sleep(0.1)
        pyautogui.moveTo(1, 1) # move the cursor to the top left corner to prevent interference
        pyautogui.press("backspace")
        await asyncio.sleep(0.25)
        """ # select "Toyota"
        location = await FindImage("Toyota.png", 0.9, interval=0.1, scroll=-1)
        pyautogui.moveTo(location)
        pyautogui.mouseDown()
        pyautogui.mouseUp() """
        pyautogui.press("up", presses=2, interval=0.05)
        pyautogui.press("right", presses=2, interval=0.05)
        pyautogui.press("enter")

        await asyncio.sleep(0.25)
        pyautogui.press("down", presses=2, interval=0.05)
        pyautogui.press("enter") # select Toyota Supra RZ
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)

        await asyncio.sleep(0.1)
        pyautogui.press('y') # enter the color menu
        await asyncio.sleep(0.5)
        pyautogui.press("enter") # select default color
        await asyncio.sleep(0.25)
        pyautogui.press("enter") # confirm color
        await asyncio.sleep(0.25)
        pyautogui.press("enter") # confirm purchase

        # wait for the Forza Vista to load
        await asyncio.sleep(5)
        await FindImage("Esc.png", 0.9, interval=0.1)

        # exit Forza Vista
        await asyncio.sleep(0.25)
        pyautogui.press("esc") # back to the Garage menu

        # wait for the Autoshow menu to load
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)

        # move to the Garage tab
        await asyncio.sleep(0.1)
        pyautogui.press("pagedown")

        # enter the Upgrade & Tuning menu
        await asyncio.sleep(0.1)
        pyautogui.press("right")
        pyautogui.press("enter")

        # wait for the Upgrade & Tuning menu to load
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)

        # enter Car Mastery menu
        await asyncio.sleep(0.1)
        pyautogui.press("down")
        pyautogui.press("enter")

        # unlock perks
        await asyncio.sleep(0.5)
        is_unlocked = await UnlockPerk() # unlock first perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        await asyncio.sleep(3)
        pyautogui.press("right")
        is_unlocked = await UnlockPerk() # unlock second perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        await asyncio.sleep(3)
        pyautogui.press("left")
        pyautogui.press("up")
        is_unlocked = await UnlockPerk() # unlock third perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        await asyncio.sleep(3)
        pyautogui.press("up")
        is_unlocked = await UnlockPerk() # unlock fourth perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        await asyncio.sleep(3)
        pyautogui.press("right")
        is_unlocked = await UnlockPerk() # unlock last perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        await asyncio.sleep(3)
        pyautogui.press("left")
        pyautogui.press("up")
        is_unlocked = await UnlockPerk() # unlock last perk
        if is_unlocked == False:
            print("No skill point left.")
            break

        # back to Upgrades & Tuning menu
        await asyncio.sleep(3)
        pyautogui.press("esc")

        # wait for the Upgrade & Tuning menu to load
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)

        # back to Garage menu
        await asyncio.sleep(0.1)
        pyautogui.press("esc")

        # wait for the Garage menu to load
        await asyncio.sleep(0.25)
        await FindImage("Esc.png", 0.9, interval=0.1)

        # move to the Autoshow tab
        await asyncio.sleep(0.1)
        pyautogui.press("pageup")

        if is_first == True:
            is_first = False

    interrupt_event.set()

async def Stopper(interrupt_event):
    await asyncio.get_event_loop().run_in_executor(None, keyboard.wait, "F2") # run the blocking function in a separate thread
    interrupt_event.set()
    print("Script will be stopped after the current loop.")

async def main():
    # wait for F1 key to start
    print("Press F1 to start the script.")
    await asyncio.get_event_loop().run_in_executor(None, keyboard.wait, "F1") # run the blocking function in a separate thread
    print("Script started.")

    interrupt_event = asyncio.Event()
    await asyncio.gather(Macro(interrupt_event), Stopper(interrupt_event))

    print("Exiting the script.")

if __name__ == "__main__":
    asyncio.run(main())