from django.shortcuts import render
from django.http import Http404
import os
import errno
import zipfile
from get_images.forms import InputForm
from get_images.download_images import Downloader
from django.conf import settings

# 'https://detail.1688.com/offer/578623301079.html?spm=a2615.7691456.newlist.134.46443e8149ucaX'

def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data
            if d['url'].startswith('https://detail.1688.com'):

                temp_folder = '%s/static/tmp' % settings.BASE_DIR
                folder_img = '%s/out' % temp_folder
                folder_zip = temp_folder
                try:
                    os.makedirs(folder_img, exist_ok=True)
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise

                clear_folder(folder_img)
                clear_folder(folder_zip)

                downloader = Downloader()
                response = downloader.load_url(d['url'])
                srcs = downloader.get_images_url(response)
                downloader.download_images(srcs, folder_img)

                zip_files(folder_img, folder_zip)

                clear_folder(folder_img)
                pass

        else:
            raise Http404

    else:
        form = InputForm()

    return render(request, 'index.html', locals())


def clear_folder(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(e)


def zip_files(folder_img, folder_zip=''):
    with zipfile.ZipFile(os.path.join(folder_zip, 'images.zip'), 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_img):
            for file in files:
                zipf.write(os.path.join(root, file), arcname=file)
