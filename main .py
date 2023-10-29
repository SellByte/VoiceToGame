#/*---------------------------------------------------------------------------------------------
 #*  Copyright (c) SellByte, lnc - All rights reserved.
 #*  Licensed under the CC BY-NC-ND 4.0 License. See License.txt in the project root for license information.
 #*--------------------------------------------------------------------------------------------*/



import speech_recognition as sr
import pyautogui
import threading

# Initialize the recognizer with PocketSphinx
recognizer = sr.Recognizer()
recognizer.recognize_sphinx

# Function to listen for voice commands
def listen_for_commands():
    with sr.Microphone(sample_rate=16000) as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for commands...")
        while True:
            try:
                audio = recognizer.listen(source, timeout=0.1)  # Listen for 0.1 seconds
                command = recognizer.recognize_sphinx(audio).lower()
                if command:
                    execute_command(command)
                    print(f"Command recognized: {command}")
            except sr.WaitTimeoutError:
                pass

# Function to execute commands
def execute_command(command):
    # Define your voice commands and their corresponding keypresses
    if "move left" in command:
        pyautogui.press("left")
    elif "move right" in command:
        pyautogui.press("right")
    elif "jump" in command:
        pyautogui.press("space")
    # Add more commands and actions as needed

if __name__ == "__main__":
    # Create separate threads for listening to voice commands and executing commands
    listen_thread = threading.Thread(target=listen_for_commands)
    listen_thread.daemon = True
    listen_thread.start()

    # Continue with your game logic or other tasks in the main thread
    while True:
        pass
