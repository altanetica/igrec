# Nater API Documentation

Используется ZeroMQ  

### Сообщения, не требующие ответа

Для сообщений без ответа [Push/Pull] запросы (порт **5558**)  

### Сообщения, требующие ответ

Для сообщений требующих ответ [Request/Response] запросы (порт **5559**)

## Формат сообщения:

    {
        "module": string
        "action": string
        "data": null, object, array
    }

### Пример сообщения без данных:

    {
        "module": "self",
        "action": "test",
        "data": null
    }

### Пример сообщения с одним экземпляром данных:

    {
        "module": "self",
        "action": "test",
        "data": {
            "ping": 10
        }
    }

### Пример с массивом данных:

    {
        "module": "self",
        "action": "test",
        "data": [
            {
                "ping": "hello",
                "pong": "world"
            },
            {
                "test": "test"
            }
        ]
    }

## Формат ответа:

    {
        "code": number
        "data": null, object, array 
        "errors": null, object, array
    }

Для **code** доступны следующие значения:
- `0` - выполнено без ошибок 
- `1` - выполнено с ошибками
- `-1` - не выполнено

Поле `errors` содержит `null` или объект (массив объектов) вида: 

    {
        "param": string
        "message": string
    }

### Пример успешно выполненной команды:

    {
        "code": 0, 
        "data": [
            {
                "ip": "10.0.2.2", 
                "mac": "52:54:00:12:35:02", 
                "state": 2
            }, 
            {
                "ip": "185.10.80.2", 
                "mac": "00:11:22:33:44:55", 
                "state": 128
            }, 
            {
                "ip": "127.0.0.1", 
                "mac": "00:00:00:00:00:00", 
                "state": 64
            }
        ], 
        "errors": null
    }

### Пример выполнения с ошибками:

    {
        "code": 1, 
        "data": {
            "mac": "02:03:04:05:06:07"
        }, 
        "errors": [
            {
                "message": "Invalid Value", 
                "param": "{'mac': u'02:03:04:05:06:QQ'}"
            }
        ]
    }

### Пример невыполненной команды:

    {
        "code": -1, 
        "data": null, 
        "errors": [
            {
                "message": "Not in module list", 
                "param": "authlist"
            }
        ]
    }

Доступные модули:

* `self` - Управление самим API
* `auth` - Авторизация
* `whitelist` - Список IP, доступ на которые не требует авторизации
* `keepttl` - Список IP, для которых не нужно менять ttl
* `arp` - Управление arp-записями
* `shaper` - (в разработке) Управление трафик-шейпером (в разработке)
* `ratelimit` - (в разработке) управление ratelimit (автошейпир)
* `dhcp` - (в разработке) управление dhcp
* `dnat` - (в разработке) dnat-mapper для internal static
