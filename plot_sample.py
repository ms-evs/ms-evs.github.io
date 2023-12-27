"""
Plots images, events and bounding boxes from an HDF5 file (helper for MS-EVS dataset)
This script comes without any guarantees.

Example usage:
    python plot_sample.py ./path/to/your/ms-evs/file.h5
"""
import argparse
import h5py
import cv2
import matplotlib.pyplot as plt
import numpy as np

R, G, B, A = 0, 1, 2, 3
EVENTS_TIME_WINDOW = 50 # ms

def binary_representation(events, time_of_interest, image_resolution, time_length_in_ms=EVENTS_TIME_WINDOW):
    """Returns a very simple representation of the events (around the time of interest)
    
    For the 'time_length' prior to time_of_interest, pixel is white if there was an event, 
    else we keep the pixel black if there was no event, regardless of polarity.
    """
    assert (image_resolution[0:2] == events.attrs['resolution']).all()
    output = np.zeros(events.attrs['resolution'], dtype=np.uint8)
    
    # Only keep events near the time of interest
    plot_flag = np.logical_and(time_of_interest - time_length_in_ms/1000 <= events['ts'][:], events['ts'][:] <= time_of_interest)
    
    plot_xs = events['xs'][plot_flag]
    plot_ys = events['ys'][plot_flag]
    for x, y in zip(plot_xs, plot_ys):
        output[y, x] = 255
    return output


def polarity_representation(events, time_of_interest, image_resolution, time_length_in_ms=EVENTS_TIME_WINDOW, transparent_bg=False):
    """Returns a polarity-separated binary representation of the events (around the time of interest)
    
    For the 'time_length' prior to time_of_interest, pixel is :
        - green if there was a positive event
        - red if there was a negative event
        - black if there was no event and transparent_bg is False
        - transparent if there was no event and transparent_bg is True
    """
    assert (image_resolution[0:2] == events.attrs['resolution']).all()
    output = np.zeros(image_resolution[0:2]+(4,), dtype=np.uint8) # RGBA
    
    # Only keep events near the time of interest
    plot_flag = np.logical_and(time_of_interest - time_length_in_ms/1000 <= events['ts'][:], events['ts'][:] <= time_of_interest)
    
    plot_xs = events['xs'][plot_flag]
    plot_ys = events['ys'][plot_flag]
    plot_ps = events['ps'][plot_flag]
    for x, y, p in zip(plot_xs, plot_ys, plot_ps):
        if p > 0:
            output[y, x, G] = 255
        else:
            output[y, x, R] = 255
        output[y,x,A] = 255
    if transparent_bg is False:
        output[:,:,A] = 255
    return output


def bboxes_on_transparent_bg(gt, time_of_interest, image_resolution):
    alpha_channel = np.zeros(image_resolution[0:2], dtype=np.uint8)
    rectangles = gt['descriptor'][np.where(gt['ts'][:]==time_of_interest)]
    for rect in rectangles:
        x1, y1, x2, y2 = map(int,rect[:4])
        cv2.rectangle(alpha_channel, (x1, y1), (x2, y2), color=255, thickness=2)

    output = np.ones(image_resolution[0:2]+(4,), dtype=np.uint8)*255
    output[:,:,A] = alpha_channel
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load and display data from an HDF5 file (MS-EVS file structure).")
    parser.add_argument("file_path", type=str, help="Path to the HDF5 file")
    args = parser.parse_args()

    with h5py.File(args.file_path, 'r') as file:
        # Get data
        events = file['device0/events']
        images = file['device0/images']
        labels = file['device0/gt/bbox_landmarks']
        
        ts_images = images['ts'][:]
        ts_gt = labels['ts'][:]

        # Initialize plot
        fig, axes = plt.subplots(3, 3, figsize=(9, 9))
        ts_to_plot = np.percentile(ts_images,[25, 50, 75], method='closest_observation')

        # Iterate over each sample to plot
        for row, t in enumerate(ts_to_plot):
            rgb = images['frames'][np.where(ts_images==t)[0][0]]
            event_binary_image = binary_representation(events, t, rgb.shape)
            event_polarity_image = polarity_representation(events, t, rgb.shape, transparent_bg=True)
            bbox_image = bboxes_on_transparent_bg(labels, t, rgb.shape)
            
            # RGB
            axes[row, 0].imshow(rgb)
            axes[row, 0].imshow(bbox_image)
            axes[row, 0].axis('off')
            # EVENTS
            axes[row, 1].imshow(event_binary_image)
            axes[row, 1].imshow(bbox_image)
            axes[row, 1].axis('off')
            # RGB + EVENTS
            axes[row, 2].imshow(rgb)
            axes[row, 2].imshow(event_polarity_image)
            axes[row, 2].axis('off')

    # Adjust layout for better spacing
    plt.tight_layout()

    # Show the plot
    plt.show()
