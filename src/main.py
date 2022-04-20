import preprocess
from scene_utils import scene_classifier
import video_download as vd
import os


def get_path(base):
    paths = []
    with os.scandir(base) as entries:
        for entry in entries:
            paths.append(base + '/' + entry.name)
            pass
    return paths


# vid_infos = vd.get_vid_paths('video.csv')
# finish_download = vd.download_vid(vid_infos)
finish_download = True

if finish_download:
    print('Start resolving...')
    vid_paths = get_path('../inputs/full_game_1080p')
    total = len(vid_paths)
    current = 1
    proccessed = 0
    for vid_path in vid_paths:
        print(f'Progress: {current}/{total}\nFailed: {proccessed}', '\n', 'Current path: ', vid_path)
        success, vid_info = preprocess.video_preprocess(vid_path)
        if success:
            current += 1
        else:
            proccessed += 1
        print('Processed: ', success, '\n', 'Video info: ', vid_info)
    print('Finish resolving!')
    print('='*30)