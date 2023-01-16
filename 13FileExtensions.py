# Ask for file format as input
format = input("File name: ").strip().lower().split(".")[-1]

# If format within cerstina list, output as name/extensions
if format == "gif" or format == "jpeg" or format == "png":
    print("image/", format, sep = "")
elif format == "jpg":
    print("image/jpeg")
elif format == "pdf" or format == "zip":
    print("application/", format, sep = "")
elif format == "txt":
    print("text/plain", sep = "")
else:
    print("application/octet-stream")
