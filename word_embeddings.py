import gensim.downloader
model = gensim.downloader.load("glove-wiki-gigaword-50")
model["tower"]

model["king"] + model["woman"] - model["man"]

from scipy.spatial import distance
print(
    distance.cosine((model["queen"] - model["king"]), (model["woman"] - model["man"])),
    sep='\n'
)

print(
    distance.cosine(model["queen"], model["king"]) - distance.cosine(model["woman"], model["man"]),
    sep='\n'
)