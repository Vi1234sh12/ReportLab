# from flask import Flask, render_template
# from reportlab.lib.pagesizes import letter
# from reportlab.lib import colors
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, PageTemplate, Frame, PageBreak
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.units import inch
# import PyPDF2
# from reportlab.lib.pagesizes import LETTER, inch
# from reportlab.pdfgen import canvas

# app = Flask(__name__)

# class FooterCanvas(canvas.Canvas):
#     def __init__(self, *args, **kwargs):
#         canvas.Canvas.__init__(self, *args, **kwargs)
#         self.pages = []
#         self.width, self.height = LETTER

#     def showPage(self):
#         self.pages.append(dict(self.__dict__))
#         self._startPage()

#     def save(self):
#         page_count = len(self.pages)
#         for page in self.pages:
#             self.__dict__.update(page)
#             if (self._pageNumber > 1):
#                 self.draw_canvas(page_count)
#             canvas.Canvas.showPage(self)
#         canvas.Canvas.save(self)

#     def draw_canvas(self, page_count):
#         page = "Page %s of %s" % (self._pageNumber, page_count)
#         x = 128
#         self.saveState()
#         self.setStrokeColorRGB(0, 0, 0)
#         self.setLineWidth(0.5)
#         self.drawImage("static/lr.png", self.width-inch*8-5, self.height-50, width=100, height=20, preserveAspectRatio=True)
#         self.drawImage("static/ohka.png", self.width - inch * 2, self.height-50, width=100, height=30, preserveAspectRatio=True, mask='auto')
#         self.line(30, 740, LETTER[0] - 50, 740)
#         self.line(66, 78, LETTER[0] - 66, 78)
#         self.setFont('Times-Roman', 10)
#         self.drawString(LETTER[0]-x, 65, page)
#         self.restoreState()


# class PDFGenerator:
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.page_width, self.page_height = letter

#     def add_page_border_and_number(self, canvas, doc):
#         # Draw borders around all sides of the page for pages other than the first page
#         if canvas.getPageNumber() > 1:
#             canvas.setStrokeColor(colors.black)
#             canvas.setLineWidth(2)
#             canvas.line(0, 0, 0, self.page_height)  # Left border
#             canvas.line(0, 0, self.page_width, 0)   # Bottom border
#             canvas.line(0, self.page_height, self.page_width, self.page_height)  # Top border
#             canvas.line(self.page_width, 0, self.page_width, self.page_height)  # Right border

#         # Add page number at the bottom of each page
#         page_number = canvas.getPageNumber()
#         text = "Page %d" % page_number
#         canvas.drawRightString(self.page_width - inch, inch, text)

#     def create_pdf(self, data):
#         # Create a PDF document
#         doc = SimpleDocTemplate(self.file_name, pagesize=letter)

#         # SampleStyleSheet provides basic styling for the elements
#         styles = getSampleStyleSheet()

#         # Welcome page content
#         def welcome_page():
#             return [Paragraph("Welcome to the PDF", styles['Title']),
#                     Paragraph("This is a welcome message.", styles['Normal'])]

#         # Index page content
#         def index_page():
#             return [Paragraph("Index Page", styles['Title']),
#                     Paragraph("This is the index page content.", styles['Normal'])]

#         # Create a list to hold the data for the table (2D array)
#         table_data = [['Name', 'Age', 'Country'],
#                       ['John', '30', 'USA'],
#                       ['Emily', '25', 'Canada'],
#                       ['Michael', '40', 'UK']]

#         # Replace the sample data with your actual data
#         if data:
#             table_data = [['Name', 'Age', 'Country']] + data

#         # Create the table and set its style
#         table = Table(table_data)
#         table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#                                    ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
#                                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#                                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#                                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#                                    ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

#         # Add the content to the PDF document in order (welcome page, index page, table)
#         elements = welcome_page() + [PageBreak()] + index_page() + [PageBreak()] + [table]

#         # Add page template to apply borders and page numbers to all pages
#         page_template = PageTemplate(frames=[Frame(inch, inch, self.page_width - 2 * inch, self.page_height - 2 * inch, id='normal')],
#                                      onPage=self.add_page_border_and_number)
#         doc.addPageTemplates([page_template])

#         # Build the PDF document with all the elements
#         doc.build(elements)

#     def read_pdf(self):
#         pdf_content = []
#         with open(self.file_name, 'rb') as pdf_file:
#             pdf_reader = PyPDF2.PdfFileReader(pdf_file)
#             for page_num in range(pdf_reader.numPages):
#                 page = pdf_reader.getPage(page_num)
#                 page_content = page.extractText()
#                 pdf_content.append((page_num + 1, page_content))
#         return pdf_content

# if __name__ == "__main__":
#     # Example usage:
#     # Generate a PDF with the sample data using the PDFGenerator class
#     pdf_generator = PDFGenerator("sample_pdf_with_all_borders.pdf")
#     pdf_generator.create_pdf(data=None)


#######################################################final code 

# from flask import Flask
# from reportlab.lib.pagesizes import letter
# from reportlab.lib import colors
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, PageBreak
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.units import inch
# import PyPDF2
# from reportlab.lib.pagesizes import LETTER, inch
# from reportlab.pdfgen import canvas

# app = Flask(__name__)

# class PDFGenerator:
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.page_width, self.page_height = letter

#     def add_page_number(self, canvas, doc):
#         page_number = canvas.getPageNumber()
#         text = "Page %d" % page_number
#         canvas.drawRightString(self.page_width - inch, inch, text)

#     def create_pdf(self, data):
#         # Create a PDF document
#         doc = SimpleDocTemplate(self.file_name, pagesize=letter, rightMargin=inch, leftMargin=inch, topMargin=inch, bottomMargin=inch)

#         # SampleStyleSheet provides basic styling for the elements
#         styles = getSampleStyleSheet()

#         # Welcome page content
#         def welcome_page():
#             return [Paragraph("Welcome to the PDF", styles['Title']),
#                     Paragraph("This is a welcome message.", styles['Normal'])]

#         # Index page content
#         def index_page():
#             return [Paragraph("Index Page", styles['Title']),
#                     Paragraph("This is the index page content.", styles['Normal'])]

#         # Create a list to hold the data for the table (2D array)
#         table_data = [['Name', 'Age', 'Country'],
#                       ['John', '30', 'USA'],
#                       ['Emily', '25', 'Canada'],
#                       ['Michael', '40', 'UK']]

#         # Replace the sample data with your actual data
#         if data:
#             table_data = [['Name', 'Age', 'Country']] + data

#         # Create the table and set its style
#         table = Table(table_data)
#         table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#                                    ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
#                                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#                                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#                                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#                                    ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

#         # Add the content to the PDF document in order (welcome page, index page, table)
#         elements = welcome_page() + [PageBreak()] + index_page() + [PageBreak()] + [table]

#         # Add page number to each page
#         doc.build(elements, onFirstPage=self.add_page_number, onLaterPages=self.add_page_number)

#     def read_pdf(self):
#         pdf_content = []
#         with open(self.file_name, 'rb') as pdf_file:
#             pdf_reader = PyPDF2.PdfFileReader(pdf_file)
#             for page_num in range(pdf_reader.numPages):
#                 page = pdf_reader.getPage(page_num)
#                 page_content = page.extractText()
#                 pdf_content.append((page_num + 1, page_content))
#         return pdf_content

# if __name__ == "__main__":
#     # Example usage:
#     # Generate a PDF with the sample data using the PDFGenerator class
#     pdf_generator = PDFGenerator("sample_pdf_with_all_borders.pdf")
#     # Sample data for the table
#     table_data = [['Name', 'Age', 'Country'],
#                   ['John', '30', 'USA'],
#                   ['Emily', '25', 'Canada'],
#                   ['Michael', '40', 'UK']]
#     pdf_generator.create_pdf(data=table_data)

#     # Read the content of the generated PDF
#     pdf_content = pdf_generator.read_pdf()
#     for page_num, content in pdf_content:
#         print(f"Page {page_num}:\n{content}\n")

########################################## page no 

# from flask import Flask
# from reportlab.lib.pagesizes import letter
# from reportlab.lib import colors
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, PageBreak
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.units import inch
# import PyPDF2
# from reportlab.lib.pagesizes import LETTER, inch
# from reportlab.pdfgen import canvas

# app = Flask(__name__)

# class PDFGenerator:
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.page_width, self.page_height = letter

#     def add_page_number_and_border(self, canvas, doc):
#         page_number = canvas.getPageNumber()
#         text = "Page %d" % page_number
#         canvas.drawRightString(self.page_width - inch, inch, text)
        
#         # Draw the page border
#         canvas.setStrokeColorRGB(0, 0, 0)  # Set the border color (black)
#         # Draw the page border
#         border_x1 = 0.5 * inch  # Left margin
#         border_y1 = 0.5 * inch  # Bottom margin
#         border_x2 = self.page_width - 0.5 * inch  # Right margin
#         border_y2 = self.page_height - 0.5 * inch  # Top margin

#         canvas.setStrokeColorRGB(0, 0, 0)  # Set the border color (black)
#         canvas.setLineWidth(2)  # Set the border line width
#         canvas.rect(border_x1, border_y1, border_x2 - border_x1, border_y2 - border_y1)
#         # canvas.rect(inch, inch, self.page_width - 2*inch, self.page_height - 2*inch)

#     def create_pdf(self, data):
#         # Create a PDF document
#         doc = SimpleDocTemplate(self.file_name, pagesize=letter, rightMargin=inch, leftMargin=inch, topMargin=inch, bottomMargin=inch)

#         # SampleStyleSheet provides basic styling for the elements
#         styles = getSampleStyleSheet()

#         # Welcome page content
#         def welcome_page():
#             return [Paragraph("Welcome to the PDF", styles['Title']),
#                     Paragraph("This is a welcome message.", styles['Normal'])]

#         # Index page content
#         def index_page():
#             return [Paragraph("Index Page", styles['Title']),
#                     Paragraph("This is the index page content.", styles['Normal'])]

#         # Create a list to hold the data for the table (2D array)
#         table_data = [['Name', 'Age', 'Country'],
#                       ['John', '30', 'USA'],
#                       ['Emily', '25', 'Canada'],
#                       ['Michael', '40', 'UK']]

#         # Replace the sample data with your actual data
#         if data:
#             table_data = [['Name', 'Age', 'Country']] + data

#         # Create the table and set its style
#         table = Table(table_data)
#         table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#                                    ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
#                                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
#                                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
#                                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#                                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
#                                    ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

#         # Add the content to the PDF document in order (welcome page, index page, table)
#         elements = welcome_page() + [PageBreak()] + index_page() + [PageBreak()] + [table]

#         # Add page number and border to each page
#         doc.build(elements, onFirstPage=self.add_page_number_and_border, onLaterPages=self.add_page_number_and_border)

#     def read_pdf(self):
#         pdf_content = []
#         with open(self.file_name, 'rb') as pdf_file:
#             pdf_reader = PyPDF2.PdfFileReader(pdf_file)
#             for page_num in range(pdf_reader.numPages):
#                 page = pdf_reader.getPage(page_num)
#                 page_content = page.extractText()
#                 pdf_content.append((page_num + 1, page_content))
#         return pdf_content

# if __name__ == "__main__":
#     # Example usage:
#     # Generate a PDF with the sample data using the PDFGenerator class
#     pdf_generator = PDFGenerator("sample_pdf_with_all_borders.pdf")
#     # Sample data for the table
#     table_data = [['Name', 'Age', 'Country'],
#                   ['John', '30', 'USA'],
#                   ['Emily', '25', 'Canada'],
#                   ['Michael', '40', 'UK']]
#     pdf_generator.create_pdf(data=table_data)

#     # Read the content of the generated PDF
#     pdf_content = pdf_generator.read_pdf()
#     for page_num, content in pdf_content:
#         print(f"Page {page_num}:\n{content}\n")

############################### page no and page border 



from flask import Flask
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import PyPDF2
from reportlab.lib.pagesizes import LETTER, inch
from reportlab.pdfgen import canvas

app = Flask(__name__)

class PDFGenerator:
    def __init__(self, file_name):
        self.file_name = file_name
        self.page_width, self.page_height = letter

    def add_page_number_and_border(self, canvas, doc):
        page_number = canvas.getPageNumber()
        text = "Page %d" % page_number
        canvas.drawRightString(self.page_width - inch, inch, text)

        # Draw the page border
        border_x1 = 0.5 * inch  # Left margin
        border_y1 = 0.5 * inch  # Bottom margin
        border_x2 = self.page_width - 0.5 * inch  # Right margin
        border_y2 = self.page_height - 0.5 * inch  # Top margin

        canvas.setStrokeColorRGB(0, 0, 0)  # Set the border color (black)
        canvas.setLineWidth(2)  # Set the border line width
        canvas.rect(border_x1, border_y1, border_x2 - border_x1, border_y2 - border_y1)

    def create_pdf(self, user_data_list):
        # Create a PDF document
        doc = SimpleDocTemplate(self.file_name, pagesize=letter, rightMargin=inch, leftMargin=inch, topMargin=inch, bottomMargin=inch)

        # SampleStyleSheet provides basic styling for the elements
        styles = getSampleStyleSheet()

        # Welcome page content
        def welcome_page():
            return [Paragraph("Welcome to the PDF", styles['Title']),
                    Paragraph("This is a welcome message.", styles['Normal'])]

        # Index page content
        def index_page():
            return [Paragraph("Index Page", styles['Title']),
                    Paragraph("This is the index page content.", styles['Normal'])]

        # Create the table and set its style
        def create_table(data):
            table_data = [['Name', 'Age', 'Country']] + data
            table = Table(table_data)
            table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                       ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
                                       ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                       ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                       ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                       ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                       ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                       ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                       ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
            return table

        # Add the content to the PDF document in order (welcome page, index page, tables)
        elements = welcome_page() + [PageBreak()] + index_page() + [PageBreak()]
        for user_data in user_data_list:
            table = create_table(user_data)
            elements.append(table)
            elements.append(PageBreak())

        # Add page number and border to each page
        doc.build(elements, onFirstPage=self.add_page_number_and_border, onLaterPages=self.add_page_number_and_border)

    def read_pdf(self):
        pdf_content = []
        with open(self.file_name, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                page_content = page.extractText()
                pdf_content.append((page_num + 1, page_content))
        return pdf_content

if __name__ == "__main__":
    # Example usage:
    # Generate a PDF with the sample data using the PDFGenerator class
    pdf_generator = PDFGenerator("sample_pdf_with_user_tables.pdf")
    # Sample data for users (each element in the list represents a user's data)
    users_data_list = [
        [['Name', 'Age', 'Country'],
         ['John', '30', 'USA'],
         ['Emily', '25', 'Canada'],
         ['Michael', '40', 'UK']],
        [['Name', 'Age', 'Country'],
         ['Alice', '28', 'Australia'],
         ['Bob', '22', 'New Zealand']]
    ]
    pdf_generator.create_pdf(users_data_list)

    # Read the content of the generated PDF
    pdf_content = pdf_generator.read_pdf()
    for page_num, content in pdf_content:
        print(f"Page {page_num}:\n{content}\n")
