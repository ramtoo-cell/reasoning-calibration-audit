"""Calibration and Abstention Audit. See METHODS.md for assumptions."""
import math
def analyze(data):
    rows=data['rows']; bins=data.get('bins',10)
    if not rows or type(bins) is not int or not 1 <= bins <= 1000:
        raise ValueError('Need rows and 1..1000 bins')
    for r in rows:
        p=r['confidence']
        if type(p) not in (int,float) or not math.isfinite(p) or not 0 <= p <= 1 or type(r['correct']) is not bool:
            raise ValueError('Expected finite confidence in [0,1] and boolean correct')
    n=len(rows); buckets=[[] for _ in range(bins)]
    for r in rows: buckets[min(bins-1,int(r['confidence']*bins))].append(r)
    histogram=[]; ece=0
    for i,b in enumerate(buckets):
        if not b: continue
        accuracy=sum(r['correct'] for r in b)/len(b)
        confidence=sum(r['confidence'] for r in b)/len(b)
        ece += len(b)/n*abs(accuracy-confidence)
        histogram.append({'bin':i,'n':len(b),'accuracy':accuracy,'confidence':confidence})
    curve=[]
    for threshold in sorted({r['confidence'] for r in rows},reverse=True):
        accepted=[r for r in rows if r['confidence']>=threshold]
        curve.append({'threshold':threshold,'coverage':len(accepted)/n,'risk':1-sum(r['correct'] for r in accepted)/len(accepted)})
    return {'n':n,'brier':sum((r['confidence']-r['correct'])**2 for r in rows)/n,'ece':ece,'bins':histogram,'risk_coverage':curve}
