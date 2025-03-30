import requests
import json
import os 
from running import run_script
import httpx
token= os.environ.get('token')
headers={
    "Authorization":f"Bearer {token}",
    "Content-Type":"application/json"
}
url='https://aiproxy.sanand.workers.dev/openai/v1/chat/completions'
print(token)
async def get_response(prompt,filepath=None):
    print(token)
    if filepath:
        syspt = (
        "You are a Python assistant. "
        "Output only valid JSON: { \"code\": \"<Python code>\", \"requirements\": \"<requirements.txt or empty string if no dependencies>\" }. "
        "The Python code should, when executed, print the final answer to stdout, whether it is a value, text, markdown, or any other content. "
        "The Python code itself must contain any content (e.g., markdown, text, JSON, HTML) as a variable and print it to stdout. "
        "If the query involves uploading to GitHub Pages or any deployment service, the Python code should perform the upload and print the final deployment URL to stdout. "
        "Do not write the content directly into the Python file. "
        "If any github username is required, take from the environment variable 'username'. "
        "Assume repositories are not created unless provided already."
        "When asked for SQL or DuckDB queries, store the queries alone as a variable and print them through the code"
        "The code should use the file path: '{}'".format(filepath)
    )
    else:
        syspt = (
       "You are a Python assistant. "
        "Output only valid JSON: { \"code\": \"<Python code>\", \"requirements\": \"<requirements.txt or empty string if no dependencies>\" }. "
        "The Python code should, when executed, print the final answer to stdout, whether it is a value, text, markdown, or any other content. "
        "The Python code itself must contain any content (e.g., markdown, text, JSON, HTML) as a variable and print it to stdout. "
        "If the query involves uploading to GitHub Pages or any deployment service, the Python code should perform the upload and print the final deployment URL to stdout. "
        "If any github username is required, take from the environment variable 'username'. "
        "Assume repositories are not created unless provided already."
        "Do not write the content directly into the Python file. "
        "When asked for SQL or DuckDB queries, store the queries alone as a variable and print them through the code. "
    )
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json={
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": syspt},
            {"role": "user", "content": prompt}]},timeout=20 )
    print(response.json())
    jsn_res= json.loads(response.json()['choices'][0]['message']['content'])
    print(jsn_res)
    fixed_code = jsn_res["code"].encode('utf-8').decode('unicode_escape')
    req=jsn_res["requirements"].encode('utf-8').decode('unicode_escape')
    with open("/tmp/script.py", "w") as f:
        f.write(fixed_code)
    with open('/tmp/req2.txt','w') as f:
        f.write(req)
    answer = run_script()
    return answer
        
