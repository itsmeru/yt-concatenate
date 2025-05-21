import os

from settings import CAPTIONS_DIR, VEDIOS_DIR


class Youtube:
    def __init__(self, url):
        self.url = url
        self.id = self.get_vedio_id_from_url(url)
        self.caption_filepath = self.get_caption_filepath()
        self.video_filepath = self.get_vedio_filepath()
        self.captions = None

    @staticmethod
    def get_vedio_id_from_url(url):
        return url.split('watch?v=')[-1]

    def get_caption_filepath(self):
        return os.path.join(CAPTIONS_DIR, f'{self.id}.txt')

    def get_vedio_filepath(self):
        return os.path.join(VEDIOS_DIR, f'{self.id}.mp4')

    def __str__(self):
        return f'<YT({self.id})>'

    def __repr__(self):
        content = ' : '.join([
            f'id={str(self.id)}',
            f'caption_filepath={str(self.caption_filepath)}',
            f'video_filepath={str(self.video_filepath)}'
        ])
        return f'<YT({content})>'
