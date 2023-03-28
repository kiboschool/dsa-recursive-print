class Print:

    def recursive_print(self, f):
        line = f.readline()
        if line == "":
            return
        print(line.replace('\n', ''))
        self.recursive_print(f)

    def print_file(self, filename):
        f = open(filename)
        self.recursive_print(f)
        f.close()

    def recursive_print_reverse(self, f):
        line = f.readline()
        if line == "":
            return
        self.recursive_print_reverse(f)
        print(line.replace('\n', ''))

    def print_file_reverse(self, filename):
        f = open(filename)
        self.recursive_print_reverse(f)
        f.close()

if __name__ == "__main__":
    p = Print()
    print("Printing file:\n==============")
    p.print_file("examples/sample.txt")
    print()

    print("Printing file in reverse:\n=========================")
    p.print_file_reverse("examples/sample.txt")
    print()
