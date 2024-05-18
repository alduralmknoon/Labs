def generate_case_variations(input_string, index=0, current_variation=""):
    if index == len(input_string):
        print(current_variation)
        return

    char = input_string[index]

    # Generate variations with the current character in lowercase
    generate_case_variations(input_string, index + 1, current_variation + char.lower())

    # Generate variations with the current character in uppercase
    generate_case_variations(input_string, index + 1, current_variation + char.upper())

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    generate_case_variations(input_string)
#Aldur almaknoon salim Al rawas