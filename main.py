import os
from PIL import Image

Image.LOAD_TRUNCATED_IMAGES = True

quality = 30

images_folder = 'images'
images_destination_folder = 'compressed'

i = 0
t = 0

if not os.path.exists(images_destination_folder):
    os.mkdir(images_destination_folder)

for root, subdirs, files in os.walk(images_folder):

    for file in os.listdir(root):

        filePath = os.path.join(root, file)

        if os.path.isdir(filePath):
            pass

        else:
            f = open(filePath, 'r')
            head, tail = os.path.split(f.name)

            if not os.path.exists(images_destination_folder + head[len(images_folder):]):
                os.makedirs(images_destination_folder + head[len(images_folder):])

            if not os.path.exists(images_destination_folder + head[len(images_folder):] + '/' + tail):
                print(f.name)
                try:
                    im = Image.open(f.name)
                    im.save(images_destination_folder + head[len(images_folder):] + '/' + tail, quality=quality)
                    i += 1
                except Exception as e:
                    print('Error: ' + f.name)
                    pass

        t += 1

print(str(i) + ' images were compressed from total of ' + str(t))
