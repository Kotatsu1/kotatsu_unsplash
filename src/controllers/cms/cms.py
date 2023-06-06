import contentful



client = contentful.Client('1zsteu2afj6i','Qwx4bsh_EGCsKZcpUEUqKJOctUNz-sZZNMiikKi65xg')

def cftest():
    entry = client.entry('nyancat')
    return entry