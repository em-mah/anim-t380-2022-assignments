source etc/.aliases
export asset=someAsset

mayapy python/prep_asset.py $asset
mkdir -p "./assets/$asset/maya/scenes"
mv assignment_3.ma $_