# my-python-template

Powered by:

<a href="https://hatch.pypa.io/latest/" title="Hatch">
    <img src="https://hatch.pypa.io/latest/assets/images/logo.svg" alt="Hatch logo" style="max-width: 100%; height: 10svh;">
</a>

## Table of Contents

- [Virtual Env](#virtual-env)
- [Running lint and format check](#running-lint-and-format-check)
- [Running Tests](#running-tests)
- [Building for Prod](#building-for-prod)
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
