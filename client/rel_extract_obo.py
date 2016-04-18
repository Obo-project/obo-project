import nltk

def semi_rel2reldict(pairs, window=5, trace=False):
    result = []
    while len(pairs) >= 2:
        reldict = nltk.sem.relextract.defaultdict(str)
        reldict['lcon'] = nltk.sem.relextract._join(pairs[0][0][-window:])
        reldict['subjclass'] = pairs[0][1].label()
        reldict['subjtext'] = nltk.sem.relextract._join(pairs[0][1].leaves())
        reldict['subjsym'] = nltk.sem.relextract.list2sym(pairs[0][1].leaves())
        reldict['filler'] = nltk.sem.relextract._join(pairs[1][0])
        reldict['untagged_filler'] = nltk.sem.relextract._join(pairs[1][0], untag=True)
        reldict['objclass'] = pairs[1][1].label()
        reldict['objtext'] = nltk.sem.relextract._join(pairs[1][1].leaves())
        reldict['objsym'] = nltk.sem.relextract.list2sym(pairs[1][1].leaves())
        #reldict['rcon'] = _join(pairs[2][0][:window])
        if trace:
            print("(%s(%s, %s)" % (reldict['untagged_filler'], reldict['subjclass'], reldict['objclass']))
        result.append(reldict)
        pairs = pairs[1:]
    return result

def extract_rels(subjclass, objclass, doc, corpus='ace', pattern=None, window=10):
    pairs = nltk.sem.relextract.tree2semi_rel(doc)

    reldicts = semi_rel2reldict(pairs)

    relfilter = lambda x: (x['subjclass'] == subjclass and
                           len(x['filler'].split()) <= window and
                           pattern.match(x['filler']) and
                           x['objclass'] == objclass)

    return list(filter(relfilter, reldicts))
