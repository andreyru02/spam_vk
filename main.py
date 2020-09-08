from time import sleep
import requests

# ПОЛУЧЕНИЕ ТОКЕНА
username = '79254615279'
password = 'agentbond999'

resp = requests.get(
    f'https://oauth.vk.com/token?grant_type=password&client_id=3697615&client_secret=AlVXZFMUqyrnABp8ncuU&username={username}&password={password}').json()
token = resp["access_token"]

# ПОЛУЧЕНИЕ СПИСКА ГРУПП
with open('group.txt', 'r') as g_file:
    group = g_file.read().splitlines()

# ПОЛУЧЕНИЕ СПИСКА ВИДЕО
with open('video.txt', 'r') as v_file:
    video = v_file.read().splitlines()


def spam(group, video, token):
    count = 0
    while True:
        try:
            for g in group:
                resp = requests.get('https://api.vk.com/method/wall.post'
                                    f'?owner_id={g}'  # ID group
                                    f'&attachments={video[count]}'  # video
                                    '&from_group=0'
                                    f'&access_token={token}&v=5.122')  # token
                res = resp.json().get('response').get('post_id')
                if res == int(res):
                    print(resp.json())
                    print(f'Пост отправлен!\n'
                          f'Группа: {g}\n'
                          f'Видео: {video[count]}')
                    print(f'Отправлено постов: {count+1}')
                    print('Пауза 1 час.')
                    sleep(3600)
            count += 1
            if count > len(video):  # если количество отправленных видео больше списка видео
                count = 0
        except:
            print('Произошла ошибка.')
            print(resp.json())
            break


if __name__ == '__main__':
    spam(group, video, token)

# получение токена https://github.com/fgRuslan/vk-spammer/blob/master/spam.py
# сохранение токена и авторизация по нему.