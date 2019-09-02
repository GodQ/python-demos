from proj.tasks import add, mul
from celery import chain

def test():
    #res = add.s(2,2).delay()
    #print res.id
    #print res.state
    #print res.get()
    #print res.state
    
    #task_list = [add.s(i,i) for i in xrange(10)]
    #print task_list
    #ch = chain(task_list)
    ch = chain(add.s(2,2), mul.s(3))
    print ch
    res = ch.delay()
    print res
    print res.id
    print res.state
    res.get(5)
    print res.state
    print res.result
    print res.info

test()
