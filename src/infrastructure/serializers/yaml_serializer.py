import yaml

class YamlSerializer:
    def serialize(self, data: dict) -> str:
        return yaml.dump(data, sort_keys=False)