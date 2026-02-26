import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the yaml file.
    
    Raises:
        ValueError: If the yaml file is empty.
        e: If there is an error reading the yaml file.  
    
    Returns:
        ConfigBox: ConfigBox object containing the yaml file data.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except ValueError as ve:
        logger.exception(f"yaml file: {path_to_yaml} is empty")
        raise ve
    except Exception as e:
        logger.exception(f"Error reading the yaml file: {path_to_yaml}")
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories.
    
    Args:
        path_to_directories (list): List of directories to be created.
    
    Returns:
        None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Directory created at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary to a json file.
    
    Args:
        path (Path): Path to the json file.
        data (dict): Dictionary to be saved.
    
    Returns:
        None
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")  

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a json file and returns a ConfigBox object.
    
    Args:
        path (Path): Path to the json file.
    
    Returns:
        ConfigBox: ConfigBox object containing the json file data.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves a binary file using joblib.
    
    Args:
        data (Any): Data to be saved.
        path (Path): Path to the binary file.
    
    Returns:
        None
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")    

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads a binary file using joblib.
    
    Args:
        path (Path): Path to the binary file.
    
    Returns:
        Any: Data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data