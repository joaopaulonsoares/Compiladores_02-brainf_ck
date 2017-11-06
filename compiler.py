import argparse
# from getch import getche

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Brainfuck filename")
parser.add_argument("-o", help="Filename to be generated")

args = parser.parse_args()

INPUT_FILENAME = args.filename
OUTPUT_FILENAME = args.o

# Dictonary from brainfuck commands to c
# bf_to_c_dict = {
#     '+': '\t++(*ptr);\n',
#     '-': '\t--(*ptr);\n',
#     '>': '\t++ptr;\n',
#     '<': '\t--ptr;\n',
#     '.': '\tprintf("%c",(*ptr));\n',
#     ',': '\t*ptr = getchar();\ngetchar();\n',
#     '[': '\twhile(*ptr) {\n',
#     ']': '\t}\n'
# }


def bf_to_c_dict(char):
    text = ""
    print(char)
    if(char == '+'):
        text = '\t\t++(*ptr);\n'
    elif(char == "-"):
        text = '\t\t--(*ptr);\n'
    elif(char == ">"):
        text = '\t\t++ptr;\n'
    elif(char == "<"):
        text = '\t\t--ptr;\n'
    elif(char == '.'):
        text = '\t\tprintf("%c",(*ptr));\n'
    elif(char == ','):
        text = '\t\t*ptr = getchar();\ngetchar();\n'
    elif(char == '['):
        text = '\t\twhile(*ptr) {\n'
    elif(char == ']'):
        text = '\t\t}\n'

    return text


def main():
    arquivo_bf_input = open(INPUT_FILENAME, 'r')
    arquivo_c_exit = open(OUTPUT_FILENAME, 'w')

    print("=========")
    print(OUTPUT_FILENAME)

    # inicializar arquivo de saída
    program_code = ("#include <stdio.h>\n#include <stdlib.h>\n int main(){"
                    "\n\tunsigned char *memory = malloc(sizeof(char)*30000);\n"
                    "\n\tunsigned char *ptr =  &memory[0];\n\n"
                    )

    for line in arquivo_bf_input:
        for c in line:
            # print(c)
            program_code += bf_to_c_dict(c)

    # program_code += "\n    return 0;\n}"
    print("=============================")
    print(program_code)
    arquivo_c_exit.write(program_code)
    arquivo_c_exit.write("\n}\n")
    arquivo_bf_input.close()
    arquivo_c_exit.close()


main()
