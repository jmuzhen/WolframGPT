from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_session import Session
from generate import *
from wolfram_api import *

app = Flask(__name__)
app.secret_key = 'your secret key'  # replace with your secret key
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

MAX_INPUT_LEN = 1024


def init_session():
    print("Initializing session...")
    
    # load system prompt (default to path /system_prompts/system_prompt.txt)
    with open(os.path.join(PATH, 'system_prompts/system_prompt.txt')) as f:
        sys_prompt = f.read().strip()

    ctx = []
    if sys_prompt:
        ctx.append({"role": "system", "content": sys_prompt})

    session['ctx'] = ctx
    session['next_prompt'] = None
    
    print("Session initialized!")
    
    
@app.route('/chat', methods=['POST', 'GET'])
def chat():
    if request.method == 'GET':
        return "GET request not supported. Please use POST request."
    
    if not session.get('ctx'):
        init_session()
        
    user_input = request.json.get('input')
    if len(user_input.split()) > MAX_INPUT_LEN:
        return jsonify({'response': "Input too long. Please try again."})
    print("POST input = {}".format(user_input))
    ctx = session.get('ctx', [])
    next_prompt = session.get('next_prompt')

    if not next_prompt or next_prompt is None:
        prompt = user_input
    else:
        prompt = next_prompt
        next_prompt = None

    ctx.append({"role": "user", "content": prompt})
    response = gen_single(ctx=ctx)
    ctx.append({"role": "assistant", "content": response})

    if "wolfram_api" in response and len(response.split()) < WOLFRAM_PROMPT_LEN_WORDS:
        new_response = give_response(response)
        next_prompt = new_response

    session['ctx'] = ctx
    session['next_prompt'] = next_prompt
    session.modified = True

    return jsonify({'response': response})
    

if __name__ == '__main__':
    CORS(app)
    app.run(debug=True)

