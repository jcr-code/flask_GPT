from flask import Flask, render_template, jsonify, Response as HTTPResponse, request as HTTPRequest
import requests
import json

app = Flask(__name__)

@app.route("/get_whatsapp_messages", methods=['POST', 'GET'])
def get_whatsapp_messages():

    if not HTTPRequest.data:  # Check if the request data is empty
            return jsonify({"status": "error", "message": "Empty payload. No data received."})
    # api_url = "http://sender.eyesimple.us/api/get/wa.received?secret=c99ea061f3ce0be0e73e3511da7b75bca5e6318a"
    
    # # Send GET request to the WhatsApp API
    # response = requests.get(api_url)

    # # Send GET request to the WhatsApp API
    # data = json.loads(HTTPRequest.data)
    # print(data)
    content_type_header = HTTPRequest.headers.get('Content-Type')
    print(content_type_header)
    response = HTTPRequest.json
    print(response)
    # Check if the request was successful (status code 200)
    # if response.status_code == 200:
    #     # Parse the JSON response
    #     data = response.json()

    #     # Extract the messages from the 'data' field
    #     messages = data.get('data', [])

    #     chat_history = []

    #     # Process each message
    #     for message in messages:
    #         message_id = message.get('id')
    #         sender = message.get('account')
    #         recipient = message.get('recipient')
    #         message_content = message.get('message')
    #         created_timestamp = message.get('created')

    #         # Process the message data as needed, e.g., store it in a list
    #         chat_history.append({
    #             "message_id": message_id,
    #             "sender": sender,
    #             "recipient": recipient,
    #             "message_content": message_content,
    #             "created_timestamp": created_timestamp
    #         })

    #     # Return the processed chat history as a JSON response
    #     return jsonify({"status": "success", "chat_history": chat_history})
    # else:
    #     return jsonify({"status": "error", "message": "Failed to retrieve WhatsApp messages"})

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=80)
