# Модуль AUTH

Модуль *auth* используется для управления списком авторизованных 
Позволяет добавлять, удалять авторизированные устройства (mac-адреса) 
Позволяет отключить авторизацию (значение по-умолчанию при старте системы)
Позволяет включить авторизацию
Выводит список авторизованных устройств

## Поддерживает следующие команды:

* `add` - добавляет mac в список
* `remove` - убирает mac из списка
* `flush` - очищает список
* `enable` - включает авторизацию
* `disable` - отключает авторизацию
* `check` - проверяет на наличие в списке
* `list` - выводит список
* `status` - позволяет получить статус (enabled/disabled)
* `counters` - кол-во устройств в списке
* `test` - не реализовано
* `save` - сохранить список

### `add` - добавить mac

Запрос:

    {
        "module": "auth",
        "action": "add",
        "data": {
            "mac": "02:03:04:05:06:07"
        }
    }

Ответ:

    {
        "code": 0, 
        "data": {
            "mac": "02:03:04:05:06:07"
        }, 
        "errors": null
    }

### `remove` - убрать mac

Запрос:

    {
        "module": "auth",
        "action": "remove",
        "data": {
            "mac": "02:03:04:05:06:07"
        }
    }

Ответ:

    {
        "code": 0, 
        "data": {
            "mac": "02:03:04:05:06:07"
        }, 
        "errors": null
    }

### `flush` - очистить список

Запрос:

    {
        "module": "auth",
        "action": "flush",
        "data": null
    }

Ответ:

    {
        "code": 0, 
        "data": null,
        "errors": null
    }

### `enable` - включить пропуск только авторизованных

Запрос:

    {
        "module": "auth",
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

### `disable` - отключить пропуск только авторизованных

Запрос:

    {
        "module": "auth",
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

### `check` - проверить наличие mac

Запрос:

    {
        "module": "auth",
        "action": "check",
        "data": {
            "mac": "02:03:04:05:06:07"
        }
    }

Ответ:

    {
        "code": 0, 
        "data": {
            "mac": "02:03:04:05:06:07"
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
        "module": "auth",
        "action": "list",
        "data": null
    }

Ответ:

    {
        "code": 0, 
        "data": [
            {
                "mac": "02:03:04:05:06:07",
            },
        ], 
        "errors": null
    }

### `status` - получить текущий режим работы

Запрос:

    {
        "module": "auth",
        "action": "status",
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

### `counters` - кол-во mac адресов в списке

Запрос:

    {
        "module": "auth",
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
        "module": "auth",
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
                "param": "auth.test"
            }
        ]
    }

### `save` - сохраняет список

Запрос:

    {
        "module": "auth",
        "action": "save",
        "data": null,
    }

Ответ:

    {
        "code": 0, 
        "data": null, 
        "errors": null
    }

