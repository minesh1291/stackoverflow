
- Model selection for given dataset that can predict response variable.
 - Start by fitting a `simple model` (multivariate regression, logistic regression), do some `feature engineering` accordingly, `regularization` and then try some `complicated models`. Always split the dataset into train, `validation`, test dataset and use cross validation to check their performance. Determine if the problem is classification or regression Favor simple models that run quickly and you can easily explain. Mention cross validation as a means to evaluate the model. Plot and visualize the data.

- What are some ways I can make my model more robust to outliers?
 - We can have regularization such as L1 or L2 to reduce variance (increase bias).
 - Changes to the `algorithm`:
   Use tree-based methods instead of regression methods as they are more resistant to outliers. For statistical tests, use non parametric tests instead of parametric ones.
 - Use robust error `metrics` such as MAE or Huber Loss instead of MSE.
 - Changes to the `data`:
   Winsorizing the data, Transforming the data (e.g. log), Remove them only if you’re certain they’re anomalies not worth predicting

-
