import urllib.request
import json

from pipeline.steps.step import Step
from settings import API_KEY
from utils import Utils


class GetVedioList(Step):
    def process(self, data: list, inputs: dict, utils: Utils) -> list:
        channel_id = inputs['channel_id']

        if utils.video_list_file_exist(channel_id):
            return self.read_file(utils.get_video_list_filepath(channel_id))

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = f'{base_search_url}key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])
                    if len(video_links) >= inputs['vedio_limit']:
                        return video_links
            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break

        self.write_to_file(video_links, utils.get_video_list_filepath(channel_id))
        return video_links

    def write_to_file(self, video_links, file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            for url in video_links:
                f.write(url + '\n')

    def read_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            vedio_links = []
            for url in f:
                vedio_links.append(url.strip())
        return vedio_links
