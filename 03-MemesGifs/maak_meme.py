from PIL import Image, ImageFont, ImageDraw


background = Image.open("Xdoubt.jpg")


width = background.width
height = background.height


lettertype = ImageFont.truetype("impact.ttf",40)


surface = ImageDraw.Draw(background)

tekst = "Samed: Mijn IP is 120\nIk: Je IP of je IQ?\nSamed: ..."
tekst_breedte, tekst_hoogte = surface.textsize(tekst, font=lettertype)

tekst_x = (width - tekst_breedte) - 10
tekst_y = (height - tekst_hoogte) - 320

surface.multiline_text((tekst_y,tekst_x), tekst, font=lettertype, fill=(0,0,0))
surface.multiline_text((tekst_x-2, tekst_y-2), tekst, font=lettertype, fill=(255,255,255))

background.show()
