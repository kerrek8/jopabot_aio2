import snscrape.modules.telegram as snstg


def all_anek(col):
    user_from = 'anekdot18'
    posts = []
    max_p = col
    for i, p in enumerate(snstg.TelegramChannelScraper(user_from).get_items()):
        if i > max_p:
            break
        elif p in posts:
            continue
        elif p.content[-10:] == '@anekdot18':
            posts.append(p.content[:-10]+'\n')
        print(i)
    with open('anek.txt', 'w', encoding='utf-8') as f:
        f.writelines(posts)


all_anek(2000)