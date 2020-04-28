# Imports the required modules
from PIL import Image, ImageOps
import os
import shutil

defaults = ['default-0.png', 'default-1.png', 'default-2.png', 'default-3.png',
        'default-4.png', 'default-5.png', 'default-6.png', 'default-7.png',
        'default-8.png', 'default-9.png']

defaults2x = ['default-0@2x.png', 'default-1@2x.png', 'default-2@2x.png', 'default-3@2x.png', 'default-4@2x.png', 'default-5@2x.png', 'default-6@2x.png', 'default-7@2x.png', 'default-8@2x.png', 'default-9@2x.png']

count = 0

os.mkdir('old_circles')

blank = Image.new('RGBA', (1, 1), (0, 0, 0, 0))

twox = input("Are you using @2x files? (requires ALL @2x files to be present) y/n: ")

try:
    shutil.copy('skin.ini', 'old_circles')
    with open("skin.ini", "r") as s:
        lines = s.readlines()
        for i, line in enumerate(lines):
            if 'HitCircleOverlap' in line:
                if twox == 'y':
                    lines[i] = 'HitCircleOverlap:300\n'
                else:
                    lines[i] = 'HitCircleOverlap:160\n'
                with open ("skin.ini", "w") as s:
                    s.writelines(lines)
except:
    shutil.copy('Skin.ini', 'old_circles')
    with open("Skin.ini", "r") as s:
        lines = s.readlines()
        for i, line in enumerate(lines):
            if 'HitCircleOverlap' in line:
                if twox == 'y':
                    lines[i] = 'HitCircleOverlap:300\n'
                else:
                    lines[i] = 'HitCircleOverlap:160\n'
                with open ("Skin.ini", "w") as s:
                    s.writelines(lines)

hcc = input("Enter a hex value (white is #FFFFFF): ")
hcc2 = input("Enter a hex value (white is #FFFFFF): ")

if twox == "y":

    for default in defaults:
        resizer = Image.new('RGBA', (300, 300), (255, 255, 255, 0))
        re_w, re_h = resizer.size

        dimw, dimh = resizer.size

        hs = Image.open('hitcircle@2x.png', 'r')#.convert("L")
        hs = hs.resize((300, 300), Image.ANTIALIAS)

        hsnc = Image.open('hitcircle@2x.png', 'r')#.convert("L")
        hsnc = hs.resize((300, 300), Image.ANTIALIAS)

        alpha = hs.getchannel('A')

        greyscale = ImageOps.grayscale(hs)
        if count % 2 == 0:
            hs = ImageOps.colorize(greyscale, (0,0,0,0), hcc)
        else:
            hs = ImageOps.colorize(greyscale, (0,0,0,0), hcc2)
        hs.putalpha(alpha)

        hso = Image.open('hitcircleoverlay@2x.png', 'r')
        hso = hso.resize((300, 300), Image.ANTIALIAS)

        hsoffset = ((dimw - re_w) // 2, (re_h - dimw) // 2)
        resizer.paste(hs, hsoffset, hsnc)

        dimw2, dimh2 = resizer.size
        hsooffset = ((dimw2 - dimw) // 2, (dimh2 - dimh) // 2)

        resizer.paste(hso, hsooffset, hso)

        default = Image.open(default, 'r')
        default_w, default_h = default.size

        offset = ((re_w - default_w) // 2, (re_h - default_h) // 2)

        resizerr = Image.new('RGBA', (300, 300), (255, 255, 255, 0))
        resizerr.paste(default, offset)

        resizerr.convert('RGBA')
        resizer.convert('RGBA')
        colourized = Image.new('RGBA', resizer.size)
        colourized = Image.alpha_composite(resizerr, resizer)

        shutil.move('default-' + str(count) + '@2x.png', './old_circles')
        fname = ('default-' + str(count) + '@2x.png')
        count += 1
        colourized.save(fname)
        print('Saved as', fname)
        
        
        shutil.move('hitcircle@2x.png', './old_circles')
        shutil.move('hitcircleoverlay@2x.png', './old_circles')
        blank.save('hitcircle@2x.png')
        blank.save('hitcircleoverlay@2x.png')

if twox == "n":

    for default in defaults:
        resizer = Image.new('RGBA', (160, 160), (255, 255, 255, 0))
        re_w, re_h = resizer.size

        dimw, dimh = resizer.size

        hs = Image.open('hitcircle.png', 'r')
        hs = hs.resize((160, 160), Image.ANTIALIAS)

        hsnc = Image.open('hitcircle.png', 'r')
        hsnc = hs.resize((160, 160), Image.ANTIALIAS)

        alpha = hs.getchannel('A')

        greyscale = ImageOps.grayscale(hs)
        if count % 2 == 0:
            hs = ImageOps.colorize(greyscale, (0,0,0,0), hcc)
        else:
            hs = ImageOps.colorize(greyscale, (0,0,0,0), hcc2)
        hs.putalpha(alpha)

        hso = Image.open('hitcircleoverlay.png', 'r')
        hso = hso.resize((160, 160), Image.ANTIALIAS)

        hsoffset = ((dimw - re_w) // 2, (re_h - dimw) // 2)
        resizer.paste(hs, hsoffset, hsnc)

        dimw2, dimh2 = resizer.size
        hsooffset = ((dimw2 - dimw) // 2, (dimh2 - dimh) // 2)

        resizer.paste(hso, hsooffset, hso)

        default = Image.open(default, 'r')
        default_w, default_h = default.size

        offset = ((re_w - default_w) // 2, (re_h - default_h) // 2)

        resizerr = Image.new('RGBA', (160, 160), (255, 255, 255, 0))
        resizerr.paste(default, offset)

        resizerr.convert('RGBA')
        resizer.convert('RGBA')
        colourized = Image.new('RGBA', resizer.size)
        colourized = Image.alpha_composite(resizerr, resizer)

        shutil.move('default-' + str(count) + '.png', './old_circles')
        fname = ('default-' + str(count) + '.png')
        count += 1
        colourized.save(fname)
        print('Saved as', fname)

        shutil.move('hitcircle.png', './old_circles')
        shutil.move('hitcircleoverlay.png', './old_circles')
        blank.save('hitcircle.png')
        blank.save('hitcircleoverlay.png')
