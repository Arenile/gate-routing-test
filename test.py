TILES_PER_FIELD_X = 8
TILES_PER_FIELD_Y = 8
MAX_HEIGHT_LEVELS = 4

#actual gate placement function
#@app.route("/place-gate", methods=['GET'])
def tileGates(field_id : int):
	# get the field boundaries using field_id and endpoint
    
    test_field : dict[str, str] = {
        'sw_point': "36.0627|-94.1606",
        'nw_point': "36.0628|-94.1606",
        'ne_point': "36.0628|-94.1605",
        'se_point': "36.0627|-94.1605"
    }

    ########################

    current_field : dict[str, str] = test_field.copy()

    trans_field : dict[str: [str, float]] = {
        "sw_point" : {
            "lat" : float(current_field["sw_point"].split('|')[0]),
            "long" : float(current_field["sw_point"].split('|')[1])
        }, 
        "nw_point" : {
            "lat" : float(current_field["nw_point"].split('|')[0]),
            "long" : float(current_field["nw_point"].split('|')[1])
        }, 
        "se_point" : {
            "lat" : float(current_field["se_point"].split('|')[0]),
            "long" : float(current_field["se_point"].split('|')[1])
        }, 
        "ne_point" : {
            "lat" : float(current_field["ne_point"].split('|')[0]),
            "long" : float(current_field["ne_point"].split('|')[1])
        }
    } 
    
    print(trans_field)
	
	# tile the field and get the width and height of each tile

    n_dist = abs(trans_field["ne_point"]["long"] - trans_field["nw_point"]["long"])
    s_dist = abs(trans_field["se_point"]["long"] - trans_field["sw_point"]["long"])
    e_dist = abs(trans_field["se_point"]["lat"] - trans_field["ne_point"]["lat"])
    w_dist = abs(trans_field["sw_point"]["lat"] - trans_field["nw_point"]["lat"])

    print("n_dist = " + str(n_dist))
    print("s_dist = " + str(s_dist))
    print("w_dist = " + str(w_dist))
    print("e_dist = " + str(e_dist))

    tile_width = ((n_dist + s_dist) / 2) / TILES_PER_FIELD_X
    tile_height = ((e_dist + w_dist) / 2) / TILES_PER_FIELD_Y

    print("tile_widt = " + str(tile_width))
    print("tile_height = " + str(tile_height))

	# normalize heights

    print("BELOW THIS IS THE TILES_DICT \n")

    tiles_dict: dict[int: [str, str]] = {}

    for i in range(TILES_PER_FIELD_Y):
        for j in range(TILES_PER_FIELD_X):
            tile_dict = {}

            tile_dict["sw_point"] = str(trans_field["sw_point"]["lat"] + i*tile_height) + \
            "|" + \
            str(trans_field["sw_point"]["long"] + (j*tile_width))

            tile_dict["nw_point"] = str(trans_field["sw_point"]["lat"] + (i*tile_height + tile_height)) + \
            "|" + \
            str(trans_field["sw_point"]["long"] + (j*tile_width))

            tile_dict["se_point"] = str(trans_field["sw_point"]["lat"] + (i*tile_height)) + \
            "|" + \
            str(trans_field["sw_point"]["long"] + (j*tile_width + tile_width))

            tile_dict["ne_point"] = str(trans_field["sw_point"]["lat"] + (i*tile_height + tile_height)) + \
            "|" + \
            str(trans_field["sw_point"]["long"] + (j*tile_width + tile_width))
            
            tiles_dict[i*TILES_PER_FIELD_X + j] = tile_dict

    print(tiles_dict)

    # go get heights of every tile in dict and add to tiles_dict

    

	# build json response object of tiles
    
tileGates(1)

#sample request body
# {
#     "field_id": "yWezzFDhrspN5lAf52Jo",
#     "location": "50|50"
# }