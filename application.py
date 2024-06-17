#HOW TO PRINT
print('Hello World')
print('This is the next statement')


#VARIABLES
number = 3523
print(number)

weight = 52
print(weight)

answer = number+weight
print(answer)

f_name = "Priyanka "
l_name = "Sahoo"
weight = 60

name = f_name+l_name
#only string can be concatenated
print(name+" weighs "+str(weight)+" lbs")


#DATA_TYPES
#In python there are 4 data types (int,float,str,bool)
print(type(30))
print(type(30.78))
print(type("321"))
print(type(True))

#we can declare variable with different data-types but if you're printing at last it will consider the last one
age = 23
data_type = type(age)
print(data_type)
age = "tr"
data_type = type(age)
print(data_type)
age = 3.23
data_type = type(age)
print(data_type)

#BASIC ARITHMATICS
num1 = 10
num2 = 4
#Addition
print(num1+num2)
#Subtraction
print(num1-num2)
#Multiplication
print(num1*num2)
#Division
print(num1/num2)#get the decimal value
print(num1%num2)#get the remainder

#use paranthesis according to your question, while you're doing more than one operation at a time
print((10*5)+3-(8%2))


#INDEXING & SLICING STRINGS
sentence = "I'm coming Home"
print(sentence)
sentence = "I'm coming\nHome"
#\n = next line
print(sentence)

sent = "This is another sentence"
print(sent[0]) #will give the character at the first index
print(sent[-1])#will give the character at the last index 
print(sent[23])

#both -1 and 23 index will give the same answer. As my sentence's length is short ,so I can count and use that index number but if a sentence is given with long length then just count as reverse with negative sign 

print(sent[0:4])
# here ':' means 0 to 4 and 4 is exculded

sent3= "abcdefg"
print(sent3[0:7:2])
#the third index specifies how to count , here 2 means count one skip one ... like this if we put 3 then count one skip two...
print(sent3[0:7:3])

#if you want to get any middle part of the string
print(sent3[3:6]) #Reminder:6 is excluded


#BASIC STRING METHODS
ano_Sent = "A big CUP of Coffee"
print(ano_Sent.upper()) #convert the whole sentece into upper case
print(ano_Sent.lower()) #convert the whole sentece into lower case
print(ano_Sent.capitalize()) #capitalize the first character of the sentence
print(ano_Sent.title()) #capitalize first letter of each word in the sentence
print(ano_Sent.isdigit())#check if all are digit
print(ano_Sent.isalpha())#check if all are alphabetics
print(ano_Sent.isalnum()) #check if it ob=nly contains alphanumerics

numSent = "A982R31"
print(numSent.startswith("A98"))#checks if it starts with passed string


#FORMATTING
formSent = "The sum is {0}".format("Big")
print(formSent)
formSent2 = "The sum of {0} + {1} is {2}".format(5,7,5+7)
print(formSent2)


#IMMUTABLE STRINGS(can't be changed)
my_var = "abcdefg"
# my_var[0] = "u"
# print(my_var) it can't change the string directly instead of this follow the bellow step
print("u"+my_var[1:])

