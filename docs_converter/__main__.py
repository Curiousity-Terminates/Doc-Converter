import typer
from pathlib import Path
import pypandoc
import sys
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

app = typer.Typer(
    name="docs-converter",
    help="A simple CLI tool to convert document formats using Pandoc."
)

SUPPORTED_FORMATS = ["pdf", "docx", "html", "md", "rst", "epub"]

@app.command()
def convert(
    source_file: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        help="The path to the source file you want to convert."
    ),
    to_format: str = typer.Argument(
        ...,
        help=f"The target format. Supported formats: {', '.join(SUPPORTED_FORMATS)}"
    ),
    output_file: Path = typer.Option(
        None,
        "--output",
        "-o",
        help="Optional: specify the full output file path."
    )
):
    """
    Converts a file from one format to another.
    """
    if to_format.lower() not in SUPPORTED_FORMATS:
        typer.secho(f"Error: Unsupported format '{to_format}'.", fg=typer.colors.RED)
        typer.echo(f"Please choose from the supported formats: {', '.join(SUPPORTED_FORMATS)}")
        raise typer.Exit(code=1)

    if not output_file:
        output_file = source_file.with_suffix(f".{to_format.lower()}")

    typer.echo(f"Converting '{source_file}' to '{output_file}'...")
    
    extra_args = ['--quiet']
    if to_format.lower() == 'pdf':
        extra_args.append('--pdf-engine=weasyprint')
    
    try:
        pypandoc.convert_file(
            source_file,
            to_format.lower(),
            outputfile=str(output_file),
            extra_args=extra_args
        )
        typer.secho(
            f"Successfully converted file to '{output_file}'",
            fg=typer.colors.GREEN
        )
    except Exception as e:
        typer.secho(f"Conversion failed: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()