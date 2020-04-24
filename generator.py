import argparse
import os
from random import seed
from random import randint
from PIL import Image, ImageDraw, ImageFont

os.mkdir("bingotickets")


def generateDict():
    dict = {}
    for i in range(100):
        dict[i+1] = 0
    return dict


def generateHeader(name=""):
    im = Image.new('RGB', (500, 200), color=(255, 105, 97))
    fnt = ImageFont.truetype("./fonts/Montserrat-Medium.ttf", 70)
    d = ImageDraw.Draw(im)
    d.line([(0, 198), (500, 198)], fill=(255, 255, 255), width=2)
    d.text((90, 25), "B I N G O", font=fnt, fill=(255, 255, 255))
    namefnt = ImageFont.truetype("./fonts/Montserrat-Bold.ttf", 30)
    d.text((25, 130), "Name : " + name, font=namefnt, fill=(255, 255, 255))
    return im


def generateCard(ticket_array):
    im = Image.new('RGB', (500, 500), color=(255, 105, 97))
    fnt = ImageFont.truetype("./fonts/Montserrat-Bold.ttf", 45)
    d = ImageDraw.Draw(im)
    # drawing horizontal lines
    for i in range(4):
        d.line([(0, (i+1)*100), (500, (i+1)*100)],
               fill=(255, 255, 255), width=2)
    # drawing vertical lines
    for i in range(4):
        d.line([((i+1)*100, 0), ((i+1)*100, 500)],
               fill=(255, 255, 255), width=2)
    # printing numbers
    for i in range(5):
        for j in range(5):
            if ticket_array[i][j] < 10:
                d.text(((i*100)+35, (j*100)+20),
                       str(ticket_array[i][j]), font=fnt, fill=(255, 255, 255))
            else:
                d.text(((i*100)+25, (j*100)+20),
                       str(ticket_array[i][j]), font=fnt, fill=(255, 255, 255))
    return im


def combineHeaderAndCard(header, card):
    dst = Image.new('RGB', (header.width, header.height + card.height))
    dst.paste(header, (0, 0))
    dst.paste(card, (0, header.height))
    return dst


def drawTicket(ticket_array, ticket_num, name=""):
    header = generateHeader(name)
    card = generateCard(ticket_array)
    combined = combineHeaderAndCard(header, card)
    # add border
    borderimage = Image.new('RGB', (520, 720), color=(255, 255, 255))
    borderimage.paste(combined, (10, 10))
    # add name
    fnt = ImageFont.truetype("./fonts/Montserrat-Regular.ttf", 10)
    d = ImageDraw.Draw(borderimage)
    d.text((350, 0), "MADE BY AVINASH TADAVARTHY", font=fnt, fill=(0, 0, 0))
    # save final card
    borderimage.save('bingotickets/ticket_number'+str(ticket_num)+'.png')


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("--tickets", help="number of tickets required")
ap.add_argument("--seed", help="seed to generate random number")
args = vars(ap.parse_args())

seedno = int(args['seed'])
seed(seedno)

number = int(args['tickets'])
print("Processing...")
for k in range(number):
    dict = generateDict()
    arr = []
    for _ in range(5):
        smol = []
        i = 0
        while i != 5:
            value = randint(1, 90)
            if dict[value] == 0:
                smol.append(value)
                dict[value] = 1
                i = i+1
        arr.append(smol)
    del dict
    drawTicket(arr, k+1)

print("Done")
print("Check the 'bingotickets' directory")
