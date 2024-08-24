
### `CONTRIBUTING.md` (Contribution Guidelines)

# Contributing to Azure CAF Naming Enforcer

Thank you for your interest in contributing to the Azure CAF Naming Enforcer! We welcome all contributions, whether it's reporting issues, suggesting new features, or submitting pull requests.

## How to Contribute

### Reporting Bugs or Issues

If you find a bug or have an issue using the tool, please open an issue in the [issue tracker](https://github.com/labenagha/iac-enforcer/issues). When reporting an issue, please include:

- A clear description of the issue.
- Steps to reproduce the issue.
- The expected behavior and what actually happened.

### Suggesting Features

If you have an idea for a new feature or improvement, feel free to open a feature request in the issue tracker. Please provide a detailed description of the feature, including potential use cases and how it would benefit users.

### Submitting Pull Requests

If you'd like to contribute code to the project, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top right of the repository page.
2. **Clone Your Fork**: Clone the repository to your local machine:
   
    ```bash
    git clone https://github.com/your-username/iac-enforcer.git
    cd iac-enforcer
    ```

3. **Create a New Branch**: Create a branch for your feature or fix:
   
    ```bash
    git checkout -b feature-name
    ```

4. **Make Changes**: Make your code changes in your new branch.
5. **Write Tests**: Ensure that your code is covered by unit tests in the `tests/` directory.
6. **Commit Your Changes**: Commit your changes with a meaningful message:

    ```bash
    git commit -m "Add feature: description of feature"
    ```

7. **Push Your Changes**: Push your changes to your fork on GitHub:

    ```bash
    git push origin feature-name
    ```

8. **Open a Pull Request**: Go to the original repository and open a pull request (PR). Describe your changes and link to any relevant issues.

### Code Style

Please ensure your code adheres to PEP 8 style guidelines for Python code.

### Running Tests

After making changes, ensure that all tests pass before submitting a pull request:

```bash
python -m unittest discover -s tests
