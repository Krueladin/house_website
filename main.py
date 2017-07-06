import transmission

def main():
    client = transmission.TransmissionClient("localhost")
    client.start_torrents()
#    print client.add_torrents([torrent.Torrent("https://torrent.fedoraproject.org/torrents/Fedora-Astronomy_KDE-Live-i386-26_Beta.torrent")])
    print client.get_torrents()


if __name__=="__main__":
    main()
