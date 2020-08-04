- stft params

```python
# STFT Settings
nperseg  = 0.5 * samplerate  # Window Size
noverlap = nperseg*0.95      # Overlap
nfft     = 1 * samplerate    # STFT
window   = 'hann'            # Window Type
```
