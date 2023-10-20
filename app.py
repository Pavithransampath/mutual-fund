from flask import Flask,render_template,request,redirect,url_for
import requests
app=Flask(__name__)

url="https://api.mfapi.in/mf/"
list1=[]

@app.route("/",methods=["POST","GET"])
def fun():
    if request.method=="POST":
        Name=request.form.get("Name")
        Fundcode=request.form.get("Fundcode")
        Funds=requests.get(url+str(Fundcode))
        Fundhouse=Funds.json().get("meta").get("fund_house")
        Investedamount=request.form.get("Investedamount")
        Unitheld=request.form.get("Unitheld")
        nav=Funds.json().get("data")[0].get("nav")
        dict1={}
        dict1.update({"Name":Name})
        dict1.update({"Fundhouse":Fundhouse})
        dict1.update({"Investedamount":Investedamount})
        dict1.update({"Unitheld":Unitheld})
        dict1.update({"nav":nav})
        Currentvalue=float(dict1.get("nav"))*int(dict1.get("Investedamount"))
        dict1.update({"Currentvalue":Currentvalue})
        Growth=float(dict1.get("Currentvalue"))-int(dict1.get("Unitheld"))
        dict1.update({"Growth":Growth})
        list1.append(dict1)
    return render_template("index.html",l1=list1)


@app.route("/<string:delete>")
def fun1(delete):
    list1.pop(int(delete)-1)
    return render_template("index.html",l1=list1)



@app.route("/edit/<string:item>",methods=["POST","GET"])
def fun2(item):
    
    if request.method=="POST":
        dict1=list1[int(item)-1]
        dict1.update({"Name":request.form.get("Name")})
        dict1.update({"Fundcode":request.form.get("Fundcode")})
        dict1.update({"Investedamount":request.form.get("Investedamount")})
        dict1.update({"Unitheld":request.form.get("Unitheld")})
        return redirect(url_for('fun'))
    l2=list1[int(item)-1]
    return render_template("edit.html",l2=l2)
        

   

if __name__ == "__main__":
    app.run(debug=True)




