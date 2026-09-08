import os, urllib.parse, urlib.request, render_template 
from app.youtube import youtube_bp

gemini_api_key = "Default_Gemini_API_Key";

def home():
  return render_template("index.html")

 def create_app():

   app=flask(_name_)

app.register_blueprint(youtube_bp, url_prefix"/youtube)

@app.route("/html")
def html():
            return render_template('index.html)

return app;                                   
 
                       

                       
                       
                       
