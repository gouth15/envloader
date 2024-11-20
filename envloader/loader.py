from pathlib import Path
from typing import Dict


class EnvLoader:
    """ This is the class for loading and parsing the environment values in the .env file.
    """
    
    def __init__(self, filename: str = ".env") -> None:
        """Initializes the .env file.

        Args:
            filename (str, optional): The environment file of the project. Defaults to ".env".
        """
        self._filename: Path = self._find_env_file(filename)
        self.env_values: Dict[str, str] = self.load_env()

    def _find_env_file(self, filename: str) -> Path:
        """Find the .env file in the current directory.

        Args:
            filename (str): The name of the environment file.

        Raises:
            FileNotFoundError: If the .env file is not found.

        Returns:
            Path: Path to the .env file.
        """
        env_file = list(Path(".").rglob(f"{filename}*"))
        if not env_file:
            raise FileNotFoundError(f"Unable to locate file {filename}")
        return env_file[0]

    def _load_file(self) -> list[str]:
        """Reads the content from the environment file.

        Raises:
            Exception: When an uncaught error occurs.

        Returns:
            list[str]: Returns the list of lines from the file.
        """
        try:
            with open(self._filename, "r") as file:
                return file.readlines()
        except Exception as error:
            raise Exception(f"Error reading file {self._filename}: {error}")

    def _extract_key_value(self, line: str) -> Dict[str, str]:
        """Extracts the key and value from the line.

        Args:
            line (str): The content line from the environment file.

        Raises:
            ValueError: When the line format is incorrect.

        Returns:
            dict[str, str]: Returns the key-value pair from the line.
        """
        line = line.strip()
        if not line or line.startswith("#"):  # Ignore empty lines or comments
            return {}

        try:
            key, _, value = line.partition("=")
            if not key or not value:
                raise ValueError(f"Invalid line: {line}")
            return {key.strip(): value.strip()}
        except ValueError as error:
            raise ValueError(f"Error parsing line '{line}': {error}")

    def load_env(self) -> Dict[str, str]:
        """Loads environment variables from the file.

        Raises:
            Exception: If there is an error loading the file.

        Returns:
            dict[str, str]: A dictionary of environment variables.
        """
        try:
            file_contents = self._load_file()
            env_values: dict[str, str] = {}
            for content in file_contents:
                env_values.update(self._extract_key_value(content))
            self.env_values = env_values
            return env_values
        except Exception as error:
            raise Exception(f"Error loading .env file: {error}")

    def get_value(self, key: str) -> str:
        """Returns the value of the given environment variable.

        Args:
            key (str): The key of the environment variable.

        Raises:
            KeyError: If the key is not found.

        Returns:
            str: The value of the environment variable.
        """
        value = self.env_values.get(key, "")
        if value is None:
            raise KeyError(f"Environment variable '{key}' not found.")
        return value