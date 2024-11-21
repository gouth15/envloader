from envloader import EnvLoader
import pytest
import shutil
from pathlib import Path


FILE_PATH = "test/sample.env"

def remove_pycache():
    """Remove the file or directory if it exists."""
    path = Path("./__pycache__")
    if path.exists():
        shutil.rmtree(path)

remove_pycache()


class TestEnvLoader:
    
    loader = EnvLoader(FILE_PATH)
    
    def test_setattr(self):
        for key, value in self.loader.env_values.items():
            print(key, value)
            self.loader.__setattr__(key, value)
        # print(self.loader.LOCATION)
        assert(self.loader.LOCATION == "NEW YORK")
        with pytest.raises(AttributeError):
            assert(self.loader.SAMPLE == "SAMPLE")
            
    def test_getattr(self):
        value = self.loader.NAME
        assert(value == "JOHN_DOE")
        with pytest.raises(AssertionError):
            assert(value == "SAMPLE")
            
    def test_dir(self):
        assert("NAME" in self.loader.__dir__())
        with pytest.raises(AssertionError):
            assert("SAMPLE" in self.loader.__dir__())
        

    def test_env_values_type(self):
        assert(isinstance(self.loader.env_values, dict))
    
    def test_load_env_type(self):
        for key, value in self.loader.load_env().items():
            assert(isinstance(key, str))
            assert(isinstance(key, str))
            
    def test_get_key(self):
        assert(hasattr(self.loader, "LOCATION"))
        value = self.loader.get_value("LOCATION")
        assert(value == "NEW YORK")
        with pytest.raises(AssertionError):
            assert(self.loader.get_value("SAMPLE") == "SAMPLE")
            
    def test_attribute_access(self):
        assert(self.loader.AGE == "34")
            
        