import pyautogui
import keyboard
import asyncio

async def FindImage(file_name, confidence, interval=0):
    while True:
        if (interval > 0):
            await asyncio.sleep(interval)
        try:
            location = pyautogui.locateOnScreen(f"./Images/{file_name}", grayscale=True, confidence=confidence)
            return location
        except pyautogui.ImageNotFoundException:
            continue

async def Macro(interrupt_event, loop=100, air_wait=60, landing_wait=12, rewind=6): # 10sp * 100 = 1000sp, adjust the values properly
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
        await asyncio.sleep(air_wait)

        # stop hovering
        pyautogui.press("backspace") # open Blueprint Builder
        await asyncio.sleep(1.5)
        pyautogui.press("esc") # exit Blueprint Builder
        await asyncio.sleep(0.25)
        pyautogui.press("enter") # confirm exit

        """ # discard alert
        await asyncio.sleep(1.5)
        pyautogui.press("enter") """

        # landing and wait for the points to be added
        await asyncio.sleep(0.25)
        pyautogui.keyDown('s') # brake
        await asyncio.sleep(landing_wait)
        pyautogui.keyUp('s')

        # rewind to the barrel roll point
        for _ in range(rewind):
            pyautogui.press('r') # rewind
            await FindImage("Esc.png", 0.75, interval=0.1) # wait for the rewind to be available
            await asyncio.sleep(0.1)
        pyautogui.press("enter") # resume

        """ # discard alert
        await asyncio.sleep(1.5)
        pyautogui.press("enter") """

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