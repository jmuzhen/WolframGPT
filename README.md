### Running WolframGPT using default settings
1. Update/install the g4f package: `pip install -U g4f`
2. Run the main script: `python3 main.py`

### Running using custom settings
>**Note**
> Unfortunately, g4f updates itself, along with its providers, frequently. So this project will
eventually become outdated. That's why running using custom settings is simple.

1. Update/install the g4f package: `pip install -U g4f`
2. Open `generate.py`. Near the start of the file you will see a few lines defining the custom settings;
you can change them to your liking. For example
```
DEFAULT_PROVIDER = g4f.Provider.<provider>
DEFAULT_MODEL = 'gpt-3.5-turbo'
```

>**Note**
> For an up-to-date list of the providers available, please check the 
[official g4f README file](https://github.com/xtekky/gpt4free/blob/main/README.md#models).