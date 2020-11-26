from typing import List

import requests

from pik_wrapper.entity.block import Block
from pik_wrapper.entity.bulk import Bulk
from pik_wrapper.entity.item import Item
from pik_wrapper.entity.location import Location
from pik_wrapper.value_object.photo import Photo


class PikWrapper:
    def __init__(self):
        self.base_url = 'https://api.pik.ru/v1/'
        self.headers = {
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                          'Version/13.0.3 Safari/605.1.15',
            'wrapper': 'https://github.com/drillcoder/python_pik_api_wrapper'
        }

    def send_request(self, url: str) -> List:
        if type(url) is not str:
            raise ValueError
        response = requests.get(self.base_url + url, headers=self.headers)
        if response.status_code != requests.codes.ok:
            raise ValueError
        if response.status_code == requests.codes.unprocessable:
            return []
        content = response.json()
        if type(content) is dict:
            if content.get('message') == 'ERR_NEWS_NOT_FOUND':
                raise []
            if type(content.get('items')) is not None:
                content = content.get('items')
        if type(content) is not list:
            raise ValueError
        return content

    def get_locations(self) -> List[Location]:
        locations = self.send_request('location')
        locations_list = []
        count = 0
        for location in locations:
            if location['id'] == 2:
                locations_list.append(Location('2', 'Москва', count))
                count += 1
                locations_list.append(Location('3', 'Московская область', count))
                continue
            locations_list.append(Location(str(location['id']), location['name'], count))
            count += 1
        return locations_list

    def get_blocks(self, location: Location) -> List[Block]:
        if type(location) is not Location:
            raise ValueError
        blocks = self.send_request(f"block?metadata=1&types=1,2&locations={location.id}")
        blocks_list = []
        for block in blocks:
            blocks_list.append(Block(str(block['id']), block['name'], block['sort']))
        return blocks_list

    def get_bulks(self, block: Block) -> List[Bulk]:
        if type(block) is not Block:
            raise ValueError
        bulks = self.send_request(f"bulk?block_id={block.id}")
        bulks_list = []
        count = 0
        for bulk in bulks:
            if bulk['type_id'] not in {1, 2, 103} or len(bulk['name']) == 0:
                continue
            bulks_list.append(Bulk(str(bulk['id']), bulk['name'], count, bulk['type_id']))
            count += 1
        return bulks_list

    def get_items(self, bulk: Bulk) -> List[Item]:
        if type(bulk) is not Bulk:
            raise ValueError
        items = self.send_request(f"news?limit=all&is_content=1&is_progress=1&bulk_id={bulk.id}")
        items_list = []
        for item in items:
            photos = []
            images_path = []
            sort = 0
            if item['preview'] != '':
                images_path.append(item['preview'])
                photos.append(Photo('https:' + item['preview'], 0))
                sort += 1
            if type(item.get('gallery')) is list:
                for photo in item['gallery']:
                    if photo['file_path'] in images_path:
                        continue
                    images_path.append(photo['file_path'])
                    photos.append(Photo('https:' + photo['file_path'], sort))
                    sort += 1
            items_list.append(Item(item['id'], item['public_date'], item['date'], photos))
        return items_list
