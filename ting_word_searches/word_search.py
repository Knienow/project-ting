def exists_word(word, instance):
    # result = []

    # for i in instance.queue:
    #     occurrences = []
    #     for line_index, line in enumerate(i["linhas_do_arquivo"], start=1):
    #         if word.casefold() in line.casefold():
    #             occurrences.append({"linha": line_index})

    #     if len(occurrences) > 0:
    #         result.append({
    #             "palavra": word,
    #             "arquivo": instance.queue[i]["nome_do_arquivo"],
    #             "ocorrencias": occurrences
    #         })

    # return result

    result = []

    for index in range(len(instance)):
        data = instance.search(index)
        data_info = {
            "palavra": word,
            "arquivo": data["nome_do_arquivo"],
            "ocorrencias": []
        }
        file_path = "linhas_do_arquivo"
        for line_index, content in enumerate(data[file_path], start=1):
            if word.lower() in content.lower():
                data_info["ocorrencias"].append({
                    "linha": line_index
                })

        if len(data_info["ocorrencias"]) > 0:
            result.append(data_info)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
