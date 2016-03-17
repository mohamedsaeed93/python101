import json


class JsonAssignment:
    def __init__(self):
        self.attribute1 = "attribute1"
        self.attribute2 = 2
        self.attribute3 = {'key1': "value", 'key2': 1}
        self.attribute4 = [1, 2, 3, 4]

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class_object = JsonAssignment()
print(class_object)
class_object.attribute5 = (1, 2, 3, 4, 5)
print(class_object)
