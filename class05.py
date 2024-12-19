class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def show_songs(self):
        print(f'Playlist: {self.name}')
        print(f'Músicas: {self.songs}')


def main():

    playlist1 = Playlist('Música Br')
    playlist1.add_song('Manu Gavassi - Gracinha')
    playlist1.add_song('Capital inicial - Depois da meia noite')
    playlist1.add_song('Restart - Recomeçar')
    playlist1.show_songs()

    playlist2 = Playlist('Músicas Internacionais')
    playlist2.add_song('The Black eyed Peas - I gotta Feeling')
    playlist2.add_song('Doja Cat - Say So')
    playlist2.add_song('Kanye West - All Of The Ligths')
    playlist2.show_songs()

if __name__ == '__main__':
    main()