def get_absolute_url(url, *args, **kwargs):

    
    s = url + '/' + args[0]
    if len(args) > 1:
        i = 1   
        for i in range(1, len(args)):
            s += '/' + args[i]
    s += '?'    
    for k, v in kwargs.items():
        s += '&' + k + '=' + v 
    print(s)

get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin')
get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small')