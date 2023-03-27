import numpy as np
import pandas as pd
import scanpy as sc
#import scanpy.api as sc


def row_normal(data, factor=1e6):
    #行表示基因，列表示细胞,设为（m,m）
    #axis=1表示按行求和，即按基因求和
    row_sum = np.sum(data, axis=1)
    #增加一个维度，为(m,1)
    row_sum = np.expand_dims(row_sum, 1)
    #对应相除
    div = np.divide(data, row_sum)
    #以e为底的(m,1)
    div = np.log(1 + factor * div)
    return div


def load_newdata(train_datapath, metric='pearson', gene_scale=False, data_type='count', trans=True):
    print("make dataset from {}...".format(train_datapath))
    df = pd.read_csv(train_datapath, sep=",", index_col=0)
    if trans:
        #转置
        df = df.transpose()
    print("have {} samples, {} features".format(df.shape[0], df.shape[1]))
    if data_type == 'count':
        df = row_normal(df)
        # df = sizefactor(df)
    elif data_type == 'rpkm':
        df = np.log(df + 1)
    if gene_scale:
        from sklearn.preprocessing import MinMaxScaler
        #归一化特征到一定数值区间的函数
        #默认范围为0~1，拷贝操作
        scaler = MinMaxScaler()
        #fit:找到df的整体指标，如均值、方差、最大值和最小值等等
        #transform:然后对df进行转换，从而实现数据的标准化和归一化
        #使得新的数据集data方差为1，均值为0
        data = scaler.fit_transform(df)
        df = pd.DataFrame(data=data, columns=df.columns)
    return df.values


def extract_features(data, gene_select=10000):
    # sehng xu pai lie qu zuida de ruo gan ji yin, ran hou dao xu
    #升序排列取最大的若干基因，然后倒序
    #计算每列的标准差
    selected = np.std(data, axis=0)
    #argsort():将数组从小到大排列并返回对应索引
    #[-10000:]最后10000个数
    #[::-1]从后向前排元素[1,2,3]->[3,2,1]
    selected = selected.argsort()[-gene_select:][::-1]
    h_data = data[:, selected]
    return h_data


def load_data_scanpy(train_datapath, data_type='count', trans=True):
    print("make dataset from {}...".format(train_datapath))
    df = pd.read_csv(train_datapath, sep=",", index_col=0)
    if trans:
        #转置函数
        df = df.transpose()
    print("have {} samples, {} features".format(df.shape[0], df.shape[1]))

    adata = sc.AnnData(df.values)
    #过滤低质量细胞样本
    #过滤少于1个细胞表达，或一个细胞中表达少于200个基因的细胞样本
    sc.pp.filter_cells(adata, min_genes=1)
    sc.pp.filter_genes(adata, min_cells=1)
    if data_type == 'count':
        #归一化，使得不同细胞样本间可比
        sc.pp.normalize_total(adata, target_sum=1e6)
        sc.pp.log1p(adata)
    elif data_type == 'rpkm':
        sc.pp.log1p(adata)
    #绘制散点基因图
    # sc.pp.highly_variable_genes(adata, n_top_genes=20000, flavor='cell_ranger', inplace=True)
    # adata = adata[:, adata.var['highly_variable']]
    # if gene_scale:
    #将每个基因缩放到单位方差，阈值超过标准偏差3
    #     sc.pp.scale(adata, zero_center=True, max_value=3)
    return adata.X
