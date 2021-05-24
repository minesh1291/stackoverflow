- Debugger Settings (launch.json)

adding current path to python environment so it can load local modules and libraries
```
{
  "configurations": [
    
    {
      "env": {
          "PYTHONPATH": "${workspaceFolder}"
      }
  }
} 
```

- Selecting Linter, Code Formater and Language Server (`settings.json`)
  - Linter: for checking programming errors, bugs, stylistic errors and suspicious constructs
  - Code Formatter: auto-format code according to set standards in order to make it easily navigable and readable
  - Language Server: to provide language features such as code completion, hover provider, go to definition, find all references, and code refactoring
```
{
    "python.linting.enabled": true,
    "python.pythonPath": "/home/minesh/anaconda3/envs/my-env/bin/python",
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "python.languageServer": "Pylance"
}
```
