import re

def check_name_pattern(resource, name, pattern):
    """
    Validate the naming convention of a resource based on a regex pattern.
    
    Args:
    - resource (str): The type of resource (e.g., Resource Group, Virtual Machine).
    - name (str): The name of the resource.
    - pattern (str): The regex pattern the name should follow.
    
    Returns:
    - bool: True if the name matches the pattern, False otherwise.
    """
    if not re.match(pattern, name):
        print(f"Resource '{resource}' does not follow the naming convention!")
        return False
    return True
