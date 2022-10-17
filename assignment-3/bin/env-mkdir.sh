mkdir -p "./assets/${asset}/maya/scenes"
mayapy python/prep_asset.py $asset "./assets/${asset}/maya/scenes/${asset}.ma"
