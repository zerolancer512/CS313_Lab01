import numpy as np
import pandas as pd
import math

# ============= Bai 1 =====================
def is_numeric(Series):
    n = np.random.randint(len(Series))
    while Series[n] == '?':
        n = np.random.randint(len(Series))
    return str(Series[n]).replace('.','').isdigit()
        
    
def summary(log_file_path = 'log.txt', input_file_path = 'data.txt'):
    data_file = pd.read_csv(input_file_path, sep=',')
    log_file = open(log_file_path,'a', encoding = 'utf-8')
    log_file.writelines('{} Summary {}\n'.format(20*'=',20*'='))
    log_file.writelines('# {}\n'.format(data_file.shape[0]))
    log_file.writelines('# {}\n'.format(data_file.shape[1]))
    for i,col in enumerate(data_file.columns):
        if is_numeric(data_file[col]):
            log_file.write('#Thuộc tính {}: <{}> <numeric>\n'.format(i+1,col))
        else:
            log_file.write('#Thuộc tính {}: <{}> <nominal>\n'.format(i+1,col))
    log_file.close()

# ===============Bai 2 ================
def mean(Series):
    sum = 0
    for i in Series.dropna():
        sum = sum + float(i)
    return sum/len(Series)


def most_frequency(Series):
    return Series.value_counts().idxmax()


def replace(log_file_path = 'log.txt', input_file_path = 'data.txt', output_file_path = 'replaced_data.txt'):
    data_file = pd.read_csv(input_file_path,sep=',')
    log_file = open(log_file_path,'a', encoding = 'utf-8')
    log_file.writelines('{} Replace {}\n'.format(20*'=',20*'='))
    for col in data_file.columns:
        counter = len(data_file.loc[data_file[col]=='?',col])
        if is_numeric(data_file[col]):
            if data_file[col].dtypes == 'object':
                data_file[col] = pd.to_numeric(data_file[col], errors = 'coerce')
            else:
                pass
            mean_col = mean(data_file[col])
            data_file.loc[data_file[col]=='?',col] = mean_col
            log_file.writelines('#Thuộc tính: <{}>, <{}>, <{}>\n'.format(col, counter, mean_col))
        else:
            most_frequency_col = most_frequency(data_file[col])
            data_file.loc[data_file[col]=='?',col] = most_frequency_col
            log_file.writelines('#Thuộc tính: <{}>, <{}>, <{}>\n'.format(col, counter, most_frequency_col))
    log_file.close()
    data_file.to_csv(output_file_path, index = False)

# ===============Bai 3 ================

def discritize(n, equal_width = True, equal_depth = False,log_file_path = 'log.txt', input_file_path = 'data.txt', output_file_path = 'discritized_data.txt'): #Equal Width Default
    data_file = pd.read_csv(input_file_path,sep=',')
    log_file = open(log_file_path,'a', encoding = 'utf-8')
    log_file.writelines('{} Discritize {}\n'.format(20*'=',20*'='))
    if equal_depth == True:   # n in equal-depth is number of components in each bin
        equal_width = False
        for col in data_file.columns:
            if is_numeric(data_file[col]):
                log_file.writelines('# Thuộc tính: <{}> '.format(col))
                if data_file[col].dtypes == 'object':
                    data_file[col] = pd.to_numeric(data_file[col], errors = 'coerce')
                else:
                    pass
                data_file.sort_values(by = [col], inplace = True, ignore_index = True)
                for i in range(0, len(data_file[col]), n):
                    i_new = i + n
                    temp = data_file.loc[i:i_new-1,col]
                    log_file.writelines('<{}, {}>: <{}> '.format(temp.min(),temp.max(),len(temp)))
                    data_file.loc[i:i_new-1,col] = mean(data_file.loc[i:i_new-1,col])
                log_file.writelines('\n')
        data_file.to_csv(output_file_path, index = False)
    else:                   # n in equal-width is number of bin
        for col in data_file.columns:
            if is_numeric(data_file[col]):
                log_file.writelines('# Thuộc tính: <{}> '.format(col))
                if data_file[col].dtypes == 'object':
                    data_file[col] = pd.to_numeric(data_file[col], errors = 'coerce')
                else:
                    pass
                data_file.sort_values(by = [col], inplace = True, ignore_index = True)
                width = int((data_file[col].max() - data_file[col].min())/n) + 1
                key = data_file[col][0]
                while key<data_file[col].max():
                    temp = [i for i in data_file[col] if i < key + width and i >=key]
                    if len(temp) == 0:
                        log_file.writelines('<0, 0>: <0> ')
                        key = key + width
                    else:
                        key = key + width
                        log_file.writelines('<{}, {}>: <{}> '.format(min(temp),max(temp),len(temp)))
                        data_file[col].replace(temp, mean(pd.Series(temp)), inplace = True)
                log_file.writelines('\n')
        data_file.to_csv(output_file_path, index = False)

# ===============Bai 4 ================

def min_max_scaler(Series):

    return pd.Series([round((i - Series.min())/(Series.max() - Series.min()),8) for i in Series.dropna()])

def std(Series):
    sum_squared = 0
    mean_series = mean(Series)
    for i in Series.dropna():
        sum_squared = sum_squared + (i-mean_series)**2
    return math.sqrt(sum_squared/(len(Series)))

def z_score(Series):
    return pd.Series([(i - mean(Series))/std(Series) for i in Series.dropna()])

def normalize(method = 1, log_file_path = 'log.txt', input_file_path = 'data.txt', output_file_path = 'normalized_data.txt'):
    data_file = pd.read_csv(input_file_path,sep=',')
    log_file = open(log_file_path,'a', encoding = 'utf-8')
    log_file.writelines('{} Normalize {}\n'.format(20*'=',20*'='))
    if method == 2:
        for col in data_file.columns:
            if is_numeric(data_file[col]):
                if data_file[col].dtypes == 'object':
                    data_file[col] = pd.to_numeric(data_file[col], errors = 'coerce')
                else:
                    pass
                data_file[col] = z_score(data_file[col])
                log_file.writelines('# Thuộc tính: <{}> <{}, {}>\n'.format(col, data_file[col].min(), data_file[col].max()))
        data_file.to_csv(output_file_path, index = False)
    if method == 1:
        for col in data_file.columns:
            if is_numeric(data_file[col]):
                if data_file[col].dtypes == 'object':
                    data_file[col] = pd.to_numeric(data_file[col], errors = 'coerce')
                else:
                    pass
                data_file[col] = min_max_scaler(data_file[col])
                log_file.writelines('# Thuộc tính: <{}> <{}, {}>\n'.format(col, data_file[col].min(), data_file[col].max()))
        data_file.to_csv(output_file_path, index = False)

if __name__ == "__main__":
    print('Các chức năng cho chương trình:\n 1 - Summary\n 2 - Replace\n 3 - Discritize\n 4 - Normalize\n')
    n = int(input('Nhập chức năng cho chương trình: '))
    while n > 4 or n < 1:
        n = int(input('Chức năng không tồn tại, vui lòng nhập lại: '))
    input_file_path = str(input('Nhập đường dẫn dữ liệu đầu vào: '))
    output_file_path = str(input('Nhập đường dẫn tập tin đầu ra (0 nếu dùng tập tin mặc định): '))
    log_file_path = str(input('Nhập đường dẫn cho tập tin log(0 nếu dùng tập tin mặc định): '))

    if n == 1:
        if log_file_path == '0':
            summary(input_file_path = input_file_path)
        else:
            summary(log_file_path = log_file_path, input_file_path=input_file_path)
    elif n == 2:
        if log_file_path == '0' and output_file_path == '0':
            replace(input_file_path = input_file_path)
        elif log_file_path == '0':
            replace(input_file_path = input_file_path, output_file_path=output_file_path)
        elif output_file_path == '0':
            replace(input_file_path = input_file_path, log_file_path=log_file_path)
        else:
            replace(input_file_path = input_file_path, log_file_path=log_file_path, output_file_path=output_file_path)
    elif n == 3:
        print('Chọn phương pháp chia giỏ:\n 1 - Equal Width\n 2 - Equal Depth\n')
        i = int(input('Nhập phương pháp: '))
        while i < 1 or i > 2:
            i = int(input('Nhập lại phương pháp: '))
        if i == 1:
            j = int(input('Nhập số giỏ muốn chia: '))
            if log_file_path == '0' and output_file_path == '0':
                discritize(n=j,input_file_path = input_file_path)
            elif log_file_path == '0':
                discritize(n=j,input_file_path = input_file_path, output_file_path=output_file_path)
            elif output_file_path == '0':
                discritize(n=j,input_file_path = input_file_path, log_file_path=log_file_path)
            else:
                discritize(n=j,input_file_path = input_file_path, log_file_path=log_file_path, output_file_path=output_file_path)
        else:
            j = int(input('Nhập số phần tử mỗi giỏ: '))
            if log_file_path == '0' and output_file_path == '0':
                discritize(n=j,input_file_path = input_file_path, equal_depth=True)
            elif log_file_path == '0':
                discritize(n=j,input_file_path = input_file_path, output_file_path=output_file_path,equal_depth=True)
            elif output_file_path == '0':
                discritize(n=j,input_file_path = input_file_path, log_file_path=log_file_path,equal_depth=True)
            else:
                discritize(n=j,input_file_path = input_file_path, log_file_path=log_file_path, output_file_path=output_file_path,equal_depth=True)
    else:
        print('Chọn phương pháp chuẩn hóa:\n 1 - Min Max Scale\n 2 - Z-Score\n')
        i = int(input('Nhập phương pháp: '))
        while i < 1 or i > 2:
            i = int(input('Nhập lại phương pháp: '))
        if i == 1:
            if log_file_path == '0' and output_file_path == '0':
                normalize(input_file_path = input_file_path)
            elif log_file_path == '0':
                normalize(input_file_path = input_file_path, output_file_path=output_file_path)
            elif output_file_path == '0':
                normalize(input_file_path = input_file_path, log_file_path=log_file_path)
            else:
                normalize(input_file_path = input_file_path, log_file_path=log_file_path, output_file_path=output_file_path)
        else:
            if log_file_path == '0' and output_file_path == '0':
                normalize(input_file_path = input_file_path,method=i)
            elif log_file_path == '0':
                normalize(input_file_path = input_file_path, output_file_path=output_file_path,method=i)
            elif output_file_path == '0':
                normalize(input_file_path = input_file_path, log_file_path=log_file_path,method=i)
            else:
                normalize(input_file_path = input_file_path, log_file_path=log_file_path, output_file_path=output_file_path,method=i)