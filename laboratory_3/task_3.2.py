def write_array(array, file_name):
    print(*array, file=file_name, sep='\n')
    pass

a=['asdad', '1231232131', 'asdad12312313123112321313213123', 'a2']
with open("text.txt", "w") as file:
    write_array(a, file)