import os
import shutil
import zipfile
import pytest

# выясняем пути
CURRENT_FILE = os.path.abspath(__file__)  # получаем абсолютный путь к текущему файлу
PROJECT_DIR = os.path.dirname(os.path.dirname(CURRENT_FILE))  # путь до директории проекта
TMP_DIR = os.path.join(PROJECT_DIR, 'temp')  # путь до папки с файлами
RESOURСE_DIR = os.path.join(PROJECT_DIR, 'resource')  # путь до папки с архивом
archive = os.path.join(RESOURСE_DIR,'test_zip.zip')


@pytest.fixture(scope="session", autouse=True)
def arсhive_file():
    # создаем папку
    if not os.path.exists(RESOURСE_DIR):
        os.mkdir(RESOURСE_DIR)
    # создаем архив с файлами в созданную папку
    with zipfile.ZipFile(archive, 'w') as zf:
        for file in os.listdir(TMP_DIR):
            add_file = os.path.join(TMP_DIR, file)
            zf.write(add_file, os.path.basename(add_file))

    yield
    # удаляем папку с архивом
    shutil.rmtree(RESOURСE_DIR)