Main.py uses OpenCV find contours to detect the chromosomes given the Karyogram. I used the cvzone library but changed mostly everything in the Utilities part of the library for the usage of this.
Diagnose.py will detect the number of chromosomes and classify the genetic disorders of the following:
- Klinefelter Syndrone
- Down Syndrome
- Turner's Syndrome
- Cancer
To differentiate Klinefelter and Down Syndrome, I sectioned off the bottom right corner of the Karyogram to identify the sex chromosomes and use the number of those to classify the diseases. I can also use this to identify the
gender of the person in the Karyogram. For more consistent results, I would need a more consistent dataset to accurately identify diseases.

Next project will be to identify chromosomes from a raw cell image using a deep learning neural network to put them into a Kaaryogram based on features.
