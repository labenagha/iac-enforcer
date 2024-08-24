# Azure CAF Naming Enforcer

This project is designed to enforce Azure Cloud Adoption Framework (CAF) naming conventions for specific Azure resources, such as resource groups, virtual machines, and DNS zones. The goal is to ensure that all defined resources in Infrastructure as Code (IaC) files (e.g., Terraform) comply with user-defined naming rules, following Azure CAF standards.

## Project Overview

The tool reads an IaC file, parses the defined resources, and checks whether the resource names conform to Azure CAF naming standards based on regular expression patterns defined in a configuration file (`config.yaml`). If a resource name does not comply with the expected pattern, the tool will flag it as a failure.

## Features

- **Enforces Azure CAF Naming Conventions**: Supports enforcing naming conventions for Azure resource groups, virtual machines, and DNS zones.
- **Extensible**: Easily add more Azure resources or modify existing rules.
- **Configurable Rules**: Define custom naming rules using regular expressions in the `config.yaml` file.
- **Simple Integration**: Can be integrated into CI/CD pipelines to enforce naming conventions automatically during code reviews.

## Project Structure

```plaintext
iac-enforcer/
│
├── azure/
│   ├── resource_group.py        # Enforces naming for Resource Groups
│   
│                    
│
├── config.yaml                  # Configuration file for naming rules
├── iac_enforcer.py              # Main script to orchestrate the checks
├── utils.py                     # Utility functions for name validation
└── tests/
    └── test_iac_enforcer.py     # Unit tests
```

### File Descriptions

- **`config.yaml`**: Defines the naming conventions for the Azure resources using regular expressions. This file is fully customizable to suit your project's needs.
- **`iac_enforcer.py`**: The main script that loads the configuration, parses the IaC files, and calls the appropriate validation functions for each resource type.
- **`azure/resource_group.py`**: Contains the logic to enforce naming conventions for resource groups.
- **`utils.py`**: Contains shared utility functions, such as pattern matching, that are used across the resource-specific validation files.
- **`tests/`**: Contains unit tests to validate that the naming enforcer works correctly.

## Configuration

The naming conventions are defined using regular expressions in `config.yaml`. These patterns can be customized for each resource type.

Example `config.yaml`:

```yaml
rules:
  resource_group:
    name_pattern: "^rg-[a-zA-Z0-9]+-[a-zA-Z0-9]+$"

```

- **Resource Group Naming Convention**: Must follow the pattern `rg-<workload>-<environment>`.

## Usage

### Prerequisites

- Python 3.x
- Required Python libraries (can be installed via `pip`):

```bash
pip install -r requirements.txt
```

### Running the Tool

To use the tool, run the `iac_enforcer.py` script with your Terraform file as input. The script will parse the file, validate the resource names, and provide output indicating whether the names follow the defined Azure CAF naming conventions.

```bash
python iac_enforcer.py
```

For example, if the resource names in your Terraform file follow the naming conventions defined in `config.yaml`, you will see output like this:

```
Resource Group 'rg-myapp-dev' passed validation.
```

If the resource names do not follow the conventions, you will see error messages like this:

```
Resource 'Resource Group' does not follow the naming convention!
```

### Example Terraform File (`example.tf`)

Here's a sample Terraform file that defines some Azure resources:

```hcl
resource "azurerm_resource_group" "example" {
  name     = "rg-myapp-dev"
  location = "West Europe"
}

```

## Extensibility

This project is designed to be modular and easily extendable. To add more resources or modify the naming rules:

1. Add the corresponding validation logic in a new file under the `azure/` folder (e.g., `storage_account.py`).
2. Define the naming rules in `config.yaml`.
3. Update `iac_enforcer.py` to handle the new resource type.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests with any improvements, bug fixes, or new features. Make sure to add tests for any new functionality.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```