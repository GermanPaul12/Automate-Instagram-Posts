import random
from PIL import Image, ImageDraw,ImageFont
import requests


def make_post():
    image_random_number = random.randint(1, 6)
    img_url = f"https://raw.githubusercontent.com/GermanPaul12/Automate-Instagram-Posts/main/Images/{image_random_number}.png"
    img = Image.open(requests.get(img_url, stream = True).raw)
    draw = ImageDraw.Draw(img)

    text_url = "https://raw.githubusercontent.com/GermanPaul12/Scrape-Stoic-Quotes-with-Requests-and-BeautifulSoup/main/quote.txt"
    res = requests.get(text_url)
    quotes = res.text.split("\n")

    with open("Scripts/post_num.txt", "r+") as f:
        num = int(f.read())
        quote = quotes[num]
    with open("Scripts/post_num.txt", "w") as f:
        f.write(str(num+1))    

    font_size = 40  # Adjust the font size as needed
    font = ImageFont.truetype("Font/Stoic.ttf", font_size)
    text = quote.encode('utf-8')  # Encode as UTF-8
    #print(random_quote)
    height = 800

    textwidth, textheight = draw.textsize(text.decode("utf-8").replace(",","\n"), font)
    width, height = img.size 
    x=width/2-textwidth/2
    y=(height+800)/2-textheight/2

    #for i in text.decode("utf-8").split(","):

    draw.text((x, y), text.decode("utf-8").replace(",","\n"), 
            align="center", font=font,
            fill="#CCC8AA",
            stroke_width=1, stroke_fill="#F1EFEF",
            )
    #height += 50
    img.save('output.png')
    #img.show()
    
if __name__ == "__main__":
    make_post()