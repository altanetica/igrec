import json


class ErrorDataObject(object):
    def __init__(self, param, message):
        self.param = param
        self.message = message

    def __str__(self):
        return 'ErrorDataObject: %s %s' % (self.param, self.message)


class ValidDataObject(object):
    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, adict):
        data = ValidDataObject()
        for key in adict:
            data.__setattr__(key, adict[key])
        return data

    def __str__(self):
        return 'ValidDataObject: ' + self.__dict__.__str__()


class ErrorDataObjectList(list):
    pass


class ValidDataObjectList(list):
    pass


class DataObject(object):
    def __init__(self, data=None):
        self.errors = ErrorDataObjectList()
        self.data = ValidDataObjectList()
        if isinstance(data, list):
            for d in data:
                self.add_data(d)
        elif isinstance(data, dict):
            self.add_data(data)
        elif data is None:
            pass
        else:
            self.add_error(data.__str__(), "Not valid object")

    def __nonzero__(self):
        return self.is_empty()

    __bool__ = __nonzero__

    def is_valid(self):
        return (not self.has_errors()) and len(self.data) > 0

    def is_empty(self):
        return not len(self.data) > 0

    def has_errors(self):
        return len(self.errors) > 0

    def add_data(self, adict):
        if isinstance(adict, dict):
            self.data.append(ValidDataObject.from_dict(adict))
        elif adict is None:
            pass
        else:
            self.add_error(adict.__str__(), "Not valid object")

    def add_error(self, param, message):
        self.errors.append(ErrorDataObject(param, message))

    def data_to_json(self):
        try:
            jsn = json.dumps(self.data)
            return jsn
        except TypeError:
            return None

    def __str__(self):
        return 'DataObject: ' + self.data.__str__() + ', ' + self.errors.__str__()
