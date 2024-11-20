# EnvLoader

EnvLoader is a Python package designed to simplify loading and accessing environment variables from a `.env` file. It reads key-value pairs from the file, stores them in memory, and allows easy access to configuration values across your application.

## Installation

```bash
pip install git+https://github.com/gouth15/envloader.git
```

## How to Use

### EnvLoader
Create an instance of the `EnvLoader` class, passing the filename of the `.env` file (defaults to `.env`).

```python
from envloader import EnvLoader

# Initialize EnvLoader (default file: .env)
env_loader = EnvLoader()
```

### 1. Load the Environment Variables
Call the `load_env()` method to load the environment variables from the `.env` file. This will populate the `env_values` dictionary with key-value pairs.

```python
# Load the environment variables from the file
env_loader.load_env()

# Access the loaded environment variables
print(env_loader.env_values)  # Outputs the dictionary of key-value pairs
```

### 2. Access Environment Variables
You can retrieve the value of a specific environment variable using the `get_value()` method.

```python
# Get the value of a specific key
database_url = env_loader.get_value("DATABASE_URL")
print(f"Database URL: {database_url}")
```

- **`EnvLoader`**: A class that loads all environment variables into a dictionary (`env_values`). You can access any environment variable by using `env_loader.get_value()` or by directly accessing the `env_values` dictionary.

### Functions

#### `EnvLoader`

- **`env_values`**: A dictionary containing all the environment variables loaded from the `.env` file.
- **`load_env()`**: Reads the `.env` file and loads the key-value pairs into the `env_values` dictionary. It returns the dictionary of environment variables.
- **`get_value(key: str)`**: Retrieves the value of a specific environment variable by its key. Returns the value associated with the given key.

### .env File Format

The `.env` file should contain key-value pairs in the following format:

```
# This is a comment
DATABASE_URL=postgres://user:password@localhost/dbname
SECRET_KEY=supersecretkey
```

## Repository

- GitHub Repository: [https://github.com/yourusername/envloader](https://github.com/yourusername/envloader)