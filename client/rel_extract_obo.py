import nltk

def precompute(sents):
    dic = {
    	"people": "PPUNIT",
    	"inhabitants": "PPUNIT"
    }

    def f(a , b):
    	if a in dic:
    		return dic[a]
    	else:
    		return b

    sents = nltk.sent_tokenize(sents)
    sents = [nltk.word_tokenize(sent) for sent in sents]
    sents = [nltk.pos_tag(sent) for sent in sents]
    sents = [[(a, f(a, b)) for (a,b) in sent] for sent in sents]
    sents = nltk.ne_chunk(sents[0])

    grammar = """
    	CDD: {<CD>*}
    	PPCD: {<CDD><PPUNIT>}
    	LOC: {<GPE>}
    	"""

    cp = nltk.RegexpParser(grammar, loop = 2)
    sents = cp.parse(sents)

    return sents

def semi_rel2reldict(pairs, window=5, trace=False, comparator='egal'):
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
        reldict['comparator'] = comparator
        if trace:
            print("(%s(%s, %s)" % (reldict['untagged_filler'], reldict['subjclass'], reldict['objclass']))
        result.append(reldict)
        pairs = pairs[1:]
    return result

def extract_rels(subjclass, objclass, doc, corpus='ace', patterns={'left': None, 'middle': None, 'comparator': 'egal'}, position='middle', window=10):
    pairs = nltk.sem.relextract.tree2semi_rel(doc)
    reldicts = semi_rel2reldict(pairs, comparator=patterns['comparator'])

    dic = {
        'middle': 'filler',
        'left': 'lcon'
    }

    relfilter = lambda x: (x['subjclass'] == subjclass and
                           len(x[dic['middle']].split()) <= window and
                           patterns['middle'].match(x[dic['middle']]) and
                           len(x[dic['left']].split()) <= window and
                           patterns['left'].match(x[dic['left']]) and
                           x['objclass'] == objclass)

    return list(filter(relfilter, reldicts))
