import requests
import wget
import platform
import colorama
import os


class Download_qbit():

    def __init__(self, operating_system):
        self.operating_system = operating_system

    def download(self):
        mirrors_command = {'Windows': 'https://nchc.dl.sourceforge.net/project/qbittorrent/qbittorrent-win32/qbittorrent-4.3.4.1/qbittorrent_4.3.4.1_x64_setup.exe',
                   'Darwin': 'https://udomain.dl.sourceforge.net/project/qbittorrent/qbittorrent-mac/qbittorrent-4.3.4.1/qbittorrent-4.3.4.1.dmg',
                   'Linux': 'sudo apt-get install -y qbittorrent qbittorrent-nox'}

        if not self.operating_system in mirrors_command:
            print(colorama.Fore.RED,
                    '[!!] Unknown Operating System.', colorama.Style.RESET_ALL)
        else:
            if self.operating_system == 'Linux':
                os.system(mirrors_command[self.operating_system])
                print(colorama.Fore.GREEN,
                      '[*] Qbittorrent is installed. Issue the command: "sudo qbittorrent-nox" to start the server.',
                      colorama.Style.RESET_ALL)
            else:
                print(colorama.Fore.GREEN, f'[*] Downloading Qbittorrent for {self.operating_system}',
                      colorama.Style.RESET_ALL)
                dl_installer = wget.download(mirrors_command[self.operating_system])


if __name__ == '__main__':
    Download_qbit(platform.system()).download()
