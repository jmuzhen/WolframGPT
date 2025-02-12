import os

from generate import *
from wolfram_api import *

# load system prompt (default to path /system_prompts/system_prompt.txt)
with open(os.path.join(PATH, 'system_prompts/system_prompt.txt')) as f:
    sys_prompt = f.read().strip()


def converse():
    ctx = []
    if sys_prompt:
        ctx.append({"role": "system", "content": sys_prompt})
    
    next_prompt = None
    
    def gen_next(p):
        nonlocal next_prompt
        ctx.append({"role": "user", "content": p})
        response = gen_single(ctx=ctx)  # response is implicitly printed
        ctx.append({"role": "assistant", "content": response})
        if "wolfram_api" in response and len(response.split()) < WOLFRAM_PROMPT_LEN_WORDS:
            new_response = give_response(response)
            next_prompt = new_response
    
    while True:
        prompt = None
        if next_prompt is None:
            prompt = input("> ")
        else:
            prompt = next_prompt
            next_prompt = None
        
        gen_next(prompt)


def main():
    converse()


if __name__ == "__main__":
    main()
