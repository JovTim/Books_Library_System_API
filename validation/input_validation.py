from dateutil.parser import parse, ParserError

def string_checker(value) -> bool:
    if type(value) != str:
        return False
    return True

def integer_checker(value) -> bool:
    if type(value) != int:
        return False
    return True

def is_valid_date(date):
    if not date:
        return False
    try:
        parsed_date = parse(date, fuzzy=False)
        return True
    except (ParserError, ValueError):
        return False

print(is_valid_date("sdasa"))
print(is_valid_date("2024-12-14")) 
