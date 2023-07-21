# Amir Hosein Rahmati 99103922 
# Saba Shamekhi 99170489

import DFA 


class Scanner:
    def __init__(self, path = "./" ,file_name = "input.txt"):
        self.path = path
        self.file_name = file_name
        self.DFA = DFA.DFA()
        self.tokens = []
        self.errors = []
        self.line_number = 1
        self.first_token_line = 1
        self.file = None
        self.open_file()
        self.character = self.read_file()

    def get_line_number(self):
        return self.line_number

    
    def open_file(self):
        self.file = open(self.path + self.file_name, "r")
    
    def read_file(self):
        character = self.file.read(1)
        if character == "":
            character = "EOF" 
            self.file.close()
        return character

    def get_next_token(self):
        if len(self.DFA.current_tokens) == 0 :
            self.first_token_line = self.line_number

        token_type, token, repeat = self.DFA.get_next_token(self.character)

        if self.character == "\n" and not repeat:
            self.line_number += 1
    

        if self.character == "EOF":
            if token_type == "not recognized":
                return "$" , "$"
            if token_type == "error":
                self.errors.append((self.first_token_line, token))
                return "$" , "$"
        
        else:
            if not repeat :
                self.character = self.read_file()
            if token_type == "error":
                self.errors.append((self.first_token_line, token))
                return self.get_next_token()
            if token_type == "not recognized":
                return self.get_next_token()
        return token_type, token

    def temporary_while(self):
        while(True):
            token_type, token = self.get_next_token()
            if token_type == "$":
                break
            if token_type == "comment" or token_type == "whitespace" :
                continue
            self.tokens.append((self.line_number, token_type, token))
 # ab 

    def write_tokens(self):
        pre_line_number = 0
        with open(self.path +"tokens.txt", "w") as f:
            for token in self.tokens:
                if token[0] != pre_line_number:
                    if token[0] == self.tokens[0][0]:
                        f.write(str(token[0]) + ".	(" + token[1] + ", " \
                            + token[2] + ") ")
                    else:
                        f.write("\n" + str(token[0]) + ".	(" + token[1] + ", " \
                            + token[2] + ") ")
                    pre_line_number = token[0]
                else:
                    f.write("(" + token[1] + ", " + token[2] + ") ")

    def write_errors(self):
        pre_line_number = 0
        with open(self.path +"lexical_errors.txt", "w") as f:
            for error in self.errors:
                if error[0] != pre_line_number:
                    if error[0] == self.errors[0][0]:
                        f.write(str(error[0]) + ".	" + error[1] + " ")
                    else:
                        f.write("\n" + str(error[0]) + ".	" + error[1] + " ")
                    pre_line_number = error[0]
                else:
                    f.write(error[1] + " ")
            if len(self.errors) == 0:
                f.write("There is no lexical error.")


    def write_symbol_table(self):
        line = 1
        with open(self.path + "symbol_table.txt", "w") as f:
            for keywords in self.DFA.keywords :
                if line == 1:
                    f.write(str(line) + ".	" + keywords)
                    line += 1
                else:
                    f.write("\n" + str(line) + ".	" + keywords)
                    line += 1
            submitted_IDs = []
            for token in self.tokens:
                if token[1] == "ID" and (token[2] not in submitted_IDs) :
                    submitted_IDs.append(token[2])
                    f.write("\n" + str(line) + ".	" + token[2])
                    line += 1




    

                


    