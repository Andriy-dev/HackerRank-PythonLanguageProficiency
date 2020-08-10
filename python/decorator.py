def uppercase(func): 
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        modified_result = original_result.upper() 
        return modified_result
    return wrapper

def addspaces(func):
    def wrapper(*args, **kwargs):
       original_result = func(*args, **kwargs)
       modified_result = "".join([x+" " for x in original_result]) 
       return modified_result
    return wrapper

@addspaces
@uppercase
def test(text):
    return text

