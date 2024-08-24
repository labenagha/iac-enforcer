# Enforces Azure CAF rules for Resource Groups

from utils import check_name_pattern

def validate_resource_group(resource_config, resource_name):
    """
    Validate the resource group naming based on Azure CAF rules.
    
    Args:
    - resource_config (dict): The rule for validating resource group names.
    - resource_name (str): The name of the resource group.
    
    Returns:
    - bool: True if the resource group name is valid, False otherwise.
    """
    valid = check_name_pattern("Resource Group", resource_name, resource_config['name_pattern'])
    
    if valid:
        print(f"Resource Group '{resource_name}' passed validation.")
    else:
        print(f"Resource Group '{resource_name}' failed validation.")
    
    return valid
