# import reportlab.lib.colors as colors
# from reportlab.lib.pagesizes import A4, landscape
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.units import cm, inch
# from reportlab.platypus import (Paragraph, SimpleDocTemplate, Spacer, Table,
#                                 TableStyle)
# from reportlab.platypus.flowables import PageBreak
# from reportlab.rl_config import defaultPageSize


# class SAMPLE_STYLES(object):
#     _styles = getSampleStyleSheet()
#     Normal = _styles['Normal']
#     BodyText = _styles['BodyText']
#     Italic = _styles['Italic']
#     Heading1 = _styles['Heading1']
#     Title = _styles['Title']
#     Heading2 = _styles['Heading2']
#     Heading3 = _styles['Heading3']
#     Heading4 = _styles['Heading4']
#     Heading5 = _styles['Heading5']
#     Heading6 = _styles['Heading6']
#     Bullet = _styles['Bullet']
#     Definition = _styles['Definition']
#     Code = _styles['Code']
    
    
# class PDF(object):

#     def __init__(self, filename, orientation='landscape'):
#         super(PDF, self).__init__()
#         self.filename = filename + '.pdf'
#         self.title = filename
#         self.pageinfo = filename
#         self.story = [Spacer(1, 2 * 2.54 * cm)]
#         self.pagesize = landscape(A4) if orientation == 'landscape' else defaultPageSize
#         self.PAGE_HEIGHT = self.pagesize[1]
#         self.PAGE_WIDTH = self.pagesize[0]
#         self.PAGE_MARGIN = 0.5 * inch

#     def build(self):
#         doc = SimpleDocTemplate(self.filename)
#         doc.pagesize = self.pagesize  # Set PDF orientation to landscape
#         doc.leftMargin = self.PAGE_MARGIN
#         doc.righMargin = self.PAGE_MARGIN
#         doc.topMargin = self.PAGE_MARGIN
#         doc.bottomMargin = self.PAGE_MARGIN
#         doc.build(self.story, onFirstPage=self._first_page, onLaterPages=self._later_pages)

#     def add_element(self, element):
#         self.story.append(element)

#     def add_paragraph(self, text):
#         style = SAMPLE_STYLES.Normal
#         p = Paragraph(text, style)
#         self.story.append(p)
#         self.story.append(Spacer(1, 0.2 * 2.54 * cm))

#     def add_page_break(self):
#         self.story.append(PageBreak())

#     def _first_page(self, canvas, doc):
#         canvas.saveState()
#         canvas.setFont('Times-Bold', 16)
#         canvas.drawCentredString(self.PAGE_WIDTH / 2.0, self.PAGE_HEIGHT - 108, self.title)
#         canvas.setFont('Times-Roman', 9)
#         canvas.drawString(cm, 0.75 * 2.54 * cm, "First Page / %s" % self.pageinfo)
#         canvas.restoreState()

#     def _later_pages(self, canvas, doc):
#         canvas.saveState()
#         canvas.setFont('Times-Roman', 9)
#         canvas.drawString(self.PAGE_MARGIN * 0.5, self.PAGE_MARGIN * 0.5, "Page %d / %s" % (doc.page, self.pageinfo))
#         canvas.restoreState()
#--------------------------------------------------------------------------------

# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.units import mm

# def coord(x, y, height, unit=1):
#     x, y = x * unit, height -  y * unit
#     return x, y

# c = canvas.Canvas("hello.pdf", pagesize=A4)
# width, height = A4

# c.drawString(*coord(80, 20, height, mm), text="Welcome to Reportlab!")
# c.showPage()
# c.save()
#---------------------------------------------------

# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas

# def apply_scripting(textobject, text, rise):
#     textobject.setFont("Helvetica-Oblique", 8)
#     textobject.setRise(rise)
#     textobject.textOut(text)
#     textobject.setFont("Helvetica-Oblique", 12)
#     textobject.setRise(0)


# def main():
#     canvas_obj = canvas.Canvas("textobj_rising.pdf",
#                                pagesize=letter)

#     # Create textobject
#     textobject = canvas_obj.beginText()
#     textobject.setFont("Helvetica-Oblique", 12)

#     # Set text location (x, y)
#     textobject.setTextOrigin(10, 730)

#     textobject.textOut('ReportLab ')
#     apply_scripting(textobject, 'superscript ', 7)

    
#     textobject.textOut('and ')

#     apply_scripting(textobject, 'subscript ', -7)


#     canvas_obj.drawText(textobject)
#     canvas_obj.save()


# if __name__ == '__main__':
#     main()





#-----------------------------------------------------