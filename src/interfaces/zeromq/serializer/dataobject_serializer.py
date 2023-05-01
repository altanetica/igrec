import json


class DataObjectEncoder(json.JSONEncoder):
    def default(self, o):
        """
        :type o: shared.dataobject.DataObject
        """
        try:
            if o.is_empty():
                data = None
            elif len(o.data) == 1:
                d = o.data[0]
                data = d.__dict__
            else:
                data = []
                for d in o.data:
                    data.append(d.__dict__)
            if o.has_errors():
                errors = []
                for e in o.errors:
                    errors.append(e.__dict__)
            else:
                errors = None
            to_serialize = {
                'models': data,
                'errors': errors,
            }
            return to_serialize
        except AttributeError:
            return json.JSONEncoder().default(o)
