from pathlib import Path
fron torch.utils.data import Dataset, DataLoader

class MyDataSet(Dataset):

    """ コンストラクタ """
    def __init__(self, dataset_dir):
        self.dataset_dir = Path(dataset_dir).resolve()
        self.paths = list(self.dataset_ir.glob("*"))

    """ len関数を定義 """
    def __len__(self):
        return len(self.paths)

    """ '[]'によるアクセスを定義 """
    def __getitem__(self, idx):
        path = self.paths[idx]
        return path


if __name__ == "__main__":
    dataloader = DataLoader(dataset=MyDataSet("."), batch_size=2)