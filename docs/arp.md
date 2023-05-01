# Модуль ARP

Модуль *auth* используется для управления списком авторизованных 
Позволяет добавлять, удалять авторизированные устройства (mac-адреса) 
Позволяет отключить авторизацию (значение по-умолчанию при старте системы)
Позволяет включить авторизацию
Выводит список авторизованных устройств

## Поддерживает следующие команды:

* `add` - добавляет привязку IP-MAC (статик биндинг) в список
* `remove` - убирает mac из списка
* `flush` - очищает список
* `enable` - включает авторизацию
* `disable` - отключает авторизацию
* `check` - проверяет на наличие в списке
* `list` - выводит список
* `status` - позволяет получить статус (enabled/disabled)
* `counters` - кол-во устройств в списке
* `test` - не реализовано
* `save` - сохраняет список

### `add` - добавить mac

Запрос:

    {
        "module": "arp",
        "action": "add",
        "data": {
            "mac": "02:03:04:05:06:07",
            "ip": "185.10.80.2"
        }
    }

Ответ:

    {
        "code": 0, 
        "data": {
            "ip": "185.10.80.2",
            "mac": "02:03:04:05:06:07"
        }, 
        "errors": null
    }

### `remove` - убрать mac

Запрос:

    {
        "module": "arp",
        "action": "remove",
        "data": {
            "ip": "185.10.80.2"
        }
    }

Или:

    {
        "module": "arp",
        "action": "remove",
        "data": {
            "mac": "02:03:04:05:06:07"
        }
    }

Ответ:

    {
        "code": 0, 
        "data": {
            "ip": "185.10.80.2",
            "mac": "02:03:04:05:06:07"
        }, 
        "errors": null
    }

### `flush` - не реализовано

Запрос:

    {
        "module": "arp",
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
                "param": "arp.flush"
            }
        ]
    }

### `enable` - не реализовано

Запрос:

    {
        "module": "arp",
        "action": "enable",
        "data": null
    }

Ответ:

    {
        "code": -1, 
        "data": null, 
        "errors": [
            {
                "message": "Not implement", 
                "param": "arp.enable"
            }
        ]
    }

### `disable` - не реализовано

Запрос:

    {
        "module": "arp",
        "action": "disable",
        "data": null
    }

Ответ:

    {
        "code": -1, 
        "data": null, 
        "errors": [
            {
                "message": "Not implement", 
                "param": "arp.disable"
            }
        ]
    }

### `check` - проверить наличие ip / mac

Запрос:

    {
        "module": "arp",
        "action": "check",
        "data": {
            "ip": "185.10.80.2"
        }
    }

Или:

    {
        "module": "arp",
        "action": "check",
        "data": {
            "mac": "02:03:04:05:06:07"
        }
    }

Ответ:

    {
        "code": 0, 
        "data": null,
        "errors": null
    }

Или:

    {
        "code": 0, 
        "data": {
            "mac": "02:03:04:05:06:07",
            "ip": "185.10.80.2",
            "state": 1
        }, 
        "errors": null
    }

Где `state` принимает следующие значения:

 * permanent - 128
 * noarp - 64
 * stale - 4
 * reachable - 2
 * none - 0
 * incomplete - 1
 * delay - 8
 * probe - 16
 * failed - 32

### `list` - вывести список

Запрос:

    {
        "module": "arp",
        "action": "list",
        "data": null
    }

Ответ:

    {
        "code": 0, 
        "data": [
            {
                "mac": "02:03:04:05:06:07",
                "ip": "185.10.80.2",
                "state": 1
            },
        ], 
        "errors": null
    }

Где `state` принимает следующие значения:

 * permanent - 128
 * noarp - 64
 * stale - 4
 * reachable - 2
 * none - 0
 * incomplete - 1
 * delay - 8
 * probe - 16
 * failed - 32

### `status` - не реализовано

Запрос:

    {
        "module": "arp",
        "action": "status",
        "data": null
    }

Ответ:

    {
        "code": -1, 
        "data": null, 
        "errors": [
            {
                "message": "Not implement", 
                "param": "auth.status"
            }
        ]
    }

### `counters` - кол-во mac адресов в списке

Запрос:

    {
        "module": "arp",
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
        "module": "arp",
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

### `save` - сохраняет список добавленных перманентно маков

Запрос:

    {
        "module": "arp",
        "action": "save",
        "data": null,
    }

Ответ:

    {
        "code": 0, 
        "data": null, 
        "errors": null
    }
