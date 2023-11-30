import sys

from file_handler import TxtFileHandler, PickleFileHandler, FileHandler

input_file = sys.argv[1]
output_file = sys.argv[2]
console_arguments = sys.argv

if input_file.endswith(".txt"):
    input_file_handler = TxtFileHandler(console_arguments)
elif input_file.endswith(".pkl"):
    input_file_handler = PickleFileHandler(console_arguments)
else:
    input_file_handler = FileHandler(console_arguments)

if output_file.endswith(".txt"):
    output_file_handler = TxtFileHandler(console_arguments)
elif output_file.endswith(".pkl"):
    output_file_handler = PickleFileHandler(console_arguments)
else:
    output_file_handler = FileHandler(console_arguments)

input_file_handler.read_data_from_file()
input_file_handler.change_data_accordingly_to_changes()
print(input_file_handler.data)
print(output_file_handler.data)
output_file_handler.data = input_file_handler.data
output_file_handler.write_data_to_file()
