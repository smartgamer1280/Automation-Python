from pytube import YouTube
import qrcode
import pafy


print("\nChoose From the Below list:\n")
print("----------------------------------")
print("1 for Youtube video download\n")
print("2 for making a qrcode for a given link\n")
print("3 for Youtube video information\n")
print("4 for downloading audio of youtube video\n")
print("5 For downloading video in highest quality\n")
print("-----------------------------------")


user_input =int(input("Enter choice:\n"))


if user_input==1:
    try:

        print("This will downlad video in the lowest quality 144p")
        _url = input("Enter url of video:\n")


        video = YouTube(_url)

        video.streams.first()
    except:
        print("Please enter valid url")

elif user_input==2:

    try:

        goto_link = input("Enter the url for which qrcode to be made")


        image = qrcode.make(goto_link).save("image.png")
    except:

        print("Please try again")
elif user_input==3:
    try:

        url_name = input("Enter url of video: ")
        v= pafy.new(url_name)

        print("Title of Video is : ",v.title)
        print("Likes on video are: ",v.likes)
        min = v.length
        print("Length of video is",min/60,"minutes")

    except:

        print("Enter valid data")

elif user_input==4:
    try:

        name_video = input("Enter URL of video: ")
        vid = pafy.new(name_video)

        bestaudio = vid.getbestaudio()
        bestaudio.download()

    except:

        print("Enter valid data")

elif user_input==5:

    try:

        url_of_video = input("Enter url of video: ")

        video = pafy.new(url_of_video)

        streams = video.streams
        for i in streams:
        	print(i)
	
        best = video.getbest()


        print(best.resolution, best.extension)

        best.download()

    except:

        print("Enter valid URL and try again")
else:

    print("Choose options from the list only !")