import bottle 
import App
import json


@bottle.route('/')
def serve_html():
  return bottle.static_file("index.html", root="")

@bottle.route('/front_end.js')
def serve_front_end_js():
  return bottle.static_file("front_end.js", root="")


@bottle.post('/BTC')
def serve_btc():
  jsonBlob = bottle.request.body.read().decode()
  content = json.loads(jsonBlob)
  data34=App.dataBTC(content)
  return json.dumps(data34)

@bottle.post('/ETH')
def serve_eth():
  jsonBlob = bottle.request.body.read().decode()
  content = json.loads(jsonBlob)
  data56=App.dataETH(content)
  return json.dumps(data56)

@bottle.post('/compare')
def serve_compare():
  jsonBlob=bottle.request.body.read().decode()
  content=json.loads(jsonBlob)
  datac=App.dataCompare(content)
  return json.dumps(datac)

@bottle.post('/compare1')
def serve_compare1():
  jsonBlob=bottle.request.body.read().decode()
  content=json.loads(jsonBlob)
  dataf=App.dataCompare1(content)
  return json.dumps(dataf)

  
  
bottle.run(host="0.0.0.0", port=8080, debug=True)