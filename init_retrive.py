from retriveWeb import retriveWeb

url = 'http://jobboard.inwavethemes.com'
path_index = '/var/www/marista/module/Web/view/web/web/index.html'
path_img = '/var/www/marista/public/image'
path_css = '/var/www/marista/public/css'
path_js = '/var/www/marista/public/js'

print('----------------- Iniciando ----------------')

try:
    retrive = retriveWeb(url=url, index=path_index, path_img=path_img, path_css=path_css, path_js=path_js)
    response = retrive.read_index()
except  ValueError:
    print 'Error:{}'.format(e)

print('----------------- Terminado ----------------')