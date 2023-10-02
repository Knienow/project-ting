from ting_file_management.file_management import txt_importer
import sys


def data(path_file):
    file = txt_importer(path_file)
    format = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file
        }
    sys.stdout.write(f"{format}")


def process(path_file, instance):
    if path_file not in instance.queue:
        instance.enqueue(path_file)
        return data(path_file)


def remove(instance):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    else:
        deq_file = instance.dequeue()
        return sys.stdout.write(f"Arquivo {deq_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        pos = instance.search(position)
        return data(pos)
    except IndexError:
        return sys.stderr.write("Posição inválida")
