from flask import Flask,request,jsonify
from flask_cors import CORS
import recommendation

app = Flask(__name__)
CORS(app) 
        
@app.route('/recommend', methods=['GET'])
def recommend():
    res = recommendation.recommend(request.args.get('article'))
    return jsonify(res)

if __name__=='__main__':
    app.run(port = 5000, debug = True)
