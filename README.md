K-means clustering
==================

    $ python k-means.py --help
    usage: k-means.py [-h] [-n DOCUMENTS] [-k CLUSTERS] [--min-x MIN_X]
                      [--min-y MIN_Y] [--max-x MAX_X] [--max-y MAX_Y]

    Finds cluster centroids of random documents.

    optional arguments:
      -h, --help            show this help message and exit
      -n DOCUMENTS, --documents DOCUMENTS
                            number of random documents to generate
      -k CLUSTERS, --clusters CLUSTERS
                            number of clusters to fit
      --min-x MIN_X         minimum generated x value
      --min-y MIN_Y         minimum generated y value
      --max-x MAX_X         maximum generated x value
      --max-y MAX_Y         maximum generated y value

Note
----

Depends on `matplotlib`.
