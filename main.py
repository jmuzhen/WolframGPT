from generate import *
from wolfram_api import *

# load system prompt (default)
with open('system_prompt.txt', 'r') as f:
    sys_prompt = f.read().strip()

def converse(sys_prompt=None):
    ctx = []
    if sys_prompt:
        ctx.append({"role": "system", "content": sys_prompt})
    
    next_prompt = None
    def gen_next(prompt):
        nonlocal next_prompt
        ctx.append({"role": "user", "content": prompt})
        response = gen_single(ctx=ctx)  # response is implicitly printed
        ctx.append({"role": "assistant", "content": response})
        if "wolfram_api" in response:
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
    converse(sys_prompt=sys_prompt)