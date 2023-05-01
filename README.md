###

# py_preformatted_logger

## Description

`py_preformatted_logger` creates a python logging object which can be used
in the place of logging.getLogger().  The resulting logger defaults to 
INFO level, and has the output format of

```
TIME_STAMP | LEVEL | FILENAME:LINE_NUMBER - MESSAGE
```


## Installation

```
python3 -m pip install  git+https://github.com/rhhayward/py_preformatted_logger.git@master
```

## Usage

### simple usage:

```
from preformatted_logger import preformatted_logger

logger = preformatted_logger.get_logger()
logger.info("message")
```

### override log level

```
from preformatted_logger import preformatted_logger

logger = preformatted_logger.get_logger(level='WARNING')
logger.info("message") ### will not output
logger.warning("message") ### will output
```
