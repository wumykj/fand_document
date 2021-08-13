# fand_document
你可以通过你手中的几篇的文献，来查找相关的研究和最新的研究状态。以及它们共同的工作和方法。
   其中find_tlcm_document用来寻找相关的研究和最新的研究状态
   其中find_cf_doucment用来寻找它们基于哪些相同工作和方法
   
给出输入你需要查找的文献，组织成一个文献标识数组如：
papers = ['10.3115/1219840.1219855','10.1145/1014052.1014073','687bac2d3320083eb4530bf18bb8f8f721477600']
文献可以是这三种类型的唯一标识，S2PaperId, DOI or ArXivId类型，下面我们提供一种找文献S2PaperId的方法：
   可以在网站 https://www.semanticscholar.org/ 搜索该文献名BERT，找到自己想要的文献，查看浏览器的url。
   如url：https://www.semanticscholar.org/paper/BERT%3A-Pre-training-of-Deep-Bidirectional-for-Devlin-Chang/df2b0e26d0599ce3e70df8a9da02e51594e0e992
   截取最后一节，这样bert文献的 S2PaperId = ‘df2b0e26d0599ce3e70df8a9da02e51594e0e992’ 

给定isInfluential参数的值，是一个bool变量，如果为TRUU,它会保证你的结果文献中出现都是具有影响力的论文，评价指标详情见semanticscholar。

此产品由myjk出品，谢谢支持！！！
