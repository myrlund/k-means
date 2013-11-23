
import matplotlib.pyplot as plt
import random
import math

def k_means(documents, K):
    
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
    
    return clusters, centroids

def generate_random_documents(n, min_x, min_y, max_x, max_y):
    # Generate N random documents
    documents = []
    for _ in xrange(n):
        documents.append((random.random() * (Max_x - Min_x) + Min_x, random.random() * (Max_y - Min_y) + Min_y))
    return documents

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Finds cluster centroids of random documents.")
    parser.add_argument('-n', '--documents', help="number of random documents to generate", type=int, default=50)
    parser.add_argument('-k', '--clusters', help="number of clusters to fit", type=int, default=5)
    parser.add_argument('--min-x', help="minimum generated x value", type=int, default=0)
    parser.add_argument('--min-y', help="minimum generated y value", type=int, default=0)
    parser.add_argument('--max-x', help="maximum generated x value", type=int, default=50)
    parser.add_argument('--max-y', help="maximum generated y value", type=int, default=50)
    args = parser.parse_args()

    N = args.documents
    K = args.clusters

    Min_x = args.min_x
    Min_y = args.min_y
    Max_x = args.max_x
    Max_y = args.max_y
    
    # Generate some documents
    documents = generate_random_documents(N, min_x=Min_x, min_y=Min_y, max_x=Max_x, max_y=Max_y)
    
    # Run the algorithm
    clusters, centroids = k_means(documents, K)
    
    # Plot the documents and the cluster centroids
    x, y = zip(*documents)
    plt.plot(x, y, 'ro')
    plt.scatter(*zip(*centroids), s=100)
    plt.show()
