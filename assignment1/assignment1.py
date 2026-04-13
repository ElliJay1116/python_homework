# Write your code here.
# Task 1
def hello():
    return "Hello!"

# Task 2
def greet(name):
    return f"Hello, {name}!"
greet("James")
  
  # Task 3


x = int()
y = int()


def calc(x,y, operation="multiply"):
    try:
        if operation == "multiply":
            return x * y
        elif operation == "add":
                 return x+y
        elif operation == "divide":
                 return x/y
        elif operation == "subtract":
                 return x-y
        elif operation == "modulo":
                 return x % y
        else: 
                    return "invalid operation"
    except ZeroDivisionError:
                return "You can't divide by 0!"
    except TypeError:
                return "You can't multiply those values!"
    
print(calc(5,6,"multiply"))
print(calc(5,6,"add"))
print(calc(20,5,"divide"))
print(calc(12.6,4.4,"subtract"))
print(calc(9,5,"modulo"))
print(calc(10,0,"divide"))
print(calc("first","second","multiply"))

# Task 4
   
def data_type_conversion(value,type):
    try:
        if type == "int":
            return int(value) 
        elif type == "float":
               return float(value)
        elif type == "str":
               return str(value)
        else: 
               return "invalid"
    except ValueError:
           return f"You can't convert {value} into a {type}."
        
print(data_type_conversion(110 , "int"))
print(data_type_conversion(5.5 , "float"))
print(data_type_conversion(7 , "float"))
print(data_type_conversion(9.1 , "str"))
print(data_type_conversion("banana" , "int"))

# Task 5
def grade(*args):
       try:
              avg = sum(args) / len(args)

              if avg >= 90:
                return "A"
              elif avg >= 80:
                     return "B"
              elif avg >= 70:
                     return "C"
              elif avg >= 60:
                     return "D"
              else: 
                     return "F"
       except(TypeError, ZeroDivisionError):
              return "Invalid data was provided."
       
print(grade(75,85,95))
print(grade("three", "blind", "mice"))

# Task 6

def repeat(word, count):
    result = ""
    for i in range (count):
     result += word
    return result

    #  Task 7

def student_scores(mode, **kwargs):
     if mode == "mean":
        scores = kwargs.values()
        return sum(scores) / len(kwargs)
     elif mode == "best":
           best_score = None
           highest_score = -1

           for name, score in kwargs.items():
                 if score > highest_score:
                       highest_score = score
                       best_student = name

     return best_student

            

student_scores("mean", Tom=75, Dick=89, Angela=91)
student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50)  

#Task 8

def titleize (sentence):
      little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
      words = sentence.split()
      result = []

      last_index = len(words) - 1

      for i, word in enumerate(words):
            if i == 0 or i == last_index or word.lower() not in little_words:
                  result.append(word.capitalize())
            else: 
                  result.append(word.lower())

      return " ".join(result)

titleize("war and peace")

# Task 9

def hangman(secret,guess):
      result = ""

      for letter in secret:
            if letter in guess:
                  result += letter
            else: 
                result += "_"
      return result


hangman("difficulty","ic")

# Task 10

def pig_latin(sentence):
    
    words = sentence.split()
    pl_words = []
    
    for word in words:
        if word[0].lower() in "aeiou":
            new_word = word + "ay"
            
        elif word.lower().startswith("qu"):
            new_word = word[2:] + "quay"
            
        else:
            cons = 0
            for i, letter in enumerate(word):
                if letter.lower() in "aeiou":
                        if letter.lower() == 'u' and i > 0 and word[i-1].lower() == 'q':
                            continue
                        cons = i
                        break

            new_word = word[cons:] + word[:cons] + "ay"
        
        pl_words.append(new_word)

    return " ".join(pl_words)


pig_latin("apple") 
pig_latin("banana")
pig_latin("cherry")
pig_latin("quiet")
pig_latin("square")
pig_latin("the quick brown fox")

            


    
