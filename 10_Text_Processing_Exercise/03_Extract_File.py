file_path = input().split("\\")
file_name = file_path[-1]
filename, fileextension = str(file_name).split(".")
print(f"File name: {filename}")
print(f"File extension: {fileextension}")


