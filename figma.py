# %%
import requests
from FigmaPy import FigmaPy
import pprint
from PIL import Image, ImageDraw
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

pp = pprint.PrettyPrinter(indent=4)
# %%
def get_figma_images():
    # https://www.figma.com/developers/api#get-images-endpoint
    # file = "jdJvnkLaXGY53ql3xgqKfb"
    file = "rRFsjxA2cuTRMzi696b5wD"

    tolken = "304957-debeb3bd-45c7-4704-bd5f-18ed6e690cf9"
    fp = FigmaPy(tolken)
    component_names = []
    ids = []
    # GET/v1/images/:key
    files = fp.get_file(file)

    pp.pprint(files.components)

    for component in files.components:
        ids.append(component.replace('-','%3A'))
        component_names.append(files.components[component]["name"])
    
    images = fp.get_file_images(file, ids)
    pp.pprint(images.images)

    for index, image_url in enumerate(images.images):
        url = images.images[image_url]
        print(url)

        img_data = requests.get(url).content
        with open(f'static/figmaDeploy/{component_names[index]}.png', 'wb') as handler:
            handler.write(img_data)
        
    return images.images

static_content_figma = get_figma_images()

# %%
import glob
from PIL import Image

# filepaths
fp_in = 'C:/Users/Tristan/Desktop/bigFungus/static/figmaDeploy/Component*.png'
fp_out = "./static/logo.gif"
paths = glob.glob(fp_in)
# im = Image.open(...)
# transparency = im.info["transparency"]
paths.sort(key=natural_keys)

def gen_frame(path):
    im = Image.open(path)
    alpha = im.getchannel('A')

    # Convert the image into P mode but only use 255 colors in the palette out of 256
    im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)

    # Set all pixel values below 128 to 255 , and the rest to 0
    mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)

    # Paste the color of index 255 and use alpha as a mask
    im.paste(255, mask)

    # The transparency index is 255
    im.info['transparency'] = 255

    return im

# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
img, *imgs = [gen_frame(f) for f in paths]
img.save(fp=fp_out, format='GIF', append_images=imgs,
    save_all=True, duration=100)