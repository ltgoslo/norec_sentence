# NoReC_sentence

This is a dataset for sentence-level sentiment classification in Norwegian, derived from the the fine-grained annotations of [NoReC_fine](https://github.com/ltgoslo/norec_fine). We here provide two versions, where the annotations have been aggregated at the sentence-level in the following ways:

* Binary: sentences that contained sentiment annotations of either positive or negative polarity (but not both).  
* Three-way: additionaly includes sentences annotated as having no sentiment at all (neutral).  

Note that for both versions, sentences that contained mixed polarity are excluded. The original NoReC_fine dataset is described in the paper [_A Fine-Grained Sentiment Dataset for Norwegian_](https://www.aclweb.org/anthology/2020.lrec-1.618) by L. Øvrelid, P. Mæhlum, J. Barnes, and E. Velldal, published at LREC 2020.

## Terms of use
NoReC_sentence inherits the license of the underlying [NoReC](https://github.com/ltgoslo/norec) corpus, copied here for convenience:

The data is distributed under a Creative Commons Attribution-NonCommercial licence (CC BY-NC 4.0), access the full license text here: https://creativecommons.org/licenses/by-nc/4.0/

The licence is motivated by the need to block the possibility of third parties redistributing the orignal reviews for commercial purposes. Note that **machine learned models**, extracted **lexicons**, **embeddings**, and similar resources that are created on the basis of NoReC are not considered to contain the original data and so **can be freely used also for commercial purposes** despite the non-commercial condition.
