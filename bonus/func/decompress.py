import zipfile as zf
import pathlib as pl


def fromZip(_filepath, _target):
    """Extracts specified .zip file to specified target
    and returns the extraction status.

    Args:
        _filepath (str): A list containing the .zip file path.
        _target (str): Destination folder for extracted files.

    Returns:
        str: Returns the status of extraction as a string.
    """

    try:
        with zf.ZipFile(_filepath, "r") as file:
            target = pl.Path(_target, "extracted")
            file.extractall(target)

        return "Files are extracted successfully!"

    except Exception as e:
        return f"Files are not extracted. See error: {str(e)}"
