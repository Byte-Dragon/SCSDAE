from sklearn.metrics import normalized_mutual_info_score, adjusted_rand_score, adjusted_mutual_info_score
import numpy as np

nmi = normalized_mutual_info_score
ari = adjusted_rand_score
ami = adjusted_mutual_info_score


def acc(y_true, y_pred):
    """
    Calculate clustering accuracy. Require scikit-learn installed
    # Arguments
        y_true: true labels, numpy.array with shape `(n_samples,)`
        y_pred: predicted labels, numpy.array with shape `(n_samples,)`

    # Return
        accuracy, in [0,1]

    计算聚类准确度。需要安装scikit-learn

    #参数
        y_true: 真实标签,numpy.array，形状为“( n_samples，)”
        y_pred:预测标签，numpy.array，形状为“( n_samples，)”

    #返回
        精度，单位为[0，1]
    """
    #变为64位整形
    y_true = y_true.astype(np.int64)
    #断点，若符合条件，程序继续往下运行
    assert y_pred.size == y_true.size
    D = max(y_pred.max(), y_true.max()) + 1
    w = np.zeros((D, D), dtype=np.int64)
    for i in range(y_pred.size):
        w[y_pred[i], y_true[i]] += 1
    #from sklearn.utils.linear_assignment_ import linear_assignment
    from scipy.optimize import linear_sum_assignment as linear_assignment
    ind = linear_assignment(w.max() - w)
    return sum([w[i, j] for i, j in ind]) * 1.0 / y_pred.size
