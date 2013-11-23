
import matplotlib.pyplot as plt
import random
import math
import argparse

parser = argparse.ArgumentParser(description="Finds cluster centroids of random documents.")
parser.add_argument('-n', '--documents', help="number of random documents to generate", type=int, default=50)
parser.add_argument('-k', '--clusters', help="number of clusters to fit", type=int, default=5)
args = parser.parse_args()

N = args.documents
K = args.clusters

Min_x = Min_y = 0
Max_x = Max_y = 50

# Generate N random documents
documents = []
for _ in xrange(N): documents.append((random.random() * (Max_x - Min_x) + Min_x, random.random() * (Max_y - Min_y) + Min_y))

# Assign cluster centroids to random documents (the first K documents)
centroids = []
for u in xrange(K): centroids.append(documents[u])

previous_clusters = None
while True:
    
    # Reset clusters
    clusters = []
    for _ in xrange(K): clusters.append([])
    
    # Assign documents to nearest centroid
    for doc in documents:
        min_j = 0
        min_dist = 1000
        for k in xrange(K):
            dist = math.sqrt((centroids[k][0] - doc[0])**2 + (centroids[k][1] - doc[1])**2)
            if dist <= min_dist:
                min_j = k
                min_dist = dist
        clusters[min_j].append(doc)
    
    # Adjust each cluster centroid to the mean of cluster members
    for u in xrange(K):
        center = [0, 0]
        for doc in clusters[u]:
            center[0] += doc[0]
            center[1] += doc[1]
        center = (center[0] / len(clusters[u]), center[1] / len(clusters[u]))
        centroids[u] = center
    
    # Break if iteration didn't cause a change in cluster config
    if previous_clusters == clusters:
        break
    previous_clusters = clusters

# Plot the documents and the cluster centroids
x, y = zip(*documents)
plt.plot(x, y, 'ro')
plt.scatter(*zip(*centroids), s=100)
plt.show()
