from PIL import Image
import pytesseract


def give_orc(ax):
    ax = Image.open(ax)
    matn = pytesseract.image_to_string(ax, lang='fas')
    return matn
