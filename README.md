# CInfoWaveGAN

An architecture for modeling lexical learning from raw acoustic inputs called Categorical InfoWaveGAN that combines Deep Convolutional GAN architecture for audio data (WaveGAN) with categorical variables in information theoretic proposal InfoGAN. 

Based on WaveGAN (https://github.com/chrisdonahue/wavegan) and InfoGAN (https://github.com/singnet/semantic-vision/blob/master/experiments/concept_learning/gans/info-wgan-gp/10_originfo_sepQ_v2_lr1e-3/train.py). 

In addition to the Generator and the Discriminator networks, the architecture introduces a network that learns to classify generated outputs and forces the Generator to encode lexical information in its latent space. Lexical and semantic encoding is represented with a set of categorical binary variables. The network is trained on five lexical items from TIMIT. The network learns to generate lexical items and encodes the identity of each item in categorical variables of the latent space. By manipulating the categorical variables in the latent space that encode lexical information, the network outputs the five lexical items, suggesting that each lexical item is represented with unique categorical code. Such representation can serve as the basis for lexical and semantic learning from raw acoustic input.  

