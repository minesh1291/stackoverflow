- spliting data
```python
np.random.seed(1291)

idx_train, idx_test = train_test_split(range(n_samples), test_size=0.2, random_state=1)
idx_train, idx_val = train_test_split(idx_train, test_size=0.25, random_state=1) # 0.25 x 0.8 = 0.2

print(f"{len(idx_train)} {len(idx_val)} {len(idx_test)}")
```
