from .Utils import *

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def bissexto():
	ano = check_input("ano: ")
	print(is_leap_year(ano))

if __name__  == "__main__":
	bissexto()