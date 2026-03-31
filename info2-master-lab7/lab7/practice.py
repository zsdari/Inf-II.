

def file_line_parser(filename:str, parser, user: list, password: list):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file.readlines():
            parser(line.strip(), user, password)

def line_parser(line:str, user: list,password: list):
    tokens = line.split(" ")
    if len(tokens)>=2:
        user.append(tokens[0])
        password.append(tokens[1])

if __name__ == "__main__":
    user = []
    password = []
    file_line_parser("words.txt", line_parser,user,password)
    print(password)