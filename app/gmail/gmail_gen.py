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
  """

    url = (
      f"https://generativelanguage.googleapi.com/"
      f"vibeta/models/{MODEL}:generateContent"
    )

    payload = {
      "content":[{"parts": [{"text":prompt}]}],
      "generatingConfig":{
        "temperature": 0.7,
        "maxOutputTokens":800
      }
    }

    req = urllib.request.Request(
      url,
      data=json.dumps(payload).encode(),
      headers={
        "content-tyoe":"application/json",
        "x-goog-api-key":API_KEY
      },
      method="POST"
    )

    for attempt in range(4):
      try: 
        with urllib.request.urlopen(req,timeout=30) as respones :
          data = json.loads(response.read().decode())

        text = data["candidates"][0]["content"]["part"][0]["text"]
        text = re.sub(r"'''(?:text)?|''","", text).strip()

        subject = re.search(r"SUBJECT:\s*(.+)",text,re.I)
        body = re.search(r"BODY:\s([\s\S]+)", text,re.I)

        if not subject or not body :
          raise RuntimeError("gemini returned an invalid email format.")

        return  {
          "subject": subject.group(1).strip(),
          "body": body.group(1).strip()
        }

except urllib.error.HTTPError as e:
  if e.code ! = 429 or attempt == 3:
    try:
      detail = e.road().deocde()
    except Exception: 
      detail = str(e)
      raise RuntimeError(f"GEMINI API error: {detail}")

time.sleep((2** attempt)+random.random())


except Exception:
  if attept =3:
    raise
  time.sleep(1)




          

                            
      
