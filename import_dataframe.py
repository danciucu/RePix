import pandas as pd
import os

# function that loads the Excel file and organizes it
def field_notes(path):
    # import the Excel file
    notes = pd.read_excel(path)
    # remove extra columns
    notes.drop(columns = ['Unnamed: 7', 'Comments'], axis = 1, inplace = True)
    # remove the empty rows
    notes.dropna(subset=['US/DS', 'Photo'], inplace = True)

    return notes

# function that loads the pictures from a folder
def pictures(path):
    # create an empty array
    pictures_array = []
    # create a variable for loop count
    count = 0
    # import the photos in an array
    for images in os.listdir(path):
        # check the picture format
        if (images.endswith(".jpg") or images.endswith(".jpeg") or images.endswith(".JPG") or images.endswith(".JPEG")):
            # if the first picture from the folder
            if count == 0:
                # loop over the picture name and extract the characters that are not digits
                for i in range(len(images)):
                    if images[i].isdigit():
                        # add the string to the array
                        pictures_array.append(images[0:i])
                        break
            # add the string to the array
            pictures_array.append(images)
        # update the count
        count += 1 

    return pictures_array