from json import load
from envloader import EnvLoader
import pytest
import shutil
from pathlib import Path


@pytest.fixture(scope = "module")
def loader() -> EnvLoader:
    cache_path = Path(".pytest_cache")
    if cache_path.exists(): shutil.rmtree(cache_path)
    return EnvLoader("test/sample.env")

@pytest.fixture()
def expected_line_result(loader: EnvLoader):
    return loader._load_file()

class TestEnvLoader:

    def test_init(self, loader: EnvLoader):
        loader.__init__(str(loader._filename))
        assert(str(loader._filename) == "test/sample.env")
    
    def test_find_env_file(self, loader: EnvLoader):
        filepath1 = "./sample.env"
        filepath2 = "./sample2.env"
        assert(loader._find_env_file(filepath1) == loader._filename)
        with pytest.raises(FileNotFoundError):
            loader._find_env_file(filepath2)
    
    def test_load_file(self, loader: EnvLoader, expected_line_result: list[str]):
        expected_result1 = expected_line_result
        assert(loader._load_file() == expected_result1)
    
    def test_extract_key_value(self, loader: EnvLoader, expected_line_result: list[str]):
        result1 = loader._extract_key_value(expected_line_result[0])
        result2 = loader._extract_key_value(expected_line_result[3])
        print(expected_line_result)
        assert({"NAME": "JOHN_DOE"} == result1)
        assert({"SAMPLE VALUE": "SAMPLE KEY"} == result2)
    
    def test_setattr(self, loader: EnvLoader):
        print(loader.load_env())
        for key, value in loader.env_values.items():
            print(key, value)
            loader.__setattr__(key, value)
        assert(loader.LOCATION == "NEW YORK")
        with pytest.raises(AttributeError):
            assert(loader.SAMPLE == "SAMPLE")
            
    def test_getattr(self, loader):
        value = loader.NAME
        assert(value == "JOHN_DOE")
        with pytest.raises(AttributeError):
            loader.SAMPLE
            
    def test_dir(self, loader):
        assert("NAME" in loader.__dir__())
        with pytest.raises(AssertionError):
            assert("SAMPLE" in loader.__dir__())
        

    def test_env_values_type(self, loader):
        assert(isinstance(loader.env_values, dict))
    
    def test_load_env_type(self, loader):
        for key, value in loader.load_env().items():
            assert(isinstance(key, str))
            assert(isinstance(value, str))
            
    def test_get_key(self, loader):
        assert(hasattr(loader, "LOCATION"))
        value = loader.get_value("LOCATION")
        assert(value == "NEW YORK")
        with pytest.raises(AssertionError):
            assert(loader.get_value("SAMPLE") == "SAMPLE")
            
    def test_attribute_access(self, loader):
        assert(loader.AGE == "34")
            
        