import os
from box.exceptions import BoxValueError
from cnnClassifier import logger
import yaml
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64
import joblib

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object

    Args:
        path_to_yaml (Path): Path to the yaml file

    Returns:
        ConfigBox: ConfigBox object containing the yaml file contents
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise e
    except Exception as e:
        logger.error(f"Error reading the YAML file: {e}")
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories if they do not exist

    Args:
        path_to_directories (list[Path]): List of directory paths to create
        verbose (bool, optional): Whether to log the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict[str, Any]) -> None:
    """Saves a dictionary to a JSON file

    Args:
        path (Path): Path to the JSON file
        data (dict[str, Any]): Data to save
    """
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        logger.info(f"Data successfully saved to JSON file at: {path}")
    except Exception as e:
        logger.error(f"Error saving data to JSON file: {e}")
        raise e
    

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a JSON file and returns a ConfigBox object

    Args:
        path (Path): Path to the JSON file

    Returns:
        ConfigBox: ConfigBox object containing the JSON file contents
    """
    try:
        with open(path, 'r') as json_file:
            content = json.load(json_file)
            logger.info(f"JSON file: {path} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise e
    except Exception as e:
        logger.error(f"Error reading the JSON file: {e}")
        raise e
    

@ensure_annotations
def save_bin(path: Path, data: Any) -> None:
    """Saves binary data to a file

    Args:
        path (Path): Path to the binary file
        data (Any): Data to save
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary data successfully saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads binary data from a file

    Args:
        path (Path): Path to the binary file

    Returns:
        Any: Loaded data
    """
    data = joblib.load(filename=path)
    logger.info(f"Binary data successfully loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in KB

    Args:
        path (Path): Path to the file

    Returns:
        str: Size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    logger.info(f"File size of {path} is {size_in_kb} KB")
    return f"{size_in_kb} KB"


@ensure_annotations
def encodeImageToBase64(image_path: Path) -> str:
    """Encodes an image to a base64 string

    Args:
        image_path (Path): Path to the image file

    Returns:
        str: Base64 encoded string of the image
    """
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    logger.info(f"Image at {image_path} successfully encoded to base64")
    return encoded_string


@ensure_annotations
def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()