# K-means Clustering

K-means alternates between assigning points to the nearest centroid and moving each centroid to the mean of its assigned points.

## Open

- [kmeans-cluster.ipynb](kmeans-cluster.ipynb)

## What To Watch

- The objective is within-cluster squared distance.
- Assignment and update steps each reduce or preserve that objective.
- Different initial centroids can lead to different final clusters.
- The method assumes clusters are well represented by Euclidean centers.

## Read Next

- [MacQueen, Some Methods for Classification and Analysis of Multivariate Observations](https://digicoll.lib.berkeley.edu/record/113015) - early k-means source.
- [Lloyd, Least Squares Quantization in PCM](https://doi.org/10.1109/TIT.1982.1056489) - classic Lloyd algorithm reference.
- [scikit-learn KMeans documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) - parameter and implementation notes.
