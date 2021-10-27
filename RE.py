import re


def is_keyword(str):
    keyword = ["return", "false", "none", "break", "from", "in", "global",
               "while", "for", "with", "class", "if", "else", "elif",
               "as", "try", "except", "raise", "finally", "continue"]
    if str in keyword:
        return ('Is Keyword')
    elif re.fullmatch("(^[^\d\W]\w*\Z)", str):
        return ('Is Identifier')
    elif(re.fullmatch("([+|-][0-9]+)|([0-9]+)", str)):
        return ("Is Int Constatnt")
    elif(re.fullmatch("([+|-][0-9]*[.][0-9]+)|([0-9]*[.][0-9]+)", str)):
        return ("Is Float Constatnt")
    elif(re.fullmatch("[\w\W]", str)):
        return ("Is Char Constatnt")
    elif (re.fullmatch("[\w\W]*", str)):
        return ("Is String Constatnt")
    else:
        return "invalid lexeme"


# def Is_Identifier(string):
#     if(re.fullmatch("(^[^\d\W]\w*\Z)", string)):
#         print('Is Identifier')
#     else:
#         Is_Int_Constatnt(string)


# def Is_Int_Constatnt(string):
#     if(re.fullmatch("([+|-][0-9]+)|([0-9]+)", string)):
#         print("Is Int Constatnt")
#     else:
#         Is_Float_Constant(string)


# def Is_Float_Constant(string):
#     if(re.fullmatch("([+|-][0-9]*[.][0-9]+)|([0-9]*[.][0-9]+)", string)):
#         print("Is Float Constatnt")
#     else:
#         Is_Char_Constant(string)


# def Is_Char_Constant(string):
#     if(re.fullmatch("[\w\W]", string)):
#         print("Is Char Constatnt")
#     else:
#         Is_String_Constant(string)


# def Is_String_Constant(string):
#     if(re.fullmatch("[\w\W]*", string)):
#         print("Is String Constatnt")
#     else:
#         return "invalid lexeme"


# str = input()
# is_keyword(str)
