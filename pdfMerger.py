# from PyPDF4 import PdfFileMerger
# import os,argparse


# def merge_pdfs(input_files=None, page_range=None, output_file=None, bookmark=True):
#     if input_files is None:
#         input_files = []
#     """
#     Merge a list of PDF files and save the combined result into the `output_file`.
#     `page_range` to select a range of pages (behaving like Python's range() function) from the input files
#         e.g (0,2) -> First 2 pages 
#         e.g (0,6,2) -> pages 1,3,5
#     bookmark -> add bookmarks to the output file to navigate directly to the input file section within the output file.
#     """
#     input_files = ["pd1.pdf", "pd2.pdf","pd3.pdf"]

#     # strict = False -> To ignore PdfReadError - Illegal Character error
#     merger = PdfFileMerger(strict=False)
#     for input_file in input_files:
#         bookmark_name = os.path.splitext(os.path.basename(input_file))[0] if bookmark else None
#         # pages To control which pages are appended from a particular file.
#         merger.append(fileobj=open(input_file, 'rb'), pages=page_range, import_bookmarks=False, bookmark=bookmark_name)
#     # Insert the pdf at specific page
#     merger.write(fileobj=open(output_file, 'wb'))
#     merger.close()


from PyPDF4 import PdfFileMerger
import os

def merge_pdfs(input_files: list, page_range: tuple, output_file: str, bookmark: bool = True):
    merger = PdfFileMerger(strict=False)
    for input_file in input_files:
        bookmark_name = os.path.splitext(os.path.basename(input_file))[0] if bookmark else None
        merger.append(fileobj=open(input_file, 'rb'), pages=page_range, import_bookmarks=False, bookmark=bookmark_name)
    merger.write(fileobj=open(output_file, 'wb'))
    merger.close()

# Example usage:
input_files = ["pd1.pdf", "pd2.pdf", "pd3.pdf"]
page_range = (0, 2)  # First 2 pages
output_file = "merged.pdf"
merge_pdfs(input_files, page_range, output_file)
print(f"Merged PDF saved as {output_file}")
