from flask import Flask,render_template, redirect, url_for, request,send_file
from image_detect import face_detect_with_webcam 
import json
from face_capture import face_capture 
from face_match import face_match
import os
import datetime
import pandas as pd


app= Flask(__name__)

@app.route('/start/',methods = ['POST', 'GET'])
@app.route('/',methods = ['POST', 'GET'])

def index():
   
    return render_template("start.html")

@app.route('/studentlist',methods = ['POST', 'GET'])
def studentlist():
    f=open('data.json','r')
    data=json.loads(f.read())
    f.close()    
    check_delete=request.args.get('delete')
    if check_delete=='yes':
        id=request.args.get('id')
        for obj in data:
            if obj['id']==id:
                data.remove(obj)
                break
        for i in range(0,50):
            if os.path.exists("db/pictures/"+id+"_"+str(i)+".png"):
                os.remove("db/pictures/"+id+"_"+str(i)+".png")
            else:
                print("The file does not exist")
        
        f=open('data.json','w')
        f.write(json.dumps(data,indent=4))
        f.close()
        return redirect('studentlist')

        
    
    return render_template("studentlist.html",data=data)

@app.route('/studentsheet',methods = ['POST', 'GET'])
def studentsheet():
    f=open('sheet.json','r')
    data=json.loads(f.read())
    f.close()    
    f=open('data.json','r')
    data1=json.loads(f.read())
    f.close()
    for d in data:
        for d1 in data1:
            if d['id']==d1['id']:
                data1.remove(d1)
                break
        
    check_delete=request.args.get('delete')
    check_add=request.args.get('add')

    if check_delete=='yes':
        id=request.args.get('id')
        for obj in data:
            if obj['id']==id:
                data.remove(obj)
                break
        
        
        f=open('sheet.json','w')
        f.write(json.dumps(data,indent=4))
        f.close()
        df = pd.read_json (r'C:\Users\Ashfaqur Rahman\Desktop\python lab\attendence_project\sheet.json')
        df.to_csv (r'C:\Users\Ashfaqur Rahman\Desktop\python lab\attendence_project\sheet.csv', index = None)
        return redirect('studentsheet')
            
        return redirect('studentlist')
    if check_add=='yes':
        id=request.args.get('id')
        for d1 in data1:
            if d1['id']==id:
                now = datetime.datetime.now()
                s2 = now.strftime("%H:%M:%S, %d/%m/%Y")
                
                data.append({'name':d1['name'],'id':d1['id'],'date':str(s2)})
                break
        f=open('sheet.json','w')
        jsonfile=json.dumps(data,indent=4)
        f.write(jsonfile)
        f.close()
        df = pd.read_json (r'C:\Users\Ashfaqur Rahman\Desktop\python lab\attendence_project\sheet.json')
        df.to_csv (r'C:\Users\Ashfaqur Rahman\Desktop\python lab\attendence_project\sheet.csv', index = None)
        return redirect('/studentsheet')

        
    
    return render_template("showsheet.html",data=data,data1=data1)

@app.route('/main',methods = ['POST', 'GET'])
def main():
    check_take=request.args.get('take')
    clear_sheet=request.args.get('clear')
    if check_take=='yes':
        id=face_match()
        f=open('sheet.json','r')
        data=json.loads(f.read())
        f.close()
        okay=True
        if any(obj['id'] == id for obj in data):
            okay=False
        if okay:
            f=open('data.json','r')
            data1=json.loads(f.read())
            f.close()

            for obj in data1:
                if obj['id']==id:
                    # get the current date and time
                    now = datetime.datetime.now()
                    s2 = now.strftime("%H:%M:%S, %d/%m/%Y")
                    data.append({'name':obj['name'],'id':obj['id'],'date':str(s2)})
            f=open('sheet.json','w')
            jsonfile=json.dumps(data,indent=4)
            f.write(jsonfile)
            f.close()
            df = pd.read_json (r'C:\Users\Ashfaqur Rahman\Desktop\python lab\attendence_project\sheet.json')
            df.to_csv (r'C:\Users\Ashfaqur Rahman\Desktop\python lab\attendence_project\sheet.csv', index = None)
            


        return redirect('main')
    elif clear_sheet=='yes':
        f=open('sheet.json','w')
        data=[]
        jsonfile=json.dumps(data,indent=4)
        f.write(jsonfile)
        f.close()
        df = pd.read_json (r'C:\Users\Ashfaqur Rahman\Desktop\python lab\attendence_project\sheet.json')
        df.to_csv (r'C:\Users\Ashfaqur Rahman\Desktop\python lab\attendence_project\sheet.csv', index = None)
        return redirect('main')


        pass
    return render_template("main.html")

@app.route('/form',methods = ['POST', 'GET'])
def form_input():
    error=False
    success=False
    if request.method=='POST':
        f=open('data.json','r')
        data=json.loads(f.read())
        f.close()
        f=open('data.json','w')
        
        
        if any(obj['id'] == request.form['id'] for obj in data):
            error=True
        else:
            data.append({'name':request.form['name'],'id': request.form['id']})
            success=True
            face_capture(request.form['name'],request.form['id'])

        
        f.write(json.dumps(data,indent=4))
        f.close()
    return render_template("form_input.html",error=error,success=success)

@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "C:/Users/Ashfaqur Rahman/Desktop/python lab/attendence_project/sheet.csv"
    return send_file(path, as_attachment=True)
if __name__ =="__main__":
    app.run(debug=True)
