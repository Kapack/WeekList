import os
# DIRECTORIES
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
WEEKLIST_DIR = "/Users/marketing/Documents/Lux-Case/Import Products/Week Lists/22/"

# XLS FIELDNAMES 
STRUCT_FIELDNAMES = ['SKU', 'Supplier', 'Supplier SKU', 'EAN_new', 'Image', 'Model', 'List', 'Gallery', 'Name (en-GB)', 'Description (en-GB)', 'Name (da-DK)', 'Description (da-DK)', 'Name (sv-SE)', 'Description (sv-SE)', 'Name (nb-NO)', 'Description (nb-NO)', 'Name (fi-FI)', 'Description (fi-FI)', 'Name (nl-NL)', 'Description (nl-NL)', 'Name (de-DE)', 'Description (de-DE)', 'Price (en-GB)', 'Final Price (en-GB)', 'Price (de-DE)', 'Final Price (de-DE)', 'Price (nl-NL)', 'Final Price (nl-NL)', 'Price (fi-FI)', 'Final Price (fi-FI)', 'Price (da-DK)', 'Final Price (da-DK)', 'Price (nb-NO)', 'Final Price (nb-NO)', 'Price (sv-SE)', 'Final Price (sv-SE)']
ONGOING_FIELDNAMES = ['Name', 'Article number', 'Barcode', 'Supplier article no.', 'Supplier', 'Location', 'Number of items']

# FILE NAMES
STRUCT_ADMIN_FILE = '-Struct-Admin.xlsx'