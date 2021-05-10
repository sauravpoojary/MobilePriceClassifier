from flask import Flask,render_template,request,redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/result',methods=["POST"])
def classify():
    battery=request.form['batteryPower']
    clkspeed=request.form['clockSpeed']
    frontCamera=request.form['frontCamera']
    internalMemory=request.form['internalMemory']
    mobileDepth=request.form['mobileDepth']
    mobileWidth=request.form['mobileWidth']
    noCores=request.form['noCores']
    pCamera=request.form['pCamera']
    pixelH=request.form['pixelH']
    pixelW=request.form['pixelW']
    ram=request.form['ram']
    screenH=request.form['screenH']
    screenW=request.form['screenW']
    talkTime=request.form['talkTime']
    
    
    return clkspeed

if __name__ == '__main__':
    app.run(debug=True,port=8001)