import getpass
import json
from typing import Protocol

class FilterProtocol(Protocol):
    def validate(self,password: str) -> list:
        raise NotImplemented("Filter must have a implemented validate function!")

class Config:

    filter : FilterProtocol = None

    def __init__(self, filter: FilterProtocol = None):
        self.filter: FilterProtocol = filter

class FilterFactory:
    @staticmethod
    def from_dict(filter_dict):
        if "type" not in fiter_dict:
            raise TypeError("Filter must have a 'type' key!")
        if "args" not in fiter_dict:
            raise TypeError("Filter must have an 'args' key!")
        if filter_dict["type"] == "AndFilter":
            filters = []
            if "filters" not in filter_dict["args"]:
                raise TypeError("Filter must have a 'filters' key!")
            for f in filter_dict["args"]["filters"]:
                filters.append(FilterFactory.from_dict(f))
        else:
            args = filter_dict["args"]
            return globals()[filter_dict["type"]](**args)

class ConfigLoader:
    @staticmethod
    def load_from_file_byname(filename: str) -> Config:
        with open(filename, "r") as f:
            return ConfigLoader.load_from_file(f)

    @staticmethod
    def load_from_file(f) -> Config:
        data:str = f.read()
        return ConfigLoader.from_json_str(data)

    @staticmethod
    def from_json_str(data: str) -> Config:
        d = json.loads(data)
        return ConfigLoader.from_dict(d)

    @staticmethod
    def from_dict(d: dict) -> Config:
        config.filter = FilterFactory.from_dict(d["filter"])
        config = Config(filter)
        return config


class LengthFilter(FilterProtocol):
    def __init__(self, min: int= 4 , max: int = None):
        self.min = min
        self.max = max

    def validate(self,password: str) -> list:
        errors = []
        if len(password) < self.min:
            errors.append(f"Password length is smaller like the min({self.min})!")
        if self.max is not None and len(password) > self.max:
            errors.append(f"Password length is bigger like the max({self.max})!")
        return errors

class SpecialCharFilter(FilterProtocol):
    def __init__(self, special_chars = [".",",","*"], min = 1):
        self.special_chars = special_chars
        self.min = min

    def validate(self,password: str) -> list:
        errors = []
        special_chars = 0
        for char in self.special_chars:
            if char in password:
                special_chars += 1
        if special_chars < self.min:
            errors.append("Password must contain at least one special char!")
        return errors


class AndFilter(FilterProtocol):
    def __init__(self, filters: list):
        self.filters = filters

    def validate(self,password: str) -> list:
        errors = []
        for filter in self.filters:
            _error: list = filter.validate(password)
            errors += _error
        return errors


if __name__ == "__main__":
    filters = []
    special_char_filter = SpecialCharFilter()
    filters.append(special_char_filter)
    lenght_filter = LengthFilter(8)
    filters.append(lenght_filter)
    and_filter = AndFilter(filters)
    config = ConfigLoader.load_from_file_byname("config.json")
    while True:
        password = getpass.getpass("Check: ")
        errors = and_filter.validate(password)
        if len(errors) == 0:
            print("Password is ok")
        else:
            print("Password error:")
            for error in errors:
                print("\t",error)