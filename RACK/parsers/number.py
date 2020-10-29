import requests


def oper(text):
    site = f'https://telefonnyenomera.ru/kto-zvonil-chei-nomer/{text}'
    r = requests.get(site)
    if r.status_code == 200:
        try:
            rt = r.text[
                 r.text.index('<span class="dop_span">2</span>') + 49:r.text.index(
                     '<span class="dop_span">2</span>') + 100]
            rt = rt[:rt.index('</strong')]
            return rt
        except:
            return False
    return False


def reg(text):
    site = f'https://telefonnyenomera.ru/kto-zvonil-chei-nomer/{text}'
    r = requests.get(site)
    if r.status_code == 200:
        try:
            rt = r.text[
                 r.text.index(f'<span class="nobr">{text}</span>') + 48:r.text.index(
                     f'<span class="nobr">{text}</span>') + 100]
            rt = rt[:rt.index('</strong')]
            return rt
        except:
            return False
    return False