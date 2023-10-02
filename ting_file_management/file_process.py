from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    files = []
    for element in instance.queue:
        files.append(element["nome_do_arquivo"])

    if path_file not in files:
        text = txt_importer(path_file)
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(text),
            "linhas_do_arquivo": text
        }
    instance.enqueue(data)
    print(data, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
