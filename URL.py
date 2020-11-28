def get_absolute_url(url, *args, **kwargs):

    
    s = url + '/' + args[0]
    if len(args) > 1:        
        for i in range(1, len(args)):
            s += '/' + args[i]
    s += '?' 
    j = 1

    for k, v in kwargs.items():
        if j < len(kwargs):
            j += 1                        
            s += k + '=' + v + '&'
        else:
            s += k + '=' + v 
                      
    print(s)

get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin')
get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small')