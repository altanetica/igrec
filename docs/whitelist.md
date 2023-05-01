# Модуль WHITELIST

Модуль *whitelist* используется для управления списком IP, доступ на которые возможен без авторизации 
Позволяет добавлять, удалять IP-адреса
Выводит список IP-адресов с whitelist

## Поддерживает следующие команды:

* `add` - добавляет ip в список
* `remove` - убирает ip из списка
* `flush` - очищает список
* `enable` - включает модуль
* `disable` - отключает модуль
* `check` - проверяет на наличие в списке
* `list` - выводит список
* `status` - позволяет получить статус (enabled/disabled)
* `counters` - кол-во IP в списке
* `test` - не реализовано
* `save` - сохраняет список

### `add` - добавить ip

Запрос:

    {
        "module": "whitelist",
        "action": "add",
        "data": {
            "ip": "8.8.8.8"
        }
    }

Ответ:

    {
        "code": 0, 
        "data": {
            "ip": "8.8.8.8"
        }, 
        "errors": null
    }

### `remove` - убрать ip

Запрос:

    {
        "module": "whitelist",
        "action": "remove",
        "data": {
            "ip": "8.8.8.8"
        }
    }

Ответ:

    {
        "code": 0, 
        "data": {
            "ip": "8.8.8.8"
        }, 
        "errors": null
    }

### `flush` - очистить список

Запрос:

    {
        "module": "whitelist",
        "action": "flush",
        "data": null
    }

Ответ:

    {
        "code": 0, 
        "data": null,
        "errors": null
    }

### `enable` - включить список

Запрос:

    {
        "module": "whitelist",
        "action": "enable",
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

### `disable` - отключить список

Запрос:

    {
        "module": "whitelist",
        "action": "disable",
        "data": null
    }

Ответ:

    {
        "code": 0, 
        "data": {
            "status": "disabled"
        }, 
        "errors": null
    }

### `check` - проверить наличие IP в списке

Запрос:

    {
        "module": "whitelist",
        "action": "check",
        "data": {
            "ip": "8.8.8.8"
        }
    }

Ответ:

    {
        "code": 0, 
        "data": {
            "mac": "8.8.8.8"
        }, 
        "errors": null
    }

Или:

    {
        "code": 0, 
        "data": null,
        "errors": null
    }


### `list` - вывести список

Запрос:

    {
        "module": "whitelist",
        "action": "list",
        "data": null
    }

Ответ:

    {
        "code": 0, 
        "data": [
            {
                "ip": "8.8.8.8",
            },
            {
                "ip": "8.8.4.4",
            },
        ], 
        "errors": null
    }

### `status` - получить текущий режим работы

Запрос:

    {
        "module": "whitelist",
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

### `counters` - кол-во IP адресов в списке

Запрос:

    {
        "module": "whitelist",
        "action": "counters",
        "data": null
    }

Ответ:

    {
        "code": 0, 
        "data": {
            "count": 1001
        }, 
        "errors": null
    }

### `test` - не реализовано

Запрос:

    {
        "module": "whitelist",
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
                "param": "whitelist.test"
            }
        ]
    }

### `save` - сохраняет список

Запрос:

    {
        "module": "whitelist",
        "action": "save",
        "data": null,
    }

Ответ:

    {
        "code": -1, 
        "data": null, 
        "errors": null
    }

