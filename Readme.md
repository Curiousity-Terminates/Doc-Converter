# Docs Converter
A command-line tool for converting document formats. Built with Python, Typer, and Pandoc.

This tool allows you to quickly convert files like .docx, .odt, or .md into formats like PDF, HTML, and more, right from your terminal.

## Features
Multiple Format Support: Convert between dozens of formats supported by Pandoc.

User-Friendly: Clear commands and easy to use

Custom Output: Specify a custom name for your converted file.

Cross-Platform: Works on Windows, macOS, and Linux.

## Installation
All you need is Python 3.7+ installed on your system. You can install `docs-converter` directly from the official PyPI repository.

- Install via pip:
```
pip install docs-converter
```

- Find the package on PyPI: https://pypi.org/project/docs-converter/

## Usage
The command structure: `docs-converter <source_file> <to_format> [options]`

- Convert a Word document to a PDF
```
docs-converter my_document.docx pdf
```

- Convert a Markdown file to HTML
```
docs-converter README.md html
```

- Convert a document and name the output file 'report.pdf'
```
docs-converter draft.odt pdf -o report.pdf
```

- You can also specify a different directory
```
docs-converter notes.md pdf -o ../archives/notes_v1.pdf
```

- Getting Help
You can always get a list of commands and options with the `--help` flag.
```
docs-converter --help
```

## Supported Formats
Currently, the below formats are supported:

pdf, docx, html, md (Markdown), rst (reStructuredText), epub

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page for this project.
