import json


class Config:
    def __init__(self, file='config.json'):
        self.file = file
        with open(self.file) as json_data_file:
            self.config = json.load(json_data_file)

    def get(self):
        return self.config
