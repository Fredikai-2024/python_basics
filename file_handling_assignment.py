# file_handling_assignment.py

def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is line 1.\n")
            file.write("The answer is 42.\n")
            file.write("Python file handling is fun!\n")
        print("File 'my_file.txt' created successfully.")
    except PermissionError:
        print("Error: Permission denied. Unable to create the file.")
    except Exception as e:
        print(f"An unexpected error occurred while creating the file: {e}")

def read_and_display_file():
    try:
        with open("my_file.txt", 'r') as file:
            contents = file.read()
            print("\nContents of 'my_file.txt':")
            print(contents)
    except FileNotFoundError:
        print("Error: 'my_file.txt' not found.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("This line is appended.\n")
            file.write("Another appended line with number 123.\n")
            file.write("Last appended line.\n")
        print("\nThree lines appended to 'my_file.txt' successfully.")
    except PermissionError:
        print("Error: Permission denied. Unable to append to the file.")
    except Exception as e:
        print(f"An unexpected error occurred while appending to the file: {e}")

def main():
    create_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()

if __name__ == "_main_":
    main()