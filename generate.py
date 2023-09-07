# https://github.com/xtekky/gpt4free

import g4f

DEFAULT_PROVIDER = g4f.Provider.DeepAi


def gen_single(prompt=None, model='gpt-3.5-turbo', provider=DEFAULT_PROVIDER, print_response=True,
               ctx=None):
    STREAM = provider.supports_stream
    if ctx is None and prompt is None:
        return None
    
    if ctx is None:
        ctx = [{"role": "user", "content": prompt}]
    
    # streamed completion
    response = g4f.ChatCompletion.create(model=model, messages=ctx,
                                         provider=provider,
                                         stream=STREAM)  # alterative model setting
    
    if not print_response:
        return
    
    r = ""
    
    if STREAM:
        for message in response:
            r += message
            print(message, end="", flush=True)
    else:
        r = response
        print(response)
    
    if not r.endswith("\n"):
        print()
        
    return r
