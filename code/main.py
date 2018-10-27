#! /usr/bin/python
# -*- coding: utf-8 -*-
from utils import Processing
from featureExtraction import Not, WordMatchShare,\
     Length, NgramJaccardCoef, long_common_sequence,\
     fuzz_partial_token_set_ratio, fuzz_partial_token_sort_ratio,\
     TFIDFSpanish

if __name__ == '__main__':
    Model_Flag = 2
    config_fp = './featwheel.conf'

    if Model_Flag == 1:
        data_pt = '../data/RowData/cikm_spanish_train_20180516.txt'
        save_pt = '../data/PreProcessingData/cikm_spanish_train.cvs'
        Processing().excute(data_pt, save_pt)

    if Model_Flag == 2:
        data_fp = '../data/PreProcessingData/cikm_spanish_train.cvs'
        feature_version = 0
        Not(config_fp).extract(data_fp=data_fp, feature_version=0)
        WordMatchShare(config_fp).extract(data_fp=data_fp, feature_version=0)
        Length(config_fp).extract(data_fp=data_fp, feature_version=0)
        NgramJaccardCoef(config_fp).extract(data_fp=data_fp, feature_version=0)
        long_common_sequence(config_fp).extract(data_fp=data_fp, feature_version=0)
        fuzz_partial_token_set_ratio(config_fp).extract(data_fp=data_fp, feature_version=0)
        fuzz_partial_token_sort_ratio(config_fp).extract(data_fp=data_fp, feature_version=0)
        TFIDFSpanish(config_fp, data_fp).extract(data_fp=data_fp, feature_version=0)
