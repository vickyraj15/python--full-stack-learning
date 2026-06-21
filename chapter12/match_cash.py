def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "Internel server error"
        case _:
            return "unknow server"
        
print(http_status(5005))        