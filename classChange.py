from isClass import isClass
def changeClassStatus(className, newValue):
    isClass()  # Call the isClass function to get the current list of classes
  
    # Iterate through the list of classes
    for cls in isClass:
        # If the name of the class matches the one passed in as an argument
        if cls['name'] == className:
        # Update the value of 'isClass' to the new value passed in as an argument
            cls['isClass'] = newValue
        # Exit the loop
        break  
