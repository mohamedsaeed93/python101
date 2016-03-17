import json


class JsonAssignment:
    def __init__(self):
        self.attribute1 = "attribute1"
        self.attribute2 = 2
        self.attribute3 = {'key1': "value", 'key2': 1}
        self.attribute4 = [1, 2, 3, 4]
        self.children = []

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_children(self, children):
        self.children = children


class_object = JsonAssignment()
print(class_object)
print("--------------------------------------")
class_object.attribute5 = (1, 2, 3, 4, 5)
print(class_object)
print("--------------------------------------")
class_object2 = JsonAssignment()
class_object3 = JsonAssignment()
object_children = [class_object2, class_object3]
class_object.set_children(object_children)
print(class_object)
print("--------------------------------------")
