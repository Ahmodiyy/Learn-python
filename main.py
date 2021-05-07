# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # Operator in python


def operators():
    print("----------  arithmetic----------")
    num1 = 5
    num2 = 3
    print("num1 + num2 ", num1 + num2)
    print("num1 - num2 ", num1 - num2)
    print("num1 * num2 ", num1 * num2)
    print("num1 / num2 ", num1 / num2)
    print("num1 ** num2 ", num1 ** num2)
    print("num1 % num2 ", num1 % num2)
    print("num1 // num2 ", num1 // num2)

    print("----------  assignment----------")
    num1 = 5
    num2 = 3
    num1 -= num2
    print("num1 -= num2 ", num1)

    print("----------  comparison----------")
    num1 = 5
    num2 = 3
    print("num1 > num2 ", num1 > num2)
    print("num1 < num2 ", num1 < num2)
    print("num1 == num2 ", num1 == num2)
    print("num1 != num2 ", num1 != num2)

    print("----------  logical----------")
    num1 = True
    num2 = False
    print("num1 and num2 ", num1 and num2)
    print("num1 or num2 ", num1 or num2)
    print("num1 not num2 ", not num2)

    print("--------- bitwise----------")
    num1 = 2  # 10
    num2 = 1  # 01
    print("num1 & num2 ", num1 & num2)
    print("num1 | num2 ", num1 | num2)
    print("num1 ^ num2 ", num1 ^ num2)
    print("num1 >> num2 ", num1 >> num2)
    print("num1 << num2 ", num1 << num2)

    print("---------identity----------")
    num1 = 2  # 10
    num2 = 1  # 01
    print("num1 is num2 ", num1 is num2)
    print("num1 is not num2 ", num1 is not num2)

    print("---------membership----------")  # membership operator are use in list
    num1 = [2, "py"]  # 10
    num2 = 2
    str1 = "py"
    print("num2 in num1 ", num2 in num1)
    print("str1 | num1 ", str1 not in num1)

def stringDataType():
    print("-------------numeric data types------")
    floats = 2.2
    ints = 5
    print("float", floats)
    print("int", ints)
    print("int", ints*2)


    print("-------------string data types------")
    string1 = "python"
    string2 = "tutorial"
    print("string concatenation", string1+string2)
    print("string repetition", string1*2)
    print("string slicing", string1[2:4])
    print("string slicing", string1[2:-3])
    print("string count method", string2.count('t'))
    print("string find method", string2.find('o'))


    print("-------------tuple data types------")
    my_tuple = ("john", "sam", 2)
    print(my_tuple)
    print("tuple concatenation", my_tuple+("han",))
    print("tuple repetition", my_tuple * 2)
    print("tuple slicing", my_tuple[2:4])
    print("tuple index", my_tuple[0])

    print("-------------list data types------")
    my_list = ["john", "sam", 2]
    print("list concatenation", my_list + ["han",])
    print("list repetition", my_list * 2)
    print("list slicing", my_list[2:4])
    print("list index", my_list[0])
    print("list append method ", my_list.append(5.5))
    print(my_list)
    print("list extend method", my_list.extend(["santur"]))
    print(my_list)
    print("list insert method", my_list.insert(0, 1))
    print(my_list)
    print("list pop method", my_list.pop())
    print(my_list)

    print("-------------dictionary data types------")
    my_dict = {1: "first", 2: "second", "third": 3}
    print("dict key method ", my_dict.keys())
    print("dict values method", my_dict.values())
    print("dict items method", my_dict.items())
    print("dict get method", my_dict.get("third"))
    print("dict update method", my_dict.update({4: "four"}))
    print(my_dict)

    print("-------------set data types------")
    my_set1 = {1, 2, "n"}
    my_set2 = {1, 2, "m"}
    print("set union ", my_set1 | my_set2)
    print("set intersection", my_set1 & my_set2)
    print("set difference", my_set1 - my_set2)


def controlFlow():
    print("------if control flow---------")
    mark = 75
    if mark > 80:
        print("grade a")
    elif (mark > 60) and (mark <= 80):
        print("grade b")
    elif (mark > 40) and (mark <= 60):
        print("grade c")
    else:
        print("grade d")


    print("-----for loop--------")
    for iterator in range(99, 0, -1):
        if iterator == 90:
            continue
        print(iterator)
        if iterator == 80:
            break

    print("------while loop-------")
    num = int(input("input the value of n="))
    if num <= 0:
        print("Enter valid number")
    else:
        summation = 0
        while num > 0:
            summation += num
            num -= 1
            print(summation)

def fibonnaci(j):
    a = 0
    b = 1
    for num in range(j):
        c = b + a
        print(c)
        a = b
        b = c
    return c

def fileHandling():
    welcomefile = open("D:\\pythonreadwrite.txt", "w+")
    welcomefile.write("Welcome to python")
    welcomefile.seek(0)
    print(welcomefile.read())
    welcomefile.close()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #operators()
    #stringDataType()
    #controlFlow()
    #print("end value of fibonnaci ", fibonnaci(int(input("enter fibonnacci"))))
    fileHandling()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
