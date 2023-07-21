import json



class DFA:
    def __init__(self):

        # load the DFA
        with open("./json/" + "NUM_DFA.json", "r") as f:
            self.NUM_DFA = json.load(f)

        with open("./json/" + "ID_DFA.json", "r") as f:
            self.ID_DFA = json.load(f)

        with open("./json/" + "SYMBOL_DFA.json", "r") as f:
            self.SYMBOL_DFA = json.load(f)

        with open("./json/" + "COMMENT_DFA.json", "r") as f:
            self.COMMENT_DFA = json.load(f)

        with open("./json/" + "WHITESPACE_DFA.json", "r") as f:
            self.WHITESPACE_DFA = json.load(f)

        # load alphabet
        with open("./json/" + "alphabet.json", "r") as f:
            self.alphabet = json.load(f)

        # initialize DFA states
        self.keywords = ["break", "else", "if", "int", "repeat", "return", "until", "void"]
        self.reset()

    def reset(self):
        self.NUM_DFA_state = "start"
        self.ID_DFA_state = "start"
        self.SYMBOL_DFA_state = "start"
        self.COMMENT_DFA_state = "start"
        self.WHITESPACE_DFA_state = "start"

        self.current_token = ""
        self.current_tokens = []

    def get_next_token(self, character):
        self.current_token = character
        token = ""
        token_type = ""
        repeat = False

        # check if character is in alphabet
        if not (self.COMMENT_DFA_state == "comment" or \
            self.COMMENT_DFA_state == "* recognized"):
            if ((character not in self.alphabet) and (character != "EOF")) \
                or (character == "/" and self.COMMENT_DFA_state != "start"\
                    and self.COMMENT_DFA_state != "/ recognized" \
                        and self.COMMENT_DFA_state != "* in start"\
                            and self.SYMBOL_DFA_state != "containing symbol ="):
                token_type = "error"
                token = "(" + "".join(self.current_tokens) \
                    + character + ", Invalid input)"
                repeat = False
                self.reset()
                return token_type , token , repeat

        # get next state for each DFA

        # NUM_DFA
        if self.NUM_DFA_state != "finished : is number" and self.NUM_DFA_state != "not_number" \
                and self.NUM_DFA_state != "error invalid number":

            current_NUM_DFA_state_dict = self.NUM_DFA[self.NUM_DFA_state]
            if character in current_NUM_DFA_state_dict:
                self.NUM_DFA_state = current_NUM_DFA_state_dict[character]
            else:
                if self.NUM_DFA_state == "start":
                    self.NUM_DFA_state = "not_number"
                elif self.NUM_DFA_state == "containing number":
                    self.NUM_DFA_state = "finished : is number"

        # ID_DFA
        if self.ID_DFA_state != "finished : is identifier" and self.ID_DFA_state != "not_identifier":
            current_ID_DFA_state_dict = self.ID_DFA[self.ID_DFA_state]
            if character in current_ID_DFA_state_dict:
                self.ID_DFA_state = current_ID_DFA_state_dict[character]
            else:
                if self.ID_DFA_state == "start":
                    self.ID_DFA_state = "not_identifier"
                elif self.ID_DFA_state == "containing letter":
                    self.ID_DFA_state = "finished : is identifier"

        # SYMBOL_DFA
        if self.SYMBOL_DFA_state != "symbol recognized" and self.SYMBOL_DFA_state != "not_symbol":
            current_SYMBOL_DFA_state_dict = self.SYMBOL_DFA[self.SYMBOL_DFA_state]
            if character in current_SYMBOL_DFA_state_dict:
                self.SYMBOL_DFA_state = current_SYMBOL_DFA_state_dict[character]
            else:
                if self.SYMBOL_DFA_state == "start":
                    self.SYMBOL_DFA_state = "not_symbol"
                elif self.SYMBOL_DFA_state == "containing symbol =":
                    self.SYMBOL_DFA_state = "symbol recognized"
                elif self.SYMBOL_DFA_state == "containing symbol *":
                    if character == "/" :
                        self.SYMBOL_DFA_state = "not_symbol"
                    else:
                        self.SYMBOL_DFA_state = "symbol recognized"



        # COMMENT_DFA
        if self.COMMENT_DFA_state != "comment finished" and self.COMMENT_DFA_state != "not_comment" \
                and self.COMMENT_DFA_state != "error unclosed comment" and self.COMMENT_DFA_state != "error unmatched":
            current_COMMENT_DFA_state_dict = self.COMMENT_DFA[self.COMMENT_DFA_state]
            if character in current_COMMENT_DFA_state_dict:
                self.COMMENT_DFA_state = current_COMMENT_DFA_state_dict[character]
            else:
                if self.COMMENT_DFA_state == "start":
                    self.COMMENT_DFA_state = "not_comment"
                elif self.COMMENT_DFA_state == "comment":
                    if character == "EOF":
                        self.COMMENT_DFA_state = "error unclosed comment"
                    else:
                        self.COMMENT_DFA_state = "comment"
                elif self.COMMENT_DFA_state == "* recognized":
                    if character == "*":
                        self.COMMENT_DFA_state = "* recognized"
                    else:
                        self.COMMENT_DFA_state = "comment"
                elif self.COMMENT_DFA_state == "/ recognized":
                    token_type = "error"
                    token = "(" + "".join(self.current_tokens) \
                        + ", Invalid input)"
                    repeat = True
                    self.reset()
                    return token_type , token , repeat
                   
        # WHITESPACE_DFA
        if self.WHITESPACE_DFA_state != "whitespace recognized" and self.WHITESPACE_DFA_state != "not_whitespace":
            current_WHITESPACE_DFA_state_dict = self.WHITESPACE_DFA[self.WHITESPACE_DFA_state]
            if character in current_WHITESPACE_DFA_state_dict:
                self.WHITESPACE_DFA_state = current_WHITESPACE_DFA_state_dict[character]
            else:
                if self.WHITESPACE_DFA_state == "start":
                    self.WHITESPACE_DFA_state = "not_whitespace"



        # check if any DFA is in final state
        if self.NUM_DFA_state == "finished : is number":
            token_type = "NUM"
            token = "".join(self.current_tokens)
            repeat = True
            self.reset()
            return token_type , token , repeat
        elif self.NUM_DFA_state == "error invalid number":
            token_type = "error"
            token = "(" + "".join(self.current_tokens) \
                + character + ", Invalid number)"
            repeat = False
            self.reset()
            return token_type , token , repeat
        elif self.ID_DFA_state == "finished : is identifier":
            token_type = "ID"
            token  = "".join(self.current_tokens)
            if token in self.keywords:
                token_type = "KEYWORD"
            repeat = True
            self.reset()
            return token_type , token , repeat

        elif self.COMMENT_DFA_state == "comment finished":
            token_type = "comment"
            token = ""
            repeat = False
            self.reset()
            return token_type , token , repeat
        elif self.COMMENT_DFA_state == "error unclosed comment":
            token_type = "error"
            token = "(" + ("".join(self.current_tokens))[0:7] + "..." \
                 + ", Unclosed comment)"
            repeat = False
            self.reset()
            return token_type , token , repeat
        elif self.COMMENT_DFA_state == "error unmatched":
            token_type = "error"
            token = "(" + ("".join(self.current_tokens)) + character \
                    + ", Unmatched comment)"
            repeat = False
            self.reset()
            return token_type , token , repeat
        elif self.SYMBOL_DFA_state == "symbol recognized":
            token_type = "SYMBOL"
            if len(self.current_tokens) != 0:
                if (self.current_tokens[-1] == "=" and character != "=") \
                    or (self.current_tokens[-1] == "*"):
                    token = "".join(self.current_tokens)
                    repeat = True
                    self.reset()
                    return token_type , token , repeat
        
            token = "".join(self.current_tokens) + character
            repeat = False
            self.reset()
            return token_type , token , repeat
        elif self.WHITESPACE_DFA_state == "whitespace recognized":
            token_type = "whitespace"
            token = ""
            repeat = False
            self.reset()
            return token_type , token , repeat
        else:
            self.current_tokens.append(character)
            token_type = "not recognized"
            token = ""
            repeat = False
            return token_type , token , repeat
