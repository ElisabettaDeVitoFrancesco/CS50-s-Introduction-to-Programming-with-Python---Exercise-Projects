import sys

def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].split(".")[1] != "py":
        sys.exit("Not a Python file")
    else:
        py_file = sys.argv[1]
        count_lines(py_file)

def count_lines(py_file):
    nr_lines = 0
    #comment_lines = 0
    #empty_lines = 0
    #tot_lines = 0
    try:
        with open(py_file) as file:
            for line in file:
                #tot_lines += 1
                if line.lstrip().startswith("#"):
                    nr_lines += 0
                    #comment_lines += 1
                #elif '"""' in line:
                #    nr_lines += 0
                elif line.isspace():
                    nr_lines += 0
                    #empty_lines += 1
                else:
                    nr_lines += 1
    except FileNotFoundError:
            sys.exit("File does not exist")
    #print("Total lines: ", tot_lines)
    print(nr_lines)
    #print("Comment lines: ", (comment_lines)
    #print("Empty lines: ", (empty_lines)



if __name__ == "__main__":
    main()
