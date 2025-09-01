def main():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, "r") as file:
            text = file.read()

        modified_text = text.upper()

        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_text)

        print(f"Modified file has been saved as '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
