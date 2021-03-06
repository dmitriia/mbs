# -*- coding: utf8 -*-
import numpy
import pandas

data = pandas.DataFrame([
	[u'RU000A0ZYJT2', u'ВТБ_1', '2019-02-01', 24799576854.94, 286128192.52],
	[u'RU000A0ZYJT2', u'ВТБ_1', '2019-05-01', 22592056261.94, 259421954.03],
	[u'RU000A0ZYJT2', u'ВТБ_1', '2019-01-01', 25531606666.14, 295704426.84],
	[u'RU000A0ZYJT2', u'ВТБ_1', '2019-03-01', 24040242789.37, 272137731.74],
	[u'RU000A0ZYJT2', u'ВТБ_1', '2019-04-01', 23250456384.04, 248552485.74],
	[u'RU000A0ZYJT2', u'ВТБ_1', '2018-11-01', 28034201996.36, 321709738.97],
	[u'RU000A0ZYJT2', u'ВТБ_1', '2018-12-01', 26837393387.14, 315004331.11],
	[u'RU000A0ZYL89', u'РФБ1', '2019-02-01', 3654496508.75, 39610708.62],
	[u'RU000A0ZYL89', u'РФБ1', '2019-05-01', 3320022495.35, 34917546.14],
	[u'RU000A0ZYL89', u'РФБ1', '2019-04-01', 3440705341.25, 32517770.18],
	[u'RU000A0ZYL89', u'РФБ1', '2019-01-01', 3786041436.77, 39311328.89],
	[u'RU000A0ZYL89', u'РФБ1', '2018-06-01', 5454187866.25, 57186128.99],
	[u'RU000A0ZYL89', u'РФБ1', '2018-07-01', 5159715681.67, 55410537.71],
	[u'RU000A0ZYL89', u'РФБ1', '2018-02-01', 6724168326.21, 71204543.76],
	[u'RU000A0ZYL89', u'РФБ1', '2019-03-01', 3541069221.10, 36038267.82],
	[u'RU000A0ZYL89', u'РФБ1', '2018-05-01', 5780677264.28, 62438690.78],
	[u'RU000A0ZYL89', u'РФБ1', '2018-12-01', 3997626372.38, 42867782.34],
	[u'RU000A0ZYL89', u'РФБ1', '2018-11-01', 4192823288.33, 43224961.60],
	[u'RU000A0ZYL89', u'РФБ1', '2018-04-01', 6145202574.78, 59259367.21],
	[u'RU000A0ZYL89', u'РФБ1', '2018-03-01', 6448880674.61, 66683405.49],
	[u'RU000A0ZYL89', u'РФБ1', '2018-10-01', 4410612378.50, 46550522.30],
	[u'RU000A0ZYL89', u'РФБ1', '2018-09-01', 4600266625.26, 49076742.12],
	[u'RU000A0ZYL89', u'РФБ1', '2018-01-01', 7000786962.80, 21181910.04],
	[u'RU000A0ZYL89', u'РФБ1', '2018-08-01', 4834772601.24, 50111532.21],
],
	columns=[u'ISIN', u'NAM', u'DAT', u'BOP', u'YLD']
)


def histcf(isin):

    df = data.loc[data['ISIN'].values==isin, :].copy(deep=True)
    df.sort_values(by=u'DAT', inplace=True)

    if not df.empty:
        df = pandas.DataFrame([[numpy.nan] * len(df.columns)], columns=df.columns).append(df, ignore_index=True)

        df['YLD'] = df['YLD'].shift(-1)
        df.at[0, 'DAT'] = numpy.datetime64(df['DAT'][1], 'M') - 1
        df['DAT'] = df['DAT'].astype('datetime64[D]')

        df['AMT'] = df['BOP'].diff(-1)
        df = df.set_index('DAT').fillna(0)[:-1]

    else:
        print time.strftime('%Y-%m-%d %H:%M:%S'), 'histcf(...):', 'cannot find history cashflows for isin=', isin

    del df[u'ISIN']
    del df[u'NAM']

    return df
