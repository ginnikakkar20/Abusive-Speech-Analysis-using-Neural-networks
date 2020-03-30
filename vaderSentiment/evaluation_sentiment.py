import os
import json
from io import open
from os import listdir
from os.path import isfile, join


if __name__ == '__main__':

    FILEPATH = 'master_dict.json'

    with open(FILEPATH, 'r') as f:
        data = json.load(f)
    
    pos_arr_cnt = [0, 0, 0, 0]
    neg_arr_cnt = [0, 0, 0, 0]
    # read data from the json file with all comments and their sentiment scores to get confusion matrix values
    for i in data:
        for j in data:
            if i <= j:
                continue
            # Scores for confusion matrix for Like-Positive Score pair
            if (data[i]['likes'] <= data[j]['likes'] and data[i]['pos_score'] <= data[j]['pos_score']):
                pos_arr_cnt[0]+=1
            if (data[i]['likes'] > data[j]['likes'] and data[i]['pos_score'] <= data[j]['pos_score']):
                pos_arr_cnt[1]+=1
            if (data[i]['likes'] <= data[j]['likes'] and data[i]['pos_score'] > data[j]['pos_score']):
                pos_arr_cnt[2]+=1
            if (data[i]['likes'] > data[j]['likes'] and data[i]['pos_score'] > data[j]['pos_score']):
                pos_arr_cnt[3]+=1
            # Scores for confusion matrix for Dislike-Negative Score pair
            if (data[i]['dislikes'] <= data[j]['dislikes'] and data[i]['neg_score'] <= data[j]['neg_score']):
                neg_arr_cnt[0]+=1
            if (data[i]['dislikes'] > data[j]['dislikes'] and data[i]['neg_score'] <= data[j]['neg_score']):
                neg_arr_cnt[1]+=1
            if (data[i]['dislikes'] <= data[j]['dislikes'] and data[i]['neg_score'] > data[j]['neg_score']):
                neg_arr_cnt[2]+=1
            if (data[i]['dislikes'] > data[j]['dislikes'] and data[i]['neg_score'] > data[j]['neg_score']):
                neg_arr_cnt[3]+=1




