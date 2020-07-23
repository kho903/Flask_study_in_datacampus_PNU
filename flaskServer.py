from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def routeFn():
    return "Hello Flask"


@app.route("/test")
def testFn():
    return "<h1>Korea</h1>"


@app.route("/a")
def aFn():
    return render_template('a.html')


@app.route("/b")
def bFn():
    return render_template('b.html', myname='김철수', myage=30)


@app.route("/addrform")
def addrFn():
    return render_template('address.html')


@app.route("/f")
def fFn():
    return render_template('f.html')


@app.route("/f_R")
def ffFn():
    weight = request.args['weight']
    height = request.args['height']
    return render_template('ff.html', weight=weight, height=height)


@app.route("/addrproc")
def addrprocFn():
    myname = request.args['myname']
    myage = request.args['myage']
    myaddr = request.args['myaddr']
    s = f'이름:{myname}나이:{myage}주소:{myaddr}'
    return s


@app.route("/pizza")
def pizzaFn():
    return render_template('pizza.html')


@app.route("/pizorder")
def pizzaoFn():
    myname = request.args['myname']
    tel = request.args['tel']
    email = request.args['email']
    size = request.args['size']
    time = request.args['time']
    re = request.args['re']
    return render_template(
        'pizzaO.html',
        myname=myname, tel=tel, email=email, size=size, time=time, re=re)


@app.route("/checkForm")
def checkFormFn():
    return render_template('check.html')


@app.route("/checkResult")
def checkResultFn():
    hobby = request.args.getlist('hobby')
    print(hobby)
    company = request.args['company']
    return render_template('checkResult.html', hobby=hobby, company=company)


@app.route("/postForm", methods=['get', 'POST'])
def postFormFn():
    return render_template('postForm.html')


@app.route("/postFormResult", methods=['POST'])
def postFormResultFn():
    myname = request.form['myname']
    mycontent = request.form['mycontent']
    return render_template('postFormResult.html', data=[myname, mycontent])


@app.route("/fileForm")
def fileFormFn():
    return render_template('fileForm.html')


@app.route("/fileResult", methods=['POST'])
def fileResultFn():
    try:
        f = request.files['myfile']
        f.save('fileData\\' + f.filename)
        return "file save..."
    except Exception as err:
        return "file error : " + err


if __name__ == '__main__':
    app.run(debug=True)
