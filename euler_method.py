def f(t, y):
    return 3*y/t + y*y/(t**4)


def euler(delta_t):
    t = 1
    y = 1/3
    while(t<7/2):
        A = f(t, y)
        t = t + delta_t
        y = y + delta_t*A
    
    return (y,t)

print("Euler:")
y1, t1 = euler(0.5)
print("y({}) = {}".format(t1, y1))

y2, t2 = euler(0.25)
print("y({}) = {}".format(t2, y2))
print("")

def runge_kutta2(delta_t):
    t = 1
    y = 1/3
    while(t<7/2):
        A = f(t, y)
        t = t + delta_t
        
        y_temp = y + delta_t*A
        B = f(t, y_temp)
        y = y + delta_t(A+B)/2
    
    return (y,t)

print("runge-kutta:")
y1, t1 = runge_kutta2(0.5)
print("y({}) = {}".format(t1, y1))

y2, t2 = runge_kutta2(0.25)
print("y({}) = {}".format(t2, y2))
