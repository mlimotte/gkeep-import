import gkeepapi
import html2text
from os import walk
from os.path import basename
import sys


def add_note(keep, c):
    print(f'Adding note: {c["title"]}. Sync required.')
    note = keep.createNote(c['title'], c['text'])
    note.labels.add(c['label'])
    return note


def slurp_text(path):
    with open(path) as x:
        html = x.read()
        s = html2text.html2text(html)
    return s


def main():

    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} PATH_TO_DIRECTORY_OF_HTML_FILES')
        sys.exit(1)

    path = sys.argv[1]
    print(f'Loading .html files from the path tree at {path}')

    keep = gkeepapi.Keep()

    email = input('Google login email: ')
    pw = input(f'Google password for {email}: ')
    keep.login(email, pw)

    labels = {str(l): l for l in keep.labels()}

    contents = []
    for (dirpath, dirnames, filenames) in list(walk(path)):
        files = [fname
                 for fname in filenames
                 if fname.endswith('.html') and fname != 'index.html']

        if files:
            label_name = basename(dirpath)
            if label_name not in labels.keys():
                label = keep.createLabel(label_name)
                labels[label_name] = label
            else:
                label = labels[label_name]

            for fname in files:
                contents.append(dict(title=fname,
                                     text=slurp_text(f'{dirpath}/{fname}'),
                                     label=label))

    for c in contents:
        add_note(keep, c)

    print('Syncing ...')
    keep.sync()


if __name__ == '__main__':
    main()
