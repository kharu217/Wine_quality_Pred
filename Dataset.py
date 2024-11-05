import torch
from torch.utils.data import DataLoader, Dataset
import pandas as pd

winery_dict = {
    'Contino' : 1,
    'Artadi' : 2,
    'La Rioja Alta' : 3,
    'Sierra Cantabria' : 4,
    'Matarromera' : 5
}


class wine_data(Dataset) :
    def __init__(self, datapath):
        super().__init__()
        raw_csv = pd.read_csv(datapath)