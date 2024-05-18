'''
testing with a string

# Define the available numbers and the target string
numbers = [20, 21, 22, 23, 24]
target_string = "MASONCYSE"

# Initialize an empty list to store the formatted strings
formatted_strings = []

# Iterate through all numbers as the first number
for num1 in numbers:
    for i in range(len(target_string) + 1):
        formatted_string = target_string[:i] + str(num1) + target_string[i:]
        # Iterate through all numbers as the second number
        for num2 in numbers:
            for j in range(len(formatted_string) + 1):
                formatted_string_with_second_num = formatted_string[:j] + str(num2) + formatted_string[j:]
                formatted_strings.append(formatted_string_with_second_num)

# Print the list of formatted strings
for i, string in enumerate(formatted_strings, 1):
    print(f"Combination {i}: {string}")
'''
# Reading from the string variation base dict line by line.

# Define the available numbers
numbers = [20, 21, 22, 23, 24]

# Initialize an empty list to store the formatted strings
formatted_strings = []

# Open the file for reading
with open('cysegmu.txt', 'r') as file:
    for line in file:
        target_string = line.strip()

        # Iterate through all numbers as the first number
        for num1 in numbers:
            for i in range(len(target_string) + 1):
                formatted_string = target_string[:i] + str(num1) + target_string[i:]
                # Iterate through all numbers as the second number
                for num2 in numbers:
                    for j in range(len(formatted_string) + 1):
                        formatted_string_with_second_num = formatted_string[:j] + str(num2) + formatted_string[j:]
                        formatted_strings.append(formatted_string_with_second_num)

# Write the list of formatted strings to a .lst file
with open('cysegmu_output.lst', 'w') as output_file:
    for i, string in enumerate(formatted_strings, 1):
        output_file.write(f"{string}\n")

print("Output written to output.lst file.")
