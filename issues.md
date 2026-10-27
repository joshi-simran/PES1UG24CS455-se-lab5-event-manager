# Lab 5: Static Code Analysis — Issues and Fixes

| Issue | Type | Line(s) Before Fix | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe deserialization using pickle | Security | 2, 51 | `pickle.load()` can execute malicious code when loading untrusted data. | Replaced pickle serialization with JSON. |
| Shell command injection risk | Security | 56 | `os.system()` constructs a shell command using the event name. | Removed shell execution and returned a validated badge filename instead. |
| Insecure random generator | Security | 72 | `random.choice()` was flagged by Bandit for security-sensitive random selection. | Replaced it with `secrets.choice()`. |
| Mutable default argument | Bug | 9 | `guests=[]` could share a list between function calls. | Changed the default to `None` and initialized a new list inside the function. |
| Non-standard function names | Style | Multiple | Function names used camelCase rather than snake_case. | Renamed functions to follow Python naming conventions. |
| Missing docstrings | Maintainability | Multiple | Functions and the module lacked explanatory docstrings. | Added module and function docstrings. |
| Unused sorting parameter | Code quality | 39 | `sortOrder` was accepted but never used. | Removed the unused parameter. |
| Formatting violations | Style | Multiple | Missing spaces and blank lines violated Flake8 rules. | Corrected spacing and blank-line formatting. |

