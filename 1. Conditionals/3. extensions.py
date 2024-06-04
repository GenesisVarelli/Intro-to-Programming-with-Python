#Outputs that file’s media type if the file’s name ends, case-insensitively
if '.gif' in extensions:
            print("image/gif")
elif '.jpg' in extensions:
            print("image/jpeg")
elif '.jpeg' in extensions:
            print("image/jpeg")
elif '.png' in extensions:
            print("image/png")
elif '.pdf' in extensions:
            print("application/pdf")
elif '.txt' in extensions:
            print("text/plain")
elif '.zip' in extensions:
            print("application/zip")

#Otherwise, output 'application/octet-stream'
else:
    print('application/octet-stream')