class InputValues:

    def __init__(self):
        pass

    def yes_values(self, userInput):
        yesInputValues = ['y', 'yes', 'yea', 'yessir']

        if userInput.lower() in(yesInputValues):
            return True
        else:
            return False

    def no_values(self, userInput):
        noInputValues = ['n', 'no', 'na', 'nosir']

        if userInput.lower() in(noInputValues):
            return True
        else:
            return False

    def boy_values(self, userInput):
        boyInputValues = ['b', 'boy', 'guy', 'man', 'male']

        if userInput.lower() in(boyInputValues):
            return True
        else:
            return False

    def girl_values(self, userInput):
        girlInputValues = ['g', 'girl', 'gal', 'woman', 'female']

        if userInput.lower() in (girlInputValues):
            return True
        else:
            return False
