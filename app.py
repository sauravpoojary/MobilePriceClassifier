from math import pi
from flask import Flask,render_template,request
import model

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def hello_world():
    res="Z"
    if request.method=='POST':
        battery=int(request.form['batteryPower'])
        clkspeed=float(request.form['clockSpeed'])
        frontCamera=int(request.form['frontCamera'])
        internalMemory=int(request.form['internalMemory'])
        mobileDepth=float(request.form['mobileDepth'])
        mobileWeight=float(request.form['mobileWeight'])
        noCores=int(request.form['noCores'])
        pCamera=int(request.form['pCamera'])
        pixelH=int(request.form['pixelH'])
        pixelW=int(request.form['pixelW'])
        ram=int(request.form['ram'])
        screenH=int(request.form['screenH'])
        screenW=int(request.form['screenW'])
        talkTime=int(request.form['talkTime'])
        bluetooth = int(request.form['btnradio1'])
        dualSim = int(request.form['btnradio2'])
        threeG =int(request.form['btnradio3'])
        fourG = int(request.form['btnradio6'])
        touchScreen = int(request.form['btnradio4'])
        wifi = int(request.form['btnradio5'])
        res = model.lr.predict((model.scaler.transform([[battery,bluetooth,clkspeed,dualSim,frontCamera,fourG,internalMemory,mobileDepth,mobileWeight,noCores,pCamera,pixelH,pixelW,ram,screenH,screenW,talkTime,threeG,touchScreen,wifi]])))
    return render_template('index.html',range=res[0])


if __name__ == '__main__':
    app.run(debug=True,port=8001)