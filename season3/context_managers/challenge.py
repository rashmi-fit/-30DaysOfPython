class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file")
        if self.file:
            self.file.close()
        # Returning False lets any exceptions propagate
        return False


with FileManager('example.txt', 'r') as f:
    contents = f.read()
    print(contents)
