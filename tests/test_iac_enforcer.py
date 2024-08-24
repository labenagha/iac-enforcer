import unittest
from azure.resource_group import validate_resource_group
# from azure.virtual_machine import validate_virtual_machine
# from azure.dns import validate_dns_zone

class TestAzureNamingEnforcer(unittest.TestCase):

    def setUp(self):
        # Define mock configurations from config.yaml
        self.resource_group_config = {
            'name_pattern': "^rg-[a-zA-Z0-9]+-[a-zA-Z0-9]+$"
        }

        # self.virtual_machine_config = {
        #     'name_pattern': "^vm-[a-zA-Z0-9]+-[a-zA-Z0-9]+-[a-zA-Z]{2}$"
        # }

        # self.dns_config = {
        #     'name_pattern': "^[a-zA-Z0-9]+\\.example\\.com$"
        # }

    # Test for Resource Group Naming
    def test_resource_group_valid_name(self):
        resource_name = "rg-myapp-dev"
        self.assertTrue(validate_resource_group(self.resource_group_config, resource_name))

    def test_resource_group_invalid_name(self):
        resource_name = "myapp-dev"
        self.assertFalse(validate_resource_group(self.resource_group_config, resource_name))

    # # Test for Virtual Machine Naming
    # def test_virtual_machine_valid_name(self):
    #     resource_name = "vm-myapp-dev-we"
    #     self.assertTrue(validate_virtual_machine(self.virtual_machine_config, resource_name))

    # def test_virtual_machine_invalid_name(self):
    #     resource_name = "myapp-dev-we"
    #     self.assertFalse(validate_virtual_machine(self.virtual_machine_config, resource_name))

    # # Test for DNS Naming
    # def test_dns_valid_name(self):
    #     resource_name = "myapp.example.com"
    #     self.assertTrue(validate_dns_zone(self.dns_config, resource_name))

    # def test_dns_invalid_name(self):
    #     resource_name = "myapp"
    #     self.assertFalse(validate_dns_zone(self.dns_config, resource_name))

if __name__ == '__main__':
    unittest.main()
