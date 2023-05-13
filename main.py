## load database from excel
# import pandas
# import excel file
# organize the data structure
## rename the pictures 
# create an array with all the names of the pictures in the folder
# create a binary tree with the sorted name of the picture asceding
# search in the binary tree the pictures there are in the database
# rename the pictures

import import_dataframe
import os

class RePix():
    def __init__(self):
        super().__init__

        # get the folder paths from user
        self.notes_path = r'C:\Computer Science Projects\RePix\PN\PHOTO LOG.xlsx'
        self.photos_path = r'C:\Users\dan.ciucu\OneDrive - AECOM\Documents\Projects\Computer Science Projects\RePix (photo renamer)\Outboard Gusset'
        # import database from excel
        self.notes = import_dataframe.field_notes(self.notes_path)
        
        # import all pictures in an array
        self.pictures = import_dataframe.pictures(self.photos_path)
        
        # rename pictures
        old_picname = ''
        new_picname = ''
        for i in range(len(self.notes['Photo'])):
            old_picname = 'DJI_' + '0' * (4 - len(str(self.notes['Photo'].iloc[i]))) + str(self.notes['Photo'].iloc[i]) + '.JPG'
            new_picname = self.notes['Node'].iloc[i] + ' ' + self.notes['US/DS'].iloc[i] + ' OB' + '-' + old_picname
            print(old_picname)
            print(new_picname)
            try:
                os.rename(os.path.join(self.photos_path + '/' + old_picname), os.path.join(self.photos_path + '/' + new_picname))
            except:
                continue



if __name__ == "__main__":
    app = RePix()
