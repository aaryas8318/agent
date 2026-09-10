import os 
import json
import re 
import time 
import random
import urllib.request
import urllib.error

API_key=os.gentenv("GEMINI_API_KEY","")
MODEL=os.gentenv("GEMINI_MODEL","gemini-3.5-flash")

def generate_email_with_gemini(command):
  if not API_key:
    raise runtimeError("GEMINI_API_KEY is missing.")
    
    prompt = f"""
  you are a professional gmail eamil writing assistant.

  convert the user's voice command into a professional email.

  rules:
  -Do not copy the command literally
  -Do not explain anything.
  -Do not invent names, dates, prices, companies, attachments,or  facts.
  -Keep the email natural and concise.

  output exactly:

  subject: <subject>
  BODY:
  <email body>

  user command
  (command)
  
