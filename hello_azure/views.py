from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from azure.storage.blob import BlobServiceClient, ContentSettings

ACCOUNT_NAME = 'pruebaaedm'
ACCOUNT_KEY = '97Bl6LBNWT4TYYc4H1tTvG57O4jQUj2ED9i13SVZU+mCPbBlf98NIRsWlcXabTi5eJEIDA+xBtU3+AStMJ59UQ=='
CONTAINER_NAME = 'prueba'

def index(request):
    print('Request for index page received')
    return render(request, 'hello_azure/index.html')

@csrf_exempt
def hello(request):
    if request.method == 'POST':
        url_imagen = f"https://pruebaaedm.blob.core.windows.net/prueba/logoED.png"
        print(url_imagen+'Holaa')
        name = request.POST.get('name')
        
        if name is None or name == '':
            print("Request for hello page received with no name or blank name -- redirecting")
            return redirect('index')
        else:
            print("Request for hello page received with name=%s" % name)
            context = {'name': name, 'url_imagen': url_imagen}
            return render(request, 'hello_azure/hello.html', context)
    else:
        return redirect('index')
    
def get_blob_service_client():
    connection_string = f"DefaultEndpointsProtocol=https;AccountName={ACCOUNT_NAME};AccountKey={ACCOUNT_KEY};EndpointSuffix=core.windows.net"
    return BlobServiceClient.from_connection_string(connection_string)

def upload_image_to_blob_storage(image_data, blob_name):
    blob_service_client = get_blob_service_client()
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)

    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(image_data, content_settings=ContentSettings(content_type='image/png'))

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
        blob_name = image_file.name

        image_data = image_file.read()

        upload_image_to_blob_storage(image_data, blob_name)

        return HttpResponse("Imagen cargada exitosamente")
    else:
        return HttpResponse("La solicitud debe ser de tipo POST y contener un archivo adjunto")