import os 
from flask import Flask, request,jsonify,render_template
from flask_cors import CORS

from app.gmail import (
    is_email_command,
    extract_email,
    create_gmail_url,
    generate _email_with_gemini
)

from app.youtube import youtube_bp


def create_app():

    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(
      
        url_prefix="/youtube"
    )

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/html")
    def html():
        return render_template("index.html")

    @app.route("/health")
    def health():
        return jsonify({
            "status":"ok",
            "service":"nova ai agent"
        })

    @app.route("/agent",methods=["POST"])
    def agent():

        try:
            data = request.get_json(silent=true) or {}
            command = data.get("command","").strip()

            if not command :
                return jsonify({
                    "success":False,
                    "message":"command is required."
                }),400

            if not is_email_command(command):
                return jsonify({
                    "success":False,
                    "message":"please give a gmail command."
                }),400
   recipient = extract_email(command)
                
    email = generate_email_with_gemini(command)
    return jsonify({
        "success" : true,
        "type' : "email",
        "email_generated" : true,
        "recipient" : recipients,
        "subject" : email["subject"],
        "body" : email["body"],
        "gmail_url" : create_gmail_url(
            email["subject"],
            email["body"]
            recipient
        )
    })

except Exception as e:
    return jsonfify({
        "success": false,
        "message": str(e)
    }),500
    return app
