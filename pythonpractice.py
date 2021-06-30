# list comprehension
number_list = [1, 2, 3, 5, 6, 7, 8, 9, 10]
oddNumber_list = [odd for odd in number_list if odd % 2 == 1]
print(oddNumber_list)
number_list = [1, 2, 3, 5, 6, 7, 8, 9, 10]
oddNumber_list = [odd if odd % 2 == 1 else None for odd in number_list]
print(oddNumber_list)


# generator as use to get Iterator object 'stream of data'
def generate_to_any_number(x=10):
    i = 0
    while i < x:
        yield i
        i += 1


print("generate to any number: ", generate_to_any_number())
for g in generate_to_any_number():
    print("generator object: ", g)

# handling error
try:
    tenth = int(input("enter num"))
except ValueError:
    print("enter an integer")

# reading from a file

txt_file = None
try:
    txt_file = open('C:/New folder/txtfile.txt', 'r')
    numbers_in_txtfile = txt_file.read()
    print("numbers in txtfile: ", numbers_in_txtfile)
except:
    print("unable to open file")
finally:
    txt_file.close()

# using python with as to autoclose object
with open('C:/New folder/txtfile.txt', 'r') as txt_file2:
    numbers_in_txtfile2 = txt_file2.read()

print("numbers_in_txtfile2: ", numbers_in_txtfile2)

