# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def multiply(a, b):
    print(a * b)

def factorial(a):
    if a == 1:
       return 1
    else:
       return a * factorial(a - 1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    multiply(1, 2)
    test = 99 > 100
    print(test)
    print(type('Hello'))
    if test == True:
        print('Minha Benga')
    print(factorial(4))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

price = 2.50

sandwich = "Ham and Cheese"

def calculate_price(product):
	if product == "Ham and Cheese":
		return 2.50
	elif product == "Tuna and Cucumber":
		return 2.25
	elif product == "Egg Mayo":
		return 2.25
	elif product == "Chicken Club":
		return 2.75
	else:
		return 2.50

print(calculate_price(sandwich))

def factors(x):
    if x == 1:
        print(1)
    elif num % x == 0:
        factors(x-1)
        print(x)
    else:
        return factors(x-1)
num = 12
factors(num)

def evalucion_dias_vacaciones(resposta_anna):
    if dias_restantes == 9 and resposta_anna == True:
       print('Correcto')
    else:
       print('Esta cagado')

dias_restantes = 9
input_anna = False
evalucion_dias_vacaciones(input_anna)
