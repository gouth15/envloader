# EnvLoader

EnvLoader is a lightweight Python package for managing environment variables in your project. It simplifies loading and accessing key-value pairs from a `.env` file, making it easier to manage application configurations.

---

## Installation

Install EnvLoader directly from the GitHub repository:

```bash
pip install git+https://github.com/gouth15/envloader.git
```

---

## Usage

### Initialize EnvLoader
Create an instance of the `EnvLoader` class by specifying the filename of your `.env` file (defaults to `.env` if not provided).

```python
from envloader import EnvLoader

# Initialize EnvLoader (default file: .env)
env_loader = EnvLoader()

# Alternatively, specify a custom file
env_loader = EnvLoader(filename="config.env")
```

---

### Load Environment Variables
The `EnvLoader` automatically loads environment variables when initialized. You can also manually reload the `.env` file using the `load_env()` method.

```python
# Reload environment variables from the file
env_loader.load_env()

# Access the loaded environment variables as a dictionary
print(env_loader.env_values)  # Outputs: {'DATABASE_URL': '...', 'SECRET_KEY': '...'}
```

---

### Access Environment Variables
#### Method 1: Use `get_value()`  
Retrieve the value of a specific environment variable using the `get_value()` method.

```python
# Access a specific environment variable
database_url = env_loader.get_value("DATABASE_URL")
print(f"Database URL: {database_url}")
```

#### Method 2: Attribute Access  
Access environment variables directly as attributes of the `EnvLoader` instance.

```python
# Direct attribute access
secret_key = env_loader.SECRET_KEY
print(f"Secret Key: {secret_key}")
```

---

## Features

- **Automatic Parsing**: Automatically parses `.env` files into key-value pairs.
- **Flexible Access**: Retrieve environment variables via dictionary, method calls, or attributes.
- **Error Handling**: Raises clear exceptions for missing files, invalid lines, or missing keys.
- **Dynamic Reload**: Reload the `.env` file anytime using `load_env()`.

---

## .env File Format

The `.env` file should consist of key-value pairs in the format `KEY=VALUE`. Comments can be added using the `#` symbol.

Example `.env` file:

```
# Application configuration
DATABASE_URL=postgres://user:password@localhost/dbname
SECRET_KEY=supersecretkey
DEBUG=True
```

---

## API Reference

### `EnvLoader`
#### Attributes
- **`env_values`**: A dictionary containing all loaded environment variables.

#### Methods
1. **`load_env()`**
   - Reloads environment variables from the `.env` file.
   - **Returns**: A dictionary of environment variables.

2. **`get_value(key: str) -> str`**
   - Retrieves the value of a specific environment variable.
   - **Args**:
     - `key` (str): The name of the environment variable.
   - **Raises**: 
     - `KeyError` if the variable is not found.
   - **Returns**: The value of the specified environment variable.

---

## Repository

- **GitHub Repository**: [EnvLoader](https://github.com/gouth15/envloader)