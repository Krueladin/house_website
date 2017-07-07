import transmission

def main():
    client = transmission.TransmissionClient("localhost")
    print client.add_torrents(["/home/smtrudo/Downloads/ubuntu-17.04-desktop-amd64.iso.torrent",
        "/home/smtrudo/Downloads/Fedora-Astronomy_KDE-Live-i386-26_Beta.torrent"])
#    print client.delete_torrents([2], True)

#    print client.add_torrents([torrent.Torrent("https://torrent.fedoraproject.org/torrents/Fedora-Astronomy_KDE-Live-i386-26_Beta.torrent")])
#    print client.get_torrents()


if __name__=="__main__":
    main()
