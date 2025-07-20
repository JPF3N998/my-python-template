# my-python-template

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Virtual Env

```console
hatch shell
```

## Running lint and format check

```console
hatch run dev:check
```

## Running Tests

### Unit Tests

```console
# Remember to check which venv you are using, should be Hatch's

hatch run test
```

# Building for Prod

```console
hatch shell -e production
```

## License

`my-python-template` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
