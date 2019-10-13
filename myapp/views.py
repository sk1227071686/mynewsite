from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Product
# Create your views here.

def about(request):
	html = '''
<!DOCTYPE html>
<html>
<head><title>About Myself</title></head>
<body>
<h2>Shi-Kang</h2>
<hr>
<p>
Hi,I am Shi-Kang. Nice to meet you!
</p>
</body>
</html>
'''
	return HttpResponse(html)

def listing(request):
	html = '''
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title>二手手机列表</title>
</head>
<body>
<h2>以下是目前本店销售中的二手手机列表</h2>
<hr>
<table width=400 border=1 bgcolor='#ccffcc'>
{}
</table>
</body>
</html>
'''
	products = Product.objects.all()
	tags = '<tr><td>产品</td><td>售价</td><td>库存量</td></tr>'
	for p in products:
		tags = tags + '<tr><td>{}</td>'.format(p.name)
		tags = tags + '<td>{}</td>'.format(p.price)
		tags = tags + '<td>{}</td></tr>'.format(p.qty)
	return HttpResponse(html.format(tags))
