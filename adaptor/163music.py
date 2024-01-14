import requests


def get_song_comments(song_id):
    url = f'https://music.163.com/api/v1/resource/comments/R_SO_4_{song_id}?limit=200'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.1 Safari/537.36',
        'Referer': 'https://music.163.com/',
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        comments = data['hotComments']
        print(f"共抓取到 {len(comments)} 条热评")
        for comment in comments:
            content = comment['content']
            print(content)
    else:
        print('Failed to get song comments.')


if __name__ == '__main__':
    search_song_id("测试")
