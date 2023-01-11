"""Edits the class of the player character"""
from is_class import is_class
def change_class_status(class_name, new_value):
    """Changes the class of the character"""
    # Call the isClass function to get the current list of classes
    classes = is_class()

    # Iterate through the list of classes
    for cls in classes:
        # If the name of the class matches the one passed in as an argument
        if cls['name'] == class_name:
        # Update the value of 'isClass' to the new value passed in as an argument
            cls['isClass'] = new_value
        # Exit the loop
        break
