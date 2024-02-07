# https://github.com/xtekky/gpt4free

import g4f

g4f.debug.version_check = False

DEFAULT_PROVIDER = g4f.Provider.Bing
DEFAULT_MODEL = 'gpt-4'
PRINT_RESPONSE = True  # print completion response.
VERBOSE = True  # print wolfram API responses as well. Used for debugging.
DEFAULT_STREAM = False  # whether to stream completion, even if provider supports it.
WOLFRAM_PROMPT_LEN_WORDS = 4000  # any prompt given longer than this will not be sent to Wolfram API


def gen_single(prompt=None, model=DEFAULT_MODEL, provider=DEFAULT_PROVIDER,
               ctx=None):
    STREAM = DEFAULT_STREAM and provider.supports_stream
    if ctx is None and prompt is None:
        return None
    
    if ctx is None:
        ctx = [{"role": "user", "content": prompt}]
    
    # streamed completion
    response = g4f.ChatCompletion.create(model=model, messages=ctx,
                                         provider=provider,
                                         stream=STREAM)  # alterative model setting
    
    if not PRINT_RESPONSE:
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
