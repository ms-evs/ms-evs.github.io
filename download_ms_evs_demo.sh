#########################################################
# Use this script to download and uncompress the MS-EVS 
#   demo samples. 
#
# Note: create the root of your dictionary and run the script from there
#     cd /your/path/to/dataset/root/
#     mkdir MS-EVS
#     cd MS-EVS
#     ./download_ms_evs_demo.sh
#
# Make sure to double check the code in the script !!
# This code comes with no guarantees
#########################################################

for subset in N-YoutubeFaces N-MobiFace N-SpectralFace
do 
    # Download
    download_path=$subset/sample
    wget -np -R "index.html*" -c -nH -r http://ms-evs.aisoft.org/$download_path/

    # Uncompress and delete compressed file
    for compressed_file_path in ./$download_path/*.h5.zst
    do
        # Extract filename without extension
        filename=$(basename "$compressed_file_path" | cut -d . -f1)
        final_file_path=./$download_path/$filename.h5
        
        zstd -d $compressed_file_path -o $final_file_path
        rm $compressed_file_path
    done
done
