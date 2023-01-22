import functions_framework

@functions_framework.http
def hello(req):
    return '안녕 ' + req.args.get('name')