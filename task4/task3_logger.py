class Logger:
    def __init__(self, filename="log.txt"):
        self.filename = filename
        self.file = open(filename, "w")
        print(f"Logger opened file: {filename}")

    def write(self, message):
        self.file.write(message + "\n")
        print(f"Written: {message}")

    def __del__(self):
        print(f"Closing file: {self.filename}")
        self.file.close()


log = Logger()
log.write("First log message")
log.write("Second log message")
log.write("Third log message")

print("\n--- Explicitly deleting Logger object ---")
del log

print("\n--- Reading file contents ---")
with open("log.txt", "r") as f:
    contents = f.read()
    print("File contents:")
    print(contents)