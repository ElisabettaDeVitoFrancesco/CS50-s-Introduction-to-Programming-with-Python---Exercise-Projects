from fpdf import FPDF
#from PIL import Image, ImageOps

def main():
    name = input("What's your name? ")
    #shirt = Image.open("shirtificate.png")
    shirtificate(name)


def shirtificate(name):
    shirt_pdf = FPDF(orientation = "portrait", unit = "mm", format = "A4")
    shirt_pdf.add_page()
    shirt_pdf.set_font('helvetica', size=40)
    shirt_pdf.cell(txt="CS50 Shirtificate", w = shirt_pdf.epw, align='C', fill = False)
    shirt_pdf.image("shirtificate.png", x = 10, y = 70, w = 190)
    shirt_pdf.set_font('helvetica', size=30)
    shirt_pdf.set_text_color(255,255,255)
    shirt_pdf.set_y(shirt_pdf.eph/2)
    shirt_pdf.cell(txt=f"{name} took CS50", w = shirt_pdf.epw, align='C', fill = False)
    shirt_pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
