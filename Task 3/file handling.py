try:
    with open("input.txt", "r") as file:
        content = file.read()
    old_word = input("Enter the word to replace: ")
    new_word = input("Enter the new word: ")
    modified_content = content.replace(old_word, new_word)
    with open("input.txt", "w") as file:
        file.write(modified_content)
    print("File updated successfully.")
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)
