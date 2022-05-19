class InvalidLength(Exception):
    """
    This "subclass" is under superclass "Exception" and represents an error when the ID number is not exactly 9 digits
    """
    def __init__(self, number):
        """
        This method is a initialization method of the "InvalidLength" class, it is numbered and it is saved as "self._number"
        :param number: number ID
        :type number: int
        :return: None
        :rtupe: None
        """
        self._number = number

    def __str__(self):
        """
        This method overrides the "__str__" method of the InvalidLength class and returns a unique error message for a number that is not 9 digits
        :return: Custom error message
        :rtype: str
        """
        return "This ID number: {} is invalid, The number must contain exactly 9 digits!".format(self._number)


def check_id_valid(id_number):
    """
    This function is a boolean function that receives an ID number and returns "true" if it is valid and "false" if it is invalid.
    Legal - If any number in odd position multiples by 1, and doubles by 2 then connects numbers that have 2 digits, and connects them all - if it divides by 10 without the remainder it is legal.
    :param id_number: The number of IDs that want to check if it is "true" or "false"
    :type id_number: int
    :raise: ValueError: raises an Exception thrown if the number is not an integer or if it is a negative number (for example, -123456789)
    :raise: InvalidLength: raises an Exception thrown if the number length is not exactly 9, zeros are not counted
    :return: "True" if the number is valid, "False" if it is invalid.
    :rtype: bool
    """
    from functools import reduce
    if not str(id_number).isdecimal(): #Excluding negative number (for example, -12345678)
        raise ValueError
    if len(str(int(id_number))) != 9: #If the number is not exactly 9 digits, zeros are not counted
        raise InvalidLength(id_number)
    list_num = [int(num) for num in str(id_number)]  #Divide the number into a list of numbers
    multiplication = [list_num[num] * 1 if num % 2 == 0 else list_num[num] * 2 for num in range(len(list_num))] #Any number from the list, if it is in an odd place (position 1 in the code = 0 which is even) multiples by 1, and any number in the place of an odd (position 2 in the code = 1 which is not even) multiplies by 2
    check_id = reduce(lambda x, y: x + y, [int(str(num)[0]) + int(str(num)[1]) if len(str(num)) == 2 else num for num in multiplication]) #Create a list where: If the number that came out in the "multiplication" list has 2 numbers - they connect in a connection (+) and return the value, otherwise the number itself will simply be returned. This list is put in the "reduce" function with the Lambda x + y function that connects the sum of all the organs in the list
    return check_id % 10 == 0  #If the total number is divided by 10 without the valid ID remaining and returned "True", otherwise "False" will be returned


class IDIterator:
    """
    This "superclass" is used as a custom iterator. Initialized with an ID number and returns anyone who follows it if valid (check_id_valid = True),
    until the number 999999999 returns a StopIteration exception
    """
    def __init__(self, id):
        """
        This method is an initialization method in the "IDIterator" class.
        It initializes instances with the "self._id" attribute which is the ID number entered
        :param id: number ID
        :type number: int
        :return: None
        :rtupe: None
        """
        self._id = id
    def __iter__(self):
        """
        This method produces a custom iterator for the instance. It is each time pointing to the next value as (using the "__next__" method)
        :return: self
        :rtype: Iterator
        """
        return self
    def __next__(self):
        """
        This is a custom __next__ method that each time moves the iterator to the next value as defined for it - any valid ID number (check_id_valid = True),
        in case the number is 999999999 or higher - an StopIteration exception is returned
        :raise: StopIteration: raises an Exception if self._id >= 999999999
        :return: self._id -1 ,if the ID is valid
        :rtype: int 
        """
        while True:
            if self._id >= 999999999:
                raise StopIteration
            if not check_id_valid(self._id): #If the number is invalid
                self._id += 1       #Proceed to the next number
            else:                   #If the number is valid
                self._id += 1       #Proceed to the next number, and return the previous number
                return self._id -1  #So if the first number itself is valid - it will also return it (including)


def id_generator(id_num):
    """
    This is a generator function that puts in an argument that is the ID number and returns each call to the next valid ID number (if check_id_valid = True)
    just as the "IDIterator" iterator does. When the number reaches 999999999, an StopIteration error is thrown
    :param id_num: number ID
    :type id_num: int
    :yield: Next id_num if valid
    :ytype: int
    """
    while id_num < 999999999:
        if check_id_valid(id_num):
            yield id_num
        id_num += 1


def main():
    while True:
        number_id = input("Enter your number ID:")
        try:
            number_id = int(number_id)
            try:
                my_iter = IDIterator(number_id)  #Iterator
                print("Print the iterator values:\n")
                for item in range(10):  #Print the following 10 valid numbers
                    print(next(my_iter))
            except StopIteration:       #If the iterator reaches 999999999, you will receive an error message:
                print("The iteration is over.\n")
            try:
                my_gen =  id_generator(number_id) #generator
                print("Print the generator values:\n")
                for item in range(10):  #Print the following 10 valid numbers
                    print(next(my_gen))  #If the iterator reaches 999999999, you will receive an error message:
            except StopIteration:       #If the iterator reaches 999999999, you will receive an error message:
                print("The iteration is over.\n")
        except ValueError:
            print("The number must only be a positive integer\n")
        except InvalidLength as e:
            print(e)

if __name__ == "__main__":
    main()
main()