from flask import  Flask , request, jsonify

app = Flask(__name__)

@app.route('/abc',methods=['GET' , 'POST'])
def test1():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify((str(result)))


@app.route('/abc1/vijay',methods=['GET' , 'POST'])
def test2():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a * b
        return jsonify((str(result)))
@app.route('/abc1/vijay/test',methods=['GET' , 'POST'])
def test3():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a ** b
        return jsonify((str(result)))

@app.route('/abc1/vijay/test4', methods=['GET', 'POST'])
def test4():
        if (request.method == 'POST'):
            a = request.json['num1']
            b = request.json['num2']
            result = a - b
            return jsonify((str(result)))


@app.route('/abc1/vijay/test5',methods=['GET' , 'POST'])
def test5():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a / b
        return jsonify((str(result)))



if __name__=='__main__'  :
    app.run()


"""
on postman API tool need to provide data-
Using URL like: 127.0.0.1: 5000/abc1/vijay/test4
Need to select; body-raw-json and click on 'Send' button
{
    "num1":10,
    "num2":20
}

"""
