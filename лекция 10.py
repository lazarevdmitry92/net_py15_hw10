import chardet


def union_unencoding_txt(list):
    all_text = ""
    for i in list:
        with open(i, 'rb') as f:
            data = f.read()
            result = chardet.detect(data)
            text = data.decode(result['encoding'])
            all_text += text
    return(all_text)


text = union_unencoding_txt(['allnews.txt', 'newsafr.txt', 'newscy.txt', 'newsfr.txt', 'newsit.txt'])


def get_top_six_words(text):
    list = text.lower().split(' ')
    words = []
    for i in list:
        if len(i) > 6:
            words.append(i)
    dct = {}
    for i in words:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    sorted_dtc = sorted(dct.items(), key=lambda x: x[1], reverse = True)
    i = 0
    while i < 6:
        print('Слово "{}" упоменалось {} раз'.format(sorted_dtc[i][0], sorted_dtc[i][1]))
        i += 1


get_top_six_words(text)