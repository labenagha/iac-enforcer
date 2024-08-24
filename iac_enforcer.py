import yaml
import hcl2
from azure.resource_group import validate_resource_group
# from azure.virtual_machine import validate_virtual_machine
# from azure.dns import validate_dns_zone

# Load configuration file
def load_config(config_file='config.yaml'):
    with open(config_file, 'r') as file:
        return yaml.safe_load(file)

# Main function to enforce naming rules
def enforce_rules(iac_file, config):
    with open(iac_file, 'r') as file:
        iac_data = hcl2.load(file)
        
        # Enforce Resource Group Naming
        for resource in iac_data.get('resource', []):
            if 'azurerm_resource_group' in resource:
                for instance_name, resource_details in resource['azurerm_resource_group'].items():
                    resource_name = resource_details.get('name')
                    if resource_name:
                        validate_resource_group(config['rules']['resource_group'], resource_name)
                    else:
                        print(f"Resource group '{instance_name}' does not have a name key.")

        # # Enforce Virtual Machine Naming
        # for resource in iac_data.get('resource', []):
        #     if 'azurerm_virtual_machine' in resource:
        #         resource_name = resource['azurerm_virtual_machine']['name']
        #         validate_virtual_machine(config['rules']['virtual_machine'], resource_name)

        # # Enforce DNS Zone Naming
        # for resource in iac_data.get('resource', []):
        #     if 'azurerm_dns_zone' in resource:
        #         resource_name = resource['azurerm_dns_zone']['name']
        #         validate_dns_zone(config['rules']['dns'], resource_name)

# Load configuration and enforce rules
config = load_config()
enforce_rules('terraform_tests/example.tf', config)
