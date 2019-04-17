import torch
from torch.nn import Module
from torch.nn.parameter import Parameter


class L2NormRunning(Module):

    def __init__(self, num_features, dim=0, eps=1e-12, momentum=0.1):
        super(L2NormRunning, self).__init__()
        self.num_features = num_features
        self.dim = dim
        self.eps = eps
        self.momentum = momentum
        self.register_buffer('running_l2_norm', torch.ones(num_features))
        self.register_buffer('num_batches_tracked', torch.tensor(0, dtype=torch.long))
        self.reset_parameters()

    def reset_parameters(self):
        self.running_l2_norm.fill_(1)
        self.num_batches_tracked.zero_()

    def forward(self, input):
        if self.training:
            if self.num_batches_tracked is not None:
                self.num_batches_tracked += 1
            l2_norm = (input ** 2).sum(self.dim) ** 0.5
            self.running_l2_norm = (1 - self.momentum) * self.running_l2_norm + self.momentum * l2_norm
        else:
            l2_norm = self.running_l2_norm

        return input / torch.max(l2_norm, torch.ones_like(l2_norm) * self.eps)
