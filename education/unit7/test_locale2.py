import locale
 
locale.setlocale(locale.LC_ALL, "")
 
number = 12345.6789
formatted = locale.format_string("%.02f", number)
print(formatted)    # 12345,68
print(locale.getlocale())   
# ('Russian_Russia', '1251') -