from NNCompressorReal import *

windows_weekly = [5, 6, 7, 8, 9, 10, 11, 12]
windows_daily = [5, 6, 7, 8, 9, 10, 11, 12,
                 13, 14, 16, 18, 20, 30, 40]

codes = ["YAHOO/INDEX_NYA", "YAHOO/INDEX_GSPTSE", "YAHOO/INDEX_HSI", "YAHOO/INDEX_MID",
         "YAHOO/INDEX_XOI", "YAHOO/INDEX_N225", "YAHOO/INDEX_AORD"]

frequencies = ["daily", "weekly"]

loss, accs = [], []
for frequency in frequencies:
    if frequency == "daily":
        windows = windows_daily
    else:
        windows = windows_weekly
    for code in codes:
        random.seed(0)
        numpy.random.seed(seed=0)
        loss, accs = compression_test_real(sims=55,
                                           code=code,
                                           window_sizes=windows,
                                           compression_rate=0.86,
                                           optimizer='sgd-momentum',
                                           sparcity='l0',
                                           max_epochs=500,
                                           start_date='1985-01-01',
                                           end_date='2016-01-01',
                                           collapse=frequency,
                                           file_out="Indices",
                                           in_loss=loss,
                                           in_accs=accs)