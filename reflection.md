# Lab 5: Static Code Analysis — Reflection

**1. What is static code analysis?**

Static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and coding-style violations.

**2. What did Pylint, Bandit, and Flake8 help identify?**

Pylint identified code-quality problems such as missing docstrings, inconsistent naming, mutable default arguments, and unused parameters. Bandit identified potentially unsafe deserialization and shell-command execution. Flake8 identified formatting violations such as missing whitespace and blank lines.

**3. How were the identified issues resolved?**

The code was updated to use JSON instead of pickle, remove shell execution, use `secrets.choice()`, avoid mutable default arguments, follow snake_case naming, add docstrings, remove unused parameters, and correct formatting issues.

**4. How does static analysis improve software quality?**

Static analysis helps detect potential problems early, improves readability and maintainability, and highlights insecure coding practices before they become larger issues. Using multiple tools provides complementary checks for security, code quality, and style.
