# Python Hatch Managed Cookiecutter template

[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v0.json)](https://github.com/charliermarsh/ruff)
[![code style - Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

```bash
pip install cookiecutter
cookiecutter gh:KingMichaelPark/hatch-python-cookiecutter
```

## Preview of Generated Project

## Development

To work with your project you can drop into a shell that keeps your
dependencies synced with the entries in your `pyproject.toml` file. You can have
dependency groups there that allow for custom shells.

You can enter a shell simply with:

```bash
hatch shell
# You can still run other shell commands such as git helpers from within the shell
hatch run git:commit
```

Project dependencies for the build can be listed with:

```bash
❯ hatch dep show table
 Env: default
┏━━━━━━━━━━━━┓
┃ Name       ┃
┡━━━━━━━━━━━━┩
│ black      │
│ pytest     │
│ pytest-cov │
│ ruff       │
└────────────┘
```

You can update these and include sub shells in your pyproject.toml.
[Environments](https://hatch.pypa.io/latest/environment/#creation)

Working on the project source code with code-completion can be done by simply
calling: `hatch shell`.

## Versioning

Commitzen is used to handle the version bumping (Hatch can do this as well but
doesn't get git tags by default)[^1](https://hatch.pypa.io/latest/version/#versioning)

```bash
hatch run git:version
```

(It is really a wrapper for `cz bump {args}`)

```console
❯ hatch run git:version --help
```

## Committing

Helper functions for nice commit messages are also built-in using commitizen.

```bash
hatch run git:commit
```

## Building

Hatch complies with modern Python packaging specs and therefore your projects
can be used by other tools with Hatch serving as just the build backend.

Invoking the build command without any arguments will build the sdist and wheel targets:

[Build](https://hatch.pypa.io/latest/build/#building)

```bash
hatch build
```

## Publishing

After your project is built, you can distribute it using the publish command.

The `-p/--publisher` option controls which publisher to use, with the default
being index.

[Publish](https://hatch.pypa.io/latest/publish/#publishing)

```bash
hatch publish
```

## License

`{{ cookiecutter.project_slug }}` is distributed under the terms of the
[MIT](https://spdx.org/licenses/MIT.html) license.
