# Invoice PDF Information Extractor

This repository contains a Python script that automatically reads invoice documents in PDF format and extracts structured information from them. The purpose of the project is to transform unstructured textual data into usable values that can later be analyzed, stored, or integrated into accounting workflows.

Instead of manual data entry, the program processes invoices programmatically and identifies key business fields such as invoice identifiers, customer names, pricing information, and payment conditions. The implementation emphasizes clarity and reproducibility so the workflow can be easily understood and extended.

---

## Project Objective

Invoices often arrive as static documents that cannot be directly queried or analyzed. Organizations typically need to manually copy data into spreadsheets or databases, which is slow and error-prone. This project demonstrates a basic automated pipeline capable of reading invoice text and extracting meaningful fields.

The application performs the following operations:

1. Reads one or multiple PDF invoices
2. Extracts the text content of each document
3. Identifies relevant data using pattern recognition
4. Computes financial values such as subtotal and total
5. Outputs the extracted information
6. Moves processed documents to a separate folder

The goal is not to support every invoice format but to illustrate a repeatable method for document parsing and structured data extraction.

---

## How It Works

### Document Reading
The script loads PDF files and retrieves textual content page by page. This converts a visual document into a continuous text string that can be analyzed programmatically.

### Pattern Recognition
Specific fields inside the invoice are identified using pattern matching rules. These rules detect labels such as invoice number, billing recipient, itemized entries, discount values, tax values, and additional notes. Each field is captured and transformed into structured data.

### Financial Calculation
After extracting individual line items, the program calculates:

- Subtotal based on item values
- Discounted amount
- Final total including tax

This demonstrates how extracted information can be used not only for storage but also for automatic validation and accounting operations.

### File Management
Once processed, invoices are moved into a separate directory. This prevents duplicate processing and establishes a simple workflow state: unprocessed and processed documents.

---

## Features

- Automatic invoice text extraction
- Field detection using structured patterns
- Financial value computation
- Batch folder processing
- Automatic file organization after processing
- Console output for verification

---

## Intended Use Cases

This project can serve as a foundation for:

- Accounting automation experiments
- Document digitization workflows
- Data preprocessing for financial datasets
- Educational demonstrations of document parsing

---

## Possible Extensions

The current implementation is intentionally simple. Future improvements may include:

- Database integration
- Spreadsheet export
- Multi-format invoice support
- Error handling and validation
- Optical character recognition for scanned invoices
- Integration with business management systems

---

## Educational Value

The repository demonstrates a full data pipeline: reading files, extracting text, identifying patterns, computing values, and managing processed assets. It provides a practical example of how unstructured documents can be transformed into structured information suitable for automation.

---

## License

This project is released under the MIT License.
