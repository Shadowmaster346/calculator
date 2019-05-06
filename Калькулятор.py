what = input( "Что делаем? (+,/,-,*):" )


a = float( input("Введи первое число: ") )
b = float( input("Введи второе число: ") )

if what == "+":
	c = a + b
	print("Результат: " + str(c))
elif what == "-":
    c = a - b
    print("Результат: " + str(c))
elif what == "*":
    c = a * b
    print("Результат: " + str(c))
elif what == "/":
    c = a / b
    print("Результат: " + str(c))
elif what == "admin":
    print("Результат: 666")

print("Что-бы выйти нажме Enter")
input()
    
 