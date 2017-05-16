# -*- coding: utf-8 -*-

import random
from scipy.io.wavfile import read
from PIL import Image


def make_image(screen, bgcolor, filename):
    img = Image.new('RGB',
                    screen,
                    bgcolor)
    img.save(filename)


def make_movie():
    """
    WIP: 生成した画像を組み合わせて動画化する
    """

    return


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

    done = []
    mc = {}

    for i in music:
        rand = gen_random_colorcode()

        if not isExistInList(done, rand):
            mc.update({i: rand})

    return mc


if __name__ == '__main__':
    # wav file読み込み
    wav_file = './ihdd.wav'
    wave = read(wav_file)
    frequency = 44100
    # 1次元に
    scale = wave[1][:frequency, 0]

    screen = (1920, 1080)

    mc = associate_music_colorcode(scale)

    count = 0
    for i in scale:
        print(mc[i])
        make_image(screen, mc[i], "images/s" + str(count) + ".png")
        count += 1
