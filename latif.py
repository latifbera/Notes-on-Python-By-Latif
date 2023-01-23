print("Hello PYTHON!") 
if 5>2:
 print("Five is greater than two!")

x = 5
y = 9
print(x)
print(y)
print(x+y)
print(y-x)
print(x*y)
print(y/x)
print(y%x)
print(y**x)
print(y//x)
print(x>y)
print(x<y)
print(x==y)
print(x!=y)
print(x>=y)
print(x<=y)
print(x-y)

x = 5
y = "John"
z = 3.978
print(type(x))
print(type(y))
print(type(z))
# NOTLAR 04.12.2022

# OPERATORS

# ** Operatörü: Üs alma işlemi yapar.
# != Operatörü: Eşit değilse anlamına gelir.
# % Operatörü: Mod alma işlemi yapar.
# // Operatörü: Tam bölme işlemi yapar.
# >= Operatörü: Büyük eşitse anlamına gelir.
# <= Operatörü: Küçük eşitse anlamına gelir.
# > Operatörü: Büyükse anlamına gelir.
# < Operatörü: Küçükse anlamına gelir.
# + Operatörü: Toplama işlemi yapar.
# - Operatörü: Çıkarma işlemi yapar.
# * Operatörü: Çarpma işlemi yapar.
# / Operatörü: Bölme işlemi yapar.
# == Operatörü: Eşitse anlamına gelir.
# = Operatörü: Atama işlemi yapar.

# GENERAL INFORMATIONS

# print() Fonksiyonu: Ekrana yazdırma işlemi yapar.
# if Koşul: Koşul sağlanırsa yapılacak işlemi belirtir.
# Python'da yorum satırı # ile başlar.
# Python'un uzantısı .py'dir.
# Python'da değişken tanımlamak için = operatörü kullanılır. Bir değişkene yeni bir değer verildiğinde artık o değişkenin yeni değeri geçerlidir. 
# Pyhton'da """ ile başlayıp """ ile biten yorumlar birden fazla yorum satırıdır.

# TYPES

# str demek string demektir. String ifadeleri yazdırmak için print() fonksiyonu kullanılır. 
# str() Fonksiyonu: Değişkeni stringe çevirir.
#int demek integer demektir. Integer ifadeleri yazdırmak için print() fonksiyonu kullanılır.
#int() Fonksiyonu: Değişkeni integera çevirir.
#float demek küsüratlı sayı demektir. Float ifadeleri yazdırmak için print() fonksiyonu kullanılır.
#type() Fonksiyonu: Değişkenin türünü gösterir.Bunun için type() fonksiyonu kullanılır.Bunun output'u string, integer, float olabilir. "print(type(x))" şeklinde yazıldığında x değişkeninin türü ekrana yazdırılır. Output: <class 'int'>, <class 'str'>, <class 'float'> şeklinde olur.
# String ifadeleri  bir ya da iki tırnak ile gösterilebilir. "Hello World!", 'Hello World!' şeklinde gösterilebilir.
# String ifadeleri birleştirilebilir. "Hello" + "World!" şeklinde gösterilebilir. Output: "HelloWorld!" şeklinde olur.
# String ifadeleri birleştirilebilir. "Hello" + " " + "World!" şeklinde gösterilebilir. Output: "Hello World!" şeklinde olur.

# VARIABLE NAMES

# Değişken isimleri büyük-küçük harfe duyarlıdır. "a" ile "A" farklı değişkenlerdir.
# Değişken isimleri rakam ile başlayamaz. 
# Değişken isimleri boşluk içeremez.
# Bir değişkenin kısa bir adı (x ve y gibi) veya daha açıklayıcı bir adı (yaş, soyadı, toplam_hacim) olabilir. ***Python değişkenleri için bazı kurallar***:
# Değişken adı bir harf veya alt çizgi karakteri ile başlamalıdır.
# Bir değişken adı bir sayı ile başlayamaz
# Bir değişken adı yalnızca alfasayısal karakterler ve alt çizgiler (A-z, 0-9 ve _ ) içerebilir
# Değişken adları büyük/küçük harfe duyarlıdır (yaş, Yaş ve YAŞ üç farklı değişkendir)
# Python, bir satırda birden çok değişkene değer atamanıza izin verir. "x, y, z = "Orange", "Banana", "Cherry" şeklinde yazılabilir. Output: "Orange", "Banana", "Cherry" şeklinde olur. Dikkat edilmesi gereken nokta, bu işlemi yaparken değişken sayısı ve değer sayısı eşit olmalıdır. Aksi takdirde hata alınır. "x, y, z = "Orange", "Banana" şeklinde yazılır ise Output: ValueError: too many values to unpack (expected 3) şeklinde olur.
# Aynı değeri tek bir satırda birden fazla değişkene atayabilirsiniz. "x = y = z = "Orange" şeklinde yazılabilir. Output: "Orange", "Orange", "Orange" şeklinde olur. 
# Bir listede değerler koleksiyonunuz varsa, Tuple vb. Python, değerleri değişkenlere çıkarmanıza izin verir. Buna paket açma denir. "fruits = ["apple", "banana", "cherry"] şeklinde yazılabilir. Output: ["apple", "banana", "cherry"] şeklinde olur. "x, y, z = fruits" şeklinde yazılabilir. Output: "apple", "banana", "cherry" şeklinde olur.
# print() fonksiyonu genelde çıktı değişkeni için kullanılır.x = "Orange" ise "print(x)" şeklinde yazıldığında Output: "Orange" şeklinde olur.
# print() işlevinde, virgülle ayırarak birden çok değişken çıktısı alırsınız. "x = "Orange" y = "Banana" z = "Cherry" şeklinde yazılabilir.print(x, y, z)" şeklinde yazılabilir. Output: "Orange", "Banana", "Cherry" şeklinde olur. Output: "Orange", "Banana", "Cherry" şeklinde olur.
# print() fonksiyonunda + operatörü ile bir dizi ve bir sayıyı birleştirmeye çalıştığınızda Python size bir hata verecektir. "x = 5 y = "John" print(x + y)" şeklinde yazılabilir. Output: TypeError: unsupported operand type(s) for +: 'int' and 'str' şeklinde olur. Çünkü x değişkeni integer, y değişkeni string türündedir. Bu yüzden + operatörü ile birleştirilemezler.
# print() işlevinde birden çok değişkenin çıktısını almanın en iyi yolu, farklı veri türlerini bile destekleyen bunları virgülle ayırmaktır. "x = 5 y = "John" print(x, y)" şeklinde yazılabilir. Output: 5 John şeklinde olur.

x = "My name is"
name =" Latif Bera Ozbey"
def myfunc():
  print(x + name)

myfunc()

# BU KODUN ÇIKTISI: My name is Latif Bera Ozbey


# Bir fonksiyon içerisinde aynı isimde bir değişken oluşturursanız, bu değişken yerel olur ve sadece fonksiyon içerisinde kullanılabilir. Aynı ada sahip global değişken, olduğu gibi, global ve orijinal değeri ile kalacaktır.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# BU KODUN  ÇIKTISI: Python is fantastic 
#                    Python is awesome

# BİR ÖRNEK
x = ["apple", "banana", "cherry"]
print(type(x))

# BU KODUN ÇIKTISI: <class 'list'> yani x değişkeni list türündedir.string değildir.

# BİR ÖRNEK
x = ("apple", "banana", "cherry")
print(type(x))

# BU KODUN ÇIKTISI: <class 'tuple'> yani x değişkeni tuple türündedir.string değildir.

# BİR ÖRNEK

x = {"name" : "John", "age" : 36}
print(type(x))

# BU KODUN ÇIKTISI: <class 'dict'> yani x değişkeni dict türündedir.string değildir.

# BİR ÖRNEK

x = True
print(type(x))

# BU KODUN ÇIKTISI: <class 'bool'> yani x değişkeni bool türündedir.string değildir.



'''
                NOTES ON PYTHON 05.12.2022
Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	 int, float, complex
Sequence Types:	 list, tuple, range
Mapping Type:	 dict
Set Types:	 set, frozenset
Boolean Type:	 bool
Binary Types: 	bytes, bytearray, memoryview
None Type:	 NoneType

                 NOTES ON PYTHON 10.12.2022

Output Separators
When printing multiple outputs, you can customize the separator using the sep parameter.

Run the code below to see the output 👇.

print("Iron", "Man", sep ="-")

Output: Iron-Man

           
                NOTES ON PYTHON 12.12.2022

               User Input
The input() command asks the user for input and returns what they enter as a string. Like this:

x = input()
print(x)       
-----------------
number = input()
print("You entered: " + number)
-----------------
name = input()
age = input()
print(name + " is " + age + " years old")
-----------------

   Input as a number

So we know that the input() function returns a string. But what if we need it to be something else, like a number? No problem, we can totally do that!

Let's assume we’ve taken the age of the user as an input. 

To convert it to a number, we can use the int() function:

age = int(input())
print(age)  
-----------------

    Convert to float

Similar to the int() function, the float() function converts a string to a float:

height = float(input())
print(height) 
-----------------

   Convert to string

Sometimes there is a need to use a number in a string concatenation.

This can be done using the str() function, which converts a number to a string.

For example:

age = 42
print("His age is " + str(age))  
-----------------

    Working with Input
Write a program to take x and y as input and output the string x, repeated y times.

Sample Input

hi

3

Sample Output

hihihi"""

#your code goes here
x=input()
y=int(input())
print(x*y)

this is the code for the above question and the output is hihihi
-----------------

In-Place Operators
In-place operators let you write code like 'x = x + 3' more concisely, as 'x += 3'.

Check it out:

x = 2
print(x)

x += 3
print(x)

output is 2 and 5
-----------------
Roald Dahl was a British novelist, short story writer, poet, screenwriter, and fighter pilot. His books have sold more than 250 million copies worldwide. He is best known for his children's books, which include the novels James and the Giant Peach, Charlie and the Chocolate Factory, Fantastic Mr. Fox, The Witches, Matilda, and The BFG. Dahl also wrote books for adults, including Tales of the Unexpected and Going Solo. He won the 1983 Academy Award for Best Adapted Screenplay for his work on the film adaptation of his book, Charlie and the Chocolate Factory.


I want to make a  Python code for Roald Dahl's accident. He did an accident in his sister's car at 35 miles per hour. In our country, kilometers are used instead of miles for distance measurement. 

So I made a simple program with Python code that can convert the 35 miles he crashed to miles.

Below is the code:

miles = int(input())
km = miles * 1.60934

print(km)

If input is 35, the output is 56.32154 km.

You can write in the comments what happened at the end of this accident that Roald Dahl had by searching Google.



******Notes on Python 13.12.2022********

     Booleans
 
We can create Booleans by comparing values, by using the equal operator ==. Like this:

my_boolean = True
print(my_boolean)
True

print(2 == 3)
False

print("hello" == "hello")
True

***Be careful not to confuse assignment (one equal sign) with comparison (two equal signs).

***Comparison operators are also called Relational operators.***

-----------------

The True and False Boolean values can be represented as integers 1 and 0, respectively. 

x = (7 > 5)
print(int(x)) 

output is 1

-----------------

              if Statements

Python uses indentation (that empty space at the beginning of a line) to delimit blocks of code.

Depending on the program's logic, indentation can be mandatory.


The statements in the if should be indented.
-----------------
x = 42
if x > 5:
   print(x , " is greater than 5")

output is 42 is greater than 5
-----------------

if Statements

The colon at the end of the expression in the if statement is important, don’t leave it out.

age = 24

if age > 18:
   print("Cool")
   output is Cool

-----------------

   NOTES ON PYTHON 15.12.2022

       else Statements

The else statement can be used to run some statements when the condition of the if statement is False.

x = 4
if x == 5:
   print("Yes")
else:
   print("No") 
 Output is No
  -----------------

*** Every if condition block can have only one else statement.

So for us to make multiple checks, we need to chain if and else statements.
-----------------

      elif Statements                   #elif is short for else if

Too many if/else statements make your code long and hard to read.

The best way to solve this is the elif (short for else if) statement. It’s a shortcut to use when chaining together if and else statements, making the code shorter and easier to read.

-----------------

 *** A series of if elif statements can have a final else block, which is called if none of the if or elif expressions is True .

-----------------

  Boolean Logic

Now it’s time to level up our Booleans with some operators, which allow us to combine multiple conditions.

Let’s start with the and operator. It is True, if both conditions evaluate to True :

print(1 == 1 and 2 == 2)
True
print(1 == 1 and 2 == 3)
False
print(1 != 1 and 2 == 2)
False
print(2 < 1 and 3 > 6)
False

-----------------

  Boolean Or

Now onto the or operator.

The or operator is True if either (or both) of its conditions are True, and False if both conditions are False.

print( 1 == 1 or 2 == 2 )
True
print( 1 == 1 or 2 == 3 )
True
print( 1 != 1 or 2 == 2 )
True
print( 2 < 1 or 3 > 6 )
False
-----------------

age = int(input())
limit = 18
height = int(input())

if (age > limit and height > 180):
  print("Welcome")
else:
    print("Go out")
    ------------
    if(hour > 20 or day == "Sunday"):
  print("Closed")
else:
  print("Open")
  ------------
  
            Boolean Not

Finally, the not operator works a little differently. not takes just one argument, and inverts it.

The result of not True is False, and not False goes to True. Like this:

print(not 1 == 1)
False
print(not 1 > 7)
True
-----------------

You can chain multiple conditional statements in an if statement using the Boolean operators.

For example:

country = "US"
age = 42

if(country == "US" or country == "GB") and (age > 0 and age < 100): 
  print("Cool")

-----------------

                      Loops

Loops allow you to repeat a block of code multiple times.

level
For example, let's say we need to process multiple user inputs, so that each time the user inputs something, the same block of code needs to be executed.
-----------------

                  while Loops

Here’s a while loop containing a variable that counts up from 1 to 5, at which point the loop terminates.

i = 1
while i <=5:
   print(i)
   i = i + 1

print("Finished!")

output is 1 2 3 4 5 Finished!
-----------------

              while Loops

The statements inside the while loop need to be indented, similar to an if statement.

x = 0
while x<10:
  print(x)
  x += 1
output is 0 1 2 3 4 5 6 7 8 9
-----------------

             while Loops  (LOOK W3 SCHOOLS*****************)
The code in the body of a while loop is executed repeatedly while the condition is True.

 This is called iteration.

The following code adds the current number to the sum variable during each iteration:

sum = 0
x = 10
while x > 0:
  sum += x
  x -= 1

print(sum)

output is 55
explaination is 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 55
explain the code is sum = 0 + 10 = 10
-----------------
       
         NOTES ON PYTHON 16.12.2022

x = 1
while x < 1001:
  if x%2 == 0:
    print(str(x) + " is even")
  else:
    print(str(x) + " is odd")

  x += 1

  explain the code is 1 from 1000 odd and even numbers

  note: str(x) is used to convert the number x to a string, so that it can be used for concatenation.
  -----------------
  
x = 0
while x <=20:
   print(x)
   x += 2  
 explain the code is 0 2 4 6 8 10 12 14 16 18 20

-----------------

If the condition of the while loop remains True, the loop will run indefinitely, causing an infinite loop.


A short way to create an infinite loop is by using while True.

  x = 8

while x > 3:
  print(x)


output is infinite 8
 
-----------------

Happy Birthday Message for My Dad with infinite loop

 x = "Happy Birthday Yusuf"

while "b" > "a":
  print(x)
-----------------
dad_age = 38
my_age = 11
x = "Happy Birthday Yusuf"

while dad_age > my_age:
  print(x)
-----------------

                   break

To end a while loop prematurely, we can use a break statement.

For example, we can break an infinite loop if some condition is met:

i = 0
while True:
  print(i)
  i = i + 1
  if i >= 5:
    print("Breaking")
    break

print("Finished")

output is 0 1 2 3 4 Breaking Finished
-----------------

Here is one example use case of break:

An infinite while loop can be used to continuously take user input. For example, you are making a calculator and need to take numbers from the user to add together and stop when the user enters "stop".

In this case, the break statement can be used to end the infinite loop when the user input equals "stop".

level
Using the break statement outside of a loop causes an error.
-----------------

              continue

Another statement that can be used within loops is continue. 

Unlike break, continue jumps back to the top of the loop, rather than stopping it. Basically, the continue statement stops the current iteration and continues with the next one.

For example:

i = 0
while i<5:
  i += 1
  if i==3:
    print("Skipping 3")
    continue
  print(i)
-----------------

i=0

while True:

    i+=1

    if(i == 2):

        continue

    if(i == 5):

        break

    

    print(i)

output is 1 3 4
-----------------

total = 0
#your code goes here
age = int(input())
age = int(input())
age = int(input())
age = int(input())
age = int(input())
while age >2:
  total += 100
else: 
continue
print (total)

-----------------

                 ************BMI Calculator*****************
          
Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using a person's weight and height, using this formula: weight / height²

The resulting number indicates one of the following categories:

Underweight = less than 18.5

Normal = more or equal to 18.5 and less than 25

Overweight = more or equal to 25 and less than 30

Obesity = 30 or more

Let’s make finding out your BMI quicker and easier, by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category.

Sample Input

85

1.9

Sample Output

Normal

level
Weight is in kg, height is in meters. 

Note, that height is a float.

the code is:

#your code goes here
weight = int(input()) 
height = float(input())
bmi = weight / (height * height) 
if bmi < 18.5:
    print("Underweight") 
elif bmi >= 18.5 and bmi < 25:
        print("Normal")
elif bmi < 30 and bmi >= 25:
             print("Overweight")
elif bmi >= 30:
            print("Obesity")               
-----------------

  NOTES ON PYTHON 17.12.2022

  Lists are used to store items. 

We can create a list by using square brackets with commas separating items. Like this:

words = ["Hello", "world", "!"]
PY
level
In this example the words list contains three string items: Hello, world and !.
-----------------

                          ***index 
If you want to access a certain item in the list, you can do this by using its index in square brackets.

In our example, that would look like this:

words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])
The first list item's index is 0, rather than 1, as you might expect.
----
Lists can hold different data types, such as strings and numbers.

x = ["a", "b", "c"]
y = [1, 2, 3, 4, 5]

print(x[1])
print(y[3])
output is b 4
-----------
         ****matrices

But lists aren’t just for shopping!

We can do some pretty cool stuff with them in Python. For example, we can use nested lists to represent 2D grids, such as matrices.

For example:

m = [
    [1, 2, 3],
    [4, 5, 6]
    ]

print(m[0][0])
print(m[0][1])
print(m[1][0])
print(m[1][1])
      output is 1 2 4 5

-----------------
To access the elements of a matrix, we specify the row and the column of the item using square brackets:
m = [
    [1, 2, 3],
    [4, 5, 6]
    ]
    
print(m[1][2])  

output is 6

****first is row and second is column***
----
                          ***Strings
Strings can be indexed like lists too!

Indexing a string is like creating a list containing each character in the string.

For example:

str = "Hello world!"
print(str[6])

output is w

***Space (" ") is also a symbol and has an index.***
-----------------
Write a program that takes an input string and outputs the 3rd character of the string.
my_list = input()
print(my_list[2])

if the input is "Latif" the output is t
-----------------
                                 List Operations
The item at a certain index in a list can be reassigned.

For example:

nums = [5, 8, 2]
nums[1] = 42

print(nums)

output is [5, 42, 2]
**************************************
so we can change the value of the list
**************************************
-----------------

List Operations
The list of cool things we can do with lists just keeps growing!

Lists can also be added the same way strings can be.

For example:

nums = [1, 2, 3]
print(nums + [4, 5, 6])

output is [1, 2, 3, 4, 5, 6]
-----------------

Figure out the output of this code:

x = [2, 4]

x += [6, 8]

print(x[2]//x[0])

output is 3
-----------------

Lists and strings share a lot of similarities - you can basically think of strings as lists of characters that can't be changed.

Similar to strings, a list can be multiplied by an integer:

nums = [1, 2, 3]
print(nums * 3)

output is [1, 2, 3, 1, 2, 3, 1, 2, 3]
-----------------
        ***in operator***
To check if an item is in a particular list, we can use the in operator.

It returns True if the item occurs one or more times in the list, and False if it doesn't. Like this:

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

output is True True False
-----------------

nums = [10, 9, 8, 7, 6, 5]

nums[0] = nums[1] - 5

# 4, 9, 8, 7, 6, 5

if 4 in nums:

  print(nums[3])

else:

  print(nums[4])

output is 7
-----------------


The in operator is also used to determine whether or not a string is a substring of another string.

x = "hello world"

if "world" in x:
  print("Yes")
  output is Yes
-----------------
                  not in operator
Similarly, to check if an item is not in a list, you can use the not operator in one of the following ways:

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

output is True True False False
-----------------
PRACTICE
Given a list of numbers, output "bingo" if it contains the input number.


Do not output anything if the number is not found.

x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]

num = int(input())
if num in x:
    print("bingo")
-----------------

    NOTES ON PYTHON 18.12.2022 
    
        ***for Loops***
We have learned about the while loop in the previous lessons. Now it's time to learn about the for loop.

The for loop is used to iterate over a given sequence, such as lists or strings.

The code below outputs each item in the list and adds an exclamation mark at the end:

words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")
output is hello! world! spam! eggs!
-----------------

A for loop can be used to iterate over strings.

For example:

str = "testing for loops"
count = 0

for x in str:
  if(x == 't'):
    count += 1

print(count)

output is 3

The code above defines a count variable, iterates over the string and calculates the count of 't' letters in it. During each iteration, the x variable represents the current letter of the string.

The count variable is incremented each time the letter 't' is found, so at the end of the loop, it represents the number of 't' letters in the string.
-----------------


Similar to while loops, the break and continue statements can be used in for loops, to stop the loop or jump to the next iteration.

text = "some text"
for x in text:
  if x == 'e':
    break
  print(x)

output is som
-----------------

                     ***for vs while
So we’ve got the for and while loops, which can be used to execute a block of code multiple times. So which do we use and when?

Usually we’d use the for loop when the number of iterations is fixed. For example, iterating over a fixed list of items in a shopping list.

The while loop is useful in cases when the number of iterations isn’t known and depends on some calculations and conditions in the code block of the loop. For example, ending the loop when the user enters a specific input in a calculator program.

While both for and while loops can be used to achieve the same results, the for loop has a cleaner and shorter syntax, making it a better choice in most cases.

-----------------
 **** PRACTICE ****
for loops allow you to easily iterate through lists.

Given a list of numbers, calculate their sum using a for loop.

Output the sum after the loop.

#sum of all numbers in a list
x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
sum = 0
for i in x:
    sum = sum + i
print(sum)
output is 9803
-----------------

x = "Hello World"
print(len(x))
output is 11
-----------------

                    NOTES ON PYTHON 19.12.2022

                    ***Range***
Python makes it super easy to create number sequences using the range() function.

By default, it starts from 0, increments by 1 and stops before the specified number.

The following code generates a list containing all of the integers, up to 10.

numbers = range(10)
print(numbers)
o

-----------------
In order to output the range as a list, we need to explicitly convert it to a list, using the list() function.

numbers = list(range(10))
print(numbers)
output is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
-----------------


If range is called with one argument, it’ll produce an object with values from 0 to that argument. 

If it’s called with two arguments, it’ll produce values from the first to the second.

For example:

numbers = list(range(3, 8))
print(numbers)
output is [3, 4, 5, 6, 7]

Remember, the second argument is not included in the range, so range(3, 8) won’t include the number 8.
-----------------

           ****STEP ARGUMENT****
   There’s also a third argument you can use with range(), and it’s really useful. It’s called Step and it determines the interval of the sequence produced. Take a look:

numbers = list(range(5, 20, 2))
print(numbers)

Output is [5, 7, 9, 11, 13, 15, 17, 19]
in this example, the step argument is 2, so the sequence contains only the odd numbers between 5 and 20.
-----------------

            ****NEGATIVE STEP****     
  Want to go backward? No problem! We can also create a list of decreasing numbers, using a negative number as the third argument.

For example:

x = list(range(7, 3, -1))
print(x)

output is [7, 6, 5, 4]
-----------------

You can use ranges in for loops, without the need to convert them into lists. It’s commonly used to repeat some code a certain number of times. Like this

for i in range(5):
  print("hello!")

output is hello! hello! hello! hello! hello!
-----------------

Ranges
You are creating a date picker for a website and need to output all of the years in a given period. 

Write a program that takes two integers as input and outputs the range of numbers between the two inputs as a list.

The output sequence should start with the first input number and end with the second input number, without including it.

Sample Input

2005

2011

Sample Output 

[2005, 2006, 2007, 2008, 2009, 2010]

Convert a range object to a list and output it.

a = int(input())
b = int(input())
z = list(range(a,b))
print(z)
output is [2005, 2006, 2007, 2008, 2009, 2010]
-----------------
   
                    NOTES ON PYTHON 20.12.2022

                    List Slices
List slices allow you to get a part of the list using two colon-separated indices. This returns a new list containing all the values between the indices.

Example:

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

output is [4, 9, 16, 25]
[9, 16, 25, 36, 49]
[0]

-----------------

If the first number in a slice is omitted, it’s taken to be the start of the list.

Example:

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])

output is [0, 1, 4, 9, 16, 25, 36]
-----------------
         
If the second number is omitted, it’s taken to be the end.

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[7:])

output is [49, 64, 81]
-----------------

*****step argument in slices******

Just like with ranges, your list slices can include a third number, representing the step, to include only alternate values in the slice. Like this:

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

output is [0, 4, 16, 36, 64]
[4, 25]
-----------------

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(sqs[1::4])
output is [1, 25, 81]
-----------------
Negative values can also be used in list slicing (as well as normal list indexing). 

Which means that when negative values are used for the first and second values in a slice (or a normal index), they count from the end of the list. Like this:

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

output is [1, 4, 9, 16, 25, 36, 49, 64]
-----------------
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(sqs[7:5:-1])
output is [49, 36]
-----------------

Using [::-1] as a slice is a common and idiomatic way to reverse a list.

nums = [5, 42, 7, 1, 0]
res = nums[::-1]
print(res)

output is [0, 1, 7, 42, 5]
-----------------
nums = [1, 2, 3, 4, 5, 6]

res = nums[::-1]

print(res[2])
Output is 4
-----------------

Write a program that takes a string as input and outputs the last character of that string.
Remember, you can use negative indices to index lists. 

-----------------

Sum of Consecutive Numbers
No one likes homework, but your math teacher has given you an assignment to find the sum of the first N numbers.

Let’s save some time by creating a program to do the calculation for you!

Take a number N as input and output the sum of all numbers from 1 to N (including N).

Sample Input

100

Sample Output

5050

Explanation: The sum of all numbers from 1 to 100 is equal to 5050.

level
You can iterate over a range and calculate the sum of all numbers in the range.

Remember, range(a, b) does not include b, thus you need to use b+1 to include b in the range.
The code is given below:

  def sum_of_consecutive_numbers(n):
  sum = 0
  for i in range(1, n+1):
    sum += i
  return sum

# Read the input
N = int(input())

# Calculate and print the result
result = sum_of_consecutive_numbers(N)
print(result)

output is 5050
----------------

NOTES ON PYTHON 21.12.2022

***Functions
A function is a group of related statements that performs a specific task.

Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.


Furthermore, it avoids repetition and makes the code reusable. 
-----------------

A function has a name and can have arguments.

For example:

print("Hello")

Here, print is the function name and "Hello" is the argument.
----------------


Functions can have multiple arguments.

For example, range(2, 20) has two arguments, 2 and 20.

Function arguments need to be separated by commas.
-----------------

You call the function by using its name, followed by parentheses, which enclose the arguments.

For example, we call the print function with a string argument to generate output:

print("some text")
-----------------
                      ***List Functions
Python has a bunch of useful built-in functions for lists.

len() lets you get the number of items in a list. Like this:

nums = [1, 3, 5, 2, 4]
print(len(nums))

output is 5
-----------------
You can also use len on strings to return their length (character count).

For example:

str = "some text"
x = len(str)
print(x)

output is 9
-----------------
The append() function is used to add an item to the end of the list:

nums = [1, 2, 3]
nums.append(4)
print(nums)

output is [1, 2, 3, 4]
-----------------
insert() inserts a new item at the given position in the list:

words = ["Python", "fun"]
words.insert(1, "is")
print(words)

output is ['Python', 'is', 'fun']

The first argument is the position index, while the second parameter is the item to insert at that position.
-----------------

nums = [9, 8, 7, 6, 5]

nums.append(4)

nums.insert(2, 11)

print(len(nums))

output is 7
-----------------
index() finds the first occurrence of a list item and returns its index.

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('q'))

output is 2 0 1

An error is returned in case the specified item is not found in the list.
-----------------

x = [2, 4, 5, 7, 4]

y = x.index(4)

print(y)

# Output: 1
-----------------
max(list): Returns the maximum value.

min(list): Returns the minimum value.

x = [1, 8, 42, 3]

print(min(x))
print(max(x))

# Output: 1 42
-----------------
                           ****COUNT, REMOVE, REVERSE****
list.count(item): Returns a count of how many times an item occurs in a list.

list.remove(item): Removes an item from a list.

list.reverse(): Reverses items in a list.

x = [2, 4, 6, 2, 7, 2, 9]
print(x.count(2)) # 3

x.remove(4)
print(x)  # [2, 6, 2, 7, 2, 9]

x.reverse()
print(x) # [9, 2, 7, 2, 6, 2]
-----------------

         ***** PRACTICE
You are working on a queue management program.

The queue is represented by a list. 

Write a program to take an input, add it to the end of the queue, and output the resulting list.


The append() method can be used to add new items to the list.


queue = ['John', 'Amy', 'Bob', 'Adam']

x = input()

queue.append(x)

print(queue)

output is ['John', 'Amy', 'Bob', 'Adam', 'input']
-----------------
nums = [2,4,8,9,5]


nums.insert(1, 3) # insert 3 at index 1 (2,3,4,8,9,5)

nums.remove(9) # remove the first 9 in the list  (2,3,4,8,5)

nums.insert(0, nums.count(8)) # insert the number of 8s in the list at index 0 (2,3,4,8,5) -> (1,2,3,4,8,5)

print(nums[3]) # print the number at index 3 (1,2,3,4,8,5) -> 4 

output is 4
-----------------

-----------------
NOTES ON PYTHON 22.12.2020

               String Formatting
Strings have a format() function, which enables values to be embedded in it, using placeholders.

Example:

nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

output is   Numbers: 4 5 6

Each argument of the format function is placed in the string at the corresponding position, which is determined using the curly braces { }.
-----------------

print("{0}{1}{0}".format("abra", "cad"))

output is abracadabra
-----------------
str="{c}, {b}, {a}".format(a=5, b=9, c=7)

print(str)

output is 7, 9, 5
----------------- 
   **join() function
join() joins a list of strings with another string as a separator.

For example:

x = ", ".join(["spam", "eggs", "ham"])
print(x)
#prints "spam, eggs, ham"
-----------------
      **split() function
split() is the opposite of join(). It turns a string with a certain separator into a list.

For example, let's split a sentence into words:

str = "some text goes here"
x = str.split(' ')
print(x)

output is ['some', 'text', 'goes', 'here']

We used a space ' ' as the split separator to get all words of the string as a list. 
-----------------
      **replace() function
replace() replaces one substring in a string with another.

For example:

x = "Hello ME"
print(x.replace("ME", "world"))

output is Hello world
-----------------
       **lower() and upper() functions

lower() and upper() change the case of a string to lowercase and uppercase.

print("This is a sentence.".upper())

print("AN ALL CAPS SENTENCE".lower())

output is THIS IS A SENTENCE.
an all caps sentence
-----------------
   ***PRACTICE
Your friend sent you a message, however his keyboard is broken and types a # instead of a space.

Replace all of the # characters in the given input with spaces and output the result.


You can use the replace() function of a string to replace one substring with another.

msg = input()
print(msg.replace("#", " ")) 

-----------------
     
     ************** NOTES ON PYTHON 23.12.2022 **************

     Functions
You can create your own functions by using the def statement.

Here’s an example of a function named my_func. It takes no arguments, and prints "spam" three times.

def my_func():
  print("spam")
  print("spam")
  print("spam")

  Output is spam     spam     spam
  -----------------
  Just like with if statements, the code block within every function starts with a colon (:) and is indented.
-----------------

So once you’ve defined a function, you can call it multiple times in your code.

Like this:

def hello():
  print("Hello world!")

hello()
hello()
hello()

Output is Hello world!

Note, that we call a function using its name and the parentheses.
-----------------

******************Arguments***************
Functions can take arguments, which can be used to generate the function output.

For example:

def exclamation(word):
  print(word + "!")

exclamation("spam")
output is spam!

-----------------

You can call the same function with different arguments.

def exclamation(word):
  print(word + "!")

exclamation("spam")
exclamation("eggs")
exclamation("python")

output is spam! eggs! python!
Arguments are used to pass information to the function. This allows us to reuse the function logic for different values.
-----------------

Even better, you can define functions with more than one argument; separate them with commas. Like this:

def print_sum_twice(x, y):
  print(x + y)
  print(x + y)

print_sum_twice(5, 8)
output is 13  
          13
-----------------
As you can see in the previous examples, arguments can be used as variables inside the function.

You can have different statements in your functions, working with the argument variables, such as if statements and loops.

               NOTES ON PYTHON 24.12.2022
        
        Returning from Functions

Certain functions, such as int or str, return a value instead of outputting it. 

The returned value can be used later in the code, for example, by getting assigned to a variable. 

To do this for your defined functions, you can use the return statement. Like this:

def sum(x, y):
  return x+y
-----------------

Now we can use our function and assign the result to a variable:

def sum(x, y):
  return x+y

res = sum(42, 7)
print(res)
Output is 49
-----------------

  Guess the output of this code:

def foo(x, y):

  if x >= y:

    return x

  else:

    return y

x = foo(4, 7)

print(x)
Output is 7
-----------------

   You can use the returned value in your code, for example, an if statement:

def max(x, y):
  if x >=y:
    return x
  else:
    return y

if(max(6, 4) > 10):
  print("Yes")
else:
  print("Nope")
Output is Nope
-----------------

  Once you return a value from a function, it immediately stops being executed. 

Any code placed after the return statement won’t be executed.

For example:

def add_numbers(x, y):
  total = x + y
  return total
  print("This won't be printed")

print(add_numbers(4, 5))
output is 9. explanation: the function stops executing after the return statement, so the print statement is never executed.
-----------------

def print_numbers():

  print(1)

  print(2)

  return

  print(4)

  print(6)

output is 1 2
-----------------
A function can only return once, thus, if you need to return multiple values, you can use a list.

For example:

def double(a, b):
  return [a*2, b*2]

x = double(6, 9)
print(x)
output is [12, 18]
-----------------
*****PRACTICE*****
Return
We need to calculate the area of a given rectangle.

Your program needs to take the width and length as input and output the area of the rectangle.

Complete the area function, which takes the length and width as arguments, to calculate and return the area.

Then call the function for the given inputs.

Sample Input

7

4

Sample Output

28


To find the area of a rectangle, multiply the length by the width.

def area(x, y):
   #your code goes here
   return x*y
   

w = int(input())
h = int(input())

print (area (w, h))
#call the function 
input is 3 and 4 output is 12
-----------------
def sum(x):

    res = 0

    for i in range(x):

        res+=i

    return res

print(sum(4))
output is 6
-----------------

       Comments        

We’re so close to the finish line! Well done for making it this far!

Comments are annotations to code used to make it easier to understand. They don't affect how code is run. 

In Python, a comment is created by inserting an octothorpe (otherwise known as a number sign or hash symbol: #). All text after it on that line is ignored.

For example:

x = 365
y = 7

print(x % y) # find the remainder

Output is 1
-----------------

You can have multiple comments in your code.

x = 365
y = 7
# this is a comment

print(x % y) # find the remainder
# print (x // y)
# another comment
output is 1
-----------------

       Docsstrings

Docstrings (documentation strings) are similar to comments, in that they’re designed to explain code. But, they’re more specific and have a different syntax.

They’re created by putting a multiline string containing an explanation of the function below the function's first line. Like this:

def shout(word):
"""
Print a word with an
exclamation mark following it.
"""
print(word + "!")

shout("spam")
output is spam!
-----------------












































'''















