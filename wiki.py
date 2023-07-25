import wikipedia


def get_wiki_arctile(arctile):
    wikipedia.set_lang('ru')
    try:
        return wikipedia.summary(arctile)
    except:
        return 'Не найдено нужной статьи'