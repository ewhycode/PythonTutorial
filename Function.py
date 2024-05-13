#function = block of reusable code
#           place () after the function name to invoke/call it

#def define

def happyBirthday(name,age): #"name" parameter
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print ("Happy birthday to you!")
    print()

happyBirthday("Bro", "20") #"BRO" argument
happyBirthday("Steve", "30")
happyBirthday("Joe", "40")



def patientDetails (name,age,address):
    print (f"The Name of the patient is {name}")
    print (f"{age} years old")
    print (f"Lives at {address}")

patientDetails("Jane","30","Melbourne")
patientDetails("Joe", "30", "Traralgon")

def displayInvoice (username, amount, dueDate):
    print(f"Hello {username}")
    print (f"Your bill of ${amount:.2f} is due {dueDate}")

displayInvoice ("Loki", 110.00, "12/01")
displayInvoice ("Troy", 52.50, "12/02")

#return = statement used to end a function
         #   and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract (x,y):
    z = x - y
    return z

def multiply (x,y):
    z = x - y
    return z

def divide (x,y):
    z = x * y
    return z

print (add(1,2))
print (subtract(1,2))
print (multiply(1,2))
print (divide(1,2))

#capitalize
def createName(first, last):
      first = first.capitalize()
      last = last.capitalize()
      return first +     " " + last

fullName = createName ("bro", "code")
print (fullName)