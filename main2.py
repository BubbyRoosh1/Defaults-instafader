from PIL import Image

defaults = ['default-0.png', 'default-1.png', 'default-2.png', 'default-3.png',
        'default-4.png', 'default-5.png', 'default-6.png', 'default-7.png',
        'default-8.png', 'default-9.png']

defaults2x = ['default-0@2x.png', 'default-1@2x.png', 'default-2@2x.png', 'default-3@2x.png', 'default-4@2x.png', 'default-5@2x.png', 'default-6@2x.png', 'default-7@2x.png', 'default-8@2x.png', 'default-9@2x.png']

count = 0

twox = input("Would you like to create @2x files? y/n (Requires @2x defaults and @2x hitcircle/hitcircleoverlay)")

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

        fname = ('def' + str(count) + '@2x.png')
        count += 1
        resizer.save(fname)
        print('Saved as', fname)
else:
    for default in defaults:
        default = Image.open(default, 'r')
        default_w, default_h = default.size

        resizer = Image.new('RGBA', (128, 128), (255, 255, 255, 0))
        re_w, re_h = resizer.size

        offset = ((re_w - default_w) // 2, (re_h - default_h) // 2)

        resizer.paste(default, offset)
        dimw, dimh = resizer.size

        hs = Image.open('hitcircle.png', 'r')
        hso = Image.open('hitcircleoverlay.png', 'r')

        hsoffset = ((dimw - re_w) // 2, (re_h - dimw) // 2)
        resizer.paste(hs, hsoffset, hs)

        dimw2, dimh2 = resizer.size
        hsooffset = ((dimw2 - dimw) // 2, (dimh2 - dimh) // 2)

        resizer.paste(hso, hsooffset, hso)

        fname = ('def' + str(count) + '.png')
        count += 1
        resizer.save(fname)
        print('Saved as', fname)
