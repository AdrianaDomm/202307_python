""" variable declaration, initialize """
num1 = 42 #int
num2 = 2.3 #float
boolean = True #boolean
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dic
fruit = ('blueberry', 'strawberry', 'banana') #tuple


print(type(fruit)) #type check
print(pizza_toppings[1]) #access value
pizza_toppings.append('Mushrooms') #add vale
print(person['name']) #access value
person['name'] = 'George' #change value
person['eye_color'] = 'blue' #add vale
print(fruit[2]) #access value

"""conditional if-else"""
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

"""conditional if-elif-else"""
if len(string) < 5: #length check
    print("It's a short word!")
elif len(string) > 15: #length check
    print("It's a long word!")
else:
    print("Just right!")

"""foor loop"""
for x in range(5): #strat:0 stop:4 increment:1
    print(x)
for x in range(2,5): #strat:2 stop:4 increment:1
    print(x)
for x in range(2,10,3): #strat:2 stop:9 increment:3
    print(x)

    """while loop"""
    #strat:0 stop:4 increment:1
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() #delete value
pizza_toppings.pop(1) #delete value
print(person)
person.pop('eye_color') #delete value
print(person)

"""for loop"""
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue #continue
    print('After 1st if statement')
    if topping == 'Olives':
        break #break

    """function"""
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): #parameter
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #argument

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4) #argument


"""
Bonus section
"""

# print(num3) #NameError: name'num3' is not defined
# num3 = 72 
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)