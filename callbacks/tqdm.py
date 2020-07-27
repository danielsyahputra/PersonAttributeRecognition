from tqdm import tqdm

class Tqdm(object):
    def __init__(self, epoch, total, phase='train'):
        """
        Tqdm Progress Bar callback
        """
        assert phase in ['train', 'val', 'test'], 'phase must in [train, val, test]'
        self.progbar = tqdm(total=total)
        self.progbar.set_description(f'Epoch {epoch}')
        self.phase = phase
    
    def on_batch_end(self, dict_metrics):
        self.progbar.set_postfix({'{}_{}'.format(self.phase, str(key)): value for key, value in dict_metrics.items()})
        # self.progbar.set_postfix({
        #     '{}_loss'.format(self.phase): loss,
        #     '{}_acc'.format(self.phase): accuracy,
        #     '{}_f1-score'.format(self.phase): f1_score})
        self.progbar.update(1)

    def on_epoch_end(self):
        self.progbar.close()


