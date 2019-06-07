import cv2
import numpy as np


DEBUG = 1  # If you want to use debug mode -> set 1, else 0
CAP = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
H_TEMPLATE = cv2.imread('H.jpg', 0)
S_TEMPLATE = cv2.imread('S.jpg', 0)
U_TEMPLATE = cv2.imread('U.jpg', 0)


def SetResolution(width=640, height=480):
    CAP.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    CAP.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


def MakeTemplate(path):
    """
    Making photo of template
    :param path: name of file (means, that photo would be saved in folder, where program exists)
    """
    while True:
        _, photo = CAP.read()
        cv2.imshow('photo', photo)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            cv2.imwrite(path, photo)
            break
    CAP.release()
    cv2.destroyAllWindows()


def DebugImShow():
    """
    just showing image
    """
    _, threshold1 = cv2.threshold(HHH, 60, 255, cv2.THRESH_BINARY)
    _, threshold2 = cv2.threshold(HGRAY, 60, 255, cv2.THRESH_BINARY)
    med = cv2.medianBlur(HGRAY, 3)

    cv2.imshow('IMAGE', HHH)
    cv2.imshow('gray', HGRAY)
    cv2.imshow('threshold1', threshold1)
    cv2.imshow('threshold2', threshold2)
    cv2.imshow('med', med)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def DebugViShow():
    while True:
        _, frame = CAP.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gaus1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

        cv2.imshow('frame', frame)
        cv2.imshow('gray', gray)
        cv2.imshow('gaus1', gaus1)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    CAP.release()
    cv2.destroyAllWindows()


def DebugImTemplateMatching():
    w, h = H_TEMPLATE.shape[::-1]
    res = cv2.matchTemplate(HGRAY, H_TEMPLATE, cv2.TM_CCOEFF_NORMED)
    threshold = 0.7
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(HHH, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 1)

    cv2.imshow('detected', HHH)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def DebugViTemplateMatching():
    threshold = 0.7
    H_w, H_h = H_TEMPLATE.shape[::-1]
    S_w, S_h = S_TEMPLATE.shape[::-1]
    U_w, U_h = U_TEMPLATE.shape[::-1]
    while True:
        _, frame = CAP.read()
        frame_temp = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # matching H
        H_res = cv2.matchTemplate(frame_temp, H_TEMPLATE, cv2.TM_CCOEFF_NORMED)
        H_loc = np.where(H_res >= threshold)
        pt = list(zip(*H_loc[::-1]))
        try:
            cv2.rectangle(frame, pt[0], (pt[0][0]+H_w, pt[0][1]+H_h), (0, 255, 255), 1)
        except IndexError:
            pass

        # matching S
        S_res = cv2.matchTemplate(frame_temp, S_TEMPLATE, cv2.TM_CCOEFF_NORMED)
        S_loc = np.where(S_res >= threshold)
        pt = list(zip(*S_loc[::-1]))
        try:
            cv2.rectangle(frame, pt[0], (pt[0][0] + S_w, pt[0][1] + S_h), (255, 0, 255), 1)
        except IndexError:
            pass

        # matching U
        U_res = cv2.matchTemplate(frame_temp, U_TEMPLATE, cv2.TM_CCOEFF_NORMED)
        U_loc = np.where(U_res >= threshold)
        pt = list(zip(*U_loc[::-1]))
        try:
            cv2.rectangle(frame, pt[0], (pt[0][0] + U_w, pt[0][1] + U_h), (255, 255, 0), 1)
        except IndexError:
            pass

        cv2.imshow('lol', frame)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    CAP.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    CAP.set(cv2.CAP_PROP_FPS, 10)
    #DebugImTemplateMatching()
    SetResolution(1200, 680)
    #DebugImShow()
    #DebugViShow()
    DebugViTemplateMatching()
    #MakeTemplate('H.jpg')

