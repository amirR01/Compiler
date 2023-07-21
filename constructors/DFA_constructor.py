import json
digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
symbols = {';', ':', '[', ']', '(', ')', '+', '-', '*', '=', '<', ',', '{', '}'}
white_space = {' ', '\n', '\t', '\r', '\f', '\v'}
comment_symbol ={'/','*'}
NUM_DFA = {}
ID_DFA = {}
SYMBOL_DFA = {}
COMMENT_DFA = {}
WHITESPACE_DFA = {}

for num in digits:
    #number dfa
    tempray_dict = NUM_DFA.get("start",{})
    tempray_dict[num] = "containing number" 
    NUM_DFA["start"] = tempray_dict

    tempray_dict = NUM_DFA.get("containing number",{})
    tempray_dict[num] = "containing number" 
    NUM_DFA["containing number"] = tempray_dict
    #ID dfa
    tempray_dict = ID_DFA.get("containing letter",{})
    tempray_dict[num] = "containing letter"
    ID_DFA["containing letter"] = tempray_dict
 
    

for letter in letters:
    #number dfa
    tempray_dict = NUM_DFA.get("containing number",{})
    tempray_dict[letter] = "error invalid number"
    NUM_DFA["containing number"] = tempray_dict
    #ID dfa
    tempray_dict = ID_DFA.get("start",{})
    tempray_dict[letter] = "containing letter"
    ID_DFA["start"] =tempray_dict

    tempray_dict = ID_DFA.get("containing letter",{})
    tempray_dict[letter] = "containing letter"
    ID_DFA["containing letter"] = tempray_dict

   


for symbol in symbols:
    #symbol dfa
    if symbol != "=" and symbol != "*" :
        tempray_dict = SYMBOL_DFA.get("start",{})
        tempray_dict[symbol] = "symbol recognized"
        SYMBOL_DFA["start"] = tempray_dict
    elif symbol == "=":
        tempray_dict = SYMBOL_DFA.get("start",{})
        tempray_dict[symbol] = "containing symbol ="
        SYMBOL_DFA["start"] = tempray_dict

        tempray_dict = SYMBOL_DFA.get("containing symbol =",{})
        tempray_dict[symbol] = "symbol recognized"
        SYMBOL_DFA["containing symbol ="] = tempray_dict
    elif symbol == "*":
        tempray_dict = SYMBOL_DFA.get("start",{})
        tempray_dict[symbol] = "containing symbol *"
        SYMBOL_DFA["start"] = tempray_dict
        SYMBOL_DFA["containing symbol *"] = {}
        



 

for symbol in comment_symbol:
    #comment
    if symbol == "/":
        tempray_dict = COMMENT_DFA.get("start",{})
        tempray_dict[symbol] = "/ recognized"
        COMMENT_DFA["start"] = tempray_dict

        tempray_dict = COMMENT_DFA.get("* recognized",{})
        tempray_dict[symbol] = "comment finished"
        COMMENT_DFA["* recognized"] = tempray_dict

        tempray_dict = COMMENT_DFA.get("* in start",{})
        tempray_dict[symbol] = "error unmatched"
        COMMENT_DFA["* in start"] = tempray_dict

    else:        
        tempray_dict = COMMENT_DFA.get("/ recognized",{})
        tempray_dict[symbol] = "comment"
        COMMENT_DFA["/ recognized"] = tempray_dict 

        tempray_dict = COMMENT_DFA.get("comment",{})
        tempray_dict[symbol] = "* recognized"
        COMMENT_DFA["comment"] = tempray_dict

        tempray_dict = COMMENT_DFA.get("start",{})
        tempray_dict[symbol] = "* in start"
        COMMENT_DFA["start"] = tempray_dict



for symbol in white_space:
    tempray_dict = WHITESPACE_DFA.get("start",{})
    tempray_dict[symbol] = "whitespace recognized"
    WHITESPACE_DFA["start"] = tempray_dict



# saving dfa

with open("." + "/NUM_DFA.json", "w") as f:
            json.dump(NUM_DFA, f)


with open("." + "/ID_DFA.json", "w") as f:
            json.dump(ID_DFA, f)


with open("." + "/SYMBOL_DFA.json", "w") as f:
            json.dump(SYMBOL_DFA, f)

with open("." + "/COMMENT_DFA.json", "w") as f:
            json.dump(COMMENT_DFA, f)

with open("." + "/WHITESPACE_DFA.json", "w") as f:
            json.dump(WHITESPACE_DFA, f)

 
 
 
 