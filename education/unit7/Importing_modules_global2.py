from message import *
  
print_message("Hello work")  # Message: Hello work - применяется функция из модуля message
 
def print_message(some_text):
    print(f"Text: {some_text}")
  
print_message("Hello work")  # Text: Hello work - применяется функция из текущего файла