# importing Youtube from pytube
from pytube import Youtube

# asking user to enter link
link = input("Enter the link ")
# showing user that the process has started
print("Downloading...")
# main code to download video
Youtube(link).streams.first().download()
# showing user that the video has downloaded
print("Video downloaded sucessfully")
