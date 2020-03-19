from PIL import Image
import os
import shutil

defaults = ['default-0.png', 'default-1.png', 'default-2.png', 'default-3.png',
        'default-4.png', 'default-5.png', 'default-6.png', 'default-7.png',
        'default-8.png', 'default-9.png']

defaults2x = ['default-0@2x.png', 'default-1@2x.png', 'default-2@2x.png', 'default-3@2x.png', 'default-4@2x.png', 'default-5@2x.png', 'default-6@2x.png', 'default-7@2x.png', 'default-8@2x.png', 'default-9@2x.png']

count = 0

os.mkdir('old_circles')
blank = Image.new('RGBA', (1, 1, ), (0, 0, 0, 0))

twox = input("Are there @2x elements? y/n: ")
override = input("Would you like HitCircleOverlap to be fixed so circles don't glitch? y/n: ")

if override == 'y':
    shutil.copy('skin.ini', 'old_circles')
    with open("skin.ini", "r") as s:
        lines = s.readlines()
    for i, line in enumerate(lines):
        if 'HitCircleOverlap' in line:
            if twox == 'y':
                lines[i] = 'HitCircleOverlap: 256\n'
            else:
                lines[i] = 'HitCircleOverlap: 128\n'
            with open ("skin.ini", "w") as s:
                s.writelines(lines)
else:
    pass

if twox == 'y':

    for default in defaults2x:
        default = Image.open(default, 'r')
        default_w, default_h = default.size

        resizer = Image.new('RGBA', (256, 256), (255, 255, 255, 0))
        re_w, re_h = resizer.size

        offset = ((re_w - default_w) // 2, (re_h - default_h) // 2)

        resizer.paste(default, offset)
        dimw, dimh = resizer.size

        hs = Image.open('hitcircle@2x.png', 'r')
        hso = Image.open('hitcircleoverlay@2x.png', 'r')

        hsoffset = ((dimw - re_w) // 2, (re_h - dimw) // 2)
        resizer.paste(hs, hsoffset, hs)

        dimw2, dimh2 = resizer.size
        hsooffset = ((dimw2 - dimw) // 2, (dimh2 - dimh) // 2)

        resizer.paste(hso, hsooffset, hso)

        shutil.move('default-' + str(count) + '@2x.png', './old_circles')
        fname = ('default-' + str(count) + '@2x.png')
        count += 1
        resizer.save(fname)
        print('Saved as', fname)

    shutil.move('hitcircle@2x.png', './old_circles')
    shutil.move('hitcircleoverlay@2x.png', './old_circles')
    blank.save('hitcircle@2x.png')
    blank.save('hitcircleoverlay@2x.png')
else:
    for default in defaults:
        default = Image.open(default, 'r')
        default = default.resize((128, 128), Image.ANTIALIAS)
        default_w, default_h = default.size

        resizer = Image.new('RGBA', (178, 178), (255, 255, 255, 0))
        re_w, re_h = resizer.size

        offset = ((re_w - default_w) // 2, (re_h - default_h) // 2)

        resizer.paste(default, offset)
        dimw, dimh = resizer.size

        hs = Image.open('hitcircle.png', 'r')
        hs = hs.resize((178, 178), Image.ANTIALIAS)
        hso = Image.open('hitcircleoverlay.png', 'r')
        hso = hso.resize((178, 178), Image.ANTIALIAS)

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
