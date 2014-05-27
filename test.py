import cgi
form = cgi.FieldStorage()
seachterm =  form.getvalue('searchbox')

print seachterm
