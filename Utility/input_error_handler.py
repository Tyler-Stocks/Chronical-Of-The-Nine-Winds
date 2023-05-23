from Utility import errors as e

inputError = e.InputErrors()


class InputErrorHandler:

    def __init__(self):
        pass

    def input_error_handler(self, userInput, dataType, length):
        errorOccured = False

        if len(userInput.strip()) == 0:
            inputError.whitespace()
            errorOccured = True
        elif userInput.isnumeric():
            inputError.type(dataType)
            errorOccured = True
        elif len(userInput) >= 100:
            inputError.length(length)
            errorOccured = True
        else:
            errorOccured = False

        return errorOccured
