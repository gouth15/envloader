from pathlib import Path
from typing import Any, Dict

class EnvLoader:
    """
    A class to load and parse environment variables from a `.env` file.

    The class locates a `.env` file in the current directory or its subdirectories,
    loads its content, and makes the variables accessible both as attributes and through
    a dictionary-like interface.
    """

    def __init__(self, filename: str = ".env") -> None:
        """
        Initialize the EnvLoader instance by locating and loading the `.env` file.

        Args:
            filename (str, optional): The name of the `.env` file. Defaults to ".env".
        """
        self._filename: Path = self._find_env_file(filename)
        self.env_values: Dict[str, str] = self.load_env()
        self.__dict__.update(self.env_values)
        
        # Set environment variables as attributes
        for key, value in self.env_values.items():
            self.__setattr__(key, value)

    def __setattr__(self, name: str, value: Any) -> None:
        """Set an attribute value."""
        super().__setattr__(name, value)

    def __getattr__(self, name: str) -> str:
        """
        Dynamically retrieve an environment variable's value as an attribute.

        Args:
            name (str): The name of the environment variable.

        Raises:
            AttributeError: If the environment variable is not found.

        Returns:
            str: The value of the environment variable.
        """
        if name in self.env_values:
            return self.env_values[name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    
    def __dir__(self):
        """Return the list of attributes (including environment variables)."""
        return super().__dir__()

    def _find_env_file(self, filename: str) -> Path:
        """
        Locate the `.env` file in the current directory or subdirectories.

        Args:
            filename (str): The name of the `.env` file.

        Raises:
            FileNotFoundError: If the `.env` file cannot be found.

        Returns:
            Path: The path to the located `.env` file.
        """
        env_file = list(Path(".").rglob(f"{filename}*"))
        if not env_file:
            raise FileNotFoundError(f"Unable to locate file {filename}")
        return env_file[0]

    def _load_file(self) -> list[str]:
        """
        Read the contents of the `.env` file.

        Raises:
            Exception: If an error occurs while reading the file.

        Returns:
            list[str]: A list of lines from the `.env` file.
        """
        try:
            with open(self._filename, "r") as file:
                return file.readlines()
        except Exception as error:
            raise Exception(f"Error reading file {self._filename}: {error}")

    def _extract_key_value(self, line: str) -> Dict[str, str]:
        """
        Parse a line from the `.env` file to extract a key-value pair.

        Args:
            line (str): A line of text from the `.env` file.

        Raises:
            ValueError: If the line is not in a valid key-value format.

        Returns:
            dict[str, str]: A dictionary containing a single key-value pair.
        """
        line = line.strip()
        if not line or line.startswith("#"):  # Ignore empty lines or comments
            return {}

        try:
            key, _, value = line.partition("=")
            if not key or not value:
                raise ValueError(f"Invalid line: {line}")
            return {key.split()[0]: value.split()[0]}
        except ValueError as error:
            raise ValueError(f"Error parsing line '{line}': {error}")

    def load_env(self) -> Dict[str, str]:
        """
        Load all environment variables from the `.env` file into a dictionary.

        Raises:
            Exception: If an error occurs during loading.

        Returns:
            dict[str, str]: A dictionary of key-value pairs from the `.env` file.
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
        """
        Retrieve the value of a specific environment variable by key.

        Args:
            key (str): The name of the environment variable.

        Raises:
            KeyError: If the specified key is not found in the environment variables.

        Returns:
            str: The value associated with the specified key.
        """
        value = self.env_values.get(key)
        if value is None:
            raise KeyError(f"Environment variable '{key}' not found.")
        return value
