# Модуль KEEPTTL

**DEPRICATED** - модуль больтше не нужен

Модуль *keepttl* используется для управления списком авторизованных 
Позволяет добавлять, удалять авторизированные устройства (mac-адреса) 
Позволяет отключить авторизацию (значение по-умолчанию при старте системы)
Позволяет включить авторизацию
Выводит список авторизованных устройств

## Поддерживает следующие команды:

* `add` - добавляет IP в список
* `remove` - убирает IP из списка
* `flush` - очищает список
* `enable` - включает сохранение TTL (включено при старте)
* `disable` - отключает сохранение TTL (меняет всем на 1)
* `check` - проверяет на наличие в списке
* `list` - выводит список
* `status` - позволяет получить статус (enabled/disabled)
* `counters` - кол-во устройств в списке
* `test` - не реализовано
* `save` - сохраняет список

### `add` - добавить IP

Запрос:

    {
        "module": "keepttl",
        "action": "add",
        "data": {
            "ip": "185.10.80.2"
        }
    }

Ответ:

    {
        "code": 0, 
        "data": {
            "ip": "185.10.80.2"
        }, 
        "errors": null
    }

### `remove` - убрать IP

Запрос:

    {
        "module": "keepttl",
        "action": "remove",
        "data": {
            "ip": "185.10.80.2"
        }
    }

Ответ:

    {
        "code": 0, 
        "data": {
            "ip": "185.10.80.2"
        }, 
        "errors": null
    }

### `flush` - очистить список

Запрос:

    {
        "module": "keepttl",
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
        "module": "keepttl",
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
        "module": "keepttl",
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
        "module": "keepttl",
        "action": "check",
        "data": {
            "ip": "185.10.80.2"
        }
    }

Ответ:

    {
        "code": 0, 
        "data": {
            "mac": "185.10.80.2"
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
        "module": "keepttl",
        "action": "list",
        "data": null
    }

Ответ:

    {
        "code": 0, 
        "data": [
            {
                "ip": "185.10.80.2",
            },
        ], 
        "errors": null
    }

### `status` - получить текущий режим работы

Запрос:

    {
        "module": "keepttl",
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

### `counters` - кол-во IP адресов в списке

Запрос:

    {
        "module": "keepttl",
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
        "module": "keepttl",
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
        "module": "keepttl",
        "action": "save",
        "data": null,
    }

Ответ:

    {
        "code": 0, 
        "data": null, 
        "errors": null
    }

