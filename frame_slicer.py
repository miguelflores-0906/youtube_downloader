from PIL import Image
import os
import sys

# Change this to the directory of the frames that need slicing
PATH = "D:\Documents\DLSU\Year 4 Term 1\Immersion CV\youtube_downloader\Olongapo City CCTV Live Stream_frames"

# def listdir(dir):
#     filenames = os.listdir(dir)
#     for files in filenames:
#         print(type(files))
#         print(files)

def four_slice(actual_img, PATH, image_name):
    try:
        os.mkdir(PATH + "\\top_left\\")
        os.mkdir(PATH + "\\top_right\\")
        os.mkdir(PATH + "\\bot_left\\")
        os.mkdir(PATH + "\\bot_right\\")
    except OSError:
        print ("Directory already created")
        pass

    for i in range(4):
        # get the height and width of the image
        width, height = actual_img.size
        if i == 0:
            # crop the image to the top left
            cropped_img = actual_img.crop((0, 0, width/2, height/2))
            # save cropped image
            cropped_img.save(PATH + "\\top_left\\" + "top_left_" + image_name[:-4] + ".jpg")
        elif i == 1:
            # crop the image to the top right
            cropped_img = actual_img.crop((width/2, 0, width, height/2))
            cropped_img.save(PATH + "\\top_right\\" + "top_right_" + image_name[:-4] + ".jpg")
        elif i == 2:
            # crop the image to the bottom left
            cropped_img = actual_img.crop((0, height/2, width/2, height))
            cropped_img.save(PATH + "\\bot_left\\" + "bot_left_" + image_name[:-4] + ".jpg")
        elif i == 3:
            # crop the image to the bottom right
            cropped_img = actual_img.crop((width/2, height/2, width, height))
            cropped_img.save(PATH + "\\bot_right\\" + "bot_right_" + image_name[:-4] + ".jpg")

def nine_slice(actual_img, PATH, image_name):
    try:
        os.mkdir(PATH + "\\top_left\\")
        os.mkdir(PATH + "\\top_mid\\")
        os.mkdir(PATH + "\\top_right\\")
        os.mkdir(PATH + "\\mid_left\\")
        os.mkdir(PATH + "\\mid_mid\\")
        os.mkdir(PATH + "\\mid_right\\")
        os.mkdir(PATH + "\\bot_left\\")
        os.mkdir(PATH + "\\bot_mid\\")
        os.mkdir(PATH + "\\bot_right\\")
    except OSError:
        print ("Directory already created")
        pass

    for i in range(9):
        # get the height and width of the image
        width, height = actual_img.size
        if i == 0:
            # crop the image to the top left
            cropped_img = actual_img.crop((0, 0, width/3, height/3))
            # save cropped image
            cropped_img.save(PATH + "\\top_left\\" + "top_left_" + image_name[:-4] + ".jpg")
        elif i == 1:
            # crop the image to the top mid
            cropped_img = actual_img.crop((width/3, 0, width/3*2, height/3))
            cropped_img.save(PATH + "\\top_mid\\" + "top_mid_" + image_name[:-4] + ".jpg")
        elif i == 2:
            # crop the image to the top right
            cropped_img = actual_img.crop((width/3*2, 0, width, height/3))
            cropped_img.save(PATH + "\\top_right\\" + "top_right_" + image_name[:-4] + ".jpg")
        elif i == 3:
            # crop the image to the mid left
            cropped_img = actual_img.crop((0, height/3, width/3, height/3*2))
            cropped_img.save(PATH + "\\mid_left\\" + "mid_left_" + image_name[:-4] + ".jpg")
        elif i == 4:
            # crop the image to the mid mid
            cropped_img = actual_img.crop((width/3, height/3, width/3*2, height/3*2))
            cropped_img.save(PATH + "\\mid_mid\\" + "mid_mid_" + image_name[:-4] + ".jpg")
        elif i == 5:
            # crop the image to the mid right
            cropped_img = actual_img.crop((width/3*2, height/3, width, height/3*2))
            cropped_img.save(PATH + "\\mid_right\\" + "mid_right_" + image_name[:-4] + ".jpg")
        elif i == 6:
            # crop the image to the bot left
            cropped_img = actual_img.crop((0, height/3*2, width/3, height))
            cropped_img.save(PATH + "\\bot_left\\" + "bot_left_" + image_name[:-4] + ".jpg")
        elif i == 7:
            # crop the image to the bot mid
            cropped_img = actual_img.crop((width/3, height/3*2, width/3*2, height))
            cropped_img.save(PATH + "\\bot_mid\\" + "bot_mid_" + image_name[:-4] + ".jpg")
        elif i == 8:
            # crop the image to the bot right
            cropped_img = actual_img.crop((width/3*2, height/3*2, width, height))
            cropped_img.save(PATH + "\\bot_right\\" + "bot_right_" + image_name[:-4] + ".jpg")

images = os.listdir(PATH)

num_cam = sys.argv[1]

actual_img = Image.open(PATH + "\\" + images[0])
nine_slice(actual_img, PATH, images[0])
actual_img.close()

for image in images:
    actual_img = Image.open(PATH + "\\" + image)
    if num_cam == "4":
        four_slice(actual_img, PATH, image)
    elif num_cam == "9":
        nine_slice(actual_img, PATH, image)
    actual_img.close()
