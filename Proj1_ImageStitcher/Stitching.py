import cv2
from cv2 import Stitcher

if __name__ == "__main__":
    img1 = cv2.imread('data/test3_l.png')
    img2 = cv2.imread('data/test3_r.png')
    # stitcher = cv2.createStitcher(False)
    stitcher = Stitcher.create(cv2.Stitcher_PANORAMA)
    (status, pano) = stitcher.stitch((img1, img2))
    # cv2.imshow('pano', pano)
    # cv2.waitKey(0)
    cv2.imwrite("res/result3_s.jpg", pano)
