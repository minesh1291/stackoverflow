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
