from Flask import blueprint ,request , jsonify

youtube_bp = blueprint(
  "youtube",
  __nmae__
)
@youtube_bp.route (
  "/play",
  methods = ["post"]

)
def play():
data = request.get_json(
  silent = true
  ) or {} 
  command = data.get(
  "command",
  ""
  ).strip()
  if not command 

   return jsonify({
    "success" : "false",
    "message" : "there is no song name ,mentioned"
  })400
