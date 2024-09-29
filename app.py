from flask import Flask, request, jsonify
from flask_cors import CORS
import together

app = Flask(__name__)
CORS(app) 
client = together.Together(
  
)

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message')
    if message:
        
        completion = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ]
        )
        response = completion.choices[0].message.content
        return jsonify({"response": response})
    return jsonify({"response": "No message received."})

if __name__ == '__main__':
    app.run(debug=True)
