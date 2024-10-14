 #Question1
>>>print("Hello, world!")
Hello, world!
>>> print("Hello", "world!")
Hello world!
>>> print(3)
3
>>> print(3.0)
3.0
>>> print(2 + 3)
5
>>> print(2.0 + 3.0)
5.0
>>> print("2" + "3")
23
>>> print("2 + 3 =", 2 + 3)
2 + 3 = 5
>>> print(2 * 3)
6
>>> print(2 ** 3)
8
>>> print(2 / 3)
0.6666666666666666

#Question2
def main():
	print("This program illustrates a chaotic function")
	x = eval(input("Enter a number between 0 and 1: "))
	for i in range(10):
		x = 3.9 * x * (1 - x)
		print(x)
main()

#Question3
def main():
	print("This program illustrates a chaotic function")
	x = eval(input("Enter a number between 0 and 1: "))
	for i in range(10):
		x = 2.0 * x * (1 - x)
		print(x)
main()

#Question4
def main():
	print("This program illustrates a chaotic function")
	x = eval(input("Enter a number between 0 and 1: "))
	for i in range(20):
		x = 2.0 * x * (1 - x)
		print(x)
main()

#Question5
def main():
	print("This program illustrates a chaotic function")
	x = eval(input("Enter a number between 0 and 1: "))
	n = eval(input("How many numbers should I print? "))
	for i in range(n):
		x = 2.0 * x * (1 - x)
		print(x)
main()

#Question6a
def main():
	print("This program illustrates a chaotic function")
	x = eval(input("Enter a number between 0 and 1: "))
	n = eval(input("How many numbers should I print? "))
	for i in range(n):
		x = 3.9 * x * (1 - x)
		print(x)
main()

#Question6b
def main():
	print("This program illustrates a chaotic function")
	x = eval(input("Enter a number between 0 and 1: "))
	n = eval(input("How many numbers should I print? "))
	for i in range(n):
		x = 3.9 * (x - x * x)
		print(x)
main()

#Question6c
def main():
	print("This program illustrates a chaotic function")
	x = eval(input("Enter a number between 0 and 1: "))
	n = eval(input("How many numbers should I print? "))
	for i in range(n):
		x = 3.9 * x - 3.9 * x * x
		print(x)
main()

#Question7
def main():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    n = int(input("How many numbers should I print? "))
    
    k = 2.0
    print(f"{'Iteration':<10}{'Value':<10}") 
    for i in range(n):
        x = k * x * (1 - x)  
        print(f"{i + 1:<10}{x:<10.6f}")  

main()
