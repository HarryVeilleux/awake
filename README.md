# Awake

Single function (awake) which keeps your computer awake and tricks some chat apps (Skype, Teams) into thinking you're online by using pyautogui to press volumeup, wait (default 150 seconds), press volumedown, wait, then loop until user exits.

I have only tested this for Skype and Teams. I have no idea if it works for Slack, Google apps, etc. Please let me know if you confirm one way or the other.

## Installation

From your shell of choice, run

```bash
pip install git+https://github.com/HarryVeilleux/awake.git
```

## Usage

In Python environment, run

```python
from awake import awake
```

Then execute `awake()` any time you want to keep your computer awake. Function will loop until you hit the escape character or close the window.
