class Bankaccount:
    def __init__(self):
        self.__balance = 10 #private

    def __get_ammount(self):
        return self.__balance


obj = Bankaccount()
print(obj.__get_ammount())  # AttributeError: 'Bankaccount' object has no attribute '__get_ammount'

#write difference between public,protected and private with example