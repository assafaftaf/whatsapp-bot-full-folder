import turtle

def req(f,s,sum,t):
    t=turtle.Turtle(t)
    sum=f+s
    t.forward(sum)
    t.right(sum)
    if(sum>100):
        return 0
    return req(sum,sum-s,sum,t)

#main:
print(0)
print(1)
print(1)

a= turtle.Turtle()

req(1,1,2,a)
turtle.done()