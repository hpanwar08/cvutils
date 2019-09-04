import numpy as np
import cv2
import matplotlib.pyplot as plt


def crop_img(img: np.array, h_val: float, w_val: float) -> np.array:
    """
    Crop image based on percentage of height and weight
    Args:
        img (np.array): image
        h_val (float): e.g. 5 or 0.05 from top and bottom
        w_val (float): e.g. 5 or 0.05 from left and right

    Returns:
        img (np.array)
    """
    if w_val > 1.0:
        w_val /= 100.0
    if h_val > 1.0:
        h_val /= 100.0
    if len(img.shape) == 2:
        h, w = img.shape
        return img[
               int(h * h_val): h - int(h * h_val),
               int(w * w_val): w - int(w * w_val)
               ]
    else:
        h, w, c = img.shape
        return img[
               int(h * h_val): h - int(h * h_val),
               int(w * w_val): w - int(w * w_val),
               :
               ]


def show_img_cv2(img, figsize=(10, 10), change_color=cv2.COLOR_BGR2RGB, alpha=1.0, ax=None, title=None):
    """
    Function to show opencv image (BGR) in matplotlib
    Args:
        img: np.array
        figsize: size of figure
        change_color:
        alpha: transparency
        ax: axis
        title: title of the image

    Returns:
        ax: axis
    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=figsize)
    if len(img.shape) == 2:
        _ = ax.imshow(img, alpha=alpha, cmap='gray')
    else:
        img = cv2.cvtColor(img, change_color)
        _ = ax.imshow(img, alpha=alpha)
    if title is not None:
        _ = ax.set_title(title, fontsize=20)
    ax.axis('off')
    return ax


def show_img(img, figsize=(10, 10), alpha=1.0, ax=None, title=None):
    """
    Function to show image (RGB) in matplotlib
    Args:
        img: np.array
        figsize: size of figure
        alpha: transparency
        ax: axis
        title: title of the image

    Returns:
        ax: axis
    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=figsize)
    if len(img.shape) == 2:
        _ = ax.imshow(img, alpha=alpha, cmap='gray')
    else:
        _ = ax.imshow(img, alpha=alpha)
    if title is not None:
        _ = ax.set_title(title, fontsize=20)
    ax.axis('off')
    return ax
