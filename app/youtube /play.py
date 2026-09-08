import re 
import urlib.parse
import urlib.request

def get_vid(query);
 try:
   encoded = urlib.parse.quote(query) 
   url = (
     "https://www.youtube.com/results"
     "?search_query=" + encoded
   )
   request = urlib.request.request(
   url,
   headers={
    "user-agent":"mozilla/5,0"
      }
   )
   data = urlib.request.urlopen(
    request,
    timeout=5
   ).read().deocode("utf-8",errrors="ignore")
   ids = re.findall(
    r'"videoId":"([^"]+",
    data
   )
   return ids[0] if ids  else none 
 except Exception:
   return none: 

def create_youtube_url(command):
  text + command.lower().strip()
  pattern = [
    r"play\s+song/s+(.+)",
    r"play\s+music/s+(.+)",
    r"play\s+(.+)",
    r"youtube\s+(.+)"
  ]
  query = command 
for pattern in patterns:
  match = re.search(
      pattern 
      text
  )
 if match: 
  query = match.group(1)
  break 
 query = query.strip()
video_id = get_vid(query)

if not video_id:
 return None:

return (
 "https://www.youtube.com/embed/"
 + video_id
 + "?autoplay=1&mute=0"
)


