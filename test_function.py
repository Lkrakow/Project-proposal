
import pandas as pd

def get_date_limits(file1: pd.DataFrame, file2: pd.DataFrame) -> list:
    """See what are the year limits of both dataset
    
    Args:
    Dataset 1 & 2
    
    Return:
    Year min and max limit of both dataset"""
    
    first_year_file1 = file1['time'].iloc[0].year
    first_year_file2 = file2['time'].iloc[0].year
    last_year_file1 = file1['time'].iloc[-1].year
    last_year_file2 = file2['time'].iloc[-1].year
    
    return [first_year_file1, first_year_file2, last_year_file1, last_year_file2]

def test_get_date_limits():
    data1 = pd.DataFrame({'time': pd.to_datetime(['1999-01-01', '2000-01-01', '2004-01-01', '2007-01-01', '2009-01-01'])})
    data2 = pd.DataFrame({'time': pd.to_datetime(['2000-01-01', '2004-01-01', '2007-01-01', '2009-01-01', '2010-01-01'])})
    result = get_date_limits(data1, data2)
    assert result == [1999,2000,2009,2010]
    
#def test_get_date_limits():
#    data1 = pd.DataFrame({'time': pd.to_datetime(['1998-01-01', '2000-01-01', '2004-01-01', '2007-01-01', '2009-01-01'])})
#    data2 = pd.DataFrame({'time': pd.to_datetime(['2000-01-01', '2004-01-01', '2007-01-01', '2009-01-01', '2010-01-01'])})
#    result = get_date_limits(data1, data2)
#    assert result == [1999,2000,2009,2010]

def test_get_date_limits():
    data1 = pd.DataFrame({'time': pd.to_datetime(['1976-01-01', '2003-01-01', '2016-01-01', '2025-01-01', '2030-01-01'])})
    data2 = pd.DataFrame({'time': pd.to_datetime(['1999-01-01', '2000-01-01', '2008-01-01', '2015-01-01', '2022-01-01'])})
    result = get_date_limits(data1, data2)
    assert result == [1976,1999,2030,2022]