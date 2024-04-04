def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hi, here is line 1\n")
            file.write("12345\n")
            file.write("Line 3: Python File Handling\n")
    except PermissionError:
        print("Permission denied to create file.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("File creation process completed.")


def read_and_display_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Content of my_file.txt:")
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)


def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Additional line 1\n")
            file.write("Another line with numbers: 67890\n")
            file.write("Final line\n")
    except PermissionError:
        print("Permission denied to append to file.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("Appending to file completed.")


# Task 1: File Creation
create_file()

# Task 2: File Reading and Display
read_and_display_file()

# Task 3: File Appending
append_to_file()

# Task 4: Error Handling
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Error handling completed.")