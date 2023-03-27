# scSDAE
Sparsity-penalized stacked denoising auto-encoders for imputing single-cell RNA-seq data

用于输入单细胞 RNA-seq 数据的稀疏惩罚堆叠去噪自编码器

# System requirements
+ Python 3.7. (version tested) or compatible
+ Tensorflow 1.12.0 (version tested) or compatible
+ keras
+ Python 3.7。(版本经过测试)或兼容
+ Tensorflow 1.12.0(已测试版本)或兼容版本
+ 深度学习


# Installation guide
Clone the github repository, install the dependencies 

克隆github仓库，安装依赖

# Usage for dataset with csv file with rows representing genes, columns representing cells
#带有csv文件的数据集的用法，其中行代表基因，列代表细胞
    parser.add_argument('--batch_size', default=256, type=int)
    parser.add_argument('--n_iters_ae', default=2000, type=int) # iteration steps for scSADE
    parser.add_argument('--n_iters_pretrain', default=1000, type=int) # iteration steps for scSADE
    parser.add_argument('--alpha', default=1.0, type=float)  # the mixture coefficient of mixture loss 
    parser.add_argument('--dr_rate', default=0.2, type=float) # dropout drate
    parser.add_argument('--nu1', default=0.0, type=float) # L1 regularization
    parser.add_argument('--nu2', default=0.0, type=float) # L2 regularization
    parser.add_argument("--train_datapath", default="./zeisel_count.csv", type=str) #path of the train file
    parser.add_argument("--data_type", default="count", type=str) 
    parser.add_argument("--outDir", default="./", type=str) #path to save output
    parser.add_argument("--name", default="zeisel", type=str)  #dataset name
    feature_parser = parser.add_mutually_exclusive_group(required=False) 
    feature_parser.add_argument('--gene_scale', dest='gene_scale', action='store_true')
    feature_parser.add_argument('--no-gene_scale', dest='gene_scale', action='store_false') 
    parser.set_defaults(gene_scale=False)  # if scale gene to [0,1]
    parser.add_argument('--GPU_SET', default="3", type=str) 
# Usage for folder containing csv files
#包含csv文件的文件夹的用法
    First, format the files into: {name}\_{data_type}.csv, then fill the blank in the file "run_pure_ae.csv":
    data_dir = "" # data path storing the data 存储数据的数据路径
    python_path = "" # path of python to use python的使用路径
    script_path = "{path}/pure_ae_new.csv"  # path storing pure_ae_new.csv  路径存储pure_ae_new.csv
    run_log_path = "" # path to store the running logfile 存储运行日志文件的路径
    out_path = ""  # path to store the output 存储输出的路径
# output
    csv file "autoencoder_r.csv" with rows representing cells, columns representing genes



