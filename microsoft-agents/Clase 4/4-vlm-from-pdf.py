from PIL import Image
import pymupdf


filename = "sherl.pdf"
doc = pymupdf.open(filename)
for i in range(doc.page_count):
    doc = pymupdf.open(filename)
    page = doc.load_page(i)
    pix = page.get_pixmap()
    original_img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    original_img.save(f"page_{i}.png")
