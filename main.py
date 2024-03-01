import os
import glob
from tqdm import tqdm
from totalsegmentator.python_api import totalsegmentator

from utils.seed import set_seed
from utils.logger import setup_logger
from utils.options import get_args

def main(args):
    data_path = glob.glob(args.dataset_dir+'*')
    for data in tqdm(data_path):
        cts = glob.glob(data+'/*')
        for ct_path in cts:
            out_dir = f'{args.output_dir}/{ct_path.replace(args.dataset_dir, "")}'
            print(out_dir)
            ct_path = glob.glob(ct_path+'/*')[0]
            out  = totalsegmentator(ct_path, out_dir, task='body', verbose=False, quiet=True)

if __name__ == '__main__':
    args = get_args()
    set_seed(args.seed)
    os.makedirs(args.output_dir, exist_ok=True)

    logger = setup_logger('Lung-Body Detection', args.output_dir)
    logger.info(str(args).replace(',','\n'))

    main(args)
