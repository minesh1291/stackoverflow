- Limit the cpu core number
```python

from keras import backend as K
import tensorflow as tf

tf.compat.v1.keras.backend.set_session(
  tf.compat.v1.Session(
    config=tf.compat.v1.ConfigProto(
      intra_op_parallelism_threads=15, 
      inter_op_parallelism_threads=15
      )
    )
  )

```
