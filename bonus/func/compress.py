import zipfile as zf
import pathlib as pl


def toZip(_filepaths, _target):
    """Compresses specified files to a .zip file in specified target
    and returns the compression status.

    Args:
        _filepaths (list): A list containing the file paths.
        _target (str): Destination folder for .zip file.

    Returns:
        str: Returns the status of compression as a string.
    """

    try:
        target = pl.Path(_target, "compressed.zip")
        with zf.ZipFile(target, "w") as file:
            for filepath in _filepaths:
                filepath = pl.Path(filepath)
                file.write(filepath, arcname=filepath.name)

        return "Files are compressed successfully!"

    except Exception as e:
        return f"Files are not compressed. See error: {str(e)}"
