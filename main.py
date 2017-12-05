import argparse
import dropbox
from flask import Flask
from settings import DROPBOX_KEY

app = Flask(__name__)

class TransferData:
    def __init__(self, dropbox_key):
        self.dropbox_key = dropbox_key

    def upload_file(self, file_from, file_to):
        """Upload a file from source to destination"""
        dbx = dropbox.Dropbox(self.dropbox_key)

        with open(file_from, 'rb') as f:
            print "Uploading File to " + file_to
            dbx.files_upload(f.read(), file_to)

@app.route("/upload_video")
def upload_video_to_dropbox():
    videoUploader = TransferData(DROPBOX_KEY)
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--source', help="file source")
    parser.add_argument('--destination', help="file destination")
    args = parser.parse_args()

    print "Arguments", args
    # file_from = 'test_video.mp4'
    # file_to = '/test_dropbox/test_video.mp4'
    file_from = args[0]
    file_to = args[1]

    videoUploader.upload_file(file_from, file_to)


# print "DROPBOX KEY", DROPBOX_KEY

if __name__ == '__main__':
    app.run()

## script has to download youtube



