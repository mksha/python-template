# my-package

A short description of your package.

## Installation

```bash
pip install my-package
```

Or install from TestPyPI (dev builds):

```bash
pip install --index-url https://test.pypi.org/simple/ my-package
```

## Usage

### As a library

```python
from my_package import greet, add

print(greet("World"))  # Hello, World!
print(add(2, 3))       # 5
```

### As a CLI

```bash
my-package hello Alice
# Hello, Alice!

my-package --version
# my-package, version 1.0.0
```

## Development

### Prerequisites

- [uv](https://docs.astral.sh/uv/) (Python package manager)
- Git

### Setup

```bash
# Clone the repo
git clone https://github.com/yourname/my-package.git
cd my-package

# Install dependencies (creates .venv automatically)
uv sync --extra dev

# Install pre-commit hooks
uv run pre-commit install
```

### Common commands

```bash
# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov

# Lint
uv run ruff check .

# Format
uv run ruff format .

# Type check
uv run mypy .

# Build locally
uv build

# Check current version (from git)
uvx --from hatch hatch version
```

### Adding dependencies

```bash
# Add a runtime dependency
uv add requests

# Add a dev dependency
uv add --extra dev hypothesis
```

## Release workflow

Releases are automated via GitHub Actions. Version is derived from git tags using `hatch-vcs`.

| Action | Trigger | Version | Target |
| --- | --- | --- | --- |
| Dev release | Push to feature branch | `x.y.z.devN` | TestPyPI |
| Pre-release | Tag `vX.Y.ZrcN` on main | `X.Y.ZrcN` | PyPI |
| Stable release | Tag `vX.Y.Z` on main | `X.Y.Z` | PyPI |

### Creating a release

```bash
# First release candidate
git tag v1.0.0rc1
git push origin v1.0.0rc1

# Stable release
git tag v1.0.0
git push origin v1.0.0
```

## License

MIT
