import pytest
import cv2
import pathlib

from cvutils.imutils import crop_img


def test_crop_img_color():
    data_root = pathlib.Path(__file__).parent.joinpath('data')
    img = cv2.imread(str(data_root / 'OpenCV_Logo.png'))
    h, w, c = crop_img(img, 5, 5).shape
    assert 1332 == h
    assert 1080 == w
    assert 3 == c


def test_crop_img_gray():
    data_root = pathlib.Path(__file__).parent.joinpath('data')
    img = cv2.imread(str(data_root / 'OpenCV_Logo_gray.png'))
    h, w, c = crop_img(img, 5, 5).shape
    assert 1332 == h
    assert 1080 == w
