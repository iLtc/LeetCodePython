import sys
import subprocess

def convert_name(name):
    if len(name[0]) < 5:
        name[0] = '0' * (5 - len(name[0])) + name[0]

    for i in range(len(name)):
        if ('a' <= name[i][0] <= 'z'):
            name[i] = name[i].capitalize()

    return ''.join(name)


def main():
    subprocess.run(['git', 'pull'])

    file_name = convert_name(sys.argv[1:])

    extension = 'py'

    file_name += '.' + extension

    print('The file name will be:', file_name)

    subprocess.run(['vim', '-c', 'set paste', file_name])

    subprocess.run(['git', 'add', file_name])

    subprocess.run(['git', 'commit', '-m', 'Added ' + ' '.join(sys.argv[1:])])

    subprocess.run(['git', 'push'])


if __name__ == '__main__':
    main()
