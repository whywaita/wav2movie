# -*- coding: utf-8 -*-

import random
import subprocess
from scipy.io.wavfile import read
from PIL import Image
import sys


def make_image(screen, bgcolor, filename):
    img = Image.new('RGB',
                    screen,
                    bgcolor)
    img.save(filename)


def make_movie():
    cmd = ('cd images ;'
           'ffmpeg -y -r 48000 -i img_%06d.png -i ../%s'
           '-acodec aac -strict experimental -ab 320k -ac 2 -ar 48000'
           '-vcodec libx264 -pix_fmt yuv420p -r 60'
           '../%s -shortest'
           % (sys.argv[1], "out.mp4")
           )
    subprocess.call(cmd, shell=True)


def gen_random_colorcode():
    """
    カラーコード相当の値をランダムで生成する
    """

    cc = '#'

    for i in range(0, 6):
        cc += random.choice('0123456789ABCDEF')

    return cc


def isExistInList(List, value):
    """
    リストの中に値があればTrue
    """
    for i in List:
        if value == i:
            return True

    return False


def associate_music_colorcode(music):
    """
    音階の配列を受け取って、カラーコードと対応付ける
    対応付けは乱数でやる
    """

    # done = []
    mc = {}

    for i in music:
        rand = gen_random_colorcode()

        # if not isExistInList(done, rand):
        mc.update({i: rand})

    return mc


if __name__ == '__main__':
    # wav file読み込み
    wav_file = sys.argv[1]
    fs, data = read(wav_file)
    # 1次元に(右だけ)
    scale = data[:, 0]  # フレーム全部
    # scale = data[:fs, 0]
    # scale = data[:120, 0]

    print(len(scale))

    # screen = (1920, 1080)
    # screen = (640, 480)
    screen = (160, 90)
    # screen = (2, 2)

    mc = associate_music_colorcode(scale)

    count = 0
    for i in scale:
        print("c : " + str(count) + ":" + mc[i])
        make_image(screen, mc[i], "images/img_{0:06d}.png".format(count))
        count += 1

    make_movie()
