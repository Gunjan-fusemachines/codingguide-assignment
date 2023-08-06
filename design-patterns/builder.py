from abc import ABC, abstractmethod

# Product: Document interface
class Document:
    def __init__(self):
        self.content = ""

    def add_content(self, content):
        self.content += content

    def get_content(self):
        return self.content

# Concrete Product: PDF Document
class PDFDocument(Document):
    pass

# Concrete Product: HTML Document
class HTMLDocument(Document):
    pass

# Concrete Product: Plain Text Document
class PlainTextDocument(Document):
    pass

# Builder: DocumentBuilder interface
class DocumentBuilder(ABC):
    @abstractmethod
    def create_document(self):
        pass

    @abstractmethod
    def add_heading(self, text):
        pass

    @abstractmethod
    def add_paragraph(self, text):
        pass

    def get_document(self):
        return self.document

# Concrete Builder: PDFDocumentBuilder
class PDFDocumentBuilder(DocumentBuilder):
    def create_document(self):
        self.document = PDFDocument()

    def add_heading(self, text):
        self.document.add_content(f"<h1>{text}</h1>")

    def add_paragraph(self, text):
        self.document.add_content(f"<p>{text}</p>")

# Concrete Builder: HTMLDocumentBuilder
class HTMLDocumentBuilder(DocumentBuilder):
    def create_document(self):
        self.document = HTMLDocument()

    def add_heading(self, text):
        self.document.add_content(f"{text}\n")

    def add_paragraph(self, text):
        self.document.add_content(f"{text}\n")

# Director: DocumentGenerator
class DocumentGenerator:
    def __init__(self, builder):
        self.builder = builder

    def generate_document(self):
        self.builder.create_document()
        self.builder.add_heading("Builder Design Pattern ")
        self.builder.add_paragraph("Hello this is an example for builder design patterm.")
        return self.builder.get_document()

# Client code
def main():
    pdf_builder = PDFDocumentBuilder()
    pdf_generator = DocumentGenerator(pdf_builder)
    pdf_document = pdf_generator.generate_document()
    print("PDF Document:\n" + pdf_document.get_content())

    html_builder = HTMLDocumentBuilder()
    html_generator = DocumentGenerator(html_builder)
    html_document = html_generator.generate_document()
    print("\nHTML Document:\n" + html_document.get_content())

if __name__ == "__main__":
    main()
