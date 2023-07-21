import scanner
import Parser
for i in range(1,11):
    num_path = str(i)
    path = "./Fixed_TestCases_3/TestCases/S" + num_path + "/"
    test_scanner = scanner.Scanner(path,"input.txt")
    test_parser = Parser.Parser(test_scanner)
    test_parser.parse()
