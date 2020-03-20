# Imports the required modules
from PIL import Image
import os
import shutil

# Sets the names for the hitcircle numbers
defaults = ['default-0.png', 'default-1.png', 'default-2.png', 'default-3.png',
        'default-4.png', 'default-5.png', 'default-6.png', 'default-7.png',
        'default-8.png', 'default-9.png']
# @2x version of the hitcircle numbers
defaults2x = ['default-0@2x.png', 'default-1@2x.png', 'default-2@2x.png', 'default-3@2x.png', 'default-4@2x.png', 'default-5@2x.png', 'default-6@2x.png', 'default-7@2x.png', 'default-8@2x.png', 'default-9@2x.png']

# Just used for file naming
count = 0

# Creates the folder for the original elements
os.mkdir('old_circles')

# Creates a blank .png for the hitcircle/hitcircleoverlay
blank = Image.new('RGBA', (1, 1, ), (0, 0, 0, 0))

# Asks the user the two questions
twox = input("Are there @2x elements? y/n: ")
override = input("Would you like HitCircleOverlap to be fixed so circles don't glitch? y/n: ")

# Checks the answer for the HitCircleOverlap question
if override == 'y':
    # Copies the skin.ini to the original files' folder
    shutil.copy('skin.ini', 'old_circles')
    # Opens the skin.ini file and reads it all
    with open("skin.ini", "r") as s:
        lines = s.readlines()
    # Checks each line for the term "HitCircleOverlap"
    for i, line in enumerate(lines):
        if 'HitCircleOverlap' in line:
            # @2x replacement
            if twox == 'y':
                lines[i] = 'HitCircleOverlap: 300\n'
            # Standard res replacement
            else:
                lines[i] = 'HitCircleOverlap: 160\n'
            # Reopens skinlini as write-able
            with open ("skin.ini", "w") as s:
                s.writelines(lines)
# HitCircleOverlap question returns anything besides 'y'
else:
    pass

# @2x version. SD version will be the same, but with different resolutions
if twox == 'y':

    # Loop so all of the defaults are changed
    for default in defaults2x:
        # Opens the default image (changes +1 per loop)
        default = Image.open(default, 'r')
        # Gets dimensions of the default
        default_w, default_h = default.size

        # Creates the image that centers the default for the hitcircle
        resizer = Image.new('RGBA', (300, 300), (255, 255, 255, 0))
        # Gets the dimensions of the resizer
        re_w, re_h = resizer.size

        # Creates the location for the centering
        offset = ((re_w - default_w) // 2, (re_h - default_h) // 2)

        # Pastes the default over the resize at the position of the offset
        resizer.paste(default, offset)
        # Gets new dimensions
        dimw, dimh = resizer.size

        # Opens hitcircle and hitcircleoverlay
        hs = Image.open('hitcircle@2x.png', 'r')
        hso = Image.open('hitcircleoverlay@2x.png', 'r')

        # Creates location for the offset to the hitcircle
        hsoffset = ((dimw - re_w) // 2, (re_h - dimw) // 2)
        # Pastes the hitcircle to the resizer image (The one with the default)
        resizer.paste(hs, hsoffset, hs)

        # Gets new new dimensions
        dimw2, dimh2 = resizer.size
        # Creates location for the offset to the hitcircleoverlay
        hsooffset = ((dimw2 - dimw) // 2, (dimh2 - dimh) // 2)

        # Pastes the hitcircleoverlay onto the resizer
        resizer.paste(hso, hsooffset, hso)

        # Moves the original default
        shutil.move('default-' + str(count) + '@2x.png', './old_circles')
        # Sets the name for the new file
        fname = ('default-' + str(count) + '@2x.png')
        # Prepares for the next loop
        count += 1
        # Saves the new file as the preconfigured fname
        resizer.save(fname)
        # Outputs
        print('Saved as', fname)

    # Moves the original hitcircle and hitcircleoverlay
    shutil.move('hitcircle@2x.png', './old_circles')
    shutil.move('hitcircleoverlay@2x.png', './old_circles')
    # Creates new hitcircle and hitcircleoverlay as 1x1 blank png files
    blank.save('hitcircle@2x.png')
    blank.save('hitcircleoverlay@2x.png')

else:
    for default in defaults:
        default = Image.open(default, 'r')
        default_w, default_h = default.size

        resizer = Image.new('RGBA', (160, 160), (255, 255, 255, 0))
        re_w, re_h = resizer.size

        offset = ((re_w - default_w) // 2, (re_h - default_h) // 2)

        resizer.paste(default, offset)
        dimw, dimh = resizer.size

        hs = Image.open('hitcircle.png', 'r')
        hs = hs.resize((160, 160), Image.ANTIALIAS)
        hso = Image.open('hitcircleoverlay.png', 'r')
        hso = hso.resize((160, 160), Image.ANTIALIAS)

        hsoffset = ((dimw - re_w) // 2, (re_h - dimw) // 2)
        resizer.paste(hs, hsoffset, hs)

        dimw2, dimh2 = resizer.size
        hsooffset = ((dimw2 - dimw) // 2, (dimh2 - dimh) // 2)

        resizer.paste(hso, hsooffset, hso)

        shutil.move('default-' + str(count) + '.png', './old_circles')
        fname = ('default-' + str(count) + '.png')
        count += 1
        resizer.save(fname)
        print('Saved as', fname)

    shutil.move('hitcircle.png', './old_circles')
    shutil.move('hitcircleoverlay.png', './old_circles')
    blank.save('hitcircle.png')
    blank.save('hitcircleoverlay.png')
