import semanticscholar as sch
'''
  该参数表示文献的数据结构
  dict_keys(['abstract', 'arxivId', 'authors', 'citationVelocity', 'citations',
                    'corpusId', 'doi', 'fieldsOfStudy', 'influentialCitationCount', 'isOpenAccess',
                    'isPublisherLicensed', 'is_open_access', 'is_publisher_licensed', 'numCitedBy', 'numCiting',
                    'paperId', 'references', 'title', 'topics', 'url', 'venue', 'year']) 
'''
def find_tlcm_document(papers1 , isInfluential):
    '''
    给定几篇文献，查找基于这几篇文章的相关研究

    :param papers1:
                     形如 papers1 = ['arXiv:1906.08237','arXiv:1907.11692']
                     是一个文献数组，每一个str代表一个文献唯一标识，可以是 S2PaperId, DOI or ArXivId类型
                     文献的S2PaperId获取方式，可以在网站 https://www.semanticscholar.org/ 搜索该文献名，找到自己想要的文献，查看浏览器的url。
                     如url：https://www.semanticscholar.org/paper/BERT%3A-Pre-training-of-Deep-Bidirectional-for-Devlin-Chang/df2b0e26d0599ce3e70df8a9da02e51594e0e992
                     截取最后一节为 S2PaperId = ‘df2b0e26d0599ce3e70df8a9da02e51594e0e992’ 为BERT3A-Pre-training-of-Deep-Bidirectional-for-Devlin-Chang 的标识
    :param isInfluential:
                    评价该文献是否具有影响力，输入为一个bool类型，true代表结果文献必须是高影响力论文
    :return: 输出最佳匹配前十篇文献
    '''
    # # XLNet(ArXivId):'arXiv:1906.08237'
    # # RoBERTa((ArXivId)): 'arXiv:1907.11692'
    # # BERT (S2PaperId):‘df2b0e26d0599ce3e70df8a9da02e51594e0e992’
    # # papers1 = ['arXiv:1906.08237','arXiv:1907.11692']
    papers = [sch.paper(p, timeout=12) for p in papers1]       # timeout避免时间超时导致错误
    if isInfluential:
        ans_co_citations = set(x['title'] for x in papers[0]['citations'] if x['isInfluential'])
        for paper in papers:
            ans_co_citations &= set(x['title'] for x in paper['citations'] if x['isInfluential'])
        co_citations = list(ans_co_citations)

        print("\n" + "这些文章（输入）被作为参考文献的文章总(且具有超级高影响力)共有：", len(co_citations), "篇   接下来将打印前10篇")
        print("\n".join(co_citations[:10]))
    else:
        ans_co_citations = set(x['title'] for x in papers[0]['citations'])
        print(papers[0]['authors'])
        for paper in papers:
            ans_co_citations &= set(x['title'] for x in paper['citations'])
        co_citations = list(ans_co_citations)

        print("\n"+"这些文章（输入）被作为参考文献的文章总共有：",len(co_citations),"篇   接下来将打印前10篇")
        print("\n".join(co_citations[:10]))

def find_cf_doucment(papers1, isInfluential):
    '''
    给定几篇文献，查找它们共同的方法，即共同引用。
    :param papers1:
    :param isInfluential:
    :return:
    '''
    papers = [sch.paper(p, timeout=12) for p in papers1]
    if isInfluential:
        ans_co_citations = set(x['title'] for x in papers[0]['references'] if x['isInfluential'])
        for paper in papers:
            ans_co_citations &= set(x['title'] for x in paper['references'] if x['isInfluential'])
        co_citations = list(ans_co_citations)

        print("\n" + "这些文献共同参考的文献总(且具有超级高影响力)共有：", len(co_citations), "篇   接下来将打印前10篇")
        print("\n".join(co_citations[:10]))
    else:
        ans_co_citations = set(x['title'] for x in papers[0]['references'])
        print(papers[0]['authors'])
        for paper in papers:
            ans_co_citations &= set(x['title'] for x in paper['references'])
        co_citations = list(ans_co_citations)

        print("\n" + "这些文献共同参考的文献总共有：", len(co_citations), "篇   接下来将打印前10篇")
        print("\n".join(co_citations[:10]))
if __name__ == '__main__':
    papers = ['10.3115/1219840.1219855','10.1145/1014052.1014073','10.3115/1218955.1218990',
              '10.1007/s10579-005-7880-9','687bac2d3320083eb4530bf18bb8f8f721477600']
    papers1 = ['arXiv:1906.08237','arXiv:1907.11692']
    isInfluential = False
    find_tlcm_document(papers,isInfluential)
    print("\n")
    find_cf_doucment(papers1,isInfluential)