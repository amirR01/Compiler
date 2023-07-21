import json


first = {
    'Program': ['epsilon', 'int', 'void'],
    'Declaration-list': ['epsilon', 'int', 'void'],
    'Declaration': ['int', 'void'],
    'Declaration-initial': ['int', 'void'],
    'Declaration-prime': ['(', ';', '['],
    'Var-declaration-prime': [';', '['],
    'Fun-declaration-prime': ['('],
    'Type-specifier': ['int', 'void'],
    'Params': ['int', 'void'],
    'Param-list': [',', 'epsilon'],
    'Param': ['int', 'void'],
    'Param-prime': ['[', 'epsilon'],
    'Compound-stmt': ['{'],
    'Statement-list': ['epsilon', '{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM'],
    'Statement': ['{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM'],
    'Expression-stmt': ['break', ';', 'ID', '(', 'NUM'],
    'Selection-stmt': ['if'],
    'Iteration-stmt': ['repeat'],
    'Return-stmt': ['return'],
    'Return-stmt-prime': [';', 'ID', '(', 'NUM'],
    'Expression': ['ID', '(', 'NUM'],
    'B': ['=', '[', '(', '*', '+', '-', '<', '==', 'epsilon'],
    'H': ['=', '*', 'epsilon', '+', '-', '<', '=='],
    'Simple-expression-zegond': ['(', 'NUM'],
    'Simple-expression-prime': ['(', '*', '+', '-', '<', '==', 'epsilon'],
    'C': ['epsilon', '<', '=='],
    'Relop': ['<', '=='],
    'Additive-expression': ['(', 'ID', 'NUM'],
    'Additive-expression-prime': ['(', '*', '+', '-', 'epsilon'],
    'Additive-expression-zegond': ['(', 'NUM'],
    'D': ['epsilon', '+', '-'],
    'Addop': ['+', '-'],
    'Term': ['(', 'ID', 'NUM'],
    'Term-prime': ['(', '*', 'epsilon'],
    'Term-zegond': ['(', 'NUM'],
    'G': ['*', 'epsilon'],
    'Factor': ['(', 'ID', 'NUM'],
    'Var-call-prime': ['(', '[', 'epsilon'],
    'Var-prime': ['[', 'epsilon'],
    'Factor-prime': ['(', 'epsilon'],
    'Factor-zegond': ['(', 'NUM'],
    'Args': ['epsilon','ID', '(', 'NUM'],
    'Arg-list': ['ID', '(', 'NUM'],
    'Arg-list-prime': [',', 'epsilon']
}

follow = {
    'Declaration-list': ['$', '{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}', "$"],
    'Declaration': ['int', 'void', '$', '{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}'],
    'Declaration-initial': ['(', ';', '[', ',', ')'],
    'Declaration-prime': ['int', 'void', '$', '{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}'],
    'Var-declaration-prime': ['int', 'void', '$', '{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}'],
    'Fun-declaration-prime': ['int', 'void', '$', '{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}'],
    'Type-specifier': ['ID'],
    'Params': [')'],
    'Param-list': [')'],
    'Param': [',', ')'],
    'Param-prime': [',', ')'],
    'Compound-stmt': ['int', 'void', '$', '{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}', 'else',
                      'until'],
    'Statement-list': ['}'],
    'Statement': ['{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}', 'else', 'until'],
    'Expression-stmt': ['{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}', 'else', 'until'],
    'Selection-stmt': ['{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}', 'else', 'until'],
    'Iteration-stmt': ['{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}', 'else', 'until'],
    'Return-stmt': ['{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}', 'else', 'until'],
    'Return-stmt-prime': ['{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}', 'else', 'until'],
    'Expression': [';', ')', ']', ','],
    'B': [';', ')', ']', ','],
    'H': [';', ')', ']', ','],
    'Simple-expression-zegond': [';', ')', ']', ','],
    'Simple-expression-prime': [';', ')', ']', ','],
    'C': [';', ')', ']', ','],
    'Relop': ['(', 'ID', 'NUM'],
    'Additive-expression': [';', ')', ']', ','],
    'Additive-expression-prime': ['<', '==', ';', ')', ']', ','],
    'Additive-expression-zegond': ['<', '==', ';', ')', ']', ','],
    'D': ['<', '==', ';', ')', ']', ','],
    'Addop': ['(', 'ID', 'NUM'],
    'Term': ['+', '-', ';', ')', '<', '==', ']', ','],
    'Term-prime': ['+', '-', '<', '==', ';', ')', ']', ','],
    'Term-zegond': ['+', '-', '<', '==', ';', ')', ']', ','],
    'G': ['+', '-', '<', '==', ';', ')', ']', ','],
    'Factor': ['*', '+', '-', ';', ')', '<', '==', ']', ','],
    'Var-call-prime': ['*', '+', '-', ';', ')', '<', '==', ']', ','],
    'Var-prime': ['*', '+', '-', ';', ')', '<', '==', ']', ','],
    'Factor-prime': ['*', '+', '-', '<', '==', ';', ')', ']', ','],
    'Factor-zegond': ['*', '+', '-', '<', '==', ';', ')', ']', ','],
    'Args': [')'],
    'Arg-list': [')'],
    'Arg-list-prime': [')']
}

diagrams = {
    "Program": {
        "int" : ["#j_main","Declaration-list" , "$" , "#delete_j_main"],
        "void" : ["#j_main","Declaration-list" , "$","#delete_j_main"],
        "epsilon" : ["#j_main","Declaration-list" , "$" ,"#delete_j_main"],
    },
    "Declaration-list": {
        "int" : ["Declaration", "Declaration-list"],
        "void" : ["Declaration", "Declaration-list"],
        "epsilon" : []
    },
    "Declaration": {
        "int" : ["Declaration-initial" , "Declaration-prime"],
        "void" : ["Declaration-initial" , "Declaration-prime"]
    },
    "Declaration-initial": {
        "int" : ["#p_input","Type-specifier" , "#dec_id","ID"],
        "void" : ["#p_input","Type-specifier" , "#dec_id","ID"]
    },
    "Declaration-prime": {
        "(" : ["Fun-declaration-prime"],
        ";" : ["Var-declaration-prime"],
        "[" : ["Var-declaration-prime"]
    },
    "Var-declaration-prime": {
        ";" : ["#dec_var",";"],
        "[" : ["[","#dec_array", "NUM", "]", ";"]
    },
    "Fun-declaration-prime": {
        "(" : ["#start_func_scope","(", "Params", ")", "#end_func_params", "Compound-stmt","#end_func_scope"]
    },
    "Type-specifier": {
        "int" : ["int"],
        "void" : ["void"]
    },
    "Params": {
        "int" : ["#p_input","int","#dec_id", "ID", "Param-prime" , "Param-list" ],
        "void" : ["void"]
    },
    "Param-list": {
        "," : [",", "Param", "Param-list"],
        "epsilon" : []
    },
    "Param": {
        "int" : ["Declaration-initial", "Param-prime"],
        "void" : ["Declaration-initial", "Param-prime"]
    },
    "Param-prime": {
        "[" : ["#dec_array_for_func","[" , "]"],
        "epsilon" : ["#dec_param"]
    },
    "Compound-stmt": {
        "{" : ["{", "Declaration-list", "Statement-list", "}"]
    },
    "Statement-list": {
        "{" : ["Statement", "Statement-list"],
        "break" : ["Statement", "Statement-list"],
        ";" : ["Statement", "Statement-list"],
        "if" : ["Statement", "Statement-list"],
        "repeat" : ["Statement", "Statement-list"],
        "return" : ["Statement", "Statement-list"],
        "ID" : ["Statement", "Statement-list"],
        "(" : ["Statement", "Statement-list"],
        "NUM" : ["Statement", "Statement-list"],
        "epsilon" : []
    },
    "Statement": {
        "{" : ["Compound-stmt"],
        "break" : ["Expression-stmt"],
        ";" : ["Expression-stmt"],
        "if" : ["Selection-stmt"],
        "repeat" : ["Iteration-stmt"],
        "return" : ["Return-stmt"],
        "ID" : ["Expression-stmt"],
        "(" : ["Expression-stmt"],
        "NUM" : ["Expression-stmt"]
    },
    "Expression-stmt": {
        "break" : ["#jp_break_save","break", ";"],
        ";" : [";"],
        "ID" : ["Expression", ";"],
        "(" : ["Expression", ";"],
        "NUM" : ["Expression", ";"]
    },
    "Selection-stmt": {
        "if" : ["if", "(", "Expression", ")", "#save_if", "Statement",  "else","#jp_save_else" ,"Statement","#jp_else"]
    },
    "Iteration-stmt": {
        "repeat" : ["repeat", "#start_repeat_scope","Statement", "#end_repeat_scope","until", "(", "Expression", ")","#jp_repeat","#jp_break"]
    },
    "Return-stmt": {
        "return" : ["return", "Return-stmt-prime","#jp_return"]
    },
    "Return-stmt-prime": {
        ";" : [";"],
        "ID" : ["Expression", ";", "#return"],
        "(" : ["Expression", ";", "#return"],
        "NUM" : ["Expression", ";", "#return"]
    },
    "Expression": {
        "ID" : ["#p_id","ID", "B"],
        "(" : ["Simple-expression-zegond"],
        "NUM" : ["Simple-expression-zegond"]
    },
    "B": {
        "=" : ["#increase_assign","=", "Expression","#assign"],
        "[" : ["[", "Expression", "]","#array_address", "H"],
        "(" : ["Simple-expression-prime"],
        "*" : ["Simple-expression-prime"],
        "+" : ["Simple-expression-prime"],
        "-" : ["Simple-expression-prime"],
        "<" : ["Simple-expression-prime"],
        "==" : ["Simple-expression-prime"],
        "epsilon" : ["Simple-expression-prime"]
    },
    "H": {
        "=" : ["#increase_assign", "=", "Expression","#assign"],
        "*" : ["G" , "D" , "C"],
        "+" : ["G" , "D" , "C"],
        "-": ["G", "D", "C"],
        "<" : ["G" , "D" , "C"],
        "==" : ["G" , "D" , "C"],
        "epsilon" : ["G" , "D" , "C"]
    },
    "Simple-expression-zegond": {
        "(" : ["Additive-expression-zegond" , "C"],
        "NUM" : ["Additive-expression-zegond" , "C"]
    },
    "Simple-expression-prime": {
        "(" : ["Additive-expression-prime" , "C"],
        "*" : ["Additive-expression-prime" , "C"],
        "+" : ["Additive-expression-prime" , "C"],
        "-" : ["Additive-expression-prime" , "C"],
        "<" : ["Additive-expression-prime" , "C"],
        "==" : ["Additive-expression-prime" , "C"],
        "epsilon" : ["Additive-expression-prime" , "C"]
    },
    "C": {
        "<" : ["Relop", "Additive-expression","#bool_op"],
        "==" : ["Relop", "Additive-expression","#bool_op"],
        "epsilon" : []
    },
    "Relop": {
        "<" : ["#p_input","<"],
        "==" : ["#p_input","=="]
    },
    "Additive-expression": {
        "(" : ["Term", "D"],
        "ID" : ["Term", "D"],
        "NUM" : ["Term", "D"]
    },
    "Additive-expression-prime": {
        "(" : ["Term-prime", "D"],
        "*" : ["Term-prime", "D"],
        "+" : ["Term-prime", "D"],
        "-" : ["Term-prime", "D"],
        "epsilon" : ["Term-prime", "D"]
    },
    "Additive-expression-zegond": {
        "(" : ["Term-zegond", "D"],
        "NUM" : ["Term-zegond", "D"]
    },
    "D": {
        "+" : ["Addop", "Term","#add", "D"],
        "-" : ["Addop", "Term", "#add","D"],
        "epsilon" : []
    },
    "Addop": {
        "+" : ["#p_input","+"],
        "-" : ["#p_input","-"]
    },
    "Term": {
        "(" : ["Factor", "G"],
        "ID" : ["Factor", "G"],
        "NUM" : ["Factor", "G"]
    },
    "Term-prime": {
        "(" : ["Factor-prime", "G"],
        "*" : ["Factor-prime", "G"],
        "epsilon" : ["Factor-prime", "G"]
    },
    "Term-zegond": {
        "(" : ["Factor-zegond", "G"],
        "NUM" : ["Factor-zegond", "G"]
    },
    "G": {
        "*" : ["*", "Factor","#mult", "G"],
        "epsilon" : []
    },
    "Factor": {
        "(" : ["(", "Expression", ")"],
        "ID" : ["#p_id","ID", "Var-call-prime"],
        "NUM" : ["#p_num","NUM"]
    },
    "Var-call-prime": {
        "(" : ["(", "Args", ")","#check_func"],
        "[" : ["Var-prime"],
        "epsilon" : ["Var-prime"]
    },
    "Var-prime": {
        "[" : ["[", "Expression", "]","#array_address"],
        "epsilon" : []
    },
    "Factor-prime": {
        "(" : ["(", "Args", ")","#check_func"],
        "epsilon" : []
    },
    "Factor-zegond": {
        "(" : ["(", "Expression", ")"],
        "NUM" : ["#p_num","NUM"]
    },
    "Args": {
        "(" : ["Arg-list"],
        "ID" : ["Arg-list"],
        "NUM" : ["Arg-list"],
        "epsilon" : []
    },
    "Arg-list": {
        "(" : ["Expression", "#assign_param", "Arg-list-prime"],
        "ID" : ["Expression", "#assign_param", "Arg-list-prime"],
        "NUM" : ["Expression", "#assign_param", "Arg-list-prime"]
    },
    "Arg-list-prime": {
        "," : [",", "Expression", "#assign_param", "Arg-list-prime"],
        "epsilon" : []
    }
}

# save in json files
with open('./json/''first.json', 'w') as fp:
    json.dump(first, fp)
with open('./json/''follow.json', 'w') as fp:
    json.dump(follow, fp)
with open('./json/''diagrams.json', 'w') as fp:
    json.dump(diagrams, fp)
