## Core Requirements

- Use Japanese.

## Environment Information

- The development environment of this repository is configured with **Devcontainer**.
- The development environment runs within a Docker container.
- All commands should be executed inside the container. Running them on the host environment may not work as expected.

## Tooling

- **Editor**: The repository is designed to be used with Visual Studio Code.
- **Dependency Management**: `uv` is used for managing dependencies.
  - Copilot should consider workflows using `uv` for dependency-related tasks.

## Code Quality Requirements

- Use Python 3.12.
- Use Ruff for linting your code.
- Use Ruff for formatting your code.
- Use double quotes for strings.
- Use type hints for all functions and variables.
- Write unit tests using pytest.

## Notes

- Ensure that necessary configuration files (e.g., `.env`, `pyproject.toml`) are properly set up.
