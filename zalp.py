import argparse

class EsotericLanguageInterpreter:
    def __init__(self, code=None, filename=None):
        if filename:
            with open(filename, 'r') as file:
                self.code = file.read()
        else:
            self.code = code

        self.pointer = 0
        self.memory = [0] * 30000
        self.data_ptr = 0
        self.bracket_map = self.build_bracket_map()
        self.variables = {}

    def build_bracket_map(self):
        stack = []
        bracket_map = {}
        for i, cmd in enumerate(self.code):
            if cmd == '<':
                stack.append(i)
            elif cmd == '>':
                start = stack.pop()
                bracket_map[start] = i
                bracket_map[i] = start
        return bracket_map

    def interpret(self):
        while self.pointer < len(self.code):
            cmd = self.code[self.pointer]
            if cmd == 'z':
                self.data_ptr += 1
            elif cmd == 'm':
                self.data_ptr -= 1
            elif cmd == 'a':
                self.memory[self.data_ptr] += 1
            elif cmd == 'l':
                self.memory[self.data_ptr] -= 1
            elif cmd == 'p':
                print(chr(self.memory[self.data_ptr]), end='')
            elif cmd == 'q':
                self.data_ptr += 1
                self.memory[self.data_ptr - 1] *= self.memory[self.data_ptr]
                self.memory[self.data_ptr] = 0
                self.data_ptr -= 1
            elif cmd == 'w':
                self.data_ptr = 0
            elif cmd == 'e':
                self.memory[self.data_ptr] = 0
            elif cmd == 'v':
                self.variables[self.data_ptr] = self.memory[self.data_ptr]
            elif cmd == '<':
                if self.memory[self.data_ptr] == 0:
                    self.pointer = self.bracket_map[self.pointer]
            elif cmd == '>':
                if self.memory[self.data_ptr] != 0:
                    self.pointer = self.bracket_map[self.pointer]
            else:
                raise ValueError(f"Unknown command: {cmd}")
            self.pointer += 1

def main():
    parser = argparse.ArgumentParser(description="ZalpScript Interpreter")
    parser.add_argument('filename', type=str, help='Path to the ZalpScript file to interpret')
    
    args = parser.parse_args()

    interpreter = EsotericLanguageInterpreter(filename=args.filename)
    interpreter.interpret()

if __name__ == "__main__":
    main()
