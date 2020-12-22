- get disk size in python

```python
import psutil

hdd = psutil.disk_usage('/')

print ("Total: %d GiB" % hdd.total / (2**30))
print ("Used: %d GiB" % hdd.used / (2**30))
print ("Free: %d GiB" % hdd.free / (2**30))
```

- Generate a CSEK, AES-256 base-64 key.
```bash
python3 -c 'import base64; import os; print(base64.encodebytes(os.urandom(32)))'
```
- Logging to file and stdout
```python
import sys
import logging

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('my_log_info.log')
sh = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
fh.setFormatter(formatter)
sh.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(sh)

def hello_logger():
    logger.info("Hello info")
    logger.critical("Hello critical")
    logger.warning("Hello warning")
    logger.debug("Hello debug")

if __name__ == "__main__":
    print(hello_logger())
```
