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

- Force GPU usage with context
```python
# list physical devices
gpus = tf.config.experimental.list_physical_devices('GPU')
# log device placement
tf.debugging.set_log_device_placement(True)

with tf.device('/device:GPU:0'):
    model = get_model()
```

- keras.utils.plot_model, dependancies
```bash
sudo apt install graphviz
pip install pydot graphviz pydotplus
```

- Plot Learning Curve
```python
def plot_lcurve(model, metrics=["loss"], name="default.jpg"):

    fig, ax = plt.subplots(len(metrics),1, figsize=(8, 6))
    if len(metrics)==1:
        ax=[ax]
    for metric, axi in zip(metrics, ax):
        axi.set_title(metric)
        axi.plot(model.history.history[metric], ".--", label="tr")
        axi.plot(model.history.history[f'val_{metric}'], ".--", label="val")
        axi.legend()
    plt.tight_layout()
    plt.savefig(name)
    plt.show()

plot_lcurve(model)
```


- Configure tensorflow keras log level
```python
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = "2"
import tensorflow as tf
import numpy as np
a = tf.Variable(np.array([0, 1, 2]))
print(a)
```

- Ways to Regularize Network 
  1. L1, L2 Weight Regularization
  2. Batch Normalization
  3. Dropout
  4. Using larger batches
  5. Label Smoothing
 

