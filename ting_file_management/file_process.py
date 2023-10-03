from ting_file_management.file_management import txt_importer
import sys


# def data(path_file):
#     file = txt_importer(path_file)
#     format = {
#             "nome_do_arquivo": path_file,
#             "qtd_linhas": len(file),
#             "linhas_do_arquivo": file
#         }
#     sys.stdout.write(f"{format}")


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    file_dir = txt_importer(path_file)
    file_return = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_dir),
        "linhas_do_arquivo": file_dir
    }
    instance.enqueue(file_return)
    sys.stdout.write(f"{file_return}\n")
    return file_return


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")

    else:
        deq_file = instance.dequeue()
        sys.stdout.write(
            f"Arquivo {deq_file['nome_do_arquivo']} removido com sucesso\n"
        )


def file_metadata(instance, position):
    try:
        pos = instance.search(position)
        print(pos, file=sys.stdout)
    except IndexError:
        return sys.stderr.write("Posição inválida")
