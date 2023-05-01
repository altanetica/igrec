# Модуль SELF

Модуль *self* используется для управления сервисом

## Поддерживает следующие команды:

* `add` - не реализовано
* `remove` - не реализовано
* `flush` - не реализовано
* `enable` - включить рабоыт системы
* `disable` - отключить (пропускать трафик)
* `check` - проверка работоспособности
* `list` - не реализовано
* `status` - позволяет получить статус (enabled/disabled)
* `counters` - не реализовано
* `test` - используется только в автотесте
* `save` - не реализовано

### `add` - не реализовано

Запрос:

    {
        "module": "self",
        "action": "add",
        "data": null
    }

Ответ:

    {
        "code": -1, 
        "data": null, 
        "errors": [
            {
                "message": "Not implement", 
                "param": "self.add"
            }
        ]
    }

### `remove` - не реализовано

Запрос:

    {
        "module": "self",
        "action": "remove",
        "data": null
    }

Ответ:

    {
        "code": -1, 
        "data": null, 
        "errors": [
            {
                "message": "Not implement", 
                "param": "self.remove"
            }
        ]
    }

### `flush` - не реализовано

Запрос:

    {
        "module": "self",
        "action": "flush",
        "data": null
    }

Ответ:

    {
        "code": -1, 
        "data": null, 
        "errors": [
            {
                "message": "Not implement", 
                "param": "self.flush"
            }
        ]
    }

### `enable` - включить работу системы

Запрос:

    {
        "module": "self",
        "action": "enable",
        "data": null
    }

Ответ:

    {
        "code": 0, 
        "data": null, 
        "errors": null
    }

### `disable` - отключить (пропускать трафик прозрачно)

Запрос:

    {
        "module": "self",
        "action": "disable",
        "data": null
    }

Ответ:

    {
        "code": 0, 
        "data": null, 
        "errors": null
    }

### `check` - возращает значение, переданное в параметре `ping`

Запрос:

    {
        "module": "self",
        "action": "check",
        "data": {
            "ping": 10
        }

Ответ:

    {
        "code": 0, 
        "data": {
            "pong": 10
        }, 
        "errors": null
    }


### `list` - не реализовано

Запрос:

    {
        "module": "self",
        "action": "list",
        "data": null
    }

Ответ:

    {
        "code": -1, 
        "data": null, 
        "errors": [
            {
                "message": "Not implement", 
                "param": "self.list"
            }
        ]
    }

### `status` - позволяет получить статус (текущий режим) (enabled/disabled)

Запрос:

    {
        "module": "self",
        "action": "status",
        "data": null
    }

Ответ:

    {
        "code": 0, 
        "data": {
            "status": "enabled"
        }, 
        "errors": null
    }

### `counters` - не реализовано

Запрос:

    {
        "module": "aut"
        "action": "add"
        "data": null

Ответ:

    {
        "code": -1, 
        "data": null, 
        "errors": [
            {
                "message": "Not implement", 
                "param": "self.counters"
            }
        ]
    }

### `test` - не реализовано

Запрос:

    {
        "module": "self",
        "action": "test",
        "data": null
    }

Ответ:

    {
        "code": -1, 
        "data": null, 
        "errors": [
            {
                "message": "Not implement", 
                "param": "self.test"
            }
        ]
    }

### `save` - не реализовано

Запрос:

    {
        "module": "self",
        "action": "save",
        "data": null,
    }

Ответ:

    {
        "code": -1, 
        "data": null, 
        "errors": [
            {
                "message": "Not implement", 
                "param": "self.save"
            }
        ]
    }

