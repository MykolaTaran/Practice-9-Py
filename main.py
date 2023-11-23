def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write("This is a sample text.\n")
            file.write("Words are separated by spaces and punctuation marks!\n")
            file.write("The quick brown fox jumps over the lazy dog.\n")
            file.write("Python programming is fun and powerful.\n")
            file.write("Artificial Intelligence is changing the world.\n")
        print(f"File '{file_name}' created successfully.")
    except IOError:
        print(f"Error creating file '{file_name}'.")


def find_and_write_words(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            words = content.split()

            # Find words with the longest length containing the letter 'a'
            filtered_words = [word for word in words if 'a' in word]
            if not filtered_words:
                with open(output_file, 'w') as output_file:
                    output_file.write("No words with the letter 'a' found.")
            else:
                max_length = max(len(word) for word in filtered_words)
                longest_words = [word for word in filtered_words if len(word) == max_length]
                with open(output_file, 'w') as output_file:
                    for word in longest_words:
                        output_file.write(word + '\n')
        print(f"Words written to '{output_file}' successfully.")
    except IOError:
        print(f"Error reading or writing files: {input_file}, {output_file}")


def read_and_print_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except IOError:
        print(f"Error reading file '{file_name}'.")


if __name__ == "__main__":
    input_file_name = "TF22_1.txt"
    output_file_name = "TF22_2.txt"

    # a) Create the text file
    create_file(input_file_name)

    # b) Find and write words to TF22_2
    find_and_write_words(input_file_name, output_file_name)

    # c) Read and print TF22_2
    read_and_print_file(output_file_name)