# pogopowerupcost [![Build status](https://travis-ci.org/mathiasbynens/pogopowerupcost.svg?branch=master)](https://travis-ci.org/mathiasbynens/pogopowerupcost) [![PyPI version](https://img.shields.io/pypi/v/pogopowerupcost.svg)](https://pypi.python.org/pypi/pogopowerupcost)

_pogopowerupcost_ makes it easy to calculate how much stardust and candy it takes to power-up a Pokémon from level `a` to level `b` in Pokémon GO.

## Installation

Using [pip](https://pip.pypa.io/):

```sh
$ pip install pogopowerupcost
```

## Usage

```py
from pogopowerupcost import calculate_powerup_cost

cost = calculate_powerup_cost(4.5, 20)
print(cost)
# → {'stardust': 43000, 'candy': 49}
```

## Author

| [![twitter/mathias](https://gravatar.com/avatar/24e08a9ea84deb17ae121074d0f17125?s=70)](https://twitter.com/mathias "Follow @mathias on Twitter") |
|---|
| [Mathias Bynens](https://mathiasbynens.be/) |

## License

_pogopowerupcost_ is available under the [MIT](https://mths.be/mit) license.
