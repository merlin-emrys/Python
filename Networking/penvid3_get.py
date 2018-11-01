import requests

myheaders={'user-agent':'Iphone 6'}

payload = {'url':'http://www.edge-security.com'}
r = requests.get('http://httpbin.org/headers',headers=myheaders)
print(r.url)
print('Status code: ')
print('\t[-]' +str(r.status_code) + '\n' )

print('Server Headers')
print('*'*10)
for x in r.headers:
    print('\t' + x + ' : ' + r.headers[x])
print('*'*10+'\n')
print("Content:\n")
print(r.text)
